# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 23 – Alerting and Monitoring  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 23 covers the tools and practices for alerting and monitoring in cybersecurity operations. Learners examine SNMP, SIEM platforms, SCAP, NetFlow, and monitoring resources to detect threats, generate alerts, and provide visibility into security events.  

---

## Module 23.1: Alerting and Monitoring Overview  
**Learning Objectives:**  
- Define alerting and monitoring in cybersecurity  
- Recognize their roles in defense  

**Key Topics:**  
- Monitoring provides visibility into systems, networks, and users  
- Alerting notifies security teams of suspicious or abnormal activity  
- Together, form the foundation of detection and response  
- **Alerting:** prrocess of notifying relevant personnel as a potential security incident occurs
	- true positive, false positive, true negative, false negative
	- alert fatigue can be avoided by maximizing true positives and minimizing false positives
- **Monitoring:** involves continuous observation of a system or network
	- automated, manual
	- monitoring resources
	- alerting and monitoring activities
	- simple network management protocol (SNMP)
	- Security Information and Event Management (SIEM)
		- agent-based, agentless
	- data from security tools
	- Security Content Automation and Protocol (SCAP)
	- Networrk Traffic Flows
	- Single Pane of Glass (SPOG)

---

## Module 23.2: Monitoring Resources  
**Learning Objectives:**  
- Explain what resources should be monitored  
- Recognize monitoring goals  

**Key Topics:**  
- Systems: servers, endpoints, applications, databases  
- Networks: firewalls, routers, switches, wireless APs  
- Users: logins, behavior, access patterns  
- Goals: detect intrusions, identify misconfigurations, ensure compliance  
- **System Monitoring:** obserrvation of computer system, including the utilization and consumption of it resources
	- **Baseline:** established performance metrics and data points for standard behavior of a system, network, or application
		- baseline allos detection of deviations and potential issues, enabling proactive troubleshooting and maintenance
- **Application Monitoring:** emphasizes the management and monitoring of software application performance and availability
- **Infrastructure Monitoring:** observation of the performance and availability of an organization's physical and virtual infrastructure
	- identify potential issues, ensure performance optimization
	- **System Monitoring:** system resources
	- **Appplication Monitoring:** softare applications
	- **Infrastructure Monitoring:** physical or virtual infrastructure
	- performance, reliability, user satisfaction

---

## Module 23.3: Alerting and Monitoring Activities  
**Learning Objectives:**  
- Recognize types of monitoring activities  
- Explain alerting considerations  

**Key Topics:**  
- Continuous vs. periodic monitoring  
- Real-time alerting vs. batch reporting  
- Reducing false positives through tuning and baselines  
- Alerts prioritized by severity and impact  
- **Log Aggregation:** process of collecting and consolidating log data from various sources into centralized location
	- system issues, security incidents, performance problems
	- monitor performance, identify bottlenecks, make informed decisions
	- failed login attempts, changes to user privileges, suspicious netwwork connections
	- detect security incidents, investigate breaches, gather evidence
- **Alerting:** involves setting up notifications to inform relevant stakeholders when specific events or conditions occur
	- email, text messages, push notifications
	- issue resolution, incient detection, compliance
- **Scanning:** involves examining systems, netwwworks, or applications to identify vulnerabilities, configurration issues, or other potential problems
	- Nessus, OpenVAS, Qualys
	- **Vulnerability Scan:** checks for vulnerabilities in systems, networks, or applications by comparing the system's state against databases of vulnerabilities
	- **Configuration Scan:** checks for misconfigurations that could impact system perrrformance or security
		- CIS Controls, PCI DSS
		- open port, eak access control, non-comppliant settings
	- **Code Scan:** checks the sourrce code of an application forr potential issues, such as security vulnerabilities or coding errors
		- SQL Injection Point, Cross-Site Scrripting (XSS), Codingg Errrors
- **Reporting:** involves generating summaries or detailed reports based on the collected and analyzed data
- **Archiving:** involves storing data for long-term retention and future referrrence, including organization's log data, perrformance data, and incident data
	- Amazon S3, Google Cloud Storage 
- **Alet Response and Remediation or Validation:** involves taking appropriate actions in response to alerts and ensuring that the identified issues have been effectively addressed
	- investigating, escalating, initiating
	- this helps to determine the specific response based on the nature of the alert
	- **Remediation:** steps used to resolve identified issues or vulnerabilities
	- **Validation:** involves verifying that the remediation implemented was actually successful and has effectively addressed the given issue or vulnerability
		- **Quarantining:** isolating a system, network, or application to prevent the spread of a threat and limit its potential impact 
		- **Alert Tuning:** adjusting alert parameters to reduce errors, false positives, and to improve the overall relevance of the alerts being generated by a given system

---

## Module 23.4: Simple Network Management Protocol (SNMP)  
**Learning Objectives:**  
- Define SNMP and its role  
- Recognize its security considerations  

**Key Topics:**  
- SNMP monitors and manages network devices  
- Versions: SNMPv1/v2c (insecure), SNMPv3 (secure, supports encryption and authentication)  
- Useful for device health, status, and alerts  
- **Simple Netwwork Management Protocol (SNMP):** internet protocol for collecting and organizing information about managed devices on IP netwworks and for modifying that information to change device behavior
	- routers, sqitches, firewalls, printers, servers, end user client devices
	- uptime, configuration changes, unexpected donwtime, other essential information
- **Granular:** sent trap messages get a unique objective identifier to distinguish each message as a unique message being received
- **Management Information Base (MIB):** used to describe the structure of the management data of a device subsystem using a hierarchical namespace containing object identifiers
- **Verbose:** SNMP traps may be configured to contain all the information about a given alert or event as a payload
	- data in these SNMP traps are stored in a simple key-value pair configuration knon as a "variable binding"
	- SNMPv1, SNMPv2, SNMPv3
	- SNMP version one and to use a community string to give them access to the device as their security mechanism
	- default community strings of public (read-only) or private (read-rite) devices are considered a security risk
	- SNMP version 3 provides three security enhancements hich added integrity, authentication, and confidentiality to the SNMP protocol
	- since DES is considered a eak algorithm, it is being replaced ith 3DES and AES in newer devices that reply on SNMP v3

---

## Module 23.5: Security Information and Event Management (SIEM)  
**Learning Objectives:**  
- Explain SIEM systems and their capabilities  
- Recognize use cases  

**Key Topics:**  
- Collect and correlate logs from across the environment  
- Provide dashboards, alerts, and forensic data  
- Support compliance reporting and incident detection  
- Examples: Splunk, QRadar, Elastic, LogRhythm  
- **SIEM:** solution that provides real-time or near-real-time analysis of security alerts that are generrated by netwwwwork hardare and applications
	- VPN System, Physical Security System
	- SIEM consolidates and correlates system logs into a central database
	- servers, databases, firewalls, orrkstations
	- repeated login failures, unusual data transfers, changes in file permissions
	- the source of the attack, the systems or data it's targeting, the methods it's using
- SIEM can be deployed using various methods
- software, hardare appliances, outsourced managed serrvice
- **Agent:** softare agent installed on each system, such as a server or orkstation, from hich the SIEM needs to collect log data
- **Agentless:** under this approach, the SIEM system directly collects log data from each system using standard protocols such as SNMP or WMI
	- log all relevan events and filter irrelevant data
	- establish and document scope of events
	- develop use cases to define a threat
	- plan incident response for a threat or event
	- establish a ticketing system to track events
	- schedule regular threat hunting
	- provide auditors and analysts an evidence trail
- There are many commercial and open-source SIEM solutions available
	- Splunk, ELK or Elastic Stack, ArcSight, QRadar
	- **Splunk:** market-leading big data information gathering and analysis tool that can import machine-generated data via a connector or a visibility add-on
	- **Elastic Stack (ELK):** collection of free and open-source SIEM tools that provide storage, search, and analysis functions
		- Elasticsearch, Logstash, Kibana, Beats
- ELK Stack may be installed locally or as a cloud-based solution
- **ArcSight:** SIEM log management and analytics software that can be used for compliance reporting for legislation and regulations like HIPAA, SOX, and PCI DSS
- **QRadar:** SIEM log management, analytics, and compliance reporrting platform created by IBM
- The choice of SIEM to use depends on specific requirements and preferences

---

## Module 23.6: Data from Security Tools  
**Learning Objectives:**  
- Recognize data sources for monitoring  
- Explain integration needs  

**Key Topics:**  
- Sources: IDS/IPS, firewalls, endpoint tools, vulnerability scanners  
- Logs, telemetry, metrics aggregated into SIEM or monitoring systems  
- Correlation improves detection accuracy  
- **Security Information and Event Management System (SIEM):** the central hub for the consolidation to provide a holistic vieww of an organization's security landscape
- **Antivirus Software:** fundamental security tool that protects systems against malware, including viruses, worms, trojans, ransomwware, and spyware
- **Data Loss Prevention Systems:** used to monitor and control data endpoint, network traffic, and data stored in the cloud to prevent potential data breaches from occuring
- **Network Intusion Detection Systems (NIDS):** passively identifies any potential threats
- **Network Intrusion Prevention Systems (NIPS):** actively blocks or pprevents these potential threats
- **Firewalls:** serve as a barrier between a trusted internal network and an untrusted external network
	- firewalls can generate logs that contain data about allowed and blocked traffic, rule changes, and any detected potential threats
- **Vulnerability Scanners:** tools that identify security weaknesses in a system, including missing patches, incorrect configurations, and other types of known vulnerabilities
- by consolidating data from these diverse seucirty tools into a SIEM, organizations can gain a comprehensive view of their security posture

---

## Module 23.7: Security Content Automation Protocol (SCAP)  
**Learning Objectives:**  
- Define SCAP and its benefits  
- Recognize its use in monitoring  

**Key Topics:**  
- Framework for automating vulnerability management and compliance checks  
- Standardizes vulnerability definitions (CVE, CVSS, OVAL)  
- Ensures consistency across security tools  
- **Security Content Automation Protocol (SCAP):** open standards that automate vulnerability management, measurement, and policy compliance for systems in an organization
	- SCAP was developed by the National Institute of Standards and Technology (NIST)
	- vulneraability scanning, configuration checking, software inventory
	- SCAP is also heavily used with internal and external compliance requirements
- **Open Vulnerability and Assessment Language (OVAL):** XML schema for describing system security states and querying vulnerability reports and information
- **Extensible Configuration Checklist Description Format (XCCDF):** XML schema for developing and auditing best-practice configuration checklists and rules
- **Asset Reporting Fromat (ARF):** XML schema for expressing information about assets and the relationships between assets and reports
	- ARF is vendor and technology neutral, it is flexible and is suited for a wwide variety of reporting applications
- **Common Configuration Enumberation (CCE):** scheme for provisioning secure configuration checks across multiple sources
- **Common Platform Enumeration (CPE):** scheme for identifying hardware devices, operating systems, and applications
	- `cpe:/`
	- `cpe:/part:vendor:product:version:update:edition:language`
- **Common Vulnerabilities and Exposures (CVE):** list of records where each item contains a unique identifier used to describe a publicly known vulnerability
	- `CVE-2017-0144`
	- Eternal Blue is the tool that was used to exploit this SMB vulnerability
- **Common Vulnerability Scoring System (CVSS):** used to provide a numerical score to reflect the severity of a given vulnerability
	- `0 = None`
	- `0.1 - 3.9 = Low`
	- `4.0 - 6.9 = Medium`
	- `7.0 - 8.9 = High`
	- `9.0 - 10.0 = Critical`
	- it does not account for any mitigation already in place
- **Benchmark:** set of security configuration rules for some specific set of products to provide a deetailed checklist that can be used to secure systems to a specific baseline
	- Red Hat Enterprise Linux
	- Center for Internet Security's Microsoft Windows 10 Enterprise
	- using benchmarks with SCAP-compliant tools helps organizations automate system security maintenance

---

## Module 23.8: NetFlow and Flow Analysis  
**Learning Objectives:**  
- Define NetFlow/flow analysis  
- Recognize its role in security  

**Key Topics:**  
- Provides metadata on network traffic flows (who talks to whom, how much, when)  
- Detects anomalies, exfiltration, DDoS patterns  
- Complements packet capture with high-level visibility  
- **Full Packet Capture (FPC):** captures the entire packet, including the header and the payload for all traffic entering and leaving a netwwork
- **Flow Analysis:** relies on a flow collwctor, which records metadata and statistics rather than recording each frame that passes through the network
	- flow analysis does not provide the actual content
	- flow analysis rapidly generates visualizations to map network connections, traffic types, and session volumes
- **NetFlow:** a Cisco-developed means of reporting network flow info to a structured database
- **IP Flow Information Export (IPFIX):** defines traffic flows based on shared packet characteristics
	- protocol interface, IP version/type, source/destination IP, source/destination port, IP service type
- **Zeek:** passively monitors a network like a sniffer, but only logs full packet capture data of potential interest
	- performs normalization of the data and stores it as a tab-delimited or JSON-formatted text file
- **Multi Router Traffic Grapher (MRTG):** created graphs showwing traffic flows through the netwwork interfaces of routers and switches by polling the appliances using SNMP

---

## Module 23.9: Single Pane of Glass  
**Learning Objectives:**  
- Define “single pane of glass” monitoring  
- Recognize its advantages  

**Key Topics:**  
- Unified dashboards aggregating multiple security and monitoring tools  
- Provides centralized visibility and faster decision-making  
- Reduces alert fatigue by consolidating events  
- a single pane of glass provides security teams with a unified view for easy access to critical information, aiding informed dedcision-making
	- simplifies security management, offering a unified view in detecting and responding to threats
	- security teams can monitor the environment for suspicious signs like unusual traffic or failed logins
	- security teams can track the progress of incident response, ensuring that all required steps are taken to resolve an incident
	- a single pane of glass can improve the efficiency of a security operation center
	- a single pane of glass improves collaboration and communication within the security teams
	- a single pane of glass simplifies compliance with regulatory requirements for the security team
	- a single pane of glass can be implemented as software or hardware
- **Defining the Requirements:** involves identifying the inforrmation, tools, and systems
- **Identifying and Integrating Data Sources:** involves identifying the data sources that the security team needs to access
	- APIs, Webhooks, Plugins, Connectors
- **Customizing the Interface:** involves designing the user interface and configuring panels and views to display information and data
- **Developing Standard Operating Procedures and Documentation:** ensures that the security teams know hoe to use the single pane of glass and understand the processes and procedures
- **Continuously Monitoring and Maintaining the Solution:** includes regular reviewing of the data and information

---

## Completion Status  
- All Section 23 materials reviewed  
- [Flashcards created for SNMP versions, SIEM capabilities, SCAP standards, and NetFlow use cases](https://jeremyrayjewell-flashcards.netlify.app/security-plus-dion.html#deck=2)        

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
