# Advent of Cyber 2025 – Day 21, 2025-12-21 
**Room:** Malware Analysis – Malhare.exe \
**Category:** Malware Analysis / Forensics  \
**Skills Practiced:** HTA static analysis, VBScript inspection, PowerShell abuse detection, obfuscation decoding, malware execution tracing

---

## Summary
Day 21 focused on **static malware analysis** of a malicious **HTA (HTML Application)** file used as a delivery mechanism. Rather than executing the sample, the investigation relied on manual inspection to understand how the file disguised itself as a legitimate salary survey while performing reconnaissance, exfiltration, and second-stage execution. The analysis demonstrated how HTA files blend HTML, VBScript, and PowerShell to bypass user suspicion and leverage built-in Windows components such as `mshta.exe`, `WScript.Shell`, and `InternetExplorer.Application`. By tracing function calls, decoding obfuscated content, and following execution flow, the true behavior of the malware was reconstructed without running it.

---

## Walkthrough Notes

### 1. Safe Handling and Initial Inspection

The sample HTA file was opened only in a text editor to prevent execution:  `pluma /root/Rooms/AoC2025/Day21/survey.hta`. The goal was to perform static analysis only, avoiding any interaction with the Windows HTA host (`mshta.exe`).
---

### 2. Inspection of the `<head>` section revealed the application metadata, including:
- The application title
- Window properties intended to make the HTA appear legitimate
- Survey-themed naming designed to blend into corporate workflows
This metadata represented the **social engineering layer**, presenting the file as a harmless internal survey. 

---

### 3. Script Discovery and Function Mapping

The malicious logic was located inside a VBScript block: `<script type="text/vbscript">`. Five key functions were identified:
- `window_onLoad`: Automatically executes when the HTA opens and initiates the malware logic.
- `getQuestions()`: Appears to download survey questions but actually retrieves executable content.
- `provideFeedback(feedbackString)`: Collects system information and performs data exfiltration.
- `decodeBase64(base64)`: Decodes obfuscated Base64 content.
- `RSBinaryToString(xBinary)`: Converts decoded binary data into executable strings.
Mapping these functions revealed that what appeared to be “survey logic” was in fact a staged execution chain.

---

### 4. Suspicious Object Creation and Capabilities

Multiple Windows automation objects were instantiated via CreateObject():
- `InternetExplorer.Application`: Used for outbound network communication.
- `WScript.Network`: Used to enumerate system information from the infected host.
- `WScript.Shell`: Used to execute commands and scripts on the system.
The presence of these objects confirmed that the HTA was not simply collecting input, but actively interacting with the host and network.

---

### 5. Network Activity and Typosquatting

The malware retrieved “survey questions” from an external domain that visually resembled a legitimate one but contained a subtle character substitution. This **typosquatting** technique was used to evade casual inspection while directing traffic to attacker-controlled infrastructure. The downloaded content was then passed directly into an execution function rather than being treated as data.

---

### 6. Execution of Downloaded Content

Analysis showed that the downloaded “questions” were not survey text at all. Instead, they were **executed in memory**, a common malware technique to avoid writing payloads to disk. The critical execution line passed the downloaded content directly into a function responsible for running it, confirming second-stage execution behavior.

---

### 7. Obfuscation and Payload Decoding

The externally hosted payload was obfuscated using:
- A popular **encoding scheme** to conceal its contents
- An additional **encryption layer** to further hinder analysis
After decoding and decrypting the payload using offline tools such as CyberChef, the final malicious logic and embedded flag were recovered.

---

### 8. Data Exfiltration

The malware enumerated host information using scripting objects and exfiltrated the data to a specific endpoint using an HTTP request. This demonstrated how even small HTA files can perform full reconnaissance and data theft with minimal code.

---

## Key Takeaways

- HTA files execute outside the browser but use web technologies, making them powerful and dangerous
- Social engineering is embedded directly into malware logic, not just delivery emails
- HTAs commonly act as launchers rather than full payloads
-  Obfuscation often hides URLs, execution logic, or second-stage malware
-  Static analysis can fully reconstruct malware behavior without execution
- Built-in Windows scripting objects enable living-off-the-land techniques

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
