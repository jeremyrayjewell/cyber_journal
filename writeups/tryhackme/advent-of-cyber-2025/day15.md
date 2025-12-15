# Advent of Cyber 2025 – Day 15, 2025-12-15
**Room:** Web Attack Forensics – Drone Alone
**Category:** Blue Team / Web Attack Forensics / SIEM
**Skills Practiced:** Splunk investigation, Apache log analysis, Sysmon process correlation, command injection detection, Base64 payload decoding, web-to-host attack reconstruction.

---

## Summary
This challenge focused on investigating a suspected command injection attack against TBFC’s drone scheduler web interface. Splunk raised an alert indicating that Apache had spawned an unusual process, suggesting that malicious HTTP requests may have resulted in backend command execution.

Acting as a Blue Team analyst, I used Splunk to correlate Apache access logs, Apache error logs, and Sysmon host telemetry to confirm exploitation, identify attacker behavior, and determine the scope of compromise. The investigation revealed command injection attempts using Base64-encoded PowerShell payloads, successful spawning of system processes by Apache, and post-exploitation reconnaissance activity.

---

## Walkthrough Notes

From the AttackBox browser, I logged into Splunk at `http://MACHINE_IP:8000` with the given credentials. Before running any queries, I adjusted the time range to `All time` to ensure all relevant events were visible.

### 1. Detecting Suspicious Web Requests (Apache Access Logs)
I began by searching for indicators of command execution attempts in web traffic:
```
index=windows_apache_access (cmd.exe OR powershell OR "powershell.exe" OR "Invoke-Expression")
| table _time host clientip uri_path uri_query status
```
This query revealed long HTTP requests targeting /cgi-bin/hello.bat, containing Base64-encoded PowerShell commands passed through URL parameters. This strongly suggested command injection via a vulnerable CGI script.

---

### 2. Decoding Obfuscated Payloads
Several Base64 strings were observed within malicious HTTP requests. Decoding one of these payloads revealed taunting text rather than functional malware, confirming that Base64 encoding was used primarily to obfuscate intent and evade simple detection mechanisms. This step provided context but was not required to answer the challenge questions.

---

### 3. Confirming Backend Execution Attempts (Apache Error Logs)
Next, I examined Apache error logs for execution failures:

`index=windows_apache_error ("cmd.exe" OR "powershell" OR "Internal Server Error")`

Viewing the events in raw format showed HTTP 500 Internal Server Errors triggered by malicious requests. This indicated that attacker input reached backend execution logic, even if some attempts failed during processing.

---

### 4. Tracing Process Creation from Apache (Sysmon)
To confirm whether commands were executed on the host, I pivoted to Sysmon logs:

`index=windows_sysmon ParentImage="*httpd.exe"`

Switching to table view, I observed child processes spawned by Apache. Seeing system binaries launched by httpd.exe confirmed that the attack successfully crossed from the web layer to the operating system.

---

### 5. Identifying Attacker Reconnaissance Activity
Finally, I searched for common post-exploitation reconnaissance commands:

`index=windows_sysmon *cmd.exe* *whoami*`

This query revealed executions of the whoami command, a classic attacker technique used immediately after gaining code execution to determine privilege level and execution context.

---

## Findings
- Apache processed attacker-supplied input that resulted in system command execution.
- The attacker attempted to execute PowerShell through the web interface.
- The attacker performed reconnaissance using whoami, confirming post-exploitation activity.
- Base64 encoding was used to obfuscate commands within HTTP requests.
- Correlating web logs with Sysmon telemetry was essential to proving impact.

---

## Final Answers
Reconnaissance executable: cmd.exe  
Executable attempted via command injection: powershell.exe  

---

## Key Takeaways
- Command injection often begins in web logs but must be confirmed at the host level.
- Apache spawning system binaries is a critical indicator of compromise.
- Sysmon process trees provide definitive proof of successful exploitation.
- Base64-encoded commands are commonly used to bypass simple detection.
- Effective Blue Team investigations rely on correlating multiple log sources to reconstruct the full attack chain.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
