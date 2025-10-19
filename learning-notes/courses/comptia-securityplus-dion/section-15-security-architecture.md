# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 15 – Security Architecture  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 15 explores security architecture models and technologies across on-premise and cloud environments. Learners review virtualization, containerization, serverless computing, microservices, SDN, IaC, and architectures for IoT, ICS/SCADA, and embedded systems. Emphasis is on comparing different approaches, their risks, and their security implications.  

---

## Module 15.1: Security Architecture   
**Learning Objectives:**  
- Define security architecture and its role  
- Recognize key architectural considerations  

**Key Topics:**  
- Structures that align IT systems with security requirements  
- Balances confidentiality, integrity, availability, and performance  
- Guides design and evaluation of secure environments  
- **Security Architecture:** design, structure, and behavior of an organization's information security environment
- **On-Premise:** traditional method of setting up infrastructure and services locally, within an organization's own premises
- **Cloud Computing:** involves delivering computing services over the Internet
- **Serverless:** computing model where the cloud provider dynamically manages the allocation and provisioning of servers
- **Software-Defined Networking (SDN):** network management method that allows dynamic and efficient network configuration to improve performance and monitoring
- **Infrastructure as Code (IaC):** IT setup where developers use software to manage and provision the technology stack for an application
- **Internet of Things (IoT):** network of physical devices, vehicles, and appliances, with sensors, software, and network connectivity
- **Supervisory Control and Data Acquisition (SCADA):** used to control and monitor physical processes

---

## Module 15.2: On-Premise versus the Cloud  
**Learning Objectives:**  
- Compare on-premise and cloud deployments  
- Recognize trade-offs of each  

**Key Topics:**  
- On-premise: full control, higher cost, more maintenance  
- Cloud: scalability, cost efficiency, less direct control  
- Hybrid and multi-cloud approaches as compromises  
- **Availability vs Resilience**
- servers, storage, databases, networking, software analytics, intelligence
- responsibility matrix, third-party vendors, hybrid solutions
- **Responsibility Matrix:** outlines the division of responsibilities between the cloud service provider and the customer
	- operating system, middleware, runtime, data, application
- **Third-Party Vendors:** provide specialized services that enhance the functionality, security, and efficiency of cloud solutions
- **Hybrid Solutions:** combine on-premise inrastructure, private cloud services, and public cloud services
	- data security, compliance, interoperability, cost
	- sensitive data is protected, regulatory requirements are met, systems can communicate with each other, the solution is cost-effective
- **On-Premise Solutions:** computing infrastructure that's physically located on-site at business
	- **availability:** system's ability to be accessed when needed 
	- **resilience:** system's ability to recover from failure and continue to function 
	- **cost:** it's ssential to consider both the immediate and long-term costs of cloud adoption
	- **responsiveness:** speed at which the system can adapt to changes in demand
	- **scalability:** system's ability to handle increased workloads 
	- **ease of deployment:** cloud services are easier to deploy than on-premie solutions 
	- **risk transference:** when using the cloud services, some risks are transferred to the provider
	- **ease of recovery:** cloud services often offer easy data recovery and backup solutions 
	- **patch availability:** cloud service providers regularly release patches to fix vulnerabilities 
	- **inability to patch:** businesses might not be able to apply patches due to compatibility issues 
	- **power:** customers don't have to worry about power consumption 
	- **compute:** amount of computational resources that a customer can use

---

## Module 15.3: Cloud Security  
**Learning Objectives:**  
- Explain challenges of cloud security  
- Recognize best practices  

**Key Topics:**  
- Shared responsibility model  
- Risks: misconfigurations, data breaches, vendor lock-in  
- Defenses: encryption, strong IAM, monitoring, compliance alignment  
- **Shared Physical Server Vulnerabilities:** can lead to vulnerabilities if one user's data is compromised
- **Inadequate Virtual Environment Security:** can lead to unauthorized access, data breaches, and other security incidents
	- using secure VM templates, regularly updating and patching VMs, monitoring VMs for unusual activities
- **User Access Management:** can lead to unauthorized access to sensitive data and systems
	- enforcing strong password policies, using multi-factor authentication, limiting user permissions based on the principle of least privilege, monitoring user activities for any suspicious behavior
- **Lack of Up-to-date Security Measures:** can lead to leaving the system vulnerable to new threats
	- keeping software and systems patched, regularly reviewing and updating security policies, staying informed about the latest threats and security best practices
- **Single Points of Failure:** can lead to a complete system outage affecting all users
	- servers, data centers, cloud providers
- **Weak Authentication and Encryption Practices:** can lead to allowing unauthorized users to gain access to cloud systems
	- multi-factor authentication, strong encryption algorithms, secure key management practices
- **Unclear Policies:** lack of clear guidelines or procedures for various security aspects
- **Data Remnants:** residual data left behind after deletion or erasure processes
	- using secure deletion methods that overwrite data, managing backups securely, verifying that data has been completely removed after deletion

---

## Module 15.4: Virtualization and Containerization  
**Learning Objectives:**  
- Define virtualization and containerization  
- Recognize security implications  

**Key Topics:**  
- Virtualization: multiple VMs on one host, hypervisor security critical  
- Containerization: lightweight, shares host OS, isolation risks  
- Security: patching, segmentation, image scanning, runtime monitoring  

---

## Module 15.5: Serverless  
**Learning Objectives:**  
- Explain serverless computing models  
- Recognize risks and benefits  

**Key Topics:**  
- No infrastructure management, event-driven execution  
- Risks: vendor lock-in, limited visibility, function abuse  
- Best practices: monitoring, secure coding, IAM controls  

---

## Module 15.6: Microservices  
**Learning Objectives:**  
- Define microservices architecture  
- Recognize benefits and challenges  

**Key Topics:**  
- Applications broken into small, independent services  
- Benefits: scalability, flexibility, resilience  
- Risks: increased attack surface, API security concerns  
- Requires monitoring, authentication, and segmentation  

---

## Module 15.7: Network Infrastructure  
**Learning Objectives:**  
- Recognize the role of network architecture  
- Identify security considerations  

**Key Topics:**  
- Core, distribution, and access layers  
- Security zones, segmentation, DMZs  
- Resilient design with redundancy and monitoring  

---

## Module 15.8: Software-Defined Networking (SDN)  
**Learning Objectives:**  
- Explain SDN principles  
- Recognize benefits and risks  

**Key Topics:**  
- Separates control plane from data plane  
- Benefits: agility, centralized management  
- Risks: centralized attack targets, misconfiguration impact  
- Requires controller security and segmentation  

---

## Module 15.9: Infrastructure as Code (IaC)  
**Learning Objectives:**  
- Define IaC and its benefits  
- Recognize risks of insecure configurations  

**Key Topics:**  
- Managing infrastructure through code and automation  
- Improves consistency, reduces manual errors  
- Risks: compromised scripts, misconfigurations at scale  
- Defenses: version control, code reviews, automated testing  

---

## Module 15.10: Centralized vs. Decentralized Architectures  
**Learning Objectives:**  
- Compare centralized and decentralized models  
- Recognize security considerations  

**Key Topics:**  
- Centralized: easier control, single points of failure  
- Decentralized: resilience, but harder to manage  
- Hybrid approaches balance risks  

---

## Module 15.11: Internet of Things (IoT)  
**Learning Objectives:**  
- Define IoT architectures  
- Recognize IoT-specific risks  

**Key Topics:**  
- Devices interconnected via networks  
- Risks: weak authentication, lack of updates, physical exposure  
- Defenses: segmentation, firmware updates, monitoring  

---

## Module 15.12: ICS and SCADA  
**Learning Objectives:**  
- Define ICS and SCADA systems  
- Recognize their critical security challenges  

**Key Topics:**  
- Used in industrial and critical infrastructure control  
- Historically designed for availability, not security  
- Risks: legacy protocols, lack of patching, remote access abuse  
- Mitigation: segmentation, compensating controls, monitoring  

---

## Module 15.13: Embedded Systems  
**Learning Objectives:**  
- Explain embedded systems and their challenges  
- Recognize examples and risks  

**Key Topics:**  
- Specialized devices with dedicated functions (medical, automotive, appliances)  
- Risks: proprietary code, long lifecycles, patching difficulties  
- Best practices: secure design, firmware validation, physical protections  

---

## Completion Status  
- All Section 15 materials reviewed  
- [Flashcards created for cloud models, virtualization vs. containers, SDN, IaC, IoT, ICS, and embedded risks](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=15)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
