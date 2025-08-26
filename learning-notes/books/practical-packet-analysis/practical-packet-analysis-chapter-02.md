SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 2: TAPPING INTO THE WIRE

---

## Overview

- How to position your sniffer so you can actually see the packets that matter.
- Trade-offs among SPAN/port mirroring, network TAPs, "hubbing out," and (lab-only) ARP poisoning.
- Practical guidance for switched and routed environments, including validation steps, pitfalls, and a field checklist.

---

## Promiscuous Mode: What It Gives You (and What It Doesn’t)

- Promiscuous mode makes your NIC deliver all frames it receives to the OS, not just frames addressed to its MAC.
- On a normal switch port you still only receive: unicast to your MAC, broadcasts, and multicasts. You will not see other hosts’ unicast without a mirroring or inline method.
- Common gotchas:
  - Offload artifacts: “bad checksum” flags often come from checksum offloading; packets were fine on the wire. If it’s confusing your analysis, temporarily disable LSO/CSO/GSO while capturing.
  - VLAN tag stripping: some drivers remove 802.1Q tags before passing frames up the stack. Prefer capture points that preserve tags and add a “VLAN ID” column in Wireshark.
  - Permissions and drivers: capturing typically requires admin/root privileges and proper capture drivers (Npcap/WinPcap on Windows; libpcap on Unix-like systems).

Quick self-check ideas (conceptual, not commands):
- Verify whether VLAN tags appear in your capture; if not, adjust switch mirroring or capture method.
- Confirm you see broadcasts like ARP and LLDP on a busy access port; that validates basic visibility.

---

## Capturing on Hubs (Legacy but Educational)

- Hubs repeat every bit to every port (half-duplex), so a sniffer sees all traffic on that segment.
- Pros: trivial to use; zero configuration.
- Cons: rare; forces half-duplex and low speeds; collisions/late errors; can destabilize modern links.
- When useful: short, ad-hoc lab work or very small legacy segments where you control both ends.
- Sanity test: copy a large file between two hosts; your sniffer should see both directions if it’s a real hub (many “hubs” sold today are actually tiny switches).

---

## Capturing on Switches: Four Practical Methods

### 1) Port Mirroring (SPAN, RSPAN, ERSPAN)

- Concept: the switch copies traffic from selected source ports or VLANs to a dedicated monitor port where your sniffer listens.
- Key configuration levers:
  - Source selection: one or multiple access ports, or an entire VLAN.
  - Direction: ingress, egress, or both (both roughly doubles mirror volume).
  - Transport: local (SPAN), remote over a dedicated VLAN (RSPAN), or GRE-encapsulated (ERSPAN).
  - Tag handling: many platforms can mirror VLAN tags to the monitor port; verify empirically.
- Strengths: no downtime; flexible; non-intrusive; fast to enable when you have switch access.
- Weaknesses and pitfalls:
  - Oversubscription: mirroring multiple 1 Gb sources to a single 1 Gb monitor port can drop mirrored frames silently. Reduce sources/directions, use a faster monitor port, or move to a TAP.
  - Limited L1/L2 visibility: SPAN often omits frames with bad FCS and certain link-control frames; if you need physical errors, use a TAP.
  - Asymmetry: if you don’t mirror both directions or all relevant VLANs, you may only see half of a conversation.
  - Timestamps: timing is from the capture host; precision is good enough for most work but not microsecond-grade.
- Validation routine (do this every time you set up a mirror):
  1. Generate a known bidirectional flow (for example, a file copy or client-server test).
  2. Confirm you see both directions and any expected VLAN tags.
  3. Check monitor-port counters on the switch for drops during high load.

Helpful capture-focus ideas (applied as capture filters if you are constraining volume):
- Focus on one host: host 10.10.10.50
- Only VLAN 120 (and keep link-layer header if supported): vlan 120
- Control-plane sanity when validating a SPAN: stp or lldp or cdp or arp

---

### 2) “Hubbing Out” (Quick Inline Visibility)

- How it works: place a true hub between a target host and the switch; plug your sniffer into the hub as a passive listener.
- Pros: simple; cheap; handy when you only need one host’s traffic.
- Cons: forces half-duplex; can create duplex mismatches; introduces errors; hard to find real hubs.
- Safer alternative: a small media TAP that preserves full-duplex and avoids duplex mismatch.

Conceptual topology:
  [Host]──(Hub)──[Switch]
               └─[Sniffer]

Mitigations if you must hub out:
- Lock both host and switch port to the same speed/duplex to avoid auto-negotiation mishaps.
- Keep captures short and low-risk; move to a TAP for anything long-lived or critical.

---

### 3) Network TAPs (Highest Fidelity)

- What they are: purpose-built inline devices that passively copy traffic to one or more monitor ports with minimal disturbance.
- Types:
  - Copper and fiber variants; match your link type.
  - Breakout TAP: exposes each direction on its own monitor port (A-TX and B-TX). Requires two capture interfaces; you merge streams in software.
  - Aggregator TAP: combines both directions into one monitor port; convenient but may drop at extreme rates.
  - Regeneration/replication TAPs: multiple monitor outputs for multiple tools or teams.
  - Fail-safe/bypass: link stays up if the TAP loses power; preferred for production links.
- Strengths:
  - Preserves FCS errors, VLAN tags, and full-duplex symmetry.
  - Minimal latency and jitter; some models support hardware timestamping for precise timing.
  - Ideal for forensics, SLA disputes, microburst analysis, and any situation where SPAN limitations matter.
- Trade-offs: cost; requires a change window and physical access to insert inline.

Breakout TAP concept:
  LAN ──[TAP]── WAN
          ├── A-TX → Monitor NIC #1
          └── B-TX → Monitor NIC #2
  Capture from both NICs simultaneously; store in one pcapng if your tool supports multi-interface capture.

Operational tips:
- Label directions clearly (A and B) so you don’t invert client/server views during analysis.
- If merging files later, be mindful of clock skew; prefer capturing both directions at once.

---

### 4) ARP Cache Poisoning (Lab-Only / With Written Authorization)

- Mechanism: forge ARP replies so a victim associates the gateway IP with your MAC (or vice-versa), causing traffic to flow through your box (man-in-the-middle).
- Where appropriate: controlled labs, your own gear, or explicitly authorized security tests.
- Hazards: intrusive; can break sessions; sets off IDS/IPS; may violate policy or law if unauthorized.
- Likely defenses encountered: Dynamic ARP Inspection, DHCP snooping, static ARP on critical hosts, and host-based protections.

Key reminder: do not use ARP poisoning in production without explicit written permission.

---

## Routed Environments: Placement and Expectations

- Routers separate broadcast domains and may NAT, filter (ACL), and shape traffic. A flow on the LAN side is not necessarily identical on the WAN side.
- Placement guidance:
  - Edge localization: capture on both sides of the router to find where loss/latency appears.
  - NAT awareness: correlate pre-NAT (inside) flows with post-NAT (outside) 5-tuples; match by timing, ports, and direction.
  - VPNs and tunnels: outside captures show ESP/GRE; inside near the endpoint you can see the decrypted inner flows. Capture near the tunnel termination if you need application details.
- If you cannot insert a TAP:
  - Use the router or L3 switch’s monitor-session features.
  - Use flow records (NetFlow/IPFIX) for triage, then perform deep packet capture at the narrowed hotspot.

---

## Practical Placement Playbook

1. Form a hypothesis, e.g., “Packets are healthy at the client edge but degrade upstream.”
2. Choose the least intrusive vantage that can prove or disprove it; SPAN is a common first step.
3. Ensure you can see both directions of the conversation; if SPAN looks asymmetric or lossy, escalate to a TAP.
4. Cross routing boundaries deliberately; compare captures before and after NAT, VPN, ACL, or QoS.
5. Iterate hop-by-hop toward the point where packets “turn bad.”

Common capture points:
- Client access port (user-reported issues)
- Server access port (application slowness)
- Between distribution and core (east–west issues)
- WAN/Internet edge (SaaS complaints)
- VPN headend (remote-user problems)
- Wireless controller/AP uplink (air captures are covered later; here you can still use wired mirrors)

---

## Field Checklist

Before
- Clarify scope (hosts, subnets, ports, VLANs) and expected partners; consider pre/post-NAT identities.
- Pick SPAN vs TAP; verify monitor-port capacity relative to mirrored sources.
- Sync the capture host with NTP; configure ring buffers (size/time) to avoid unwieldy files.

During
- Use capture filters to constrain volume while keeping needed context.
- Validate early: do you see both directions; are VLAN tags present when expected; are there signs of mirror drops.
- Watch device counters (on the monitor port and mirrored sources) for drops or errors.

After
- Document exact placement, SPAN/TAP configuration, timestamps, and known limitations (for example, SPAN does not include FCS errors).
- Sanity-check time alignment and directionality before deep protocol analysis.

---

## Common Pitfalls and Remedies

- SPAN oversubscription leading to silent drops
  - Remedy: reduce sources/directions; use faster monitor ports; or move to a TAP.
- Seeing only one side of a conversation
  - Remedy: mirror both directions/VLANs; choose a vantage immune to asymmetric routing; capture on both sides of a routing boundary.
- “Bad checksum” everywhere in the capture
  - Remedy: recognize offload artifacts; disable NIC offloads for the session or ignore at L3 and above.
- Missing VLAN tags in captures
  - Remedy: enable tag forwarding on the mirror; avoid drivers that strip tags; prefer TAPs.
- Duplex mismatch after hubbing out
  - Remedy: prefer a TAP; if hubbing out is unavoidable, hard-set speed/duplex on both ends.
- Legal/ethical exposure (especially with ARP poisoning)
  - Remedy: obtain written authorization; avoid intrusive methods outside controlled labs.

---

## Command and Filter Snippets (to adapt in your environment)

tcpdump and dumpcap style ideas:
- Focused server capture on HTTP and HTTPS:
  tcpdump -i mon0 -w srv-http.pcap '(host 10.20.30.40) and (tcp port 80 or 443)'
- VLAN-aware capture including link-layer header (if supported):
  tcpdump -i mon0 -e -w vlan120.pcap 'vlan 120 and host 10.20.30.40'
- Breakout TAP with two monitor NICs into one rolling pcapng:
  dumpcap -i monA -i monB -b filesize:512000 -w tap-breakout.pcapng

Useful Wireshark display filters during analysis:
- ip.addr == 10.20.30.40
- tcp.stream eq 7
- vlan.id == 120
- icmp or icmpv6
- tcp.analysis.flags or tcp.retransmission
- frame.checksum_bad == 1

---

## Mini-Labs (Hands-On)

1) SPAN validation
- Mirror a busy server port.
- Generate bidirectional traffic (for example, a two-way throughput test).
- Confirm both directions and expected VLAN tags appear.
- Observe monitor port counters for drops during peak.

2) Oversubscription experiment
- Mirror two saturated 1 Gb sources to a 1 Gb monitor.
- Note mirror drops; then reduce to one source and compare captured throughput.

3) TAP timing
- Insert a TAP on a lightly used link.
- Compare handshake and request-response timings captured via SPAN versus TAP to appreciate timestamp and error-visibility differences.

---

## Final Thoughts

- Start with the least intrusive method that can still answer your question.
- Always validate what your vantage actually shows: symmetry, VLAN tags, and whether physical errors are visible.
- When precision matters (errors, microbursts, exact timing), prefer a TAP.
- Document placement and limitations so your findings are defensible later.

---

## Summary author: Jeremy Ray Jewell
GitHub: https://github.com/jeremyrayjewell
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
