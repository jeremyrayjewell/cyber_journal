# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 19 – Malicious Activity  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 19 examines malicious activity that targets networks, systems, and applications. Learners review denial-of-service attacks, DNS exploits, traversal and escalation attacks, replay and hijacking techniques, injection methods, on-path attacks, and indicators of compromise (IoCs). The focus is on recognizing attack types and understanding their impact.  

---

## Module 19.1: Malicious Activity Overview  
**Learning Objectives:**  
- Define malicious activity in cybersecurity  
- Recognize general attack categories  

**Key Topics:**  
- Encompasses deliberate actions to disrupt, damage, or exploit systems  
- Includes availability attacks, privilege escalation, data theft, and traffic manipulation  
- Understanding attacks helps design defenses  

---

## Module 19.2: Distributed Denial of Service (DDoS)  
**Learning Objectives:**  
- Explain how DDoS attacks work  
- Recognize their effects  

**Key Topics:**  
- Overwhelming a system with malicious traffic  
- Botnets used to flood targets with requests  
- Impact: downtime, lost revenue, degraded services  
- Mitigation: traffic filtering, scrubbing, CDNs, rate limiting  

---

## Module 19.3: DNS Attacks  
**Learning Objectives:**  
- Identify DNS attack types  
- Recognize their consequences  

**Key Topics:**  
- DNS poisoning/cache poisoning: redirecting traffic to malicious sites  
- DNS tunneling for covert exfiltration  
- Amplification attacks using DNS servers  
- Mitigation: DNSSEC, monitoring, secure recursive resolvers  

---

## Module 19.4: Directory Traversal Attack  
**Learning Objectives:**  
- Define directory traversal  
- Recognize how it is exploited  

**Key Topics:**  
- Manipulating input to access unauthorized directories/files  
- Example: `../../etc/passwd` injection  
- Risks: exposure of sensitive system files, credential theft  
- Defenses: input validation, least privilege  

---

## Module 19.5: Execution and Escalation Attacks  
**Learning Objectives:**  
- Explain execution and escalation techniques  
- Recognize their impact  

**Key Topics:**  
- Exploiting software flaws to execute arbitrary code  
- Privilege escalation to gain higher-level access  
- Common in OS and application vulnerabilities  
- Mitigation: patching, least privilege, monitoring  

---

## Module 19.6: Replay Attacks  
**Learning Objectives:**  
- Define replay attacks  
- Recognize risks and defenses  

**Key Topics:**  
- Capturing and retransmitting valid authentication data  
- Allows unauthorized access without cracking credentials  
- Defenses: session tokens, timestamps, encryption  

---

## Module 19.7: Session Hijacking  
**Learning Objectives:**  
- Explain session hijacking  
- Recognize methods used  

**Key Topics:**  
- Taking over an active session (e.g., stealing cookies, session IDs)  
- Allows impersonation of legitimate users  
- Defenses: encryption (TLS), secure cookies, session expiration  

---

## Module 19.8: On-Path Attacks  
**Learning Objectives:**  
- Define on-path attacks (formerly MITM)  
- Recognize their consequences  

**Key Topics:**  
- Attacker intercepts and alters communication between two parties  
- Examples: eavesdropping, data manipulation, credential theft  
- Defenses: TLS, VPNs, certificate pinning  

---

## Module 19.9: Injection Attacks  
**Learning Objectives:**  
- Recognize common injection attack types  
- Explain their impact  

**Key Topics:**  
- Attacker inserts malicious code/commands into input fields  
- Types: SQL, XML, LDAP, command injection  
- Risks: data exposure, system compromise  
- Defenses: input validation, parameterized queries, sanitization  

---

## Module 19.10: Indicators of Compromise (IoCs)  
**Learning Objectives:**  
- Define IoCs and their importance  
- Recognize examples  

**Key Topics:**  
- IoCs are forensic artifacts indicating malicious activity  
- Examples: unusual outbound traffic, suspicious logins, file hash changes, abnormal DNS requests  
- Used in threat hunting, detection, and incident response  

---

## Completion Status  
- All Section 19 materials reviewed  
- Flashcards created for DDoS, DNS attacks, injection methods, and IoCs  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
