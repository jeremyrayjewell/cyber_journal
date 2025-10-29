# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 24 – Incident Response  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 24 covers incident response processes, including threat hunting, forensic analysis, and testing response readiness. Learners explore structured incident response frameworks, root cause analysis, and digital forensic procedures to manage and recover from security incidents effectively.  

---

## Module 24.1: Incident Response Overview  
**Learning Objectives:**  
- Define incident response (IR)  
- Recognize its goals  

**Key Topics:**  
- Structured approach for detecting, containing, and recovering from incidents  
- Protects confidentiality, integrity, and availability  
- Ensures lessons learned to strengthen defenses  
- **Incident Response Process:** outlines a structured approach to manage and mitigate security incidents effectively
	- minimize impact, reduce response time, hasten recovery
	- incident detection and classification, threat containment and eradication, evidence preservation, communication and reporting, lessons learned
- incident response overview, threat hunting, root cause analysis, incident response training and testing, digital forensic procedures, disk imaging and analysis

---

## Module 24.2: Incident Response Process  
**Learning Objectives:**  
- Explain stages of the IR process  
- Recognize their importance  

**Key Topics:**  
- Common framework: **Preparation → Detection → Containment → Eradication → Recovery → Lessons Learned**  
- Provides repeatable and structured response  
- Reduces impact, speeds recovery  
- **Incident:** act of violating an explicit or implied security policy
- **Incident Response Procedures:** guidelines for handling security incidents
	- **Preparation:** involves strengthening systems and networks to resist attacks
		- the preparation phase is about getting readyy for future incidents
	- **Detection:** identifies security incidents
	- **Analysis:** involves a thorough examination and evaluation of the incident
		- stakeholders are informed, containment begins, and initial response actions are taken
	- **Containment:** limits the incident's impact by securring data and protecting business operations
	- **Eradication:** starts after containment and aims to remove malicious activity from the system or network
	- **Recovery:** restores systems and services to their secure state after an incident
		- restoring from a known good backup, installing security patches, implementing configuration updates
		- recovery procedures can involve monitoring for lingering threats to ensure a smooth return to normal operations
	- **Post-incident activity/Lessons learned:** happens after containment, eradication, and full system recovery
- **Root Cause Analysis:** idnetifies the incident's source and how to prevent it in the future
	- define/scope the incident, determine the casual relationships that led to the incident, identify an effective solution, implement and track the solutions
- **Lessons Learned Process:** documents experiences during incidents in a formalized way
- **After-action Report:** collects formalized information about what occurred
	- incident response and recovery are crucial in organizations due to frequent major data breaches in the news
	- large organizations have full-time incident response teams, while smaller ones form temproary teams for specifc incidents
	- leader, subject-matter experts, IT support staff, legal counsel, human resources, public relations
	- leadership and management ensure the incident response team has necessary funding, resources, and expertise
	- management makes crucial decisions and communicates them during incident response
		- expensive, unfamiliar

---

## Module 24.3: Threat Hunting  
**Learning Objectives:**  
- Define threat hunting  
- Recognize its role in IR  

**Key Topics:**  
- Proactive search for adversaries before alerts are triggered  
- Involves analyzing logs, threat intel, and anomalies  
- Complements reactive detection methods  
- **Threat Hunting:** cybersecurity method for finding hidden threats not caught by regular security monitoring
	- **Establiish a Hypothesis:** predicting high-impact, likely event s through threat modeling
		- Who might want to harm us?
		- Who might want to break our networks?
		- How might they be able to do that?
	- **Profiling Threat Actors and Activities:** envisioning how potential attackers might intrude and what they aim to achieve
		- What TTPs might they use?
		- Are they an insider threat, a hacktivist, a criminal organization, or a nation-state APT?
		- analyze the logs and data on processes, file systems, and server changes to gather information
		- in threat hunting, it starts by assuming that the current rules haven't flagged potential threats
		- normal sensors excel at detecting known threats with established signatures in the defense systems
		- seek undetected issues, focus on what bypasses existing rules, explore cases where queries do not yield expected data
		- the goal in threat hunting is to uncover and detect new threat tactics and IoCs
			- **Advisories and Bulletins:** published by vendors and security researchers when new TTPs and vulnerabilities are discovered
			- **Intelligence Fusion and Threat Data:** use SIEM and analysis platforms to spot concerns in the logs and real-world security threats
		- if it is suspicious, examine other infected hosts and check for similarities
		- identify how the malicious process was executed on various hosts
		= identify and create new signatures for the IPS to block future attacks
- threat hunting improves detection by revealing attack methods, which allows for updated rules for more accurate future detection and prevention
- integrate threat hunting with threat intelligence to align external threats with internal logs and data sources

---

## Module 24.4: Root Cause Analysis  
**Learning Objectives:**  
- Define root cause analysis (RCA)  
- Recognize its benefits  

**Key Topics:**  
- Identifies the origin of an incident, not just symptoms  
- Prevents recurrence by addressing underlying issues  
- Uses techniques like the “5 Whys” and fault tree analysis  
- **Root Cause Analysis:** a systematic process to identify the initial source of the incident and how to prevent it from occurring again
	- define the scope of the incident, determine the casual relationships, identify an effective solution, implement and track the solution
	- look across the network and see if there are any other machines that could have been affected as well
	- identify the incident's cause and assess how many other network or organization elements share similar features
	- make sure that this process uses a no-blame approach
	- using a no-blame approach can encourage open and honest reporting
	- it was determined that both crashes were caused by issues in the aircraft's new flight control software
- the NTSB is known for recognizing that human errors are often the result of systemic issues within the aviation industry
- the primary purpose is not to assign blame but to instead figure out exactly what has occurred to cause the incident

---

## Module 24.5: Incident Response Training and Testing  
**Learning Objectives:**  
- Explain the role of training and testing in IR  
- Recognize methods used  

**Key Topics:**  
- Tabletop exercises, simulations, red team/blue team drills  
- Ensures teams are prepared and roles are clear  
- Validates effectiveness of incident response plans  
- **Training:** ensures staff grasp processes and priorities for incident response; prepares staff to handle incidents effectively
	- tailored training for diverse employee needs is essential
	- **First Responder:** procedure, machine re-image, removing a malware, change configuration settings
	- **Manager or Executive:** risk vs. reward, decision-making and communication, law enforcement and media
	- **End User:** report suspected incident occurring, remedial training
	- incorporate past incident lessons into training
	- blend technical and soft skills in training for team cohesion
- **Testing:** practical exercise of incident response procedures; evaluates applying response training in real scenarios
	- tabletop, penetration test, simulation
	- **Tabletop Exercise (TTX):** exercises simulate incidents within a control framework
		- tabletop exercises offer cost-effective training
		- tabletop exercises lack hands-on network actions
	- red team vs. blue team fosters better solutions by considering attacker and defender perspectives
- **Penetration Test:** simulates network intrusion based on threat scenarios
	- scenario-driven actions based on threat modeling
	- agree on test rules and methodology before performing a pentest
	- Metasploit, Cobalt Strike, Kali Linux, ParroOS, Commando OS
- **Simulation:** replicates real incidents for hands-on experience; replicates real incidents to assess response teams
	- **Simple scenarios:** phishing or ransomware
	- **Complex scenarios:** multi-stage attacks, data breaches in coordination with external parties
	- match simulations to the organization's risks and threats
- identifying gaps in incident response plan, improving coordination between teams, ensuring roles for all during real incidents

---

## Module 24.6: Digital Forensic Procedures  
**Learning Objectives:**  
- Define digital forensics in IR  
- Recognize forensic best practices  

**Key Topics:**  
- Preserves and analyzes digital evidence for investigations  
- Chain of custody critical for admissibility  
- Forensic tools used to analyze logs, memory, storage  
- **Digital Forensic:** process of investigating and analyzing digital devices and data to uncover evidence for legal purposes
	- **Identification:** ensures the safety of the scene, secures it to prevent any evidence contamination, and determines the scope of the evidence to be collected
		- tablet, smartphone, smart TV, server
	- **Collection:** refers to the process of gathering, preserving, and documenting physical or digital evidence in various fields
		- CIO, CSO, CEO
		- follow the proper acquisition procedures
	- **Order of Volatility:** dictates the sequence in which data sources should be collected and preserved based on their susceptibility to modification or loss
		- collect data from the system's memory
		- capture data from the system state
		- collect data from storage devices
		- capture network traffic and logs
		- collect remotely stored or archived data
	- **Chain of Custody:** documented and verifiable record that tracks the handling, transfer, and preservation of diggital evidence from the moment it is collected until it is presented in a court of law
		- maintaining a secure and unbroken chain of custody is essential
		- disk imaging, file carving
	- **Disk Imaging:** involves creating a bit-by-bit or logical copy of a storage device, preserving its entire content, including deleted files and unallocated space
	- **Analysis:** involves systematically scrutinizing the data to uncover relevant information, such as potential signs of criminal activity, hidden files, timestamps, and user interactions
	- **Reporting:** involves documenting the findings, processes, and methodologies used during a digital forensic investigation
	- **Legal Hold:** formal notification that instructs employees to preserve all potentially relevant electronic data, documents, and records
		- ensure that preservation practices are used to protect the systems and the potential evidence
		- overwritten, deleted, modified
		- making backup copies, isolating critical systems, implementing access controls
	- **Electronic Discovery:** process of identifying, collecting, and producing electronically stored information during potential legal proceedings
		- emails, documents, databases
		- forensic analysts must adhere to a code of ethics
		- avoiding bias, repeatable actions, preservation of evidence
		- use a forensic analyst who is completely removed from the situation to avoid any kind of potential bias
		- time, actions, results
		- it is important that any evidence collected is not changed or manipulated

---

## Module 24.7: Data Collection Procedures  
**Learning Objectives:**  
- Recognize methods for data collection  
- Explain integrity preservation  

**Key Topics:**  
- Collect logs, network captures, system images, memory dumps  
- Data must be preserved without alteration  
- Documented process ensures reliability  
- use digital forensic collection techniques to make forensic images of the data on those servers
- capture and hash the system image
- Forensic Toolkit (FTK), EnCase
- capture screenshots of the machines
- always follow the order of volatility when collecting evidence
- review licensing and documentation forr all systems
- **Data Acquisition:** the method and tools used to create a forensically sound copy of the data from a source device, such as system memory or a hard disk
- policiies for bringing one's own device (BYOD) complicate data acquisition because it may not be legally possible to search or seize the devices
- some data can only be collected once the system is shutdown or the power is suddenly disconnected
	- CPU registers and cache memory
	- system memory (RAM), routing tables, ARP caches, process table, temporary swap files
	- data on persistent mass storage (HDD/SDD/flash drive)
	- remote logging and monitoring data
	- physical configuration and network topology
	- archival media
	- WARNING: some Windows registry keys, like HKLM\Hardware, are only in memory and require a memorry dump to analyze

---

## Module 24.8: Disk Imaging and Analysis  
**Learning Objectives:**  
- Define disk imaging  
- Recognize its use in forensics  

**Key Topics:**  
- Exact copy of a storage device for investigation  
- Preserves evidence while original remains untouched  
- Analysis reveals malware, deleted files, hidden partitions  

---

## Completion Status  
- All Section 24 materials reviewed  
- [Flashcards created for IR process stages, forensic procedures, and RCA methods](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=24)          

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
