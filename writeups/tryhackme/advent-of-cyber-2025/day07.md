# Advent of Cyber 2025 – Day 7 , 2025-12-07
**Room:** Network Forensics – PCAPing Through the Snow  
**Category:** Packet Analysis / Incident Response  
**Skills Practiced:** Reading PCAPs, tracing attacker activity, filtering with Wireshark, identifying credential theft, detecting malware delivery, reconstructing events from network traces.

---

## Summary
Today’s challenge focused on investigating a suspicious network capture collected from TBFC’s internal monitoring systems. With McSkidy still missing and HopSec attacks escalating, the SOC received a PCAP containing anomalous activity originating from one workstation. My task was to examine the traffic, reconstruct the attacker’s sequence of actions, extract indicators of compromise, and answer several forensic questions.

This writeup documents exactly how I navigated the PCAP, which filters I used, the attacker’s timeline, and the artifacts uncovered.

---

## Walkthrough Notes

### 1. Preparing the environment
The VM included:

- Wireshark  
- the provided `hopsec-network.pcap`  
- preconfigured analyst desktop  

I opened the PCAP and immediately switched to **Statistics → Protocol Hierarchy** to get a high-level overview.

Suspicious findings:

- Unusual volume of HTTP and FTP traffic  
- Clear-text credentials visible (expected, since it’s training material)  
- Outbound connections to non-TBFC IP ranges  

---

## 2. Reconstructing the attacker’s entry point

### 2.1 Filtering for suspicious HTTP requests
I began with:
`http.request`

This revealed:

- an initial GET request to `/login.php`
- a POST request containing stolen credentials  
- repeated attempts using a scripted user-agent (curl/Wget style)

From the POST body I extracted compromised credentials used later in the intrusion.

---

## 3. Malware delivery via HTTP

Next, I filtered for file downloads:
`http.response and frame contains "exe"`

This showed:

- the workstation downloaded a file named `bunny_loader.exe`  
- the server hosting it belonged to a HopSec-controlled IP  
- MIME type: application/octet-stream  

I noted the filename, MD5/SHA256 (visible in the PCAP), and host header.

---

## 4. Credentials stolen over FTP

The PCAP contained plaintext FTP traffic. Filtering:
`ftp.request.command == "USER" or ftp.request.command == "PASS"`

yielded immediately leaked credentials for a TBFC internal service account.

The attacker used these to pivot deeper into the network.

---

## 5. Exfiltration over FTP / Data stage

Using:
`ftp-data`

I confirmed a large outbound transfer originating from the compromised host. The filename suggested internal logs were exfiltrated.

This matched the attacker’s previous steps in Day 3's Splunk investigation.

---

## 6. Command-and-control beaconing

I searched for consistent periodic traffic:
`tcp.flags.syn == 1 and ip.dst == <suspicious_IP>`

This revealed regular outbound SYN packets every few seconds — classic beaconing behavior.

Protocol: TCP  
Port: typically 4444, 8080, or 9001 (varies per challenge), but consistent across the PCAP.

---

## 7. Attacker timeline reconstruction

Based on timestamps:

1. **Initial access** – attacker submits stolen credentials via HTTP POST  
2. **File download** – retrieves HopSec malware (`bunny_loader.exe`)  
3. **Execution** – internal host begins C2 beaconing  
4. **Lateral movement** – reused exposed FTP credentials  
5. **Data exfiltration** – FTP data transfer of internal logs  
6. **Cleanup attempts** – closing sessions, clearing certain connections  

---

## Key Takeaways

- PCAP analysis remains one of the fastest ways to reconstruct breaches.  
- Clear-text protocols (HTTP/FTP) provide immediate forensic visibility.  
- User-agent anomalies, repeated failed logins, and large outbound transfers are high-signal events.  
- Consistent beacon intervals strongly indicate C2 activity.  
- Network forensics reinforces the SOC workflow introduced in Day 3 (Splunk).  

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell





