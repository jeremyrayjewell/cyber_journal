SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 12: PACKET ANALYSIS FOR SECURITY

---

## Overview

- Apply packet skills to **defense and investigation**: spotting **recon/scans**, **spoofing/MitM**, **session hijacking**, and **malware/C2 & exfil** patterns.
- Build repeatable workflows for **alert triage**, **pcap-first incident response**, and **forensic evidence** handling.

---

## Mindset & Workflow for Security Packet Work

1) **State the question**: what exactly is suspected (scan, beacon, data theft, phish)?  
2) **Choose vantage**: capture where evidence is most truthful (edge TAP, sensor SPAN, server access port).  
3) **Scope broadly**, then focus with display filters; **preserve originals** (pcapng) and work on copies.  
4) **Tell the story** with timestamps, 5-tuples, and protocol semantics; annotate packet comments.  
5) **Decide/act** (block, isolate, collect more), then **verify** with fresh capture.

**Evidence hygiene**
- Keep **pcapng**, enable **packets dropped** counters, use **NTP sync**, and record **capture point** + **mirror/TAP config** in file comments.
- Avoid decrypting traffic or inspecting payloads without authorization; consider privacy and legal constraints.

---

## Reconnaissance & Scanning

**TCP scans**
- **SYN scan**: many `SYN` probes to varied ports/hosts; replies `SYN/ACK` (open) or `RST` (closed).  
- **NULL/FIN/Xmas scans**: strange flag combos to elicit `RST` from closed ports; useful when SYNs are filtered.  
- **Banner hunts**: quick connection followed by protocol-identifying requests (e.g., `GET / HTTP/1.0\r\n\r\n`).

**UDP scans**
- Lack of response ≠ open; closed ports often answer with **ICMP Port Unreachable** (type 3, code 3). Expect **many ICMP errors** during UDP scans.

**OS fingerprint clues (coarse)**
- Initial **TTL**, **TCP window size**, **MSS**, and **timestamps** can hint at OS families (not definitive; middleboxes skew this).

**Filters (copy/paste)**
- SYN probes: `tcp.flags.syn==1 and tcp.flags.ack==0`  
- Xmas/FIN/NULL:  
  - `tcp.flags.fin==1 and tcp.flags.ack==0 and tcp.flags.syn==0 and tcp.flags.rst==0 and tcp.flags.psh==1 and tcp.flags.urg==1` (Xmas)  
  - `tcp.flags.fin==1 and tcp.flags.ack==0 and tcp.flags.syn==0 and tcp.flags.rst==0 and tcp.flags.psh==0 and tcp.flags.urg==0` (FIN)  
  - `tcp.flags==0x000` (NULL)  
- UDP scan fallout: `icmp.type==3 and icmp.code==3`

**Signs of stealth**
- Low-and-slow scanning (hours/days); target spread across subnets; randomized destination ports; spoofed sources.

---

## Manipulation & Spoofing (MitM, ARP, Session Hijacking)

**ARP cache poisoning / MitM (lab-only unless authorized)**
- Symptoms: **multiple MACs** claim one IP; **gateway IP** suddenly resolves to an unexpected MAC.  
- Look for **gratuitous ARP storms**, alternating **ARP replies** with differing `arp.src.hw_mac` for the same `arp.src.proto_ipv4`.

**Session hijacking (legacy HTTP)**
- Unencrypted HTTP cookie theft → forged requests with stolen `Cookie:` header.
- Tell: new TCP connection from attacker IP using victim’s session cookie; target accepts and serves authenticated content.

**DNS manipulation**
- Unexpected **A/AAAA**/CNAME answers for known domains; TTLs near zero; answers from **non-authorized** resolvers.
- **NXDOMAIN spikes** when a DGA (domain-generation algorithm) is active.

**Filters**
- ARP conflict/poisoning:  
  - `arp`  
  - `arp.opcode == 2 and eth.src != arp.src.hw_mac`  
- DNS anomalies:  
  - `dns.flags.response == 1 and dns.count.answers > 0` (inspect answers)  
  - `dns.flags.rcode > 0` (errors)  
  - `dns.qry.name matches "[A-Za-z0-9]{20,}"` (very long/entropy-heavy labels)

**Mitigations to expect**
- Dynamic ARP Inspection, DHCP Snooping, static ARP for critical systems, DNSSEC, HTTPS everywhere.

---

## Malware, C2, and Exfiltration Patterns

**C2 beaconing**
- **Periodic small flows** to the same IP/FQDN at fixed intervals (30s/60s/5m), often **long-lived TCP** with keep-alives.
- **HTTP/HTTPS beacons**: odd `User-Agent`, consistent path like `/gate.php`, small POST/GET with base64-like blobs.  
- **TLS-based C2**: unusual SNI (or **no SNI**), self-signed certs, rare JA3/JA3S fingerprints, **very long-lived** low-throughput TLS sessions.

**DNS misuse**
- **DNS tunneling**: many TXT queries/responses or **very long labels** (base32/64-ish); consistent subdomain patterns; high `NXDOMAIN` rate.  
- **DGA**: bursty queries to many never-before-seen domains; high error rates.

**Exfiltration**
- **Large outbound POST/PUT** to uncommon hosts; upload-shaped byte counts.  
- **High-entropy payloads** over protocols that usually carry small text (e.g., ICMP with large data, DNS TXT bloat).  
- **Time-of-day** anomalies (exfil during off-hours) and **new destinations** outside normal ASNs.

**Filters**
- HTTP beacons/errors: `http and (http.request or http.response.code >= 400)`  
- TLS client hellos (for SNI/JA3 pivot): `tls.handshake.type == 1`  
- Long-lived TCP: `tcp.analysis.ack_rtt and frame.len == 66` (proxy for keep-alive trick; adjust)  
- DNS TXT/tunnel hint: `dns and (dns.qry.type == 16 or dns.count.add_rr > 10)`  
- ICMP exfil hint (lab): `icmp and frame.len > 200`

**Artifacts to extract**
- **Export Objects → HTTP/SMB** (policy permitting)  
- **Follow {TCP/UDP} Stream**, save payloads, hash & compare with EDR findings.

---

## Triaging Alerts with PCAP

**Given an IDS alert (e.g., Suricata/Snort/Zeek)**:
1) Load the **pcap** at the alert time; apply a display filter for the alert’s 5-tuple + time window.  
2) **Follow Stream** (TCP/UDP) to view context; mark key packets.  
3) Decide: **benign**, **suspicious**, or **malicious** based on protocol semantics, frequency, and destination reputation.  
4) If encrypted, pivot on **SNI**, **cert metadata**, **flow timing** and **sizes**.  
5) Export a **minimal evidence pcapng** (marked/displayed) and annotate decisions.

**Fast scope tools**
- **Endpoints/Conversations** → top talkers and new peers.  
- **I/O Graphs** → bursts aligned with alert time.  
- **Expert Info** → malformed packets, resets, protocol violations.

---

## Color Rules & Columns for Security Work

**Columns**
- `tcp.stream`, `udp.stream`, `frame.time_delta_displayed`, `vlan.id`, `ip.ttl/ipv6.hlim`, `tcp.flags`, `http.host`, `http.request.uri`, `tls.handshake.extensions_server_name`, `dns.qry.name`, `dns.qry.type`, `dns.flags.rcode`

**Coloring ideas**
- Red: `tcp.analysis.retransmission or tcp.flags.reset==1`  
- Orange: `tcp.flags==0x000 or (tcp.flags.fin==1 and tcp.flags.ack==0)` (NULL/FIN probe)  
- Purple: `icmp or icmpv6` (errors/control)  
- Blue/Gray: `arp or (stp or lldp or cdp)` (background L2 chatter)  
- Yellow: `dns.flags.rcode > 0` (DNS errors)

---

## Mini-Labs (safe, reproducible)

1) **Scan detection lab**  
   - Run `nmap` with SYN, then FIN/NULL/Xmas against a test VM.  
   - Capture and build filters for each technique; observe ICMP type 3/code 3 flood for UDP scan.

2) **HTTP beacon**  
   - Simulate a periodic HTTP GET every 30s to a lab server.  
   - Use I/O Graph (30s bins) to see regular spikes; identify with `http.host`/URI columns.

3) **DNS tunneling demo**  
   - Use a lab tool (iodine/dnstunnel) between two hosts.  
   - Observe very long subdomain labels, TXT responses, and high query volume; compare to normal DNS.

4) **ARP poisoning (lab only)**  
   - Poison a test segment; watch competing ARP replies and route-through host; then enable DAI to see mitigation effect.

---

## Common Pitfalls → Remedies

- **Mistaking retransmissions for attacks**  
  → Check rate & clustering; correlate with loss/congestion before calling it malicious.

- **Blocking ICMP broadly “for security”**  
  → Breaks PMTUD and diagnostics; permit required types (v4 Frag Needed, v6 Packet Too Big, Time Exceeded).

- **Overreliance on names or GEO**  
  → Use IP/ASN and certificate/SNI evidence; CDNs/shared hosting can mislead attribution.

- **Assuming encryption = invisibility**  
  → Side channels (SNI, certs, timing, sizes, JA3/JA3S) still provide signal.

- **Forgetting chain-of-custody**  
  → Preserve originals, hash evidence, document vantage/time, and who handled files.

---

## Display Filters (grab bag)

- TCP scans: `tcp.flags.syn==1 and tcp.flags.ack==0`  
- FIN/NULL/Xmas: see patterns above  
- UDP scan fallout: `icmp.type==3 and icmp.code==3`  
- ARP suspect: `arp.opcode == 2 and eth.src != arp.src.hw_mac`  
- DNS tunnel hints: `dns.qry.type == 16 or frame.len > 512 and dns`  
- TLS pivot: `tls.handshake.type == 1`  
- Long-lived quiet TLS (heuristic): `tls and tcp.len == 0 and tcp.flags.ack==1` (use with stream focus)

---

## What You Should Be Able to Do After Chapter 12

- Detect and classify **recon/scans** and recognize **spoofing/MitM** signatures.  
- Pivot through encrypted traffic using **metadata and timing** to spot **beacons/C2**.  
- Identify **exfil** patterns (DNS/HTTP/ICMP) and build focused evidence pcaps.  
- Triage IDS alerts with a packet-first workflow and produce concise, defensible findings.  
- Handle packet evidence with proper **documentation and care**.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
