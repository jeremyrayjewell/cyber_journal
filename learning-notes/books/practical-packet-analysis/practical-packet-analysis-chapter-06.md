SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 6: PACKET ANALYSIS ON THE COMMAND LINE

---

## Why the CLI matters

- **Scale:** handle giant captures and high-rate links without a GUI.
- **Speed:** one-liners for quick triage (who/what/how much) and batch jobs.
- **Repeatability:** exact commands become auditable playbooks you can re-run.

**Core tools**

- `tcpdump` — capturing with BPF (Berkeley Packet Filter) syntax
- `dumpcap` — Wireshark’s high-performance capture engine (great for ring buffers)
- `tshark` — Wireshark’s CLI analyzer using *display* filters
- `editcap`, `mergecap`, `capinfos` — trim/merge/inspect pcaps
- `text2pcap` — build pcaps from hex/text (rare but handy)

---

## Capture at line rate (tcpdump & dumpcap)

**tcpdump basics (BPF capture filters)**

- List interfaces:  
    tcpdump -D
- Capture on eth0 to rotating files by size (500 MB, keep 8 files):  
    tcpdump -i eth0 -nn -s 0 -w cap-%Y%m%d-%H%M%S.pcap -C 500 -W 8
- Rotate by time (every 5 minutes):  
    tcpdump -i eth0 -nn -s 0 -G 300 -w cap-%Y%m%d-%H%M%S.pcap
- Smaller headers-only capture for triage:  
    tcpdump -i eth0 -nn -s 256 -w headers.pcap

**Common BPF patterns**

- One host:  
    host 10.20.30.40
- Subnet:  
    net 10.20.30.0/24
- Web to/from a host:  
    host 10.20.30.40 and \(tcp port 80 or 443\)
- DNS only:  
    udp port 53
- VLAN 120:  
    vlan 120
- Drop control-plane noise:  
    not \(stp or lldp or cdp\)

**dumpcap (prefer for long runs/ring buffers)**

- High-throughput ring buffer by size (500 MB x 20 files):  
    dumpcap -i eth0 -b filesize:512000 -b files:20 -w ring-%F-%T.pcapng
- Rotate by duration (5-minute slices):  
    dumpcap -i eth0 -b duration:300 -b files:24 -w ring-%F-%T.pcapng
- Multi-interface capture (e.g., breakout TAP A/B):  
    dumpcap -i monA -i monB -b filesize:102400 -w dual-%F-%T.pcapng

**Practical capture tips**

- Disable name resolution and avoid display filters during capture.
- Prefer **pcapng** for per-interface metadata and drop counters.
- Ensure fast storage (SSD/NVMe) and sufficient write buffers.

---

## Post-capture analysis (tshark)

**Display-filter driven reads (Wireshark syntax, not BPF)**

- List retransmissions:  
    tshark -r cap.pcapng -Y "tcp.analysis.retransmission"
- Print selected fields as CSV:  
    tshark -r cap.pcapng -Y "http" -T fields -E header=y -E separator=, -e frame.number -e frame.time -e ip.src -e ip.dst -e http.request.method -e http.host -e http.response.code
- Dump hex/ASCII of matched packets (careful with PII):  
    tshark -r cap.pcapng -Y "tcp.port==443" -x

**Useful display filters**

- Host focus:  
    ip.addr == 10.20.30.40
- One TCP conversation:  
    tcp.stream eq 7
- TCP trouble (umbrella):  
    tcp.analysis.flags
- DNS queries only:  
    dns.flags.response == 0
- TLS SNI present:  
    tls.handshake.extensions_server_name
- VLAN focus:  
    vlan.id == 120

**Built-in stats (no GUI)**

- Protocol hierarchy:  
    tshark -r cap.pcapng -q -z io,phs
- Conversations (TCP):  
    tshark -r cap.pcapng -q -z conv,tcp
- Endpoints (IPv4):  
    tshark -r cap.pcapng -q -z endpoints,ip
- I/O buckets (1s bins; bytes and retrans counts):  
    tshark -r cap.pcapng -q -z io,stat,1,"SUM(frame.len) frame.len","COUNT(tcp.analysis.retransmission) tcp.retx"

**Reading the outputs quickly**

- `conv,tcp`: sort by Bytes to find heavy talkers; by Packets for chattiest pairs.
- `io,stat`: spikes in retransmissions suggest loss or congestion.
- `endpoints`: inventory who’s on the wire.

---

## File surgery (editcap / mergecap / capinfos)

- Slice to a time window:  
    editcap -A "2025-08-26 14:00:00" -B "2025-08-26 14:15:00" big.pcapng slice.pcapng
- Sample packets (downsample for a quick look):  
    editcap -S 10 big.pcapng sampled.pcapng      ← keeps ~1/10 packets
- Remove duplicates (basic):  
    editcap --remove-duplicates in.pcapng dedup.pcapng
- Merge multiple files (preserve timestamps):  
    mergecap -w merged.pcapng part1.pcapng part2.pcapng
- Get metadata quickly (times, rates, drops):  
    capinfos -Tmrs big.pcapng

**Time alignment**

- If two capture hosts aren’t perfectly NTP-aligned, use Wireshark **Time Shift** or `editcap -t <offset>` to align traces before comparison.

---

## Streaming workflows (pipes & SSH)

- Remote capture into local GUI Wireshark:  
    ssh user@server "tcpdump -i eth0 -s 0 -w - 'not port 22'" | wireshark -k -i -
- Headless live analysis (no giant files):  
    ssh user@server "tcpdump -i eth0 -n -l 'udp port 53'" | stdbuf -oL awk '{print $3}' | sort | uniq -c | sort -nr
- Compress on the fly:  
    tcpdump -i eth0 -w - 'host 10.20.30.40' | gzip > focus-$(date +%F-%H%M).pcapng.gz

---

## Common patterns you’ll reuse

**Top talkers (TCP) from a large file**

- Conversations summary, then skim heaviest:
    tshark -r big.pcapng -q -z conv,tcp

**HTTP request/response timing (TTFB)**

- Requests (method, host, URI, time):  
    tshark -r web.pcapng -Y "http.request" -T fields -e tcp.stream -e frame.time -e http.request.method -e http.host -e http.request.uri | sort -n
- Responses (join later on tcp.stream):  
    tshark -r web.pcapng -Y "http.response" -T fields -e tcp.stream -e frame.time -e http.response.code

**DNS success/error per second**

- Bucketed counters:  
    tshark -r dns.pcapng -q -z io,stat,1,"COUNT(dns.flags.response==1) dns.resp","COUNT(dns.flags.rcode>0) dns.err"

**Extract one conversation to a small evidence file**

- Identify stream 17, then:  
    tshark -r big.pcapng -Y "tcp.stream eq 17" -w stream17.pcapng

---

## Pitfalls & fixes (CLI edition)

- **Filter language mix-ups** (BPF vs display filters).  
  Fix: BPF only at capture; display filters for `tshark/wireshark`.
- **Shell quoting** (parentheses, spaces).  
  Fix: wrap display filters in single quotes; escape parentheses in BPF.
- **Packet drops under load** (slow disk, tiny buffers).  
  Fix: prefer `dumpcap`; use fast SSD; ring buffers; reduce snaplen; mirror less.
- **Monolithic files too big to open.**  
  Fix: rotate at capture; later slice with `editcap`.
- **Clock skew/timezone confusion** across hosts.  
  Fix: NTP everywhere; align with Time Shift or `editcap -t`.

---

## Minimal CLI starter kit (copy/paste)

- 24/7 ring capture on eth0 (5-minute files, keep 8):
    dumpcap -i eth0 -b duration:300 -b files:8 -w /var/captures/eth0-%F-%T.pcapng

- Heavy talkers (TCP) from latest file:
    tshark -r /var/captures/eth0-latest.pcapng -q -z conv,tcp

- Filter and export one host’s web traffic:
    tshark -r big.pcapng -Y "ip.addr==10.20.30.40 and (tcp.port==80 or tcp.port==443)" -w host-web.pcapng

- CSV of DNS queries (time, src, name, type):
    tshark -r dns.pcapng -Y "dns.flags.response==0" -T fields -E header=y -E separator=, -e frame.time -e ip.src -e dns.qry.name -e dns.qry.type > dns-queries.csv

---

## What you should be able to do after Chapter 6

- Capture reliably at scale with `tcpdump`/`dumpcap` using ring buffers and sensible snaplen.
- Slice, merge, and summarize with `editcap`/`mergecap`/`capinfos`.
- Produce quick, defensible answers via `tshark` (conversations, endpoints, protocol mix, I/O stats, CSV exports).
- Automate remote captures and live triage with SSH pipelines.
- Avoid common CLI pitfalls (filter mix-ups, quoting, time skew, silent drops).

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
