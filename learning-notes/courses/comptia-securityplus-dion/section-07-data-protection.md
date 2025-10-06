# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 7 – Data Protection  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 7 focuses on the protection of data across its types, states, classifications, and lifecycles. Learners study concepts of ownership and sovereignty, technical methods for securing data, and the use of Data Loss Prevention (DLP) solutions. The section emphasizes regulatory compliance and the alignment of security practices with organizational policies.  

---

## Module 7.1: Data Protection Overview  
**Learning Objectives:**  
- Define data protection and its objectives  
- Explain the need to safeguard sensitive data throughout its lifecycle  

**Key Topics:**  
- Protecting confidentiality, integrity, and availability of information  
- Regulatory and compliance drivers  
- Data lifecycle: creation, storage, use, sharing, archiving, destruction 
- Data Protection: process of safeguarding important inrofmation from corruption, compromise, or loss


---

## Module 7.2: Data Classifications  
**Learning Objectives:**  
- Identify common data classifications  
- Apply classifications to organizational contexts  

**Key Topics:**  
- Public, restricted, confidential, private, critical  
- Classification informs handling requirements (storage, access, transmission)  
- Supports risk management and compliance :contentReference
- Data Classification: category based on the organization's value and the sensitivity of the information if it were to be disclosed
- Sensitive Data: any information that can result in a loss of security or a loss of advantage to a company if accessed by an unauthorized person
- *Overclassifying data leads to protecting all data at a high level*
- Classification schemes:
	- Commerical Business
		- Public: has no impact on the company if released and is often posted in an open-source environment
		- Sensitive: has minimal impact if released (organization's financial data)
		- Private: contains data that should only be used within the organization; is information that relates to an individual entity
		- Confidential: contains items such as trade secrets, intellectual property data, and source code that affect the business if disclosed
		- Critical: contains valuable information
	- Government
		- Unclassified: data that can be released to the public or under the Freedom of Information Act
		- Sensitive but Unclassified: data that would not hurt national security if released but could impact those whose data was being used
		- Confidential: data that could seriously affect the government if unauthorized disclosures happen; *serious effect*
		- Secret: data that could seriously damage national security if disclosed
		- Top Secret: data that would damage national security if disclosed
- the life cycle of data: collect, retain, dispose
	- the life cycle of the data should be defined in policies
	- follow the local, state, and national laws and regulations for data retention time requirements

---

## Module 7.3: Data Ownership  
**Learning Objectives:**  
- Explain the concept of data ownership and responsibilities  
- Recognize roles in data governance  

**Key Topics:**  
- **Owner:** determines classification and access requirements  
- **Custodian:** enforces policies and manages storage/security  
- **User:** responsible for compliant use  
- Ownership ensures accountability for compliance and protection
- Data Ownership: process of identifying the person responsible for the confidentiality, integrity, availability, and privacy of the information assets
- Enterprise roles:
	- Data Owner: senior executive role that has the responsibility for maintaining the confidentiality, integrity, and availability of the information asset
	- Data Controller: entity that holds responsibility for deciding the purposes and methods of data storage, collection, and usage, and for guaranteeing the legality of processes
	- Data Processor: group or individual hired by the data controller to help with tasks like collecting, storing, or analyzing data
	- Data Custodian: responsible for handling the management of the system on which the data assets are stored; i.e. system administrator
	- Data Steward: focused on the quality of the data and the associated metadata
	- Data Privacy Officer: responsible for the oversight of any kind of privacy-related data, like PII, SPI, or PHI
- The *data owner* should be a business entity responsible for creating this information, with each owner being assigned to their own department
- IT people should *not* be the data owners, but rather those who know more about the data based on the content of the company

---

## Module 7.4: Data Types  
**Learning Objectives:**  
- Recognize categories of data requiring protection  
- Differentiate regulated, proprietary, and personal data  

**Key Topics:**  
- Regulated data: PCI DSS (financial), HIPAA (health), GDPR (personal)  
- Proprietary data: trade secrets, intellectual property  
- Personal and sensitive personal data: PII, PHI  
- Critical data: mission-essential systems and processes

---

## Module 7.5: Data States  
**Learning Objectives:**  
- Explain the three states of data  
- Identify protections for each state  

**Key Topics:**  
- **At rest:** stored on drives or media → protect with encryption, access controls  
- **In transit:** moving across networks → protect with TLS, VPNs, IPSec  
- **In use:** actively processed → protect with memory protections, secure enclaves

---

## Module 7.6: Data Sovereignty  
**Learning Objectives:**  
- Define data sovereignty and its impact  
- Recognize risks of cross-border data storage  

**Key Topics:**  
- Data is subject to laws of the country where stored  
- Issues: compliance with GDPR, HIPAA, local regulations  
- Risks: conflicting jurisdictions, legal exposure  
- Mitigation: clear data storage policies, local compliance checks

---

## Module 7.7: Securing Data  
**Learning Objectives:**  
- Identify methods of protecting data confidentiality and integrity  
- Explain obfuscation and segmentation techniques  

**Key Topics:**  
- **Encryption:** symmetric/asymmetric, full-disk, file-level  
- **Hashing & digital signatures:** ensure integrity and authenticity  
- **Tokenization & masking:** limit exposure of sensitive values  
- **Segmentation:** isolating critical data sets

---

## Module 7.8: Data Loss Prevention (DLP)  
**Learning Objectives:**  
- Explain the function of DLP solutions  
- Recognize types of DLP deployments  

**Key Topics:**  
- DLP prevents unauthorized sharing or exfiltration of data  
- Types: endpoint DLP, network DLP, cloud DLP  
- Capabilities: content inspection, contextual analysis, enforcement of policies 

---

## Module 7.9: Configuring DLP  
**Learning Objectives:**  
- Describe key steps in deploying and tuning DLP  
- Explain challenges of configuration  

**Key Topics:**  
- Define policies and sensitive data types  
- Configure inspection rules and enforcement actions  
- Monitor alerts and refine thresholds  
- Challenges: false positives, business disruption

---

## Completion Status  
- All Section 7 materials reviewed  
- Flashcards created for data classifications, states, sovereignty, and DLP concepts  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
