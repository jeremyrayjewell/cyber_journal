SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 3: NETWORK ANALYSIS

---

- This chapter surveys practical tools for observing and understanding live network traffic, from CLI utilities (e.g., `ifconfig`, `ping`, `netstat`) to full packet sniffers (`tcpdump`, Wireshark). The goal is to become comfortable selecting an interface, capturing traffic, and narrowing analysis with filters. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## Command Line Tools

- **`ifconfig` (Linux) / `ipconfig` (Windows)**: used to retrieve interface details. The chapter highlights fields you should recognize: IPv4 address, netmask, broadcast address, IPv6 address, MAC address, and loopback address. :contentReference[oaicite:2]{index=2}
- **`ping`**: verifies reachability using an IP or a domain. Examples show pinging a domain (`hackers-arise.com`) and a specific IP, confirming replies and revealing the resolved IP. :contentReference[oaicite:3]{index=3}
- **`netstat`**: lists inbound/outbound connections; useful for monitoring, troubleshooting, or spotting malware callbacks. Basic usage `netstat -a`; you can pipe to `grep` to locate services (e.g., `| grep http`). The chapter also notes `ss` as a similar, often more informative tool, and flags for TCP (`-t`), UDP (`-u`), and listening sockets (`-l`). :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

## Network Sniffers

- **What sniffers do & why they matter**: A sniffer (packet/protocol/network traffic analyzer) intercepts and inspects traffic—vital for network/security engineers, forensic investigators, and sometimes hackers (e.g., observing unencrypted credentials, DNS/MiTM behaviors, sites visited, cookies, user agents, or unencrypted emails). :contentReference[oaicite:7]{index=7}
- **Representative tools**: SolarWinds DPI, `tcpdump`, WinDump, Wireshark, Network Miner, Capsa, `tshark`. The chapter focuses on `tcpdump` and Wireshark (and later uses Wireshark to dissect NSA’s EternalBlue exploit). :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}
- **Legal/operational context**: Mentions the FBI’s “Carnivore” traffic-sniffing tool as controversial yet (as presented) legal in the U.S. :contentReference[oaicite:10]{index=10}
- **Prerequisites to effective sniffing**: 
  - NIC in **promiscuous mode** to capture any packet on the wire, not just frames addressed to the NIC’s MAC. 
  - Captures use **PCAP**; systems rely on `libpcap` (Linux) / `WinPcap` (Windows) to write `.pcap` files. :contentReference[oaicite:11]{index=11}

## tcpdump

- **Starting and capturing**: `tcpdump` (circa 1988) is CLI-first, lightweight, and ideal for servers/remote hosts without GUIs. Launch with `tcpdump`; packets begin scrolling (e.g., ICMP during a `ping`). Save captures with `-w myoutput.cap`. :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}
- **Simple traffic generation for learning**: In one terminal, `ping` a target; in another, run `tcpdump` to observe ICMP echo request/reply. :contentReference[oaicite:14]{index=14}
- **BPF filtering**: `tcpdump` uses Berkeley Packet Filter (BPF) syntax (originating with BSD) to narrow traffic:
  - By **host/IP**: `tcpdump host 192.168.0.114`. :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}
  - By **TCP flags** (ACK/FIN/RST/PSH/URG) using byte tests like `tcpdump 'tcp[tcpflags]==tcp-rst'` (and variants for other flags). :contentReference[oaicite:17]{index=17}
  - **Combining** filters with logical AND/OR and **negation**: e.g., `host 192.168.0.114 and port 80`; `port 80 or port 443`; `not host 192.168.0.114`. :contentReference[oaicite:18]{index=18}
  - **Hunting artifacts** in plaintext protocols by piping to `egrep`/`grep`: user-agents and cookies; even naive password pattern searches across common service ports. :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20}
- **Takeaway**: Time spent mastering BPF syntax pays off; `tcpdump` remains the go-to when GUI capture is impractical. :contentReference[oaicite:21]{index=21}

## Wireshark

- **Positioning & startup**: Wireshark (formerly Ethereal) is the de-facto standard sniffer, bundled in Kali. Start via terminal or Applications → Sniffing and Spoofing → Wireshark; then select the most active interface (e.g., `eth0` in VMs, `wlan0` on laptops). :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}
- **Capture format & UI panes**: Captures are `.pcap`. Three panes:
  1) **Packet List** (chronological list, color-coded), 
  2) **Packet Details** (expanded header fields of the selected frame), 
  3) **Packet Bytes** (hex on left, ASCII on right). :contentReference[oaicite:24]{index=24} :contentReference[oaicite:25]{index=25}

## Creating Filters in Wireshark

- **Display filters**: Start with protocol filters (e.g., `tcp`; green = valid syntax, pink = invalid). :contentReference[oaicite:26]{index=26}
- **IP/port narrowing**: `ip.addr==<IP>` (note the **double** equals); example `ip.addr==192.168.1.107`. Port example: `tcp.dstport==80`. :contentReference[oaicite:27]{index=27} :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29}
- **Payload searches**: use `contains` to search strings within packet payloads (e.g., `tcp contains facebook`). :contentReference[oaicite:30]{index=30}
- **Expression builder**: The **Expression** dialog lists protocols/fields and relations (e.g., `==`, `!=`, `>`, `<`, `>=`, `<=`, `contains`, `matches`); you can compose filters like `tcp.flags.rst==1`. :contentReference[oaicite:31]{index=31}

## Following Streams

- **Conversation-level view**: Right-click a packet → **Follow → TCP Stream** to reconstruct the two-way conversation—handy for investigating suspicious user activity or insider threats. The Follow Stream window also shows byte counts and the display mode (e.g., ASCII). :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33}

## Statistics

- **Observed in context**: Within the Follow Stream dialog, Wireshark surfaces basic statistics such as total bytes in the captured conversation (example noted: 5,796 bytes) and the display mode. :contentReference[oaicite:34]{index=34}

## Exercises

- The chapter concludes with an **Exercises** section (see TOC), encouraging hands-on practice applying the tools and filters introduced here. :contentReference[oaicite:35]{index=35}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
