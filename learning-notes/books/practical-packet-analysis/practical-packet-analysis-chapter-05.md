SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 5: ADVANCED WIRESHARK FEATURES

---

## What this chapter adds to your toolkit
- Turn raw packets into **answers** using Wireshark’s higher-level tools: **Statistics**, **Expert Information**, **graphs**, **“Follow Stream”**, **Decode As**, **name resolution**, **reassembly**, **decryption hooks**, and **profiles** tuned for specific tasks.
- Build fast, repeatable **workflows** for triage (What’s talking? How much? Where is it slow? Is anything broken?).

---

## Expert Information (your early-warning dashboard)
- Opens via: Analyze → Expert Information.
- Buckets: **Errors**, **Warnings**, **Notes**, **Chats** (informational). Use it to jump straight to outliers (checksum errors, malformed packets, retransmissions, zero-window, bad TLS alerts, ICMP errors).
- Typical uses:
  - Verify “slow network” complaints: look for **tcp.analysis.retransmission**, **duplicate ACKs**, **zero-window**, **out-of-order**.
  - Verify application issues: look for **HTTP 4xx/5xx**, malformed DNS, TLS alerts (e.g., `bad_record_mac`, `handshake_failure`).
- Practice tip: sort by “Packet” column to step the narrative in order; mark key packets as you go.

---

## Statistics suite (who/what/how much)

### Protocol Hierarchy
- Stack-rank of bytes/packets per protocol. Use it to answer “What’s dominating the link?” or “Why is this capture mostly SMB/HTTP/QUIC?”.
- Fast checks:
  - Unexpected protocols (e.g., `nbns`, `bittorrent`) → scope creep / policy violations.
  - Control-plane bloat (ARP, LLDP, CDP, STP) → misconfiguration or loops.

### Conversations
- Breaks traffic into **talker pairs** at each layer (Ethernet, IPv4/v6, TCP, UDP) with packet/byte counts and durations.
- Use cases:
  - Identify **top talkers** and noisy peers.
  - Sort by **Bytes** (heaviest), **Packets** (chattiest), **Start/Duration** (burst timing).
  - Right-click → **Apply as Filter** to drill down instantly.

### Endpoints
- Per-host/port stats (as opposed to pairwise). Great for “who’s present on this segment?” and inventorying subnets, MAC OUIs, or wireless stations.

### I/O Graphs (trend visualization)
- Plot metrics over time (packets or bytes per tick, display-filter-scoped series).
- Practical series you’ll reuse:
  - `tcp.analysis.retransmission` (spikes = loss / congestion episodes)
  - `tcp.analysis.zero_window` (receiver stalls)
  - `dns` vs `http` (control vs payload pacing)
- Tuning tips:
  - Set tick interval to match RTT scale (e.g., 10–100 ms for LAN, 100–500 ms for WAN).
  - Use multiple series to compare **client-side** vs **server-side** captures.

### Flow Graph (conversation call graph)
- Visualizes request/response ordering across hosts with absolute or relative timestamps.
- Use it to explain sequencing to non-packet folks (“SYN here, first byte at t=… , server resets at …”).

---

## Follow Streams, reassembly, and “Export Objects”

### Follow TCP/UDP/SSL Stream
- Reconstructs conversations in order; reduces noise to just the session of interest.
- For TCP, ensure **reassembly** is enabled (Preferences → Protocols → TCP: “Allow subdissector to reassemble TCP streams”). This lets HTTP/2, SMB, etc., display full messages that span segments.

### Export Objects
- File → Export Objects → {HTTP, SMB, DICOM, …} to pull transferred files, images, payloads.
- Use sparingly in sensitive environments; respect data-handling policy.

---

## Decode As (correct the dissector)
- If a custom app runs on a non-standard port, Wireshark may label it “TCP” only.
- Use **Analyze → Decode As…** to force a specific dissector (e.g., decode TCP/12345 as HTTP). This instantly unlocks higher-level views and fields.

---

## Name Resolution (readable, but be deliberate)
- MAC vendor, transport service names, and DNS lookups can make traces human-friendly.
- Trade-offs:
  - May slow analysis or mislead (stale DNS, split-horizon).
  - Best practice: keep it off by default; enable selectively; document when enabled in your case notes.

---

## Graphs for TCP deep-dives (time and reliability)
- **TCP Stream Graphs** (under Statistics → TCP Stream Graph or from a TCP packet’s context menu):
  - **Time-Sequence (tcptrace)**: shows data flight over time; plateaus/gaps indicate stalls; sawtooth patterns show congestion windows.
  - **Round-Trip Time (RTT)**: rising median = path delay; spikes = loss/retrans triggers.
  - **Throughput**: bytes per interval; good for capacity vs reality comparisons.
- Workflow:
  - Baseline “healthy” streams from the same site/app.
  - Compare against problem streams to see where behavior diverges (e.g., frequent fast retransmits, small receive windows).

---

## TLS decryption hooks (when you’re allowed)
- **Pre-Master Secrets / SSLKEYLOGFILE**: set an env var on the client (`SSLKEYLOGFILE`) so browsers write session secrets; point Wireshark to the log (Preferences → Protocols → TLS → (Pre)-Master-Secret log filename). Works for modern ECDHE suites.
- **RSA private key**: legacy method for non-ephemeral RSA key exchanges only; declining relevance.
- **Kerberos/SMB** and other protocols support keytabs/creds in their dissector options (advanced; only with authorization).
- Always obtain written permission before decrypting real traffic.

---

## Profiles (task-specific workspaces)
- Bundle **columns**, **coloring rules**, **display-filter buttons**, **name-resolution**, and **protocol-specific prefs** by task (Latency, DNS, TLS/HTTP, Wireless).
- Share profiles:
  - Keep a versioned “Team-Wireshark-Profiles” folder.
  - Export/import so analyses remain consistent across machines and people.

Suggested fields to keep handy across profiles:
- `tcp.stream`, `frame.time_delta_displayed`, `vlan.id`, `ip.ttl`/`ipv6.hlim`, `tcp.flags`, `http.host`, `tls.handshake.extensions_server_name`.

---

## Small features that save big time
- **Apply as Column** from any field in the Details pane; prune columns ruthlessly.
- **Packet comments** (File → File Properties → Comments or per-packet) for chain-of-custody and narrative.
- **Saved display filters** and **buttons** (toolbar) for one-click pivots (`tcp.analysis.flags`, `dns`, `http`, `tls`, `icmp`, `arp`).
- **Coloring rules** for: retransmissions, dup-ACKs, zero-window, ICMP errors, control protocols (ARP/LLDP/CDP/STP).

---

## Workflows to memorize

### Slow app triage (client-side first)
1. Open capture; set **Time of Day (UTC)** or **Seconds Since Beginning**.
2. **Follow TCP Stream** for the suspect flow; set **Time Reference** on the client request.
3. Read deltas to first byte (TTFB) and full response; check **Expert Info** for retrans/zero-window.
4. Open **I/O Graph** with a series for `tcp.analysis.retransmission`.
5. If inconclusive, capture on the **server side** and compare deltas (is slowness on wire, client, or server?).

### “Who’s noisy?” scoping
1. **Protocol Hierarchy** → identify dominant protocols.
2. **Conversations** (TCP/UDP) → sort by **Bytes**; right-click top pairs → **Apply as Filter**.
3. Export a **focused pcapng** of just the culprits (File → Export Specified Packets → Displayed).

### HTTP/S investigation with decryption
1. Configure **SSLKEYLOGFILE** and point Wireshark TLS prefs to it.
2. Reproduce the transaction; **Follow TCP/SSL Stream**.
3. Use **Export Objects → HTTP** if policy permits.

---

## Common mistakes (and fixes)
- Depending solely on packet list scrolling.  
  Fix: Start with **Expert Info** and **Statistics** to jump to outliers/top talkers.
- Ignoring reassembly.  
  Fix: Enable TCP reassembly so higher-layer protocols decode correctly.
- Chasing names not numbers.  
  Fix: Use IP/port filters; toggle name resolution only when needed and document it.
- Misdecoding custom ports.  
  Fix: Use **Decode As…** to bind the correct dissector.

---

## Quick reference (display filters you’ll use constantly)
- TCP stream focus: `tcp.stream eq N`
- All TCP analysis flags: `tcp.analysis.flags`
- Retransmissions only: `tcp.analysis.retransmission`
- Zero-window: `tcp.analysis.zero_window`
- ICMP errors/alerts: `icmp or icmpv6`
- DNS queries only: `dns.flags.response == 0`
- HTTP errors: `http.response.code >= 400`
- TLS SNI present: `tls.handshake.extensions_server_name`
- VLAN focus: `vlan.id == 120`

---

## What you should be able to do after Chapter 5
- Use **Expert Info**, **Protocol Hierarchy**, **Conversations/Endpoints** to scope issues within minutes.  
- Visualize behavior with **I/O Graphs**, **Flow Graph**, and **TCP Stream Graphs**.  
- Reassemble payloads, **Follow Streams**, and **Export Objects** when appropriate.  
- Correct dissector guesses with **Decode As**; apply **profiles** that surface the right fields fast.  
- (Where permitted) decrypt TLS using session secrets to reveal application-layer truth.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
