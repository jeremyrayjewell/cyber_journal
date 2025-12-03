# Advent of Cyber 2025 – Day 3, 2025-12-03  
**Room:** Splunk Basics – Did You SIEM?  
**Category:** SIEM / Log Analysis  
**Skills Practiced:** Splunk search (SPL), timecharting, anomaly detection, field analysis, source type triage, path traversal detection, SQLi detection, exfiltration investigation, C2 correlation, firewall log analysis.

---

## Summary
This challenge introduced Splunk as a SIEM platform for investigating a ransomware attack on TBFC’s web server. Two datasets were pre-ingested into Splunk:  
- **web_traffic** (HTTP access logs)  
- **firewall_logs** (ingress/egress firewall events)

My goal was to triage the logs, identify the attacker IP, trace each phase of the intrusion (recon → vulnerability scanning → exploitation → RCE → ransomware execution → C2 communication → exfiltration), and answer quantitative questions using SPL.

---

## Walkthrough Notes

### Connecting to the Machine
The Splunk search head was available only inside the TryHackMe VM. The VM acted as a local browser session; external browsers cannot access it.  
Using the sidebar, I opened **Search & Reporting** and ran `index=maim`. Time range was set to **All time**.

---

## My Steps

### 1. Initial Dataset Triage
I confirmed two sourcetypes:

- `web_traffic`
- `firewall_logs`

Then began with `index=main sourcetype=web_traffic`. Splunk displayed ~17K events and a noticeable traffic spike — the likely attack window.

---

### 2. Event Volume Over Time
```
index=main sourcetype=web_traffic
| timechart span=1d count
```

Visualization identified the day with peak traffic, used later for the answer.

Adding sort:

```
| sort by count | reverse
```

---

### 3. Identifying Suspicious User Agents
Filtering out real browsers:

```
index=main sourcetype=web_traffic
user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox*
```

All suspicious activity originated from a **single IP**, which became the `<REDACTED>` attacker IP used in subsequent queries.

---

### 4. Confirming Attacker IP (Top Offensive Traffic)
```
sourcetype=web_traffic
user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox*
| stats count by client_ip
| sort -count
| head 5
```

This produced the attacker’s IP with the highest malicious log volume.

---

### 5. Reconnaissance Activity
```
sourcetype=web_traffic client_ip="<REDACTED>"
AND path IN ("/.env", "/*phpinfo*", "/.git*")
| table _time, path, user_agent, status
```

Confirmed probing using curl/wget against sensitive files (.env, phpinfo, git).

---

### 6. Path Traversal & Enumeration Attempts
```
sourcetype=web_traffic client_ip="<REDACTED>"
AND path="*..\/..\/*" OR path="*redirect*"
| stats count by path
```

Showed attempts to read system files via `../../`, plus open redirect exploration.

---

### 7. SQL Injection (Automated Tooling)
```
sourcetype=web_traffic client_ip="<REDACTED>"
AND user_agent IN ("*sqlmap*", "*Havij*")
| table _time, path, status
```

Returned events for **sqlmap** and **Havij** with payloads such as `SLEEP(5)`, including 504 responses consistent with time-based SQLi.

---

### 8. Exfiltration Attempts
```
sourcetype=web_traffic client_ip="<REDACTED>"
AND path IN ("*backup.zip*", "*logs.tar.gz*")
| table _time, path, user_agent
```

Showed archive downloads using non-browser tools (curl, zgrab).

---

### 9. Ransoming & Remote Code Execution
```
sourcetype=web_traffic client_ip="<REDACTED>"
AND path IN ("*bunnylock.bin*", "*shell.php?cmd=*")
| table _time, path, user_agent, status
```

This confirmed successful:
- **webshell execution** (`shell.php?cmd=`)  
- **ransomware launch** (`cmd=./bunnylock.bin`)

---

### 10. Correlating C2 Traffic in Firewall Logs
```
sourcetype=firewall_logs
src_ip="10.10.1.5"
AND dest_ip="<REDACTED>"
AND action="ALLOWED"
| table _time, action, protocol, src_ip, dest_ip, dest_port, reason
```

Revealed outbound C2 contact from the compromised server.  
`reason=C2_CONTACT` confirmed malware beaconing.

---

### 11. Volume of Data Exfiltrated
```
sourcetype=firewall_logs
src_ip="10.10.1.5"
AND dest_ip="<REDACTED>"
AND action="ALLOWED"
| stats sum(bytes_transferred) by src_ip
```

Returned the number of bytes exfiltrated.

---

## Key Takeaways
- Splunk SIEM workflows revolve around sourcetype triage, field analysis, SPL filtering, and correlation across multiple log sources.  
- The attack followed a clean kill-chain sequence visible directly in logs:  
  Recon → Enumeration → SQLi → Webshell → RCE → Ransomware → C2 → Exfiltration.  
- Combining web logs and firewall logs provides the complete picture of intrusion and data loss.  
- Query refinement (`!=`, `IN()`, `stats`, `timechart`, `sort`, `reverse`) is essential for efficient SOC work.  
- This exercise reinforced practical SIEM analysis workflows directly applicable to Tier-1/Tier-2 SOC roles.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
