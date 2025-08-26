SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 7: NETWORK LAYER PROTOCOLS

---

## Overview

- The **network layer** is where packets are addressed and routed between networks. In practice you’ll work with **ARP (L2 helper), IPv4, IPv6, and ICMP/ICMPv6** constantly.
- Skills from this chapter: reading ARP handshakes, interpreting IPv4/v6 headers, recognizing fragmentation/PMTUD issues, and using ICMP types/codes (including how **traceroute** works) to localize path problems.

---

## ARP (Address Resolution Protocol) — Bridging IP ↔ MAC on a LAN

**Purpose**
- ARP maps an IPv4 address to a Layer-2 (MAC) address within a broadcast domain so frames can be delivered on Ethernet/Wi-Fi.

**Packet types you’ll see**
- **ARP Request:** “Who has 192.168.1.10? Tell 192.168.1.5.”
- **ARP Reply:** “192.168.1.10 is at aa:bb:cc:dd:ee:ff.”
- **Gratuitous ARP (GARP):** sender announces/claims its own IP→MAC mapping (used during boot, IP change, or conflict detection).

**Common patterns in captures**
- **Normal resolution:** Host A broadcasts a request; the owner unicasts a reply.
- **Cache churn:** Repeated ARP requests for the same IP indicate cache expiry, host rebooting, or L2 instability.
- **Conflicts / poisoning signs:** Multiple **different** MACs claiming the same IP in a short period; alternating replies from two MACs; frequent GARP storms.

**Display filter ideas**
- `arp`
- `arp.opcode == 1`  (requests)
- `arp.opcode == 2`  (replies)
- `arp.duplicate-address-detected == 1` (if present)

**Troubleshooting tips**
- If an IPv4 host “can’t reach” a peer on the same subnet, check for **no ARP reply**, duplicate IPs, or switch port security features blocking ARP.

---

## IPv4 — The Workhorse

**Header fields you should recognize at a glance**
- **Version (4)**, **Header Length (IHL)**, **DSCP/ECN**, **Total Length**, **Identification**, **Flags** (DF/More Fragments), **Fragment Offset**, **TTL**, **Protocol** (e.g., 1=ICMP, 6=TCP, 17=UDP), **Header Checksum**, **Source/Destination**.
- **TTL** decrements by 1 at each hop; if it reaches 0, a router sends **ICMP Time Exceeded**.
- **DF (Don’t Fragment)** controls fragmentation; modern stacks prefer **DF=1** and rely on **Path MTU Discovery (PMTUD)**.

**Fragmentation and reassembly**
- A large IP packet may be split into multiple fragments when the path MTU is smaller than the packet size and DF=0.
- Fragments share the same **Identification**; first fragment carries L4 headers; later fragments start mid-payload.
- Excessive fragmentation → throughput loss; “missing middle” fragments → reassembly failures.
- Prefer **PMTUD** over fragmentation.

**Path MTU Discovery (PMTUD)**
- Sender sets **DF=1** and transmits. If a hop can’t forward due to small MTU, it returns **ICMP Destination Unreachable (Fragmentation Needed)** with the next-hop MTU.
- If these ICMPs are **filtered**, PMTUD breaks → symptoms: connection stalls on larger payloads; small pings work, big transfers hang.

**Useful display filters**
- `ip`  
- `ip.flags.df == 1`  
- `ip.flags.mf == 1` or `ip.frag_offset > 0` (fragments)  
- `ip.ttl <= 5` (late-path view; handy in big networks)  
- `icmp.type == 3 and icmp.code == 4` (Frag Needed for PMTUD)

---

## IPv6 — Cleaner Header, Different Habits

**Key differences from IPv4**
- **128-bit addresses**, no broadcast (uses **multicast** instead).
- **No header checksum** (relies on upper layers and link checks).
- **Extension headers** carry options (Routing, Fragment, AH/ESP, etc.).
- **Neighbor Discovery (ND)** replaces ARP using **ICMPv6** (Router Solicitation/Advertisement, Neighbor Solicitation/Advertisement, Redirect).

**What to watch in captures**
- **Hop Limit** (IPv6’s TTL analog).
- **Extension headers**: ensure order/reasonable size; some middleboxes mishandle them.
- **ICMPv6 is essential** (don’t block it blindly): MTU discovery, ND, error signaling.
- **SLAAC vs DHCPv6** address assignment flows.

**Useful display filters**
- `ipv6`
- `ipv6.hlim <= 5`
- `icmpv6`
- `icmpv6.type == 2` (Router Advertisement)
- `icmpv6.type == 135` / `136` (Neighbor Solicitation/Advertisement)
- `ipv6.nxt == 44` (Fragment header)

---

## ICMP / ICMPv6 — The Control & Error Signaling Plane

**ICMP (v4) common types/codes**
- **Echo Request/Reply** (8/0) — basic ping.
- **Destination Unreachable** (type 3; important codes):
  - **0** Network Unreachable
  - **1** Host Unreachable
  - **3** Port Unreachable (e.g., UDP probe to closed port)
  - **4** Fragmentation Needed (PMTUD signal; includes next-hop MTU)
- **Time Exceeded** (type 11) — TTL hit zero; used by traceroute.

**ICMPv6 essentials**
- **Echo Request/Reply** (128/129)
- **Destination Unreachable** (1)
- **Packet Too Big** (2) — PMTUD for IPv6 (includes MTU)
- **Time Exceeded** (3)
- **Parameter Problem** (4)
- **ND messages** (Router/Neighbor Solicitations & Advertisements, Redirect)

**Display filter ideas**
- `icmp or icmpv6`
- `icmp.type == 3 and icmp.code == 4` (v4 PMTUD)
- `icmpv6.type == 2` (v6 Packet Too Big)
- `icmp.type == 11 or icmpv6.type == 3` (Time Exceeded)

**Security & hygiene**
- Don’t blanket-block ICMP; allow essential types (PMTUD, Time Exceeded). Blocking breaks performance and diagnostics.

---

## How Traceroute Works (and What to Look For)

**Mechanism**
- Sends probes with **TTL/Hop-Limit = 1, 2, 3…** so each hop expires one set and returns **Time Exceeded**.
- Classic UNIX traceroute uses **UDP to high ports**; Windows `tracert` historically used **ICMP Echo**; many tools can use **TCP SYN** or **UDP** for firewall traversal.

**In captures**
- Probe from the source with TTL=N → router N sends Time Exceeded back.
- Some routers don’t respond to expired TTLs → you see `* * *` (but traffic still forwards).
- Late hops may show policy filtering; asymmetry is common (return path can differ).

**Filters**
- `icmp.type == 11` or `icmpv6.type == 3` (the replies)
- Drill by probe 5-tuple to line up requests ↔ replies.

---

## Practical Workflows (Network Layer)

**1) “Host can’t reach host” on same subnet**
- Filter: `arp or (ip.addr == A and ip.addr == B)`
- Expect ARP request from A, reply from B. If no reply → B offline/filtered/duplicate IP.
- Look for conflicting ARP replies (two MACs for same IP).

**2) “Downloads hang; small pings OK” (PMTUD break)**
- Filter: `icmp.type == 3 and icmp.code == 4` (v4) or `icmpv6.type == 2` (v6)
- If absent during large transfers, a middlebox is likely **dropping PMTUD** messages.
- Workarounds: lower MSS (temporary), fix firewalls/ACLs to allow PMTUD ICMP.

**3) “Intermittent timeouts across WAN”**
- Add column for `ip.ttl`/`ipv6.hlim`.
- Check `tcp.analysis.retransmission` spikes alongside `icmp.type == 11` responses.
- Look for routing changes (TTL swings) and asymmetry.

**4) “Why is app slow only cross-site?”**
- Compare client-side vs server-side captures:
  - Observe **TTL/Hop-Limit**, **RTT**, and **ICMP errors** on each side.
  - If server never receives large segments but client sends them, suspect **path MTU black-hole** in between.

---

## Columns & Quick Filters You’ll Reuse

**Columns to add for this layer**
- `ip.ttl` and/or `ipv6.hlim`
- `ip.flags` and `ip.frag_offset`
- `icmp.type` / `icmp.code` (or `icmpv6.type`)
- `vlan.id` (if applicable)

**Display filters (copy/paste)**
- `ip.flags.mf == 1 or ip.frag_offset > 0`
- `ip.flags.df == 1 and tcp`
- `icmp or icmpv6`
- `icmp.type == 3 and icmp.code == 4`      (IPv4 PMTUD)
- `icmpv6.type == 2`                        (IPv6 Packet Too Big)
- `ipv6.nxt == 44`                          (Fragment header)
- `arp and arp.opcode == 2 and eth.src != arp.src.hw_mac`  (suspicious replies)

---

## Mini-Labs

**A) ARP and GARP**
- Start capture on a LAN; reboot a host or replug NIC.
- Observe ARP Requests/Replies and any **Gratuitous ARP**.
- Deliberately assign a duplicate IP (in a lab!) to see conflict behavior.

**B) Fragmentation vs PMTUD**
- Send pings with DF set and increasing sizes until failure.
- Watch for **ICMP Frag Needed** (v4) / **Packet Too Big** (v6).
- Repeat with DF cleared to see real fragmentation and reassembly.

**C) Traceroute under policy**
- Run UDP-based and TCP-based traceroutes to the same destination.
- Compare which hop replies; note where policy blocks `Time Exceeded`.

---

## Common Pitfalls → Remedies

- **Blocking all ICMP** and then wondering why VPN/web transfers stall.  
  → Allow PMTUD-critical types (v4: type 3/code 4; v6: type 2) and Time Exceeded.
- **Misreading fragments** (analyzing a middle fragment without layer-4 headers).  
  → Reassemble or follow the first fragment (offset 0) for L4 context.
- **Assuming `*` in traceroute means a dead hop.**  
  → It often means “no ICMP Time Exceeded sent”; forwarding can still occur.
- **Confusing ARP cache churn with an attack.**  
  → Check for normal lease renewals, host sleep/wake cycles, or L2 flaps before concluding poisoning.
- **Using IPv4 mental models on IPv6.**  
  → Remember: no broadcast, ND instead of ARP, ICMPv6 is mandatory for basic operation.

---

## What You Should Be Able to Do After Chapter 7

- Read ARP/ND traffic and diagnose local-segment reachability problems.  
- Interpret IPv4/IPv6 headers, fragmentation flags, TTL/Hop-Limit behavior, and extension headers.  
- Detect **PMTUD failures**, explain symptoms, and confirm with ICMP evidence.  
- Use **ICMP/ICMPv6** types/codes (and traceroute logic) to localize path issues.  
- Build filters/columns that surface network-layer truths quickly.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
