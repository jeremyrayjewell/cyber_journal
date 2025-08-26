SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 4: WORKING WITH CAPTURED PACKETS

---

## Opening, Saving, and Managing Capture Files

- **Open** existing traces with `File → Open…` (supports `.pcapng`, `.pcap`, and many others).  
  - Prefer **PCAPNG**: it stores per-interface metadata, comments, dropped-packet counters, name-resolution results, and capture hosts—useful for forensics and multi-NIC captures.
- **Save / Save As…** (`.pcapng` recommended). Add **file comments** via `File → File Properties → Comments` to record where/when/how you captured.
- **Export** subsets when you only need a slice:
  - `File → Export Specified Packets…` (by display filter, marked packets, or packet ranges).
  - `File → Export Packet Dissections…` (Text/CSV/JSON/PDML) for reports or scripting.
  - `File → Export Objects → {HTTP, SMB, …}` to extract transferred files/payloads.
- **Split / rotate** long captures at creation time (ring buffers), or later with `Editcap/Mergecap` (CLI companions) if you need to trim or merge files.

---

## Navigating Packets Efficiently

- **Packet list → details → bytes**: select a row (summary), expand headers/fields (details), inspect raw hex/ASCII (bytes).  
- **Find packets**: `Edit → Find Packet…` by **Display filter**, **String**, or **Hex**.  
  - Use this to jump to first SYN, DNS query for a domain, the first 404, etc.
- **Go To Packet…**: jump by absolute packet number (helpful after reading Expert Info or Conversations tables that reference packet IDs).
- **Marking**: right-click a packet → **Mark/Unmark**.  
  - Great for building a narrative (SYN, first byte of response, server error, teardown).  
  - Combine with **Export Specified Packets → Marked** to produce a focused evidence file.
- **Follow Stream** (TCP/UDP): reconstruct request/response payloads in order; filter to just that conversation; save the stream if needed.

---

## Time Handling (Getting the Story Straight)

- **Choose a display format**: `View → Time Display Format`  
  - Common picks: **Time of Day (UTC)** for cross-site work, or **Seconds Since Beginning of Capture** for latency and sequencing.
- **Delta time columns**: add `frame.time_delta_displayed` to see the gap between adjacent **displayed** packets (respects your filters).  
  - Use for spotting pauses, server think-time, or microbursts.
- **Set Time Reference**: right-click a key packet → **Set/Unset Time Reference**.  
  - All subsequent times show **+Δ** from that moment (e.g., t=0 at the SYN, measure first byte time, TTFB, etc.).
- **Time Shift**: `Edit → Time Shift…` to align captures from different vantage points (e.g., client-side and server-side traces taken simultaneously).

---

## Filters: Capture vs Display (Working with What You Already Captured)

- **Capture filters (BPF)** were decided before the file existed; after the fact, you’ll mostly use **display filters** to slice the view.
- **Display filter basics**:
  - Equality/inequality: `ip.addr == 10.0.0.5`, `tcp.port != 80`
  - Logical ops & grouping: `and`, `or`, `not`, parentheses
  - Field presence: `_ws.col.Info` contains text, or simply `http` to show all HTTP
  - Useful predicates:  
    - `contains` (byte-string search in fields/byte ranges)  
    - `matches` (regex on text fields)  
  - Examples you’ll use constantly:
    - Host focus: `ip.addr == 10.20.30.40`
    - One conversation: `tcp.stream eq 7`
    - Retransmissions & friends: `tcp.analysis.flags`
    - DNS queries only: `dns.flags.response == 0`
    - Filter to a time window (right-click a packet → **Prepare a Filter** by time, or use `frame.time` comparisons)

---

## Columns, Coloring, and Profiles (Make the File Work for You)

- **Columns** (apply fields as columns from the Details pane):
  - Time (since first displayed), Source, Destination, Protocol, Length, Info
  - **tcp.stream**, **tcp.flags**, **frame.time_delta_displayed**
  - **vlan.id**, **ip.ttl / ipv6.hlim**, **http.host** or **tls.handshake.extensions_server_name**
- **Coloring rules** (visual triage):
  - Errors/alerts: `icmp or icmpv6`
  - TCP trouble: `tcp.analysis.retransmission`, `tcp.analysis.duplicate_ack`, `tcp.analysis.zero_window`
  - Control-plane noise: `stp or lldp or cdp or arp`
- **Profiles**: save different column sets, filters, and coloring for **Latency**, **DNS**, **TLS/HTTP**, **Wireless**. Export/import to stay consistent across machines.

---

## File Operations You’ll Actually Use

- **Export Specified Packets** by:
  - **Displayed** (whatever your current display filter shows)
  - **Marked** (hand-picked story packets)
  - **Packet range** (e.g., 100–250 for a handshake to teardown slice)
- **Export Packet Dissections** as:
  - **Plain text** (readable report)
  - **CSV** (for spreadsheets/graphs)
  - **JSON/PDML** (for automation, parsing in scripts)
- **Print**: `File → Print…` with options to include summary lines, details, and/or raw bytes—useful for appendices in incident reports.

---

## Name Resolution (Readable vs Reliable)

- Toggle under `View → Name Resolution` or Preferences.  
  - **Pros**: human-friendly (DNS names, vendor OUIs, service names).  
  - **Cons**: can be slow or misleading (stale DNS, split-horizon).  
- Best practice: keep it **off during capture**; enable selectively while analyzing. For critical endpoints, annotate known IPs in your notes rather than trusting live lookups.

---

## Practical Mini-Workflows with Existing Files

1. **Build a clean evidence subset**
   - Apply a display filter for the incident scope.
   - Mark the handshake, the first server response, the error, and the teardown.
   - `Export Specified Packets → Marked` to a small `.pcapng` you can share.

2. **Measure server think-time & TTFB**
   - Set time reference on client’s **HTTP request**.
   - Find first **HTTP/2 HEADERS (200)** or **HTTP/1.1 200 OK** from server.
   - Read the delta column and record it; repeat across multiple requests to trend.

3. **Align two vantage points**
   - Open client-side and server-side captures.
   - Use `Edit → Time Shift…` to align their SYNs to t=0.
   - Compare deltas to localize latency (client stack vs wire vs server stack).

---

## Common Mistakes (and Quick Fixes)

- **Working from a giant single file** → you miss the forest for the trees.  
  - Fix: filter to scope; mark key packets; export a focused subset.
- **Trusting names over numbers** → DNS/SNI can mislead.  
  - Fix: filter by IP/port and annotate known mappings.
- **Confusing capture vs display filters** → nothing matches or you drop needed traffic.  
  - Fix: remember BPF (capture) vs Wireshark (display); after capture, use **display** filters.
- **Comparing deltas across filtered views** incorrectly.  
  - Fix: use `frame.time_delta_displayed` (respects your filtered view) and clearly note your filter context.

---

## Quick Reference: Display Filters for Post-Capture Work

- Host / subnet focus:  
  - `ip.addr == 10.20.30.40`  
  - `ip.addr == 10.20.30.0/24`
- One TCP stream: `tcp.stream eq 5`
- TLS/SNI present: `tls.handshake.extensions_server_name`
- HTTP response codes: `http.response.code >= 400`
- TCP issues: `tcp.analysis.flags`
- DNS queries: `dns.flags.response == 0`
- ICMP errors: `icmp.type >= 3 and icmp.type <= 5`

---

## What You Should Be Able to Do After Chapter 4

- Open large captures, navigate quickly, and isolate exactly what matters.  
- Use **Find**, **Go To**, **Mark**, **Set Time Reference**, and **Time Shift** to tell a coherent, time-accurate story.  
- Export clean subsets and human-readable dissections for tickets/reports.  
- Configure columns/coloring/profiles so your captures are immediately informative.  
- Avoid name-resolution traps and filter confusion when working from existing files.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
