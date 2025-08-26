SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 10: BASIC REAL-WORLD SCENARIOS

---

## Overview

- This chapter applies earlier techniques to **end-to-end troubleshooting**.  
- Each scenario follows a repeatable pattern: **define the question → choose the capture point(s) → capture with sane filters → read the story (time, flags, codes) → confirm root cause → fix and verify**.  
- Below are condensed **playbooks** you can copy into your runbook and adapt on the fly.

---

## Scenario 1 — “Web page loads partially / some objects missing”

**Symptoms**
- Base HTML arrives, but images/CSS/JS fail or stall; browser dev tools show long “pending” or 404/5xx on subresources.

**Capture plan**
- SPAN/TAP the **client access port** (first), optionally the **server VIP/edge** (second).  
- Keep capture **wide**; use display filters while analyzing.

**Display filters (starter set)**
- `http or tls`  
- `tcp.analysis.flags`  
- Errors only: `http.response.code >= 400`  
- By host: `ip.addr == <client> or ip.addr == <server>`

**Packet story (what to look for)**
- Normal 3-way handshake, then HTTP GETs.  
- Missing objects → 404/403 (app/config) or TCP resets from LB/WAF (policy).  
- Repeated `tcp.analysis.retransmission` and no 4xx/5xx → path issues.  
- **TTFB** high but low loss → slow server/back-end.

**Root causes seen often**
- CDN/LB misrouting, broken rewrite rules, expired cookies, WAF blocking, PMTUD black hole for large assets, stale DNS.

**Fix & verify**
- Correct LB/WAF/DNS; re-load and confirm steady **200 OK** and reduced deltas.

---

## Scenario 2 — “Internet access down” (client can’t reach the web)

**Symptoms**
- Ping to gateway fails or succeeds inconsistently; DNS lookups fail; browsers spin.

**Capture plan**
- Client access port (or host capture), and if possible **inside vs outside** of the gateway.

**Quick tests to drive packet evidence**
- `arp`, `icmp`, `dns`, `http` probes.

**What good looks like**
- ARP request→reply to gateway, DNS queries→answers, TCP SYN→SYN/ACK to remote.

**Failure signatures**
- **No ARP reply** → gateway down or L2 block.  
- **DNS NX/SERVFAIL/timeout** → resolver unreachable/misconfigured.  
- **SYN retransmissions** with no SYN/ACK → upstream ACL/NAT/ISP outage.  
- **ICMP “Frag Needed/Packet Too Big” suppressed** → PMTUD black hole.

**Fix & verify**
- Repair L2, DHCP options (DNS/GW), NAT rules, or permit ICMP needed for PMTUD. Re-test end-to-end.

---

## Scenario 3 — “Branch can’t reach HQ app”

**Symptoms**
- Site-to-site traffic flaps; app login OK but data transfer stalls or resets.

**Capture plan**
- At the **branch edge** and **HQ edge** (both sides of the VPN/edge router).  
- If using a TAP, preserve both directions; otherwise mirror relevant VLAN/port.

**What to compare**
- **Before tunnel** (inner traffic) vs **on the wire** (encapsulated ESP/GRE).  
- Sequence: SYN at branch → appears as ESP from branch to HQ? If inner traffic never shows at HQ, problem is in transit.

**Failure signatures**
- SPI/key rollover desync (ESP in one direction only).  
- MTU mismatch on tunnel interface (large inner packets stall; outer path OK).  
- Asymmetric routing (only one direction seen at the far side).  
- Idle timers causing RST/teardown mid-flow.

**Fix & verify**
- Re-negotiate SAs, clamp MSS on tunnel, correct routes. Confirm symmetric flows and stable keepalives.

---

## Scenario 4 — “Printer intermittently fails / jobs vanish”

**Symptoms**
- Tiny test pages work; big PDFs fail mid-transfer; users re-queue jobs.

**Capture plan**
- Mirror **client→printer** switch ports or capture at print server.

**Tell-tale patterns**
- TCP **zero-window** from the printer (small buffers); long gaps, then window update.  
- RST from printer under overload.  
- Multicast/broadcast discovery (mDNS/LLMNR) noise crowding a small segment.  
- Spurious retransmissions on weak Wi-Fi bridges to the printer.

**Fix & verify**
- Increase printer memory/firmware updates; move to wired; throttle job size; segment chatty discovery. Watch zero-window disappear.

---

## Scenario 5 — “3rd-party API/‘weather service’ unreachable”

**Symptoms**
- Local app logs show HTTP 5xx/timeout; curl sometimes works, app fails.

**Capture plan**
- Client/app host and **Internet edge**.

**Evidence to collect**
- TLS handshake completion (ClientHello ↔ ServerHello).  
- SNI value (`tls.handshake.extensions_server_name`), HTTP Host header, response codes.

**Likely culprits**
- TLS middlebox mismatch (Server Name Indication vs cert CN/SAN).  
- Proxy auto-config (PAC) pointing some clients to a dead proxy.  
- Egress ACL change blocking `tcp/443` to the provider’s new IP range.  
- DNS split-horizon (internal resolver returns private IP unreachable from your network).

**Fix & verify**
- Correct proxy/ACL/DNS; confirm **200 OK** and clean TLS alert-free session.

---

## Scenario 6 — “File transfer corrupt / app says data mismatch”

**Symptoms**
- Hashes don’t match; app reports corrupt payloads; network team blamed.

**Capture plan**
- Server and client edges (two vantage points) or TAP inline on the path.

**What the packets say**
- On-wire corruption would show as **bad FCS** (SPAN can’t see this) or repeated **retransmissions** and out-of-order that eventually recover exactly the same bytes.  
- If both sides show identical bytestream reassembled by TCP, corruption is **not** on the wire—it’s at rest or app layer (encoding, compression, or post-write).

**Fix & verify**
- Prove wire-level integrity with **Follow Stream** and matching hashes of payload extracted via “Export Objects”/pcap carve; engage app/storage team.

---

## Scenario 7 — “VoIP choppy / call quality poor”

**Symptoms**
- Users report clipping/robotic audio; signaling OK, media bad.

**Capture plan**
- Mirror phone/VLAN and SBC/Media gateway ports; add **RTP** decode.

**Evidence**
- RTP **sequence gaps** (loss) and **jitter** spikes; DSCP marking stripped by a hop; codec mismatch forces transcoding.

**Fix & verify**
- Restore QoS (DSCP preservation), prioritize media, stabilize links. Confirm MOS/jitter improvement.

---

## “Choose-Your-Own-Adventure” Triaging (generic recipe)

1. **Define the transaction** (who talks to whom, protocol/port, success criteria).  
2. **Pick vantage(s)** that guarantee **both directions** of the flow (client first, then the other side of each L3 boundary).  
3. **Capture wide** (minimal BPF), rotate files; annotate where/when/how.  
4. **Render the story**:  
   - Set **Time Reference** at request; measure **TTFB** and total time.  
   - Check **tcp.analysis.flags** (retrans, dupACK, zero-window).  
   - For UDP, rely on **ICMP** evidence and app semantics.  
   - For TLS/HTTPS, use **SNI**/cert metadata if you can’t decrypt.  
5. **Localize**: compare client-side vs server-side traces to decide **client vs wire vs server**.  
6. **Change one thing** (route, MTU/MSS, DNS, LB pool, policy) and **re-measure**.

---

## Fast Filters & Columns (paste once, reuse forever)

**Columns**
- `frame.time_delta_displayed`, `tcp.stream`, `tcp.flags`, `ip.ttl`/`ipv6.hlim`, `vlan.id`, `http.response.code`, `dns.qry.name`, `tls.handshake.extensions_server_name`

**Filters**
- Handshake issues: `tcp.flags.syn==1 and tcp.flags.ack==0`  
- Loss/pressure: `tcp.analysis.flags`  
- HTTP errors: `http.response.code >= 400`  
- DNS trouble: `dns.flags.rcode > 0 or tcp.port==53`  
- PMTUD: `icmp.type==3 and icmp.code==4 or icmpv6.type==2`  
- Resets: `tcp.flags.reset==1`  
- RTP focus: `rtp` (after “Decode As… RTP” if needed)

---

## Mini-Labs (hands-on)

1) **PMTUD black-hole**  
   - Download a large file across a WAN while blocking ICMP Frag-Needed/Packet-Too-Big.  
   - Observe stalls and retransmissions; restore ICMP and confirm recovery.

2) **LB/WAF troubleshooting**  
   - Hit an app through the VIP and directly to a node (maintenance window).  
   - Compare response codes/TTFB; identify the layer enforcing the block.

3) **Branch VPN MTU**  
   - Lower tunnel MSS and repeat a large file transfer.  
   - Watch stalls disappear and RTT smooth out in I/O Graphs.

---

## What You Should Be Able to Do After Chapter 10

- Turn vague complaints into **packet-level narratives** that isolate **where** and **why** a transaction fails.  
- Choose **capture points** and **filters** that preserve the necessary truth while keeping files sane.  
- Recognize recurring root-cause patterns (DNS, NAT/ACL, PMTUD, LB/WAF, buffer pressure).  
- Fix and **prove** resolution with before/after captures and clear timing deltas.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
