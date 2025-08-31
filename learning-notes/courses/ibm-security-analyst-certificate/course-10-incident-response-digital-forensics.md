# IBM Cybersecurity Analyst Professional Certificate  
## Course 10 – Cybersecurity Incident Response and Digital Forensics  

[Coursera](https://www.coursera.org/learn/ibm-incident-response-digital-forensics/home/module/1)   
---

## Overview  
Course 10 focuses on incident response (IR) and digital forensics (DFIR). Learners study industry frameworks (NIST, SANS), incident response processes (preparation → detection/analysis → containment → eradication → recovery → post-incident), and documentation best practices. The course also emphasizes digital forensics methods — evidence collection, imaging, RAM and network forensics, log and email analysis, cloud/mobile forensics, chain of custody, and advanced analysis (live analysis, reverse steganography). Tools covered include SIEMs, SOAR platforms, EDR solutions, forensic utilities, and compliance/reporting platforms. The final project requires creating an incident response plan and completing a simulated digital investigation.  

---

## Module 1: Incident Response  
**Learning Objectives:**  
- Explain IR principles, events vs incidents, and IR benefits  
- Apply NIST and SANS frameworks  
- Describe preparation, detection/analysis, containment, eradication, recovery, and post-incident review  
- Document and communicate IR processes effectively  

**Key Topics & Details:**  
- **Events vs Incidents:** Events = observable activities (logins, system changes). Incidents = confirmed breaches affecting confidentiality, integrity, availability.  
- **Benefits of IR Plans:** Reduce financial/regulatory impact, support system recovery, minimize downtime. IBM’s 2024 Cost of a Data Breach Report shows orgs with IR teams/plans saved ~$2.66M vs those without:contentReference[oaicite:1]{index=1}.  
- **Frameworks:**  
  - **NIST IR Lifecycle:** Preparation → Detection/Analysis → Containment/Eradication/Recovery → Post-incident activity.  
  - **SANS IR Framework:** Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned. Differences: SANS more granular; specifies two-week review meeting.  
- **Preparation:** Policies (roles, classification, comms, investigations, strategies, improvement, training), IR plans (playbooks), IR teams, and simulations.  
- **Tools & Practices:** SIEM (Splunk, Sentinel, QRadar, Snort), EDR (Defender, CrowdStrike, SentinelOne, OSSEC), SOAR (Splunk Phantom, IBM Resilient, Cortex XSOAR, DFLabs IncMan), incident response platforms (TheHive), and compliance tools (AuditBoard, Netwrix, Vanta, OpenSCAP).  
- **Documentation:** Pre-IR (plans, roles, comms), during IR (event logs, comms records, severity assessments), post-IR (reports, lessons learned, improvement recs).  

---

## Module 2: Digital Forensics  
**Learning Objectives:**  
- Define digital forensics and its role in investigations  
- Explain DFIR (integration of forensics with IR)  
- Apply NIST’s 4-step process: Identification → Examination → Analysis → Reporting  
- Use tools and techniques to preserve and analyze evidence  

**Key Topics & Details:**  
- **Evidence Collection:** Imaging (bit-for-bit, incl. slack/free space) vs logical backups. Chain of custody ensures admissibility; NIST framework includes Identify, Protect, Detect, Respond, Recover.  
- **Data Sources:**  
  - File systems (metadata, deleted files, timestamps, slack/free space).  
  - Memory (RAM) — malware detection, encryption keys, running processes.  
  - Network — IPs, payloads, comms paths (Wireshark, NetFlow, Scrutinizer).  
  - Applications/logs — reveal user actions, errors, anomalies.  
  - Email — phishing/malware entry vectors.  
  - Mobile/IoT — GPS, call logs, texts, installed apps.  
  - Cloud — logs, VM snapshots, storage.  
- **Analysis:** Live analysis (volatile data capture) vs reverse steganography (detect hidden messages in media). Tools: EnCase, FTK, Autopsy.  
- **Reporting:** Must be clear, legally sound, and accessible to non-technical stakeholders. Includes evidence chain, methods, findings, limitations. Often used in legal testimony.  

---

## Module 3: Final Project and Wrap-Up  
**Project Tasks:**  
- Create an incident response plan covering roles, policies, detection, containment, eradication, and recovery.  
- Perform a simulated digital forensic investigation.  
- Collect/analyze evidence across multiple sources (files, RAM, logs, email, cloud/mobile).  
- Apply chain of custody and document actions.  
- Report findings in structured format suitable for both technical and non-technical audiences.  

**Wrap-Up:**  
- Course glossary of IR and DFIR terms  
- Guidance on continuing practice with tools and resources (NIST, CISA, SANS, FBI InfraGard, Incident Response Consortium, Cyber Essentials Starter Kit, DoD testing guide, etc.):contentReference[oaicite:2]{index=2}  

---

## Hands-On Labs & Projects  
- **Incident Response Simulations** – Interactive activities applying NIST and SANS frameworks  
- **Log Investigation Lab (Cowrie)** – Detect and analyze malicious activity through log files  
- **Forensic Data Labs** – File recovery, slack/free space analysis, MAC metadata, deleted files  
- **Advanced Analysis Labs** – Live analysis, reverse steganography exercises  
- **Documentation Exercises** – Draft event logs, comms records, severity assessments, lessons learned  
- **Final Project** – Full IR plan + digital forensic investigation with reporting  

---

## Completion Status  
- All modules completed  
- All videos, readings, labs, and case studies completed  
- All graded assignments and final project submitted with perfect scores (100%)  
