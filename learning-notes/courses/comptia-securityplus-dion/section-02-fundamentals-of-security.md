# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 2 – Fundamentals of Security  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 2 introduces the foundational principles of security. Learners study the interplay between threats, vulnerabilities, and risk, the CIA triad, non-repudiation, AAA, and the categories and types of security controls. The section also explains how to conduct a gap analysis and explores the concepts behind Zero Trust architectures.

---

## Module 2.1: Threats, Vulnerabilities, and Risk  
**Learning Objectives:**  
- Define and distinguish between threats, vulnerabilities, and risks  
- Explain the role of risk management  

**Key Topics:**  
- **Threats:** natural disasters, cyber-attacks, disclosure of information, data integrity breaches  
- **Vulnerabilities:** software flaws, misconfigurations, missing patches, weak physical security  
- **Risk:** intersection of threats and vulnerabilities  
	Threat + No Vulnerability = No Risk
	Vulnerability + No Threat = No Risk
- **Risk management:** reducing likelihood and impact through controls

**Notes:**
- Remember **end user risk** - they will try to bypass for convenience
- **Security posture** must be loosened or strengthened to balance end user risk
- **Information security** (data) vs **information systems security** (devices)


---

## Module 2.2: The CIA(NA) Triad(Pentagon)  
**Learning Objectives:**  
- Summarize confidentiality, integrity, and availability  
- Apply methods to preserve each principle  

**Key Topics:**  
- **Confidentiality:** encryption, access controls, data masking, physical security measures, training and awareness 
	- to protect personal privacy
	- to maintain a business advantage
	- to achieve regulatory compliance
- **Integrity:** hashing (#1 method), digital signatures, checksums, access controls, regular audits  
	- to ensure data accuracy
	- to maintain trust
	- to ensure system operability
- **Availability:** redundancy of servers (#1 method), data, networks, power sources
	- 2 nines: 99%... 3.5 days of downtime per year
	- 3 nines: 99.9%... 8,760 hours are available and can only be down for a maximum of 8.76 hours
	- 5 nines: 99.999%... system guarantees a downtime of no more than 5.26 minutes in a year
	- ensuring business continuity
	- maintianing customer trust
	- upholding an organization's reputation
	- redundancies: server, data, network, power
- **Non-repudiation:** digital signature (#1 method)
	- confirming the authenticity of digital transactions
	- ensuring integrity 
	- providing accountability 
- **Authentication**
	- something you know - password
	- something you have - badge, phone
	- something you are - inherence factor, biometric
	- something you do - action factor, handwriting samples
	- somewhere you are - location factor
	- 2FA (two-factor authentication) 2 of the above 5 factors
	- MFA (multi-factor authentication) 2 or more of the above 5 factors
	- purposes: prevent unauthorized access, protect user data and privacy, ensure resource validity

---

## Module 2.3: Non-repudiation and AAA  
**Learning Objectives:**  
- Define non-repudiation in communications (action/event cannot be denied by the parties involved)  
- Explain authentication, authorization, and accounting  

**Key Topics:**  
- **Non-repudiation:** ensures actions cannot be denied (e.g., digital signatures)  
- **Authentication:** verifying identity (passwords, biometrics, MFA)  
- **Authorization:** permissions granted *after* authentication
	- role-based, rule-based, attribute-based  
	- protect sensitive data, maintain system integrity in organizations, create more streamlined user experiences
 	- set of rules and policies that are used to dictate what actions users can perform once verified
	- serves as the gatekeeper to ensure that the right people have access for the right things
- **Accounting:** logs, audit trails, SIEM for tracking use of resources
	- Actions to monitor and log:
		- logging into the system
		- accessing files
		- modifying configuration settings
		- downloading or installing software
		- attempting unauthorized actions on systems and networks
	- Accounting system to contain:
		- audit trail: chronological record of all user activities, used to trace changes, unauthorized access, anomalies back to user/time
		- regulatory compliance: comprehensive record of users' activities
		- forensic analysis: logs to understand what happened, how it happened, and how to prevent in the future
		- resource optimization: optimize system performance and minimize costs by tracking utilization and allocation
		- user accountability: deters potential misuse and promotes adherence to the organizations' policies
	- Technologies
		- syslog servers: aggregate logs from various network devices and systems to detect patterns/anomalies
		- network analysis tools: capture and analyze network traffic to gain detailed insights
		- SIEMs: (Security Information and Event Management) real-time analysis of security alerts generated by various hardware/software infrastructures

---

## Module 2.4: Security Control Categories and Types  
**Learning Objectives:**  
- Identify security control categories  
- Recognize different control types  

**Key Topics:**  
- **Categories:**  
  - Technical (firewalls, encryption, IDS/IPS)
	- The technologies, hardware, and software mechanisms that are implemented to manage and reduce risks
	- IDS = Intrusion Detection Systems
  - Managerial (policies, risk assessments, governance)  
	- a.k.a. administrative controls
	- involve the strategic planning and governance side of security
	- also encompass security policies, training programs, and incident response strategies 
  - Operational (incident response, change management)  
	- procedures and measures that are designed to protect data on a day-to-day basis and are mainly governed by internal processes and human actions
	- backup procedures, account reviews, user training programs
  - Physical (locks, guards, surveillance) 
	- tangible, real-world measures taken to protect assets
	- shredding of sensitive documents, security guards, locking the doors 
- **Types of security controls:** 
	- *preventive*: proactive measures implemented to thwart potential security threats or breaches (i.e. firewalls)
	- *deterrent*: aim to discourage potential attackers by making the effort seem less appealing or more challenging (i.e. warning signs or banners)
	- *detective*: monitor and alert organizations to malicious activities as they occue or shortly thereafter (i.e. IDS [Intrusion Detection System])
	- *corrective*: mitigate any potential damage and restore the systems to their normal state (i.e. antivirus quarantine features)
	- *compensating*: alternative measures that are implemented when primary security controls are not feasible or effective (i.e. using a VPN on top of WPA2 for lack of WPA3)
	- *directive*: often rooted in policy or documentation and set the standards for behavior within an organization (i.e. AUP [Acceptable Use Policy] + most other policies) 
---

## Module 2.5: Gap Analysis  
**Learning Objectives:**  
- Explain how a gap analysis identifies weaknesses  
- Use analysis to compare current vs. desired state  

**Key Topics:**  
*Gap Analysis* is the process of evaluating the differences between an organization's current performance and its desired performance
**current state - desired state = difference between the two**
- Steps: define scope, gather data on current state, analyze the data to identify the gaps (compare to objectives), develop a plan to bridge the gap (remediation)  
- Variants: technical vs. business gap analysis  
	- technical gap analysis: evaluating an organization's current technical infrastructure and idnetifying any areas where it falls short of the technical capabilities required to fully utilize their security solutions
	- business gap analysis: evaluating an organization's current business processes and idnetifying any areas where they fall short of the capabilities required to fully utilize cloud-based solutions

---

## Module 2.6: Zero Trust Architecture  
**Learning Objectives:**  
- Understand Zero Trust principles  
- Differentiate between control plane and data plane functions  

**Key Topics:**  
*Zero Trust*: a best practice
- Principle: “Never trust, always verify” - threats can emerge from both inside and outside
- no user or system is trusted by default; they require continuous verification for access to organizational resources 
- **Control Plane:** the overarching framework and set of components responsible for defining, managing, and enforcing the policies related to user and system access within an organization
	- adaptive identity: use adaptive identities that rely on real-time validation that takes into account the user's behavior, device, location, and other factors like that
	- threat scope reduction: limit the user's access to only what they need for their work tasks because thos drastically reduces the network's potential attack surface
	- policy-driven access: developing, managin, and enforcing user access policies based on their roles and responsibilities
	- secured zones: isolated enviornments within a network that are designed to house sensitive data  
- **Data Plane:** ensures that the policies and procedures are properly executed
	- subject/system: the individual or entity attempting to gain acces
	- policy engine: cross-references the access request with its predefined policies
	- policy administrator: used to establish and manage the access policies
	- policy enforcement point: allow or restrict access, and it will effectively act as a gatekeeper to the senstiive areas of the systems or networks


---

## Completion Status  
- All Section 2 materials reviewed  
- Flashcards created for CIA triad, AAA, control categories/types, gap analysis, and Zero Trust  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
