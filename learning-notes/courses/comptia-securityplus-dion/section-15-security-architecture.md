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
- **Virtualization:** technology that allows for the emulation of servers
- **Containerization:** lightweight alternative to full machine virtualization
- **Type 1:** known as a bare metal or native hypervisor, it runs directly on the host hardware and functions similarly to an operating system
	- Microsoft's Hyper-V, Citrix's XenServer, VMware's ESXi, VMware's vSphere
- **Type 2:** operates within a standard operating system, such as Windows, Mac, or Linux
	- *Type 1* hypervisor is faster and more efficient than a *Type 2* hypervisor
- efficiency, speed, portability, scalability, isolation, consistency
- Docker, Kubernetes, Red Hat OpenShift
- virtual machines are segmented a separated by default
- **Virtual Machine Escape:** occurs when an attacker is able to break out of one of these normally isolated virtual machines
- **Privilege Elevation:** occurs when a user is able to gain the ability to run functions as a higher level user
- **Live Migration of Virtual Machines:** when a virtual machine needs to move from one physical host to another
- **Resource Reuse:** concept in computing where system resources like memory or processing power are reused
- update the operating system in the applications, ensure that each virtual machine has a good antivirus solution installed, good strong passwords and good policies
- remember that a hypervisor needs to be updated and secured
- limit the connections between VMs and the physical machines
- minimize and remove any unneeded features to support operations
- *Be aware of Virtualization Sprawl*

---

## Module 15.5: Serverless  
**Learning Objectives:**  
- Explain serverless computing models  
- Recognize risks and benefits  

**Key Topics:**  
- No infrastructure management, event-driven execution  
- Risks: vendor lock-in, limited visibility, function abuse  
- Best practices: monitoring, secure coding, IAM controls  
- **Serverless:** model where the responsibility of managing servers, databases, and some application logic is shifted away from developers
- serverless offers automatic scaling
- **Vendor Lock-in:** one of the most significant risks of serverless computing

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
- **Microservices:** a software architecture where large applications are broken down into smaller and independent services
	- unlike monolithic architecture, each service in microservice architecture is self-contained and able to run independently
	- microservices offer several advantages over traditional monolithic architectures
	- scalability, flexibility, resilience, faster deployment and updates
	- microservices is not without challenges
	- complexity, data management, network latency, security

---

## Module 15.7: Network Infrastructure  
**Learning Objectives:**  
- Recognize the role of network architecture  
- Identify security considerations  

**Key Topics:**  
- Core, distribution, and access layers  
- Security zones, segmentation, DMZs  
- Resilient design with redundancy and monitoring  
- **Physical Separation / Air Gapping:** isolation of a network by removing any direct or indirect connections from other networks
	- physical separation is one of the most secure method of security but it is still vulnerable to sophisticated attacks
- **Logical Separation:** creates boundaries within a network, restricting access to certain areas
	- logical separation should be properly condifugred to be more effective in network security

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
- **Software-Defined Networking (SDN):** enables efficient network configuration to improve performance and monitoring
- **Data Plane:** also called the forwarding plane that is responsible for handling packets and makes decisions based on protocols
- **Control Plane:** the brain of the network that decides where traffic is sent and is centralized in SDN
- **Application Plane:** the plane where all network applications interacting with the SDN controller reside

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
- **Infrastructure as Code (IaC):** a method in which IT infrastructures are defined in code files that can be versioned, tested, and audited
	- **YAML, JSON, HashiCorp Configuration Language (HCL)**
- **Snowflake System:** a configuration that lacks consistency that might introduce risks, so it has to eliminated
- **Idempotence:** the ability of an operation to produce the same results as many times as it is executed
- IaC offers significant benefits:
	- speed and efficiency, consistency and standardization, scalability, cost savings, auditability and compliance
	- learning curve, complexity, security risks

---

## Module 15.10: Centralized vs. Decentralized Architectures  
**Learning Objectives:**  
- Compare centralized and decentralized models  
- Recognize security considerations  

**Key Topics:**  
- Centralized: easier control, single points of failure  
- Decentralized: resilience, but harder to manage  
- Hybrid approaches balance risks  
- **Centralized:** all the computing functions are coordinated and managed from a single location or authority
	- efficiency and control, consistency, cost and effectiveness
	- there are risks involed in centralized syste, architectures
	- single point of failure, scalability issues, security risks
- **Decentralized:** computing functions are distributed across multiple systems or locations
	- resiliency, scalability, flexibility
	- decentralized architectures also come with risks
- security risks,management challenges, data inconsistency
- the choice between the two system architectures depends on the specific needs of the organization

---

## Module 15.11: Internet of Things (IoT)  
**Learning Objectives:**  
- Define IoT architectures  
- Recognize IoT-specific risks  

**Key Topics:**  
- Devices interconnected via networks  
- Risks: weak authentication, lack of updates, physical exposure  
- Defenses: segmentation, firmware updates, monitoring  
	- **Internet of Things (IoT):** refers to the network of physical items with embedded systems that enables connection and data exchange
	- **Hub:** the central point connecting all IoT devices and sends commands to them
	- **Smart Devices:** everyday objects enhanced with computing capabilities and Internet connectivity
	- **Wearbles:** subset of smart devices designed to be worn on the body
	- **Sensors:** detect changes in the environment and transform them into analyzable data
- weak defaults, poorly configured network services

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
- **Industrial Control Systems (ICS):** control systems used to monitor and control industrial processes ranging from simple systems to complex systems
	- **Distributed Control Systems (DCS), Programmable Logic Controllers (PLCs)**
- **Supervisory Control and Data Acquisition (SCADA):** a type of ICS used to monitor and control geographically dispersed industrial processes
	- electric power generation, transmission, and distribution systems
	- water treatment and distribution systems
	- oil and gas pipeline monitoring and control systems
- unauthorized access, malware attacks, lack of updates, physical threats
- strong access controls, regular updates and system patches, firewall and intrusion detection systems, regular security audits, employee training

---

## Module 15.13: Embedded Systems  
**Learning Objectives:**  
- Explain embedded systems and their challenges  
- Recognize examples and risks  

**Key Topics:**  
- Specialized devices with dedicated functions (medical, automotive, appliances)  
- Risks: proprietary code, long lifecycles, patching difficulties  
- Best practices: secure design, firmware validation, physical protections  
- **Embedded System:** specialized computing component designed to perform dedicated functions within a larger structure
- **Real-Time Operating System (RTOS):** ensures data processing in real-time and is crucial for time-sensitive applications
	- embedded systems also have vulnerabilities
	- hardware failure, software bugs, security vulnerabilities, outdated systems
	- there are four key strategies in securing embedded systems
- **Network Segmentation:** divides a network into multiple segments or subnets, limiting potential damage in case of a breach
- **Wrappers:** show only the entry and exit points of the data hen traveling between networks
- **Firmware Code Control:** this can be achieved through secure coding practices, code reviews, and automated testing
- **Inability to Patch:** strategies like over-the-air (OTA) updates, where patches are delivered and installed remotely, can be applied

---

## Completion Status  
- All Section 15 materials reviewed  
- [Flashcards created for cloud models, virtualization vs. containers, SDN, IaC, IoT, ICS, and embedded risks](https://jeremyrayjewell-flashcards.netlify.app/security-plus-dion.html#deck=15)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
