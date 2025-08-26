SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 3: INTRODUCTION TO WIRESHARK

---

## What You Set Up in This Chapter

- Install and launch Wireshark; ensure capture permissions and drivers are correct.
- Learn the **three-pane UI** and how to start/stop/save captures.
- Understand **capture filters (BPF)** vs **display filters (Wireshark)**.
- Configure **columns**, **profiles**, **coloring rules**, and **timestamps** so packets tell a story at a glance.

---

## Installing & Capture Permissions (Quick Guide)

- **Windows:** install Wireshark with **Npcap** (packet capture driver). Allow “WinPcap API-compatible mode” if you need legacy tools.
- **macOS:** install via the official package or Homebrew; grant permission for packet capture when prompted.
- **Linux:** install Wireshark and allow non-root capture (preferred):
  - Add your user to the `wireshark` group, then log out/in.
  - Ensure `dumpcap` has the needed capabilities (usually set by the package).
- **If you can’t see interfaces or capture fails:** it’s almost always a driver/permissions issue—fix that first.

---

## The Wireshark UI (Three Panes, One Story)

1) **Packet List** (top)  
   - One row per packet; columns are your “dashboard” (time, src/dst, protocol, length, info).  
   - You can **mark** packets, **set a time reference** on a packet, and **follow** conversations from here.

2) **Packet Details** (middle)  
   - Protocol tree view; expand to see header fields (frame, Ethernet, VLAN, IP, TCP/UDP, application).

3) **Packet Bytes** (bottom)  
   - Hex + ASCII view; highlights the exact bytes corresponding to the selected field in the middle pane.

**Power move:** Right-click a field → **Apply as Column** to expose it in the Packet List.

---

## First Capture (Minimal, Repeatable Workflow)

1) Choose the correct **interface** (wired, Wi-Fi, virtual adapters).  
2) Ensure **Promiscuous mode** is enabled (Preferences → Capture) for wired; for Wi-Fi, normal mode only sees your own traffic unless using monitor mode with the right adapter/OS.  
3) Click **Start**. Reproduce the issue or generate test traffic.  
4) Click **Stop**, then **File → Save As** (`.pcapng` preferred).  
5) Add an **annotation** (File → File Properties → Comments) describing where/when/how you captured.

**Good hygiene:** Use **ring buffers / file rotation** for long captures (Capture Options → Output) so you don’t produce a 40 GB single file.

---

## Capture Filters vs Display Filters (Don’t Mix Them Up)

- **Capture filters (BPF)**: applied **before** writing to disk; syntax like `host 10.0.0.5 and tcp port 443`. Use sparingly—don’t filter out data you may later need.
- **Display filters (Wireshark)**: post-capture; extremely expressive and safe for analysis. Examples:
  - `ip.addr == 10.0.0.5`
  - `tcp.port == 443`
  - `dns && ip.ttl < 10`
  - `tcp.analysis.flags` (useful umbrella for retransmissions, dup ACKs, zero window, etc.)

**Rule of thumb:** Capture wide (with a light BPF if needed for sheer volume), slice narrow with display filters.

---

## Columns That Make Troubleshooting Faster

Add these once and save them in a profile:

- **Time** (set to “Seconds Since First Displayed Packet” or “Time of Day”)
- **Source**, **Destination**
- **Protocol**, **Length**
- **Info**
- **TCP Stream** (`tcp.stream`) — to group packets by conversation
- **TCP Flags** (`tcp.flags`) — use the field’s string version or individual bits
- **Delta Time Displayed** (`frame.time_delta_displayed`) — inter-packet gap
- **VLAN ID** (`vlan.id`) — if you expect tagging
- **TTL / Hop Limit** (`ip.ttl`, `ipv6.hlim`) — quick path health indicator
- **TCP Window Size** (`tcp.window_size_value`) and **Calculated Window** (`tcp.window_size` in some builds)
- **HTTP Host** (`http.host`) or **SNI** (`tls.handshake.extensions_server_name`) — when doing web triage

How to add: Right-click a field in the Details pane → **Apply as Column**, then re-order in **Preferences → Appearance → Columns**.

---

## Profiles (Task-Focused Workspaces)

Create separate **profiles** for use-cases (e.g., “Latency,” “DNS,” “TLS,” “Wireless”):

- Each profile can have its own **columns**, **coloring rules**, **display filter buttons**, and **name-resolution** settings.
- Switch profiles from the status bar; export/import profiles to share with teammates.

Suggested profiles:
- **Latency/Throughput:** adds delta time, TCP windows, `tcp.analysis.flags`.
- **DNS:** columns for `dns.qry.name`, `dns.qry.type`, `dns.flags.response`.
- **TLS/HTTP:** SNI, HTTP host, response codes.
- **Wireless:** RSSI, channel, data rate (when available via radiotap/monitor mode).

---

## Coloring Rules (Visual Triaging)

Color by protocol and by **conditions** that signal trouble:

- **TCP problems:** `tcp.analysis.retransmission`, `tcp.analysis.duplicate_ack`, `tcp.analysis.zero_window`
- **Errors/alerts:** `icmp or icmpv6`
- **Control noise:** `stp or lldp or cdp or arp`
- **High-latency markers:** `frame.time_delta_displayed > 0.250` (example threshold)

Keep your palette small and meaningful; too many colors become noise.

---

## Time Handling That Avoids Confusion

- **Display format:** Pick one across the team (UTC “Time of Day” is defensible in multi-site work).
- **Set Time Reference:** Right-click a key packet → “Set/Unset Time Reference” → zeros “Time” for everything after.
- **Delta columns:** Use `frame.time_delta_displayed` to see gaps between adjacent displayed packets (respects your filters).

Consistency in time handling makes multi-capture comparisons (client-side vs server-side) far easier.

---

## Name Resolution (Use Carefully)

- **Transport/Network name resolution** (resolving MAC OUIs, ports, or IPs to names) can aid readability but risks confusion:
  - Reverse DNS may be slow/wrong; consider disabling during live capture.
  - Prefer known hosts files or local notes for critical endpoints.
- Toggle from **View → Name Resolution** or in **Preferences**.

---

## Small But Mighty Features to Start Using Now

- **Follow TCP/UDP Stream:** reconstructs a conversation; great for HTTP/S metadata, SMTP, etc.
- **Find/Mark:** search for strings, hex, or fields; mark key packets to build a narrative.
- **Export Objects** (HTTP/SMB/…): pull retrieved files or payloads when relevant.
- **Protocol Hierarchy** (Statistics): shows traffic makeup, helps spot bloat/outliers quickly.
- **Endpoints/Conversations** (Statistics): “top talkers” and heavy flows—excellent scoping tools.

(Full deep-dive on statistics typically appears in later chapters, but you’ll touch them here.)

---

## Minimal Starter Kit (Repeatable Setup)

1) Install Wireshark + driver; fix permissions until you can see interfaces.  
2) Create a **“Baseline” profile**:
   - Columns: time (since first), src/dst, proto, len, info, tcp.stream, vlan.id, ip.ttl, frame.time_delta_displayed.
   - Coloring: retransmissions (red), dup ACKs (orange), ARP/LLDP/STP/CDP (grey/blue), ICMP (purple), TLS handshake (green).
   - Display filter buttons: `tcp.analysis.flags`, `dns`, `http`, `tls`, `icmp`, `arp`.
3) Set **Name Resolution** off by default; enable only when needed.  
4) Practice **Follow Stream** and **Time Reference** on a 30-second sample capture.  
5) Save the profile; export it so you can import on other machines.

---

## Common Mistakes (and the Fix)

- **Mixing filter languages** (typing Wireshark display filters into the capture filter box).  
  Fix: Remember BPF for capture, Wireshark language for display.
- **Capturing too narrowly** (over-aggressive BPF).  
  Fix: Capture wider; constrain with display filters during analysis.
- **Gigantic single files** that crash tools.  
  Fix: Use ring buffers/rotation by size/time; split captures per host/segment.
- **Trusting DNS/hostnames blindly.**  
  Fix: Disable name resolution during capture; annotate known IPs manually.
- **Ignoring offload artifacts** (“bad checksum” on every packet).  
  Fix: Recognize offload effects; disable offloads only if they impede analysis.

---

## Quick Reference: Example Filters

**Capture (BPF) examples**
- Only one host: `host 10.20.30.40`
- Only web to/from a host: `host 10.20.30.40 and (tcp port 80 or 443)`
- Only VLAN 120 (platform-dependent): `vlan 120`

**Display (Wireshark) examples**
- Host focus: `ip.addr == 10.20.30.40`
- One TCP conversation: `tcp.stream eq 5`
- DNS queries only: `dns.flags.response == 0`
- TLS with SNI present: `tls.handshake.extensions_server_name`
- TCP trouble: `tcp.analysis.flags`
- ICMP trouble tickets: `icmp or icmpv6`

---

## What You Should Be Able to Do After Chapter 3

- Launch Wireshark and capture on the right interface with proper permissions.  
- Save, reopen, and navigate captures confidently using the three panes.  
- Build and switch **profiles** to match the task at hand.  
- Use **display filters**, **columns**, **coloring**, and **time tools** to surface the story inside packets.  
- Avoid typical traps (filter confusion, offload artifacts, name-resolution misreads).

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
