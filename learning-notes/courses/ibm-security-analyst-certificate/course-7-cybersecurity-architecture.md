# IBM Cybersecurity Analyst Professional Certificate  
## Course 7 – Cybersecurity Architecture  

[Coursera](https://www.coursera.org/learn/cybersecurity-architecture/home/module/1)  
---

## Overview  
Course 7 focuses on the design of secure systems through the lens of cybersecurity architecture. Learners study foundational security principles, the CIA Triad, roles and tools of cybersecurity architects, and the domains of modern security practice. The course emphasizes frameworks such as the NIST Cybersecurity Framework (CSF), and applies architectural thinking to identity and access management, endpoint security, networking, applications, and data. Case studies and labs illustrate practical implementation of defense-in-depth, least privilege, separation of duties, secure-by-design, and KISS (Keep It Simple, Stupid) principles.  

---

## Module 1: Cybersecurity Architecture Fundamentals  
This module establishes core principles, the CIA Triad, and the mindset of the cybersecurity architect.  

**Learning Objectives:**  
- Apply the five fundamental security principles and avoid security by obscurity  
- Explain the CIA Triad (Confidentiality, Integrity, Availability) with technical examples  
- Define the role of the cybersecurity architect and their key tools  
- Relate security frameworks (NIST CSF) to architectural practice  

**Key Topics & Details:**  
- **Five Principles:**  
  1. **Defense in Depth** – multiple overlapping layers (MFA, EDR, firewalls, vulnerability testing, encryption) to eliminate single points of failure.  
  2. **Least Privilege** – grant only necessary rights, eliminate unused services, change defaults, prevent privilege creep, and run annual recertification.  
  3. **Separation of Duties** – split responsibilities between requesters/approvers or multi-key systems to prevent single points of control.  
  4. **Secure by Design** – integrate security from requirements through design, coding, testing, and deployment; not a “bolt-on” at the end.  
  5. **KISS Principle** – keep controls simple for legitimate users; complexity increases bypasses and weakens real security.  
  - **Anti-Principle:** Security by Obscurity — relying on secrecy rather than strong, open algorithms violates Kerckhoff’s principle; use transparent algorithms (AES, RSA) where only the key is secret:contentReference[oaicite:1]{index=1}.  

- **CIA Triad:**  
  - **Confidentiality** – achieved through authentication, authorization, encryption (MFA + RBAC + symmetric/asymmetric encryption).  
  - **Integrity** – enforced with cryptographic functions (digital signatures, MACs, blockchain immutability). Protects against tampered logs or altered transactions.  
  - **Availability** – ensuring uptime for authorized users, defending against DoS/DDoS, SYN floods, reflection/amplification attacks, and requiring backups, fail-safes, and DR plans:contentReference[oaicite:2]{index=2}.  

- **Architect Role & Mindset:**  
  - Architects = “whiteboard”; engineers = “keyboard.”  
  - Architects start with stakeholder requirements → reference diagrams → security overlays.  
  - They anticipate *how systems may fail* (stolen credentials, infected devices, breached networks) and plan mitigations (MFA, MDM/EDR, firewalls, encryption).  
  - Tools of the trade: Business Context diagrams, System Context diagrams, Architecture Overview diagrams.  
  - Use frameworks (NIST CSF: Identify, Protect, Detect, Respond, Recover) to ensure complete coverage:contentReference[oaicite:3]{index=3}.  

---

## Module 2: Access Management and Endpoint Security  
This module covers identity, access control, and endpoint device security.  

**Learning Objectives:**  
- Implement IAM to enforce least privilege  
- Compare RBAC and PAM approaches  
- Apply endpoint security controls (AV, EDR, MDM)  

**Key Topics & Details:**  
- **IAM (Identity & Access Management):** Authenticate (passwords, MFA), authorize (RBAC policies), and account for usage. Ensures right users/devices access right resources, at right times.  
- **RBAC (Role-Based Access Control):** Permissions tied to roles (e.g., Developer, HR, Sales) instead of individuals; reduces admin overhead and unauthorized access.  
- **PAM (Privileged Access Management):** Secures privileged accounts via credential rotation, access request workflows, monitoring, and logging. Prevents misuse of admin rights.  
- **Case Studies:**  
  - *Worldwide Capital* – IAM reduced unauthorized access to financial client data.  
  - *Velocity Tech* – RBAC streamlined permissions management and improved efficiency.  
  - *Optima Health* – PAM reduced risks of privileged account misuse and data breaches:contentReference[oaicite:4]{index=4}.  
- **Endpoint Security:**  
  - MDM (Mobile Device Management) for enforcing policy on BYOD/jailbroken devices.  
  - EDR (Endpoint Detection & Response) for advanced telemetry and mitigation.  
  - Antivirus and hardening against unnecessary services and default accounts.  

---

## Module 3: Network, Application, and Data Security  
This module examines layered protections across infrastructure.  

**Learning Objectives:**  
- Apply network-level defenses (firewalls, VPNs, IDS/IPS)  
- Integrate DevSecOps into application development  
- Encrypt and classify data according to sensitivity  

**Key Topics & Details:**  
- **Network Security:**  
  - Firewalls (perimeter + internal segmentation)  
  - IDS/IPS (detection + blocking)  
  - VPNs for secure tunnels  
- **Application Security:**  
  - Vulnerability scanning, penetration testing, DevSecOps lifecycle  
  - Secure coding practices and CI/CD integration  
- **Data Security:**  
  - Encryption (AES, RSA), access controls, and masking/tokenization for sensitive fields  
  - Classification: public, private, restricted, confidential, critical  

---

## Module 4: Detection and Response  
This module highlights how security telemetry is monitored and how organizations respond to attacks.  

**Learning Objectives:**  
- Monitor telemetry with SIEM tools  
- Detect intrusions and anomalies  
- Orchestrate incident response and recovery plans  

**Key Topics & Details:**  
- **SIEM (Security Information & Event Management):** Aggregates logs from endpoints, networks, applications, and databases. Detects anomalies, correlates events, and triggers alerts.  
- **Incident Response Lifecycle:** Preparation → Detection → Containment → Eradication → Recovery → Lessons learned.  
- **Response Orchestration:** Automating containment (firewall rules, account disablement) and escalating high-severity incidents.  

---

## Module 5: Final Project, Exam, and Wrap-Up  
The final module consolidates all domains into a project and exam.  

**Learning Objectives:**  
- Apply architectural principles to design a secure enterprise system  
- Align with the NIST CSF functions (Identify, Protect, Detect, Respond, Recover)  
- Evaluate case studies and glossary for professional application  

**Key Topics:**  
- **Final Project:** Develop a secure enterprise reference architecture covering IAM, endpoint, network, application, and data domains, including monitoring and response.  
- **Case Study:** Apply lessons to a real-world business scenario.  
- **Glossary & Exam:** Reinforce terminology and confirm mastery across all modules.  

---

## Supplementary Projects  
- **IAM Lab** – Implement least privilege using IAM tools  
- **RBAC Case Study** – Assign permissions across organizational roles  
- **PAM Simulation** – Secure privileged accounts with monitoring and credential rotation  
- **CIA Triad Scenarios** – Confidentiality via MFA/encryption, Integrity via hashing/blockchain, Availability via DoS mitigation  
- **SIEM Monitoring Lab** – Analyze logs, detect anomalies, simulate response workflows  
- **Final Project** – Develop secure architecture blueprint with NIST CSF integration  

---

## Completion Status  
- All modules completed  
- All videos, readings, and case studies completed  
- All graded assignments and final project submitted with perfect scores (100%)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
