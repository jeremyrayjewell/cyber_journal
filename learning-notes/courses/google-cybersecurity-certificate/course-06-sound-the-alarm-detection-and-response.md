# Sound the Alarm: Detection and Response – Notes  

## Google Cybersecurity Certificate (Course 6) 

[Coursera](https://www.coursera.org/learn/detection-and-response/home/welcome)

---

### **Course Overview**  
Course 6 provides a comprehensive overview of incident detection, analysis, and response. It covers the SOC’s role in monitoring, detecting, and investigating suspicious activity, along with frameworks like NIST’s Computer Security Incident Handling Guide (SP 800-61r2). Learners gain familiarity with the incident response lifecycle, key detection methods, investigation tools, and reporting processes. The course emphasizes communication, documentation, and collaboration across teams during incident handling.  

---

### **Core Structure**  
1. Introduction to Detection and Incident  and Response  
2. Network Monitoring and Analysis
3. Incident investiagtion and Response
4. Network Traffic and Log Using IDS and SIEM Tools
  
---

### **Key Cybersecurity Concepts & Acronyms**  
- **SOC** – Security Operations Center: centralized unit for monitoring, detecting, analyzing, and responding to security events.  
- **IR** – Incident Response: organized approach to addressing and managing a security breach or attack.  
- **SIEM** – Security Information and Event Management: platform that collects and analyzes log data for suspicious activity.  
- **IOCs** – Indicators of Compromise: forensic data that identifies potential intrusion.  
- **SOAR** – Security Orchestration, Automation, and Response: integrates security tools and processes for faster incident handling.  
- **Playbook** – A documented, repeatable process for handling specific incident types.  
- **NIST SP 800-61r2** – U.S. federal guide for computer security incident handling.  
- **Chain of Custody** – Documentation process to preserve evidence integrity.  
- **Eradication** – Removing threat artifacts and vulnerabilities post-containment.  
- **Lessons Learned** – Review process to improve future incident handling.  

---

### **Core Skills Introduced**  
**Transferable Skills:**  
- Communication and collaboration under time-sensitive conditions  
- Incident documentation and reporting  
- Coordinating cross-team efforts  

**Technical Skills:**  
- Using SIEM tools for detection and analysis  
- Identifying IOCs through log analysis and alerts  
- Applying NIST IR lifecycle phases  
- Preserving evidence and maintaining chain of custody  
- Executing containment, eradication, and recovery measures  

---

### **Incident Response Lifecycle (NIST SP 800-61r2)**  
1. **Preparation** – Develop IR policy, establish communication channels, train personnel, prepare detection tools.  
2. **Detection & Analysis** – Identify suspicious events, validate incidents, analyze IOCs.  
3. **Containment, Eradication & Recovery** – Short-term and long-term containment strategies, remove malware, patch vulnerabilities, restore systems.  
4. **Post-Incident Activity** – Lessons learned meeting, update playbooks, adjust security posture.  

---

### **Detection Methods**  
- **Signature-Based Detection** – Uses known patterns (hashes, IPs) to identify threats.  
- **Anomaly-Based Detection** – Identifies deviations from baseline activity.  
- **Behavioral Detection** – Flags actions consistent with malicious tactics (MITRE ATT&CK).  

---

### **Investigation Tools & Techniques**  
- **Log Analysis** – Reviewing system, application, firewall, and IDS/IPS logs.  
- **SIEM Queries** – Filtering events, correlating alerts.  
- **Packet Capture Tools** – Wireshark, tcpdump for network-level investigation.  
- **Endpoint Analysis** – Checking processes, services, registry entries, startup items.  

---

### **Incident Response Actions**  
- **Containment:** isolate affected systems, block malicious IPs, disable accounts.  
- **Eradication:** remove malware, close vulnerabilities, wipe/rebuild compromised hosts.  
- **Recovery:** restore from backups, monitor systems for signs of reinfection.  

---

### **Reporting & Documentation**  
- **Internal Reports** – SOC to management, technical summaries, incident timeline.  
- **External Reports** – Required for compliance (PCI DSS, HIPAA, GDPR breach notifications).  
- **Chain of Custody Forms** – Track evidence collection, handling, and transfer.  

---

### **Readings – Additional Insights**  
- **NIST Guidelines** – Stress the importance of preparation and structured processes.  
- **Incident Classification** – Clear definitions for events vs. incidents prevent misallocation of resources.  
- **Communication Plans** – Pre-defined escalation paths ensure faster response.  
- **Metrics for IR** – Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR) are key performance indicators.  
- **Automation Benefits** – SOAR reduces analyst fatigue and improves response speed.  
- **Legal & Regulatory Considerations** – Data breach laws vary by jurisdiction; IR plans must align with applicable regulations.  

---

### **Key Takeaways**  
- Incident handling must be systematic and follow a recognized framework.  
- Effective communication and documentation are critical for both technical and legal purposes.  
- Combining human expertise with automation tools increases SOC efficiency.  
- Lessons learned are essential to improve defenses and readiness.  

---

**Completion Status:**
- All modules, readings, and videos completed.
- All graded assignments passed with high scores.

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
