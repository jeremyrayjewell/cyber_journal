SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 8: TRANSPORT LAYER PROTOCOLS

---

## Overview

- The transport layer provides **end-to-end conversations** atop IP. In practice you’ll analyze mainly **TCP** (reliable, connection-oriented) and **UDP** (best-effort, connectionless).
- Mastering **flags, sequence/ack numbers, windows, MSS/PMTUD, retransmissions, and timing** is essential for diagnosing slowness, resets, and reachability.

---

## Ports, Sockets, and Conversations

- A **socket** is `{IP, Port, Protocol}`; a **connection** (TCP) is identified by the **5-tuple** `{src IP, src port, dst IP, dst port, protocol}`.
- **Well-known ports** (0–1023), **registered** (1024–49151), **ephemeral** (49152+ by default on many OSes; ranges vary).
- Useful columns/filters:
  - Columns: `tcp.stream`, `tcp.seq`, `tcp.ack`, `tcp.window_size_value`, `tcp.analysis.bytes_in_flight`
  - Filters: `tcp.stream eq N`, `tcp.port == 443`, `udp.port == 53`

---

## UDP (User Datagram Protocol)

- **Connectionless, best effort**, minimal header (src/dst port, length, checksum).
- No sequencing, no retransmission, no built-in congestion control → relies on app logic.
- Typical protocols: **DNS**, **DHCP**, **SNMP**, **RTP/VoIP**, some gaming/streaming apps.
- Troubleshooting patterns:
  - **Port unreachable** → ICMP type 3/code 3 from receiver when no listener exists.
  - **One-way silence** → server replies dropped by ACL/NAT, or asymmetric routing.
- Filters: `udp`, `icmp.type==3 and icmp.code==3` (UDP port unreachable).

---

## TCP Fundamentals

### Handshake & Teardown

- **3-way handshake:** `SYN` → `SYN,ACK` → `ACK`.  
  - MSS, Window Scale, SACK Permitted, and Timestamps are often negotiated here (TCP options).
- **Graceful close:** `FIN`/`ACK` on each side; **Abortive close:** `RST`.
- Filters:  
  - Handshake: `tcp.flags.syn==1 and tcp.flags.ack==0` (client SYN)  
  - Resets: `tcp.flags.reset==1`  
  - Teardown: `tcp.flags.fin==1`

### Sequence, ACKs, and Data Flow

- **Sequence numbers** count bytes sent; **ACK** is “next byte I expect”.
- **Bytes in flight** (not yet ACKed) reflect the sender’s current outstanding data; spikes then flat lines suggest stalls.

### Flow Control (Receiver-side)

- **Advertised Receive Window (RWND):** how much more data the receiver can accept.
- **Window scaling** (option): multiplies the 16-bit window to support high-BDP paths.
- **Zero-window**: receiver buffer full → sender must pause; **window update** resumes.
- Key fields/filters: `tcp.window_size_value`, `tcp.analysis.zero_window`, `tcp.window_size_scalefactor`.

### Congestion Control (Network-side)

- Sender detects loss via **RTO** (timeout) or **DupACKs**:  
  - **Fast retransmit** after ≥3 DupACKs (no timeout).  
  - **Exponential backoff** on repeated timeouts.
- Indicators: `tcp.analysis.retransmission`, `tcp.analysis.fast_retransmission`, `tcp.analysis.duplicate_ack`.

### Important TCP Options (seen in the SYN/SYN-ACK)

- **MSS**: maximum segment size (payload, excludes headers). Often `MTU - 40` (IPv4+TCP).
- **Window Scale**: enables large RWND (high-speed paths).
- **SACK Permitted**: allows selective ACK of non-contiguous blocks (efficient recovery).
- **Timestamps**: RTT measurement and PAWS protection.
- Filters:  
  - `tcp.options.mss_val`  
  - `tcp.options.wscale.shift`  
  - `tcp.option_kind == 4` (SACK-Permitted)  
  - `tcp.options.timestamp.tsval`

---

## Interactions with MTU/PMTUD

- With **DF=1** and path MTU smaller than segment size, a router should send **ICMP Frag Needed** (v4) / **Packet Too Big** (v6). If blocked, large transfers **stall** (PMTUD black hole).
- Symptoms: small requests succeed; bulk data or TLS handshake fragments stall; sporadic `RST` from middleboxes.
- Confirm with:  
  - ICMP evidence (`icmp.type==3 && icmp.code==4` or `icmpv6.type==2`)  
  - Handshake options (MSS) and segment sizes vs observed MTU.

---

## Common TCP Pathologies (What They Look Like)

- **SYN retransmissions** (server unreachable or filtered): repeating client SYNs, increasing intervals.
- **SYN flood / backlog issues**: many half-open connections; server sends SYN/ACK but never gets final ACK (context matters).
- **Zero-window stalls**: `tcp.analysis.zero_window` followed by long gaps until `window_update`.
- **High loss / congested path**: bursts of `duplicate_ack`, `fast_retransmission`, rising RTT; I/O Graph spikes.
- **Out-of-order vs retransmission**:  
  - Out-of-order often transient on parallel paths;  
  - Retransmissions repeat the same sequence numbers after loss (Wireshark tracks both).
- **RST storms**: abrupt terminations by endpoints or middleboxes (policy, idle timers, malformed traffic).

---

## Practical Workflows

1) **Is it the network or the app? (slow download)**  
   - Add columns: delta time, RWND, bytes-in-flight.  
   - Look for **retransmissions** vs **zero-window**.  
   - If retrans heavy → likely path issues; if zero-window → receiver/app slow.

2) **TLS handshake stalls**  
   - Follow TCP Stream; ensure full 3-way handshake completed.  
   - Check MSS vs path MTU; look for missing ICMP “Frag Needed/Packet Too Big”.

3) **Intermittent resets**  
   - Filter `tcp.flags.reset==1`; group by `tcp.stream`.  
   - Identify who sent the RST (src IP) and preceding context (idle timeout vs immediate policy block).

4) **UDP service reachability**  
   - Send a test query; if host replies with **ICMP Port Unreachable**, no listener on that port.  
   - If no reply at all, suspect ACL/NAT asymmetry.

---

## Display Filters You’ll Reuse

- TCP handshakes: `tcp.flags.syn==1 and tcp.flags.ack==0`  
- Retransmissions: `tcp.analysis.retransmission or tcp.analysis.fast_retransmission`  
- Receiver stalls: `tcp.analysis.zero_window or tcp.window_size_value == 0`  
- SACK seen: `tcp.option_kind == 5 or tcp.options.sack_le`  
- Resets: `tcp.flags.reset==1`  
- UDP port unreachable: `icmp.type==3 and icmp.code==3`  
- Single conversation: `tcp.stream eq N` or `udp.stream eq N`

---

## Mini-Labs

- **Handshake Explorer:** capture a web fetch; locate SYN, SYN/ACK, ACK; note **MSS**, **WS**, **SACK-Permitted**, **TS**.  
- **Loss & Recovery:** transfer a large file across a congested link; chart `tcp.analysis.retransmission` in I/O Graph (1 s bins).  
- **Zero-Window Demo:** throttle receive app or use a tiny receive buffer; observe zero-window and window updates.  
- **UDP Unreachable:** send a UDP probe to a closed port; verify ICMP Port Unreachable.

---

## What You Should Be Able to Do After Chapter 8

- Read and interpret **TCP handshakes, options, windows, and flags**; separate **congestion/loss** from **receiver pressure**.  
- Recognize **RST, FIN**, retransmissions, and out-of-order traffic and explain their causes.  
- Tie **MSS/PMTUD** and ICMP behavior to real throughput problems.  
- Triage **UDP** issues using ICMP evidence and simple reachability tests.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
