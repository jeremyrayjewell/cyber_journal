# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 20 – Hardening  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 20 covers hardening practices that strengthen systems, networks, and applications against attacks. Learners study configuration management, application restrictions, service reduction, patching, group policies, SELinux, encryption, and secure baselines. The focus is on eliminating unnecessary risk exposure while maintaining system functionality.  

---

## Module 20.1: Hardening Overview  
**Learning Objectives:**  
- Define system hardening  
- Recognize its importance in security  

**Key Topics:**  
- Hardening reduces attack surfaces through configuration and policy  
- Applies to OS, applications, networks, and devices  
- Supports compliance, reliability, and defense-in-depth  
- **Hardening:** process of enhancing the security of a system, application, or network
	- apply security patches, configure access controls, disable unnecessary services, adopt best practices
	- default configurations, restricting applications, unnecessary services, trusted operating systems, patch management, group policies, SELinux (Security-Enhanced Linux), data encryption levels
	- *Updates:* software modifications
	- *Patches:* specific software updates
	- data encryption levels: full-disk, partition, file, volume, database, record

---

## Module 20.2: Changing Default Configurations  
**Learning Objectives:**  
- Explain risks of default settings  
- Recognize common changes needed  

**Key Topics:**  
- Default passwords and settings are widely known  
- Must disable or modify defaults to prevent compromise  
- Includes renaming admin accounts, changing ports, adjusting default access  
- default passwords, unneeded ports and protocols, extra open ports
- default passwords: choose a long, strong, and unique password for maximum protection
- disable any unneeded ports and protocols on the system
	- **SMTP:** port 25
- check for any open ports on the devices
	- several devices have ports 22, 23, 80 and 443 open by default upon initial power-up
		- **SSH:* port 22, **Telnet:** port 23, **HTTP:** port 80, **HTTPS:** port 443

---

## Module 20.3: Restricting Applications  
**Learning Objectives:**  
- Define application restrictions  
- Recognize security benefits  

**Key Topics:**  
- Restrict which apps can run using allowlists  
- Prevent unauthorized software from executing  
- Supports least functionality principle  
- **Least Functionality:** a process of configuring a workstation or server with only essential applications and services for the user
	- restrict, uninstall
- **Secure Baseline Image:** a standardized workstation setup, including OS, essential applications, and strict policies in corporate networks
- **Allowlisting:** a security measure that permits only approved applications to run on an operating system
	- Allowlisting, in terms of access control, functions much like an Explicit Allow Statement, from Network+ studies
	- more secure but complex to manage
	- blocks everything except listed applications
- **Blocklisting:** entails preventing listed applications from running, allowing all others to execute
	- easier to manage but less secure
	- allwos everthing except listed applications

---

## Module 20.4: Unnecessary Services  
**Learning Objectives:**  
- Explain risks of unnecessary services  
- Recognize examples  

**Key Topics:**  
- Unneeded services increase attack surface  
- Disable unused protocols, daemons, or system features  
- Regular audits identify unnecessary processes  
- **Services:** background applications that operate within the OS, executing a range of tasks

---

## Module 20.5: Trusted Operating Systems  
**Learning Objectives:**  
- Define trusted operating systems  
- Recognize their role in secure environments  

**Key Topics:**  
- Designed with security controls built-in (e.g., security certifications, hardened kernels)  
- Support access control, auditing, secure policies  
- Used in military, government, and critical systems  
- **Trusted Operating System (TOS):** designed to provide a secure computing environment by enforcing stringent security policies that usually rely on mandatory access controls
	- **Integrtiy-178B:** POSIX-based operating system that is designed for embedded system use
	- **Evaluation Assurance Level (EAL) 6:** based on a set of predefined security standard and certification from the Common Criteria for Information Technology Security Evaluation
		- Common Criteria standards assess the security controls in an operating system for effectiveness
		- **Mandatory Access Control (MAC):** access permissions are determined by a policy defined by the system administrators and enforced by the operating system
	- **SELinux (Security-Enhanced Linux):** set of controls that are installed on top of another Linux distribution like CentOS or Red Hat Linux
	- **Trusted Solaris:** offers secure, multi-level operations with MAC, detailed system audits, and data/process compartmentalization
	- **Evaluation Assurance Level (EAL) 4:** the operating system was carefully designed, tested, and reviewed, offering good security assurance
- Trusted OS enhances security with microkernels by minimizing the trusted base and reducing attack surface and vulnerabilities
	- usability, performance, functional requirements


---

## Module 20.6: Updates and Patches  
**Learning Objectives:**  
- Explain role of updates and patches  
- Recognize patch management needs  

**Key Topics:**  
- Regular patching reduces vulnerabilities  
- Must test before deployment to avoid disruptions  
- Includes OS, applications, firmware  
- manual, automated
- **Hotfix:** a software patch that solves a security issue and should be applied immediately after being tested in a lab environment
- **Update:** provides a system with additional functionality, but it does not usually provide any patching of security related issues
- **Service Pack:** includes all the hotfixes and updates since the release of the operating system
	- assign a dedicated team to track vendor security patches
	- establish automated system-wide patching for OS and applications
	- include cloud resources in the patch management
	- categorize patches as urgent, important, or non-critical for prioritization
	- create a test environment to verify critical patches before production deployment
	- establish a process for evaluating, testing, and deploying firmware updates
	- develop a technical process for deploying approved urgent patches to productino
	- periodically assess non-critical patches for combined rollout

---

## Module 20.7: Patch Management  
**Learning Objectives:**  
- Define patch management processes  
- Recognize best practices  

**Key Topics:**  
- Centralized management via patch servers or tools  
- Includes inventorying, testing, deploying, and auditing patches  
- Critical to mitigate zero-day and known exploits  
- **Patch Management:** planning, testing, implementing, and auditing of software patches
	- **Planning:** creating policies, procedures, and systems to track and verify patch compatibility
		- a good patch management tool confirms patch deployment, installation, and functional verification on servers or clients
			- Microsoft Endpoint Configuration Manager
			- large organizations should use a central update server instead of Windows Update
	- **Patch Rings**
	- **Cisco UCS Manager:** centralized resource and device management, including firmware for server network interfaces and devices 

---

## Module 20.8: Group Policies  
**Learning Objectives:**  
- Explain role of group policies in hardening  
- Recognize common controls  

**Key Topics:**  
- Centralized enforcement of security configurations  
- Examples: password policies, screen locks, software restrictions  
- Supports consistency across environments  
- access the Group Policy Editor by opening the Run prompt and enter "gpedit"
- password requirements, account lockout policies, software restrictions, application restrictions
- Active Directory domain controllers have a more advanced Group Policy Editor
- **Security Template:** a group of policies that can be loaded through one procedure
- **Group Policies** are also used to create a secure baseline as part of the larger configuration management program
- **Baselining:** process of measuring changes in the network, hardware, or software environment

---

## Module 20.9: SELinux  
**Learning Objectives:**  
- Define SELinux (Security-Enhanced Linux)  
- Recognize its capabilities  

**Key Topics:**  
- Mandatory Access Control (MAC) framework for Linux  
- Restricts processes and users beyond discretionary access controls  
- Provides fine-grained security enforcement  
- **Mandatory Access Control (MAC):** system-enforced access control mechanism that's based on subject clearance and the object labels
- **Context-based Permissions:** permission schemes that are defined by various properties for a given file or process
- **SELinux**, **AppArmor**
- **Discretionary Access Control (DAC):** each object has a list of entities that are allowed to access it 
- **SELinux:** default context-based permission scheme that's included inside of CentOS and Red Hat Enterprise Linux
	- SELinux is used to enforce MAC on processes and resources and enables information to be classified and protected
	- **User:** defines what users can access an object
		- Unconfined_u (all users)
		- User_u (unprivileged user)
		- Sysadmin_u (system administrators)
		- Root (root user)
	- **Role:** defines what roles can access a given object
	- **Type:** groups objects together that have similar security requirements or characteristics
	- **Level:** used to describe the sensitivity level of a given file, directory, or process
		- **Disabled:** SELinux is essentially turned off, and so MAC is not going to be implemented
		- **Enforcing:** all the SELinux security policies are being enforced
		- **Permissive:** SELinux is enabled, but the security policies are not enforced
	- targeted policies, strict policies
	- violation occurs when an attempt to access an object or an action goes against an existing policy
	- *SELinux* is only as strong as the restricted profiles being created

---

## Module 20.10: Data Encryption Levels  
**Learning Objectives:**  
- Explain different encryption levels  
- Recognize their applications  

**Key Topics:**  
- Encryption at rest, in transit, and in use  
- Protects confidentiality and integrity of sensitive data  
- Must align with compliance and business needs  
- **Data Encryption:** process of converting data into a secret code to prevent unauthorized access
	- **Full-disk Encryption:** encrypts the entire hard drive to protect all of the data being stored on it
	- **Partition Encryption:** similar to full-disk encryption, but it is only applied to a specific partition on the storage device
		- **VeraCrypt:** users can selectively encrypt partitions, like sensitive documents, while leaving the OS partition unencrypted
	- **Volume Encryption:** used to encrypt a set space on the storage medium, creating an encrypred container that can house various files and folders
	- **File-level Encryption:** used to encrypt an individual file instead of an entire partition or an entire disk drive
		- **GNU Privacy Guard (GPG):** provides cryptographic privacy and authentication for data communication
	- **Database Encryption:** secures the entire database, extending to multiple storage devices or cloud storage, similar to full-disk encryption
		- **SQL Server Transparent Data Encryption (TDE):** auto-encrypts the entire database without needing application changes, as the system handles encryption and decryption
	- **Record-level Encryption:** used to encrypt individual records or rows within a database

---

## Module 20.11: Secure Baselines  
**Learning Objectives:**  
- Define secure baselines  
- Explain their role in hardening  

**Key Topics:**  
- Documented standard configurations for systems/devices  
- Serve as reference for compliance and audits  
- Baseline drift must be monitored and corrected  
- **Secure Baseline:** standard security configuration applied to guarantee minimum security for a system, network, or application
	- establish a secure baseline; monitor and validate created group policies and configurations for security
	- deploy secure baseline across all of the organization's digital assets
		- firewalls, user permissions, encrpytion protocols, up-to-date antivuris and antimalware
		- admins can employ GPOs for a domain-wide secure baseline, governing password policies, user rights, and audit settings
		- **AWS Config:** defines and deploys secure configurations across cloud resources
	- maintain the secure baseline on all assets

---

## Completion Status  
- All Section 20 materials reviewed  
- [Flashcards created for patching, group policies, SELinux, and baseline management](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=20)   

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
