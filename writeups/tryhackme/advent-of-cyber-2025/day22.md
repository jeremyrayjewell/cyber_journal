# Advent of Cyber 2025 – Day 22, 2025-12-22 
**Room:** C2 Detection – Command & Carol \
**Category:** Network Forensics / Threat Hunting  \
**Skills Practiced:** PCAP analysis, Zeek log generation, C2 beacon detection, RITA analysis, network-based IOC identification

---

## Summary
Day 22 focused on **command-and-control (C2) detection** through large-scale network traffic analysis. Instead of manually inspecting raw packet captures, the task demonstrated how to **convert PCAP data into structured Zeek logs** and apply **RITA (Real Intelligence Threat Analytics)** to identify suspicious communication patterns associated with malware. The investigation showed how encrypted traffic can still be profiled through metadata, timing, and behavioral indicators such as periodic beacons, rare TLS signatures, unusual domains, and low-prevalence external hosts. This lab reinforced that effective detection does not require payload visibility, only good telemetry and analytics.

---

## Walkthrough Notes

### 1. Environment Preparation

The target machine was started, providing access to:
- Pre-collected PCAP files
- Zeek
- RITA
Two relevant directories were present in the home directory:
- `pcaps/` – raw packet captures
- `zeek_logs/` – output directory for parsed Zeek logs

---

### 2. Converting PCAP to Zeek Logs

Before RITA could be used, the PCAP had to be converted into Zeek’s structured log format. Command used: `zeek readpcap pcaps/AsyncRAT.pcap zeek_logs/asyncrat`. This produced multiple Zeek log files, including:
- `conn.log`
- `dns.log`
- `http.log`
- `ssl.log`
- `x509.log`
These logs summarize network behavior at the connection and protocol level, which is exactly what RITA analyzes.

---

### 3. Importing Zeek Logs into RITA

The generated Zeek logs were then imported into RITA for analysis: `rita import --logs ~/zeek_logs/asyncrat/ --database asyncrat`. During import, RITA:
- Parsed the logs
- Normalized timestamps and fields
- Checked threat intelligence feeds
- Calculated behavioral metrics such as beacon likelihood

---

### 4. Viewing and Interpreting RITA Results

The analysis results were viewed with:
`rita view asyncrat`
RITA’s interface displayed:
- A results pane with suspicious connections
- A details pane showing threat modifiers and connection metadata
Two standout findings appeared immediately:
- A suspicious Cloudflare tunnel domain used for C2
- A malicious external IP address confirmed by threat intelligence

---

### 5. Understanding Threat Modifiers

RITA assigned severity based on several Threat Modifiers, including:
- Prevalence – how many internal hosts communicate with the same destination
- Rare signature – unusual TLS or protocol characteristics
- Connection duration – long-lived sessions uncommon for normal web traffic
- First seen – newly observed external infrastructure
- Beaconing behavior – regular, periodic connections
These indicators allowed C2 detection even though the traffic itself was encrypted.

---

### 6. Challenge PCAP Analysis

After reviewing RITA output using the provided AsyncRAT dataset, the same workflow was applied to the challenge PCAP (`rita_challenge.pcap`).
Using the same workflow, the challenge PCAP (rita_challenge.pcap) was analyzed:
- Converted to Zeek logs
- Imported into RITA
- Filtered using RITA’s search syntax
This allowed identification of:
- Hosts communicating with malhare.net
- Beaconing activity to rabbithole.malhare.net
-  The internal host and port used for C2 communication
RITA’s search filters made it possible to isolate high-confidence C2 traffic based on:
- Destination domain
- Beacon score threshold
- Connection duration sorting
RITA’s search syntax was used to isolate high-confidence beaconing activity. For example, the following filter was used to identify long-duration, high-beacon-score connections to a known C2 domain:
`dst:rabbithole.malhare.net beacon:>70 sort:duration-desc`

---

## Key Takeaways

- C2 detection does not require payload decryption
- Behavioral analytics can reveal malicious activity over encrypted channels
- RITA excels at identifying low-prevalence, high-risk connections
- Zeek provides powerful structured telemetry from raw PCAPs
- Beacon timing, destination rarity, and connection metadata are strong indicators of compromise
- Automated analysis dramatically reduces investigation time compared to manual packet inspection

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
