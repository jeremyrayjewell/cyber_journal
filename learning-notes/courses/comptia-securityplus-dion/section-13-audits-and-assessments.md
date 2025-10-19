# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 13 – Audits and Assessments  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 13 covers the processes of audits and assessments, both internal and external, to ensure compliance and improve security posture. Learners also examine penetration testing, including reconnaissance and execution, and conclude with the importance of documenting and attesting findings.  

---

## Module 13.1: Audits and Assessments Overview  
**Learning Objectives:**  
- Define audits and assessments in cybersecurity  
- Recognize their goals and differences  

**Key Topics:**  
- **Audits:** formal evaluations of compliance with standards, policies, regulations  
- **Assessments:** broader evaluations of security posture and practices  
- Both provide visibility, accountability, and direction for improvement  
- **Audits:* systematic evaluations of an organizatins information systems, applications, and security controls
- internal vs external audits
- network security, data encryption methods, access control mechanisms
- policies, procedures, controls
- General Data Protection Regulation (GDPR)
- Health Insurance Portability and Accountability (HIPAA)
- Payment Card Idustry Data Security Standard (PCI DSS)
- **Assessments:** performing a detailed analysis of an organiation's security systems to identify vulnerabilities and risks
	- risk assessments, vulnerability assessments, threat assessments
- processes, controls, compliance
- third-party, independent auditor, assessor
- **penetration testing:** simulated cyber attack against a computer system, network, or web application
	0 known environment, partially known environment, unknown environmnet

---

## Module 13.2: Internal Audits and Assessments  
**Learning Objectives:**  
- Explain internal audits and assessments  
- Recognize their benefits  

**Key Topics:**  
- Conducted by internal teams or departments  
- Focused on compliance, internal controls, policy adherence  
- Benefits: early detection, cost-effective, tailored to organization  
- **Internal Audit** vs **Internal Assessment**
- **Internal Audit:** systematic evaluation of the effectivenes of internal controls, compliance, and integrity of information systems and processes
	- data protection, network security, access controls, incident response
		- 1. review access control policies and procedures for alignment with best practices and regulatory requirements
		- 2. examine access rights
		- 3. verfy access rights processes, including approvals and timely revocation
		- 4. test the effectiveness of access controls
		- 5. document findings to serve as basis for recommending access control policy and procedure improvements
	- **Compliance:** ensuring that information systems and security practices meet established standards, regulations, and laws
	- **Audit Committee:** group of people responsible for supervising the organization's audit and compliance functions
- *Internal Assessment:** an in-depth analysis to identify and assess potential risks and vulnerabilities in an organization's information systems
	- **Self-assesment:** internal review conducted by an organization to gauge its adherence to particular standards or regulations
	- a large prganization may have a dedicated internal assessment team that travels throughout the enterprises to evaluate network
		- 1. conducting threat modeling exercise where potential threats are identified
		- 2. assessing vulnerability by using automated scanning tools and manual testing techniques
		- 3. performing risk assessments to evaluate the potential impact of identified threats
		- 4. recommending mitigation strategies based on the results

---

## Module 13.3: Performing an Internal Assessment  
**Learning Objectives:**  
- Describe steps in conducting internal assessments  
- Identify outputs and follow-up  

**Key Topics:**  
- Planning, scoping, data collection, analysis, reporting  
- Use of interviews, document reviews, vulnerability scans  
- Results feed into remediation plans and continuous improvement  
- **Minnesota Counties Intergovernmental Trust (MCIT):** created a checklist to help members to reduce data and cyber security risks by identifying and addressing vulnerabilities
- **Cyber-security Self-assessment:** helps organizations identify and strengthen data security areas internally
	- organizations may use various checklists, but the format and purpose of self-assessments generally stay consistent
	- identifying and addressing cybersecurity and data risks prepares organizations for long-term risk management

---

## Module 13.4: External Audits and Assessments  
**Learning Objectives:**  
- Explain the role of external audits  
- Recognize compliance drivers  

**Key Topics:**  
- Conducted by third-party auditors or regulators  
- Required for regulatory compliance (PCI DSS, HIPAA, ISO standards)  
- Provide objectivity, certification, and external accountability  
- **External Audit:** systematic evaluation carried out by external entities to assess an organization's information systems and controls
	- data protection, network security, access controls, incident response
	- the aim of an external audit is to uncover deficiencies in policies and controls to ensure alignment with diverse regulatory standards
		- GDPR, HIPAA, PCI DSS
- **External Assessment:** detailed analysis conducted by independent entities to identify vulnerabilities and risks 
	- risk assessment, vulnerability assessment, threat assessment
	- **regulatory compliance:** objective that organizations aim to reach in adherence to applicable laws, policies, and regulations
		- compliance involves adhering to industry-specific requirements (e.e., HIPAA and PCI DSS) and broader regulations like GDPR
	- **examination:** comprehensive security infrastructure inspections that conducted externally
		- examinations review policies, procedures, and controls, and address weaknesses
		- industry-specific examinations can also arise based on sector regulations
	- **Independent Third-party Audit:** offers validation of security practices, fostering trust with customers, stakeholders, and regulatory authorities
		- GDPR and PCI DSS mandate regular third-party independent audits as part of compliance obligations for organizations

---

## Module 13.5: Performing an External Assessment  
**Learning Objectives:**  
- Identify the process of external evaluations  
- Recognize challenges and benefits  

**Key Topics:**  
- Steps: scope definition, evidence collection, analysis, reporting  
- Benefits: impartiality, credibility, compliance assurance  
- Challenges: cost, time, operational disruption  
- Governance, Risk, Compliance practices
- **External assessments** are seeking to get a quick overview of the orgnization's current risk posture through a truly independent, third-party assessor

---

## Module 13.6: Penetration Testing  
**Learning Objectives:**  
- Define penetration testing and its purpose  
- Recognize pen testing phases  

**Key Topics:**  
- Simulated attacks to test defenses  
- Goals: identify exploitable vulnerabilities, measure response capability  
- Phases: planning, reconnaissance, exploitation, reporting  
- **Penetration Testing (Pentesting):** simulated cyber attack that helps in the assessment of computer systems for exploitable vulnerabilities
	- **Physical Pentesting:** testing an organization's physical security through testing locks, access cards, security cameras, and other protective measures
		- a physical pentest aims to find weaknesses in an organization's physical security and suggest enhancements to bolster it
		- identify physical vulnerabilities, improve security awareness, prevent unauthorized access
	- **Offensive Pentest (Red Teaming):** proactive approach that involves use of attack techniques, akin to real cyber threats, that seek and exploit system vulnerabilities
		- offensive pentesting simulates real-world attacks so the organizations learn to recognize and defend against such threats
	- **Defensive Pentesting (Blue Teaming):** reactive approach that entails fortifying systems, idnetifying and addressing attacks, and enhancing incident response times
		- improve incident response time, strengthen systems, enhance detection capabilities
	- **Integrated Pentesting (Purple Teaming):** combination of aspects of both offensive and defensive testing into a single penetration test
		- integration pentesting promotes teamwork by facilitating security assessment and attack-response simulations

---

## Module 13.7: Reconnaissance in Penetration Testing  
**Learning Objectives:**  
- Explain reconnaissance techniques  
- Identify passive vs. active recon  

**Key Topics:**  
- Passive: OSINT, reviewing public data, social media, DNS lookups  
- Active: scanning, probing, enumeration  
- Provides intelligence for later exploitation  
- **Reconnaissance:** an initial phase where critical information about a target system is gathered to enhance an attack's effectiveness and success
	- reconnaissance is a crucial step in penetration testing
	- **Active Reconnaissance:** direct engagement with the target system, ofering more information but with a higher detection risk
	- **Passive Reconnaissance:** gathering information without direct engagement with the target system, offering lower detection risk but less data
	- reconnaissance necessity and extent depend on the test type and environment
	- **Known Environment:** detailed target infrastructure information from the organization is received prior to the test
		- focuses on known assets, evaluates vulnerabilitiies and weaknesses, aims to understand exploitability and potential damages, resembles an insider threat scenario
	- **Partially Known Environment:** involves limited information provided to testers, who may have partial knowledge of the system
		- partially known environment testing aims to identify vulnerabilities in both known and hidden assets
	- **Unkown Environment:** testers receive minimal to no information about the target system
		- unknown environment testing aims to mimic an external attacker with limited knowledge
- Reconnaissance is a critical first step in penetration testing

---

## Module 13.8: Performing a Basic Penetration Test  
**Learning Objectives:**  
- Explain steps in a basic penetration test  
- Recognize common tools and techniques  

**Key Topics:**  
- Exploiting vulnerabilities after recon and scanning  
- Use of tools like Metasploit, Nmap, Wireshark  
- Controlled execution with safeguards and defined rules of engagement  
- **Metaspoloit:** multi-purpose computer security and penetration testing framework that encompasses a wide array of powerful tools, enabling the execution of penetration tests

---

## Module 13.9: Attestation of Findings  
**Learning Objectives:**  
- Explain the need to document and attest to findings  
- Recognize accountability measures  

**Key Topics:**  
- Reports summarize scope, methodology, vulnerabilities, and recommendations  
- Attestation confirms accuracy, integrity, and accountability  
- Provides actionable guidance for remediation and compliance reporting 
- **Attestation:** process that involves the formal validation or confirmation provided by an entity that is used to assert the accuracy and authenticity of specific information
	- GLBA, HIPAA, Sarbanes-Oxley, PCI DSS
	- ensure providing a summary of the assessment findings along with evidence of its completion
	- letter of attestation is discussed to provide proof of a conducted penetration test
	- software attestation, hardware attestation, system attestation
- **software attestation:** involves validating the integrity of software by checking that it hasb't been tampered with or altered maliciously 
	- accuracy of financial records, effectiveness of risk management strategies, adherence to internal policies and procedures
- strengthening trust, enhancing transparency, ensuring accountability
- build confidence among stakeholders, promote transparency in business operations, ensure that the organiztion is held accountable for its actions

---

## Completion Status  
- All Section 13 materials reviewed  
- Flashcards created for audit types, pen test phases, and reporting requirements  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
