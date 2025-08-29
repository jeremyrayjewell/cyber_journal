# IBM Cybersecurity Analyst Professional Certificate  
## Course 9 – Penetration Testing, Threat Hunting, and Cryptography  

[Coursera](https://www.coursera.org/learn/ibm-penetration-testing-threat-hunting-cryptography/home/module/1)  
---

## Overview  
Course 9 introduces penetration testing (ethical hacking), threat hunting, and cryptography as advanced practices for securing systems. Learners gain hands-on experience with pen testing methodologies (planning, discovery, attack, reporting), reconnaissance techniques (passive/active, Google Dorking), exploitation tools (Metasploit, BeEF, SQLMap), and reporting frameworks (PTES). The course also emphasizes the role of threat intelligence platforms and SIEM in proactive defense, and cryptographic methods (AES, RSA, hashing, key management) for confidentiality, integrity, and authenticity. The final project simulates real-world vulnerability analysis using IBM X-Force Exchange and Google Dorking, culminating in a penetration testing plan.  

---

## Module 1: Penetration Testing – Planning and Discovery Phases  
**Learning Objectives:**  
- Explain the purpose and types of penetration testing  
- Apply planning concepts (scope, rules of engagement, legal considerations)  
- Perform passive and active reconnaissance with ethical boundaries  
- Use Google Dorking for discovery  

**Key Topics & Details:**  
- **Pen Testing vs Vulnerability Scanning:** Pen tests simulate real attacks, actively exploiting flaws, unlike automated scans .  
- **Why Pen Testing Matters:** Supports compliance (HIPAA, GDPR, PCI DSS, ISO 27001), helps prevent breaches, reveals lateral movement opportunities.  
- **Types of Pen Tests:**  
  - Application (web, mobile, IoT, cloud, APIs; OWASP Top 10 issues like injection/XSS).  
  - Network (external vs internal).  
  - Hardware (IoT, OT, laptops, mobile devices).  
  - Personnel (phishing, vishing, smishing, tailgating).  
- **Five Phases:** Planning → Discovery → Attack → Verification → Cleanup/Reporting.  
- **Planning:** Define scope (5 elements: specification, resources, risk assessment, communication plan, legal/compliance) and rules of engagement (8 elements: scope, methods, timing, personnel, comms, legal/ethics, incident response, post-test):contentReference[oaicite:1]{index=1}.  
- **Reconnaissance:**  
  - Passive: websites, WHOIS, social media, public filings, job postings, forums.  
  - Active: Nmap, ping sweeps, traceroutes, banner grabbing, Wireshark, Nessus/OpenVAS, DNS enumeration, phishing, dumpster diving.  
- **Google Dorking:** Advanced search operators (e.g., `site:`, `filetype:`, `intitle:`, `inurl:`, `before:`, `after:`). Used responsibly to reveal exposed files, directories, or misconfigured services.  

---

## Module 2: Penetration Testing – Attack Phase  
**Learning Objectives:**  
- Conduct exploitation using standard tools  
- Bypass defenses and escalate privileges  
- Initiate post-attack activities  

**Key Topics & Details:**  
- **Exploit Tools:** Metasploit (exploit db/payloads), BeEF (browser exploitation), SQLMap (automated SQL injection):contentReference[oaicite:2]{index=2}.  
- **Bypassing Defenses:** Proxies, Tor, IP obfuscation; physical bypass via lockpicking, RFID cloning.  
- **Privilege Escalation:** Move from user-level to admin/root for persistence.  
- **Post-Exploitation:** Data exfiltration, persistence mechanisms, lateral movement, credential harvesting.  
- **Reporting Vulnerabilities:** Document findings, map them to real-world risks.  

---

## Module 3: Penetration Testing – Reporting Phase  
**Learning Objectives:**  
- Apply PTES reporting framework  
- Conduct software and application pen tests  
- Scan code repositories for vulnerabilities  

**Key Topics & Details:**  
- **Reporting Framework:** Penetration Testing Execution Standard (PTES) — structured documentation of findings, exploitation methods, evasion techniques, remediation advice.  
- **Repository Scanning:** Identify insecure dependencies and misconfigurations (tools: OWASP ZAP, Snyk).  
- **Importance of Reports:** Translate technical findings into actionable remediation steps for management/security teams.  

---

## Module 4: Threat Hunting and Threat Intelligence  
**Learning Objectives:**  
- Apply threat hunting methodologies  
- Use intelligence platforms and SIEMs for detection  
- Review reports with IBM X-Force Threat Exchange  

**Key Topics & Details:**  
- **Threat Hunting:** Proactive search for indicators of compromise (IOCs) and tactics, techniques, procedures (TTPs).  
- **Threat Intelligence:** Sources include reports, open feeds, dark web monitoring. Platforms correlate data (TIPs, MISP).  
- **SIEM Systems:** Collect, normalize, and analyze logs for anomaly detection. Support incident detection/response workflows.  
- **Case Study:** Reviewing X-Force Exchange reports to identify emerging attack campaigns.  

---

## Module 5: Cryptography – Techniques and Principles  
**Learning Objectives:**  
- Explain cryptographic goals: confidentiality, integrity, authenticity  
- Apply encryption algorithms and hashing functions  
- Manage cryptographic keys securely  

**Key Topics & Details:**  
- **Encryption Algorithms:** Symmetric (AES), asymmetric (RSA).  
- **Hash Functions:** SHA family, MD5 (deprecated), HMAC.  
- **Key Management:** Secure generation, storage, rotation, revocation.  
- **Applications:** TLS/SSL, digital signatures, PGP/GPG, blockchain integrity mechanisms.  
- **Hands-On Labs:** Encrypt/decrypt data, validate hash integrity, apply signing workflows.  

---

## Module 6: Final Project and Wrap-Up  
**Project Tasks:**  
- Use IBM X-Force Exchange to identify a real vulnerability  
- Perform Google Dorking to gather additional intelligence  
- Draft a penetration testing plan including scope, rules of engagement, and reconnaissance findings  
- Submit a comprehensive report summarizing vulnerabilities, exploitation potential, and recommendations  

**Wrap-Up:**  
- Glossary of penetration testing, threat hunting, and cryptography terms  
- Final exam consolidating concepts across modules  

---

## Supplementary Projects  
- **Pen Testing Case Study** – Gaming platform test with SQL injection, outdated Apache exploit, phishing simulation, vulnerability chaining:contentReference[oaicite:3]{index=3}  
- **Reconnaissance Labs** – Passive vs active reconnaissance tasks, Google Dorking exercises  
- **Attack Phase Labs** – Exploiting SQL injection with SQLMap, browser exploitation with BeEF  
- **Threat Intel Lab** – Reviewing IBM X-Force reports, analyzing indicators  
- **Crypto Labs** – AES/RSA encryption, hashing with SHA-256, signing verification  
- **Final Project** – Real-world-inspired vulnerability assessment and pen test planning  

---

## Completion Status  
- All modules completed  
- All videos, readings, labs, and glossary reviewed  
- All graded assignments and final project submitted with high scores (90-100%)  
