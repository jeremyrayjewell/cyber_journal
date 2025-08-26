SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 11: FIGHTING A SLOW NETWORK

---

## Overview

- This chapter is about turning a vague complaint (“the network is slow”) into packet-level evidence that pinpoints **where** latency or throughput is being lost: **client**, **server**, or **the wire**.
- You’ll correlate **TCP mechanics** (loss recovery, flow/congestion control, MSS/PMTUD, windows) with **timing** (RTT, TTFB, inter-packet gaps) to explain slowness in concrete terms.

---

## Performance vocabulary you’ll use

- **RTT (Round-Trip Time):** time for a packet + its ACK; estimate from TCP timestamps or SYN↔SYN/ACK delta.
- **TTFB (Time To First Byte):** request→first server byte; separates network from server “think time.”
- **Throughput vs Goodput:** bytes per sec on the wire vs useful app payload per sec.
- **BDP (Bandwidth–Delay Product):** `link_capacity × RTT`; max in-flight data needed to fully utilize a path.
- **rwnd (Receive Window):** receiver’s buffer advertisement; limits sender if small.
- **cwnd (Congestion Window):** sender’s path estimate; shrinks on loss, grows on success.
- **MSS / PMTUD:** segment sizing vs path MTU; black-holed ICMP breaks PMTUD and stalls bulk transfers.

---

## The TCP truth you’ll look for

- **Loss & recovery:** `tcp.analysis.retransmission`, `duplicate_ack`, `fast_retransmission`, SACK blocks.
- **Receiver pressure:** `tcp.analysis.zero_window`, tiny `tcp.window_size_value`, slow `window_update`.
- **Handshake options:** MSS, Window Scale, SACK Permitted, Timestamps; these cap ceiling performance.
- **Ordering vs re-sends:** `out_of_order` isn’t always bad; repeated sequence numbers confirm true retransmits.
- **Resets & teardowns:** `tcp.flags.reset==1` (policy/timeout/misbehaving app), `fin` pairs (graceful close).

---

## Columns and views that surface slowness fast

Add these as columns:
- `frame.time_delta_displayed` (inter-packet gap you actually see)
- `tcp.stream`
- `tcp.window_size_value` (and scaled window if exposed)
- `tcp.analysis.bytes_in_flight`
- `tcp.flags`
- `ip.ttl` / `ipv6.hlim`
- App hints (when applicable): `http.response.code`, `tls.handshake.extensions_server_name`

Graphs you’ll use:
- **I/O Graphs:** series for total bytes/second, `tcp.analysis.retransmission`, and optionally `tcp.analysis.zero_window`.
- **TCP Stream Graphs:** Time–Sequence, RTT, and Throughput to visualize stalls, sawtooth patterns, and recovery.

---

## A practical decision tree (field-proven)

1) **Is the TCP handshake healthy?**  
   - Look for SYN→SYN/ACK→ACK with reasonable RTT; repeated SYNs = reachability/policy issue, not “slowness.”

2) **Where is the time going on first request?**  
   - Set **Time Reference** on the client request; measure **TTFB**.  
   - Large TTFB with clean transport → slow server/back-end.  
   - Large TTFB with retrans/dupACKs → path loss or MTU problem.

3) **Once data flows, who’s the bottleneck?**  
   - **Loss symptoms**: bursts of `dupACK`, `fast_retransmission`, rising RTT → network/congestion.  
   - **Receiver-limited**: small/zero `rwnd`, frequent `window_update` → slow app/host.  
   - **Sender-limited**: no loss, healthy rwnd, but flat goodput well under BDP → shaping/policing or tiny `cwnd` (middlebox/algorithm), sometimes app pacing.

4) **Is MTU/PMTUD broken?**  
   - Big objects stall, small ones OK; missing `Frag Needed/Packet Too Big` evidence; handshake MSS larger than path allows.  
   - Temporary mitigation: MSS clamp; real fix: allow PMTUD ICMP.

5) **Compare vantage points**  
   - Capture client-side **and** server-side (or across a TAP) and compare deltas to localize: client vs wire vs server.

---

## Recognizable slow-network patterns (and what to do)

- **Lossy path (congestion or physical):**  
  Evidence: `dupACK` trains, `fast_retransmission`, stepwise RTT spikes, throughput seesaw.  
  Action: verify link errors/QoS policies, remove oversubscription, test without WAN shapers, consider QoS tuning.

- **Receiver buffer pressure (rwnd-limited):**  
  Evidence: `zero_window`, tiny windows, long think-times before `window_update`.  
  Action: fix slow consumer/app, increase socket buffers, resolve storage thrash.

- **PMTUD black hole:**  
  Evidence: small objects fine; large transfers stall; no ICMP “Frag Needed/Too Big”; MSS too large for path.  
  Action: enable required ICMP, set MSS clamp on tunnel/WAN edge, validate with jumbo-ish payloads.

- **Bufferbloat / over-queuing:**  
  Evidence: RTT climbs during sustained transfer with little loss; TTFB okay but steady degradation under load.  
  Action: enforce AQM/CoDel/FQ policies, right-size queues, separate traffic classes.

- **Shaping/policing / rate limiters:**  
  Evidence: clean transport but hard throughput ceiling; occasional periodic loss coinciding with token bucket refill.  
  Action: confirm provider policy; align app expectations; tune window sizes and parallelism.

- **Middlebox resets/timeouts:**  
  Evidence: `tcp.flags.reset==1` from a VIP/firewall; idle timers or DPI hits.  
  Action: extend idle timers; bypass features for the flow; verify SSL/TLS inspections aren’t breaking sessions.

- **Asymmetric routing / reordering:**  
  Evidence: frequent `out_of_order` without high retrans; TTL/hop differences by direction.  
  Action: capture at both sides or inside core; prefer vantage where both directions are visible; correct ECMP/hashing if needed.

---

## Quick math to sanity-check expectations

- **Throughput upper bound (ideal):** approximately `min(rwnd, cwnd) / RTT`.  
- **BDP target:** if BDP is 4 MB and the receiver only advertises ~512 KB, you can’t fill the pipe without scaling/bigger buffers.  
- **RTT realism:** WAN RTT of 80–120 ms is normal transcontinent; “LAN RTT” should be single-digit ms.

Use these to explain “why it tops out at X MB/s” even with zero loss.

---

## Focused workflows you can paste into a runbook

- **Slow download (is it network or server?)**  
  - Columns: delta, bytes-in-flight, rwnd, flags.  
  - Graph: I/O (bytes/s) + retrans series.  
  - If retrans spikes → network. If no retrans and TTFB or server inter-chunk gaps are large → backend.

- **TLS handshake stalls**  
  - Verify 3-way handshake completes.  
  - Compare MSS with path MTU; check for missing PMTUD ICMP; look for mid-handshake retrans.  
  - Try smaller record size or clamp MSS at edge to confirm.

- **WAN “only slow at lunchtime”**  
  - I/O Graph in 1 s bins: bytes/s vs retrans; correlate with DSCP/QoS class loads.  
  - Check provider shaping marks/policing counters; consider flow pinning changes or class budgets.

- **Remote file copy inconsistent**  
  - Plot RTT graph for the stream; if RTT oscillates with queue fill, suspect bufferbloat.  
  - If RTT steady but goodput flat and below BDP, look for shaping or small windows.

---

## Display filters you’ll reuse constantly

- Loss/recovery: `tcp.analysis.retransmission or tcp.analysis.fast_retransmission`  
- Receiver stalls: `tcp.analysis.zero_window or tcp.window_size_value == 0`  
- One conversation: `tcp.stream eq N`  
- Handshake options (check SYN/SYN-ACK): `tcp.flags.syn==1`  
- PMTUD hints (v4/v6): `icmp.type==3 and icmp.code==4 or icmpv6.type==2`  
- Resets: `tcp.flags.reset==1`

---

## Mini-labs (hands-on proofs)

- **Loss vs pressure:** run a large transfer twice—once with WAN loss injected (netem), once with an artificially small receive buffer. Compare retrans spikes vs zero-window behavior.
- **PMTUD failure:** block ICMP Frag-Needed/Too-Big on a test path; observe stalls for larger responses; then enable MSS clamping and confirm recovery.
- **Bufferbloat demo:** saturate an uplink with bulk traffic; run small pings; watch RTT inflate and then normalize with AQM enabled.

---

## Common pitfalls → quick fixes

- Assuming “slow = packet loss” every time.  
  Fix: check rwnd/zero-window and server think-time first.
- Reading retrans as failure when it’s a one-off.  
  Fix: judge **rate and clustering** of retrans, not isolated events.
- Ignoring handshake options.  
  Fix: MSS and Window Scale often explain ceilings; verify before deep dives.
- Comparing deltas across different filter contexts.  
  Fix: rely on `frame.time_delta_displayed` and record the filter used when measuring.
- Blaming the WAN with only one vantage.  
  Fix: collect **client and server** captures (or a TAP in the middle) and compare.

---

## What you should be able to do after Chapter 11

- Turn “slow” into measurable **TTFB**, **RTT**, **goodput**, and **error indicators**.  
- Identify loss-driven slowness vs receiver/app bottlenecks vs MTU/PMTUD failures.  
- Explain throughput ceilings using **BDP**, **MSS**, and **window scaling**.  
- Build concise graphs and filters that make slowness root causes obvious to others.  
- Propose targeted fixes (buffers, MSS clamp, QoS/AQM, policy changes) and verify with before/after captures.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
