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

## Module 7.4: Data States  
**Learning Objectives:**  
- Explain the three states of data  
- Identify protections for each state  

**Key Topics:**  
- **At rest:** stored on drives or media → protect with encryption, access controls  
	- a prime target for threat actors
	- encryption methods:
		- Full Disk Encryption: encrypts the entire hard drive
		- Partition Encryption: encrypts specific partitions of a hard drive, leaving other partitions unencrypted
		- File Encryption: encrypts individual files
		- Volume Encryption: encrypts a set of selected files or directories
		- Database Encryption: encrypts data stored in a database
		- Record Encryption: encrypts specific fields within a database record
- **In transit/in motion:** moving across networks → protect with TLS, VPNs, IPSec  
	- Secure Socket Layer (SSL): cryptogrphic protocol to secure over a network
	- Transport Layer Security (TLS): cryptogrphic protocol to secure over a network
	- Virtual Priate Network (VPN): creates secure connetion over a less secure network (internet)
	- Internet Protocol Security (IPSec): Protocol suite used to secure IP communications by authenticating and encrpyting each IP packet in a data stream
- **In use:** actively processed → protect with memory protections, secure enclaves
	- Application level
	- Access controls
	- Secure enclaves
	- Intel software guards

---

## Module 7.5: Data Types  
**Learning Objectives:**  
- Recognize categories of data requiring protection  
- Differentiate regulated, proprietary, and personal data  

**Key Topics:**  
- Regulated data: PCI DSS (financial), HIPAA (health), GDPR (personal)  
- Proprietary data: trade secrets, intellectual property  
- Personal and sensitive personal data: PII, PHI  
- Critical data: mission-essential systems and processes
- Types:
	- Regulated Data: information controlled by laws, regulations, or industry standards
		- General Data Protection REgularion (GDPR): EU data protection law
		- Personal Identification Information (PII): any information that can be used to identify an individual
		- Protected Health Information (PHI): (protected by HIPAA) any information about health status, provision of healthcare, or payment for healthcare that can be linked to a specific individual
	- Trade secrets: type of confidential business information that provides a company with a competitive edge
	- Intellectual property (IP): creations of the mind, such as inventions, literary and artistic works, designs, and symbols
		- unauthorized use of IP can lead to legal action
	- Legal information: includes any data related to legal proceedings, contracts, or regulatory compliance
	- Financial information: includes data related to an organization's financial transactions, such as sales records, invoices, tax documents, and bank statements
		- Payment Card Industry Sata Security Standard (PCI DSS): set of security standards designed to ensure that all companies that accept, process, store, or transmit credit card information maintain a secure environment
	- Human-readable: information that can be understood by humans without the need for a machine or software
	- Non-human readable data: information that requires a machine or software to interpret

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
- Data Sovereignty: the concept that digital information is subject to the laws of the country in which it is located
- Geographical considerations: the geographical location of sata storage and processing can significantly impact businesses
- information is subject to the laws of the nation where it is collected or processed
- General Data Protection REgularion (GDPR): stringent rules for data protection and grants individuals strong rights over their personal data
- China and Russia have strict data sovereignty laws that require companies to store and process data within their national borders
- understanding:
	- know the physical locations of data centers
	- ensure that information is not illegally transferered

---

## Module 7.7: Securing Data  
**Learning Objectives:**  
- Identify methods of protecting data confidentiality and integrity  
- Explain obfuscation and segmentation techniques  

**Key Topics:**  
- **Geographic restrictions (Geofencing):** virtual boundaries to restrict data access based on geographic location
- **Encryption:** transforms readable data (plaintext) into unredable data (ciphertext) using an algorithm and an encryption key; symmetric/asymmetric, full-disk, file-level  
- **Hashing:** converts data into a fixed size of numerical or alphanumeric characters, known as a hash value; often used to store sensitive data, like passwords
- **Tokenization:** replaces sensitive data with non-sensitive substitutes, known as tokens
- **Masking:** replacing some or all of the data in a field with a placeholder; limit exposure of sensitive values  
- **Segmentation:** dividing a network into separate segments, each with its own security controls; isolating critical data sets
- **Obfuscation:** involves making data unclear or unintelligible, making it difficult for unauthorized users to understand
- **Permission restrictions:** defining who has access to specific data and what they can do with it; often involve access control lists or Role-based Access Control (RBAC)

---

## Module 7.8: Data Loss Prevention (DLP)  
**Learning Objectives:**  
- Explain the function of DLP solutions  
- Recognize types of DLP deployments  

**Key Topics:**  
- DLP prevents unauthorized sharing or exfiltration of data  
- Types: endpoint DLP, network DLP, cloud DLP  
- Capabilities: content inspection, contextual analysis, enforcement of policies 
- **Data Loss Prevention (DLP):** set up to monitor the data of a system while it's in use, in transit, or at rest in order to detect any attempts to steal the data
- software or hardware
- **Endpoint DLP System:** software that's installed on a workstation or a laptop, and it's going to monitor the data that's in use on that computer
- **Network SLP System:** piece of software or hardware that's a solution placed at the perimeter of the network to detect data in transit
- **Storage DLP:** software that is installed on a server in the data center and inspects the data while it's at rest on the server
- **Cloud-based CLP System:** usually offered as software-as-a-service, and it's part of the cloud service and storage needs

---

## Module 7.9: Configuring a DLP  
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
- [Flashcards created for data classifications, states, sovereignty, and DLP concepts](https://jeremyrayjewell.neocities.org/security-plus-dion#deck-6)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
