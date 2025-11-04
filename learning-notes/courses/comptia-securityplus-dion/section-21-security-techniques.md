# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 21 – Security Techniques  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 21 covers practical security techniques applied across networks, wireless systems, applications, and user activity monitoring. Learners review infrastructure defenses such as NAC, filtering, and EDR, along with protocol selection and wireless security practices.  

---

## Module 21.1: Security Techniques Overview  
**Learning Objectives:**  
- Define security techniques in cybersecurity  
- Recognize categories of implementation  

**Key Topics:**  
- Techniques are applied to protect data, users, and infrastructure  
- Cover network, wireless, application, and endpoint security  
- Provide layered defenses against evolving threats 
- Wireless Infrastructure Security
- Wireless Security Settings
- Application Security
- Network Access Control (NAC)
- Web and DNS Filtering
- Email Security
- Endpoint Detection and Response
- User Behavior Analytics
- Selecting Secure Protocols 

---

## Module 21.2: Wireless Infrastructure Security  
**Learning Objectives:**  
- Explain securing wireless infrastructure  
- Recognize vulnerabilities and countermeasures  

**Key Topics:**  
- Secure placement of access points and antennas  
- Segmentation of guest vs. enterprise networks  
- Monitoring for rogue access points  
- Range, Coverage, Signal Strength
- Access point placement is a huge concern in terms of the security of the wireless network
- Place the wireless access points near the center of the facility to minimize the risk of unauthorized access
- always place the access point in a higher location
- **Extended Service Set (ESS) configuration:** involves multiple wireless access points working together to create a unified and extended coverage area for users in a large building or facility
	- consider interference between different wireless access points
- Co-channel, Adjacent Channel
- **Adjacent Channel Interference:** occurs when the channels selected for adjacent wireless access points do not have enough space between the channels
	- always select Channels 1, 6, and 11 when operating in the 2.4 GHz wireless frequency band
- **Site Survey:** process of planning and designing a wireless network to provide a solution
	- wireless coverage, data rates, network capacity, roaming capability, quality of service levels
- **Heat Map:** graphical representation of the wireless coverage, the signal strength, and frequency utilization data at different locations on a map

---

## Module 21.3: Wireless Security Settings  
**Learning Objectives:**  
- Recognize wireless security configuration best practices  
- Explain encryption and authentication methods  

**Key Topics:**  
- WPA3 recommended; WPA2 minimum standard  
- Disable outdated protocols (WEP, TKIP)  
- Use strong authentication (802.1X, RADIUS)  
- Enforce SSID policies and disable WPS  
- **WPA3, AAA, RADIUS, EAP**
- WEP, WPA, WPA2, WPA3
- Wireles encryption and cryptographic protocols protect wireless networks by securing data from interception
- **Wired Equivalent Privacy (WEP):** outdated 1999 wireless security standard meant to match wired LAN security for wireless networks
	- WEP uses a fixed encryption key for all devices on the same network to secure messages
	- 64-bit, 128-bit
	- **128-bit WEP:** includes 104 bits of key data and an additional 24 bits initialization vector
	- WEP is insecure and should be avoided because it's vulnerable to simple cryptographic attacks
	- **WEP:** insecure because of a weak 24-bit intitialization vector
- **Wi-Fi Protected Access (WPA):** introduced in 2003 as a temporary improvement over WEP while the more robust IEEE 802.11i standard was in development
	- WPA improved security with TKIP, which generates new 128-bit keys for each packet, eliminating WEP's key-reuse vulnerabilities
	- Due to TKIP vulnerabilities, WPA was susceptible to cryptographic attacks, underscoring the need for advanced wireless security
	- **WPA:** insecure because of the lack of sufficient data integrity checks in the TKIP implementation
- **Wi-Fi Protected Access 2 (WPA2):** improved data protection and network access control by addressing weaknesses in WPA version
	- WPA2 replaced WPA's TKIP with the AES protocol and adopted CCMP for stronger encryption
	- Counter Cipher Mode with Block Chaining Message Authentication Code Protocol (CCMP)
	- switching to WPA2 provides stronger encryption and introduces Message Integrity Code (MIC) for integrity checking
- **Wi-Fi Protected Access 3 (WPA3):** latest version using AES encryption and introducing new features like SAE, Enhanced Open, updated cryptographic protocols, and management protection frames
	- **Simultaneous Authentication of Equals (SAE):** enhances security by offering a key establishment protocol to guard against offline dictionary attacks
	- WPA3 provides stronger protection even with weak passwords
	- WPA3 simplifies security setup
- **Enhanced Open/Opportunistic Wireless Encryption (OWE):** major advancement in wireless security, especially for networks using open authentication
	- Enhanced Open improves user privacy and security by guarding against eavesdropping attacks in public Wi-Fi settings
- **Cryptographic Protocol:** uses a newer variant of AES known as the AES GCMP
- **Galois Counter Mode Protocol(GCMP):** supports 128-bit AES for personal networks and 192-bit AES for enterprise networks with WPA3
- **Management Protection Frames:** required to protect network from key recovery attacks
- eavesdropping, forging, tampering
- **Authentication, Authorization, and Accounting (AAA) Protocol:** plays a vital role in network security by centralizing user authentication to permit only authorized users to access network resources
- **Remote Authentication Dial-In User Service (RADIUS):** client/server protocol offering AAA services for network users
	- RADIUS is used for secure network access, confirming user identities via a central server and enforcing predefind access rules
	- RADIUS aids in monitoring user activity to ensure accountability and security policy enforcement
- **Terminal Access Controller Access-Control System Plus (TACACS+):** separates the functions of AAA to allow for a more granular control over processes
	- TACACS+ uses TCP and encrypts authentication for improved security over older AAA protocols
- **Authentication Protocols:** confirm user identity for network security and authorized access
	- EAP, PEAP, EAP-TTLS, EAP-FAST
	- **Extensible Authentication Protocol (EAP):** authentication framework that supports multiple authentication methods
	- **Protected Extensible Authentication Protocol (PEAP):** authentication protocol that secures EAP within an encrypted and authenticated TLS tunnel
		- certificate (server/client)
	- **Extensible Authentication Protocol-Tunneled Transport Layer Security (EAP-TTLS):** authentication protocol that extends TLS support across multiple platforms
		- certificate (server)
	- **Extensible Authentication Protocol-Flexible Authentication via Secure Tunneling (EAP-FAST):** developed by Cisco, it enables secure re-authentication while roaming within a network without full authentication each time
		- EAP-FAST was developed to replace LEAP due to security vulnerabilities in the latter
- Summary:
	- WPA3 offers strong protection even with less complex passwords
	- RADIUS network protocol for AAA management of users accessing network services
	- TACACS+ allows granular control over AAA, enhancing security through full authentication encryption
	- EAP: universal authentication framework used to support various authentication methods

---

## Module 21.4: Application Security  
**Learning Objectives:**  
- Define application security measures  
- Recognize common practices  

**Key Topics:**  
- Secure coding, input validation, and patch management  
- Runtime application self-protection (RASP)  
- Security testing: static/dynamic analysis, fuzzing  
- Protects against SQLi, XSS, and other software flaws 
- **Application Security:** critical aspect of software development that focuses on building applications that are secure by design
	- **Input Validation:** acts as a gatekeeper to ensure that applications only act on well-defines and uncontiminated data
		- the need to authenticate clean, and secure data inputs cannot be overstated
		- each of these types of data being input will represent a point of interaction as well as a potential vulnerability to the systems
		- input validation serves as a kind of quality control for data to ensure that every piece of information is valid, secure, and correctly formatted
			- **Validation Rules:** these rules delineate acceptable and unacceptable inputs
				- input validation is also an important security measure to ensure that data is validated early in the process
				- while input validation is critical to perform, it is important to remember that it is not a cure-all solution 
				- secure communication protocol, regular security auditing, implementing proper error handling
	- **Secure Cookies:** trnsmitted over secure HTTPS connections to prevent potential eavesdroppers from intercepting the cookie data
		- **Cookies:** small pieces of data sotred on the user's computer by the wed browser while browsing a website
		- always refrain from utiliing persistent cookies for session verification
		- to secure cookies from client-side access, use the HttpOnly attribute
	- **Static Code Analysis (SAST):** a method of debugging an application by reviewing and eaming its source code before the program is ever run
		- static analysis is usually performed using software analyzers
		- **Manual Code Review:** performing the code review using a human instead of a static software analysis tool
	- **Dynamic Code Analysis:** testing method that analyzes an application while it's running
		- **Fuzzing:** finds software flaws by bombarding it with random data to trigger crashes and security vulnerabilities
		- **Stress Testing:** type of software testing that evaluates the stability and reliability of a system under extreme conditions
	- **Code Signing:** technique used to confirm the identity of the software author and guarantee that the code has not been altered or corrupted since it was signed
		- this certificate has a public key that the receiving computer uses to check and confirm the signature is valid
		- the presence of a digital signature on a file or program does not guarantee its absolute security
		- the digital signature confirms that the file is in the same state that the developer intended it to be when they distributed it
	- **Sandboxing:** security mechanism that is used to isolate running programs by limiting the resources they can access and the changes they can make to a system
		- sandboxes allow for testing code under various environments, not just the current system configuration

---

## Module 21.5: Network Access Control (NAC)  
**Learning Objectives:**  
- Define NAC and its function  
- Recognize deployment methods  

**Key Topics:**  
- NAC validates devices before granting network access  
- Enforces posture checks (patch level, AV, compliance)  
- Types: pre-admission (before connection) and post-admission (after connection)  
- Integrates with identity and role-based controls  
- **Network Access Control (NAC):** scans devices for their security status before granting network access, safeguarding against both known and unknown devices
	- when a device attempts to connect to the network, it's places into a virtual holding area while it's being scanned
	- if a device clears the inspection, it gains access to the network's organizational resources
	- after meeting the requirements, the device is again granted full network access
	- NAC solutions can run either using *persistent* versus *non-persistent*
		- **Persistent Agent:** a software installed on a device requesting network access
		- **Non-Persistent Agent:** users connect to Wi-Fi, access a web portal, and click a link for login in these solutions
	- Network Access Control can be offered as a hardware or a software solution
	- common network control mechnisms: **IEEE Standard 802.1x**
	- with time-based factors, the organization will define access periods using a time-based schedule
	- location-based factors assess the endpoint's location using its IP geolocation, GPS, etc.
	- *role-based* factors reassess a device's authorization during its use
	- *rule-based* factors apply a series of rules through a detailed admission policy

---

## Module 21.6: Web and DNS Filtering  
**Learning Objectives:**  
- Explain filtering techniques  
- Recognize benefits  

**Key Topics:**  
- Web filtering: blocks malicious or inappropriate sites  
- DNS filtering: prevents resolution of known malicious domains  
- Helps prevent phishing, malware downloads, and C2 communication  
- **Web Filtering:** technique used to restrict or control the content a user can access on the internet
	- **Agent-based Web Filtering:** installing a small piece of software known as an agent on each device that will require web filtering
	- **Centralized Proxies:** server that acts as an intermediary between an organization's end users and the internet
		- if the request does not conform with the policies, then the request is simply blocked or denied
	- **URL Scanning:** used to analyze a website's URL to determine if it is safe or not to access
	- **Content Categorization:** websites are categorized based on content, like social media, adult content, or gambling, which are frequently restricted in workplaces
	- **Block Rules:** specific guidelines set by an organization to prevent access to certain websites or categories of websites
	- **Reputation-based Filtering:** blocking or allowing websites based on their reputation score
- **DNS Filtering:** technique used to block access to certain websites by preventing the translation of specific domain names to their corresponding IP addresses
	- DNS filtering is a powerful tool for preventing access to malicious websites and it is commonly used to enforce internet usage policies
	- web filtering and DNS filtering are two important tools for ensuring the safe and productive use of the internet

---

## Module 21.7: Email Security  
**Learning Objectives:**  
- Explain email security practices  
- Recognize filtering and authentication mechanisms  

**Key Topics:**  
- Spam and phishing filters to block malicious content  
- Authentication: SPF, DKIM, DMARC  
- Encryption for confidentiality (PGP, S/MIME)  
- Security awareness for social engineering  
- **DomainKeys Identified Mail (DKIM):** allows the receiver to check if the email was actually sent by the domain it claims to be sent from and if the content was tampered with during transit
	- email authentication, protection against email soofing, improved email deliverability, enhanced reputation score
- **Sender Policy Framework (SPF):** email authentication method designed to prevent forging sender addresses during email delivery
	- preventing email spoofing, improving email deliverability, enhanced domain's reputation
- **Domain-based Message Authentication, Reporting, & Conformance (DMARC):** an email-validation system designed to detect and prevent email spoofing
	- DMARC can work with either DKIM, SPF, or both
	- email compromise attacks, phishing emails, email scams
- **Email Gateway:** server or system that serves as the entry and exit point for emails
	- email routing, email security, policy enforcement, encryption and decryption
	- **On-Premise Email Gateway:** physical server that is located within an organiation's own data center or premises that provides an organization with full control over their email system 
	- **Cloud-Based Email Gateway:** email gateway that is hosted by third-party cloud service providers to provide greater scalability and ease of maintenance 
	- **Hybrid Email Gateway:** used to combine the benefits of both on-premise and cloud-based gateways into a single offering
- **Spam Filtering:** process of detecting unwanted and unsolicited emails and preventing them from reaching a user's email inbox
	- content analysis, Bayesian filtering, DNS-based sinkhole list, general email filtering rules 

---

## Module 21.8: Endpoint Detection and Response (EDR)  
**Learning Objectives:**  
- Define EDR and its role  
- Recognize EDR capabilities  

**Key Topics:**  
- Monitors and analyzes endpoint activity in real time  
- Detects and responds to malware, ransomware, and insider threats  
- Provides centralized logging and forensic data  
- Often cloud-integrated with advanced analytics  
- **Endpoint Detection and Response (EDR):** category of security tools that monitor endpoint and network events and record the information in a central database
	- EDR works by continuously monitoring and gathering data from endpoints
	- data collection, data conolidation, threat detection, alerts and threat response, threat investigation, remediation
	- system processes, changes to the registry, memory usage, patterns of network traffic
	- signaure-based detection, behavioral-based detection
- **File Integrity Monitoring (FIM):** used to validate the integrity of operating system and application software files using a verification method between the current file state and a known, good baseline
	- FIM uses software known as an agent to continuously monitor critical system files for changes
- **Extended Detection and Response (XDR):** security strategy that integrates multiple protection technologies into a single platform to improve detection accuracy and simplify the incident response process
	- email, endpoint, server, cloud workloads, network
	- network security, email security, endpoint security
	- organizations can consolidate serparate solutions into a single, consolidated platform
	- endpoint detection and response is really focused on endpoints

---

## Module 21.9: User Behavior Analytics (UBA)  
**Learning Objectives:**  
- Explain UBA concepts  
- Recognize its benefits  

**Key Topics:**  
- Uses machine learning to detect abnormal activity  
- Identifies insider threats, compromised accounts, and anomalies  
- Complements SIEM and EDR for holistic monitoring  
- **User Behavior Analytics (UBA):** deploys big data and machine learning to analyze user behaviors for detecting security threats
	- **User and Entity Behavior Analytics (UEBA):** built upon the foundation of UBA with monitoring of entities as an additional function
	- UBA aims to spot anomalies in established patterns, indicating potential threats
	- collect and analyze data from diverse sources
	- employ advanced analytics methods
	- create a baseline for normal user behavior
	- continuously monitor user activity to detect anomalies
	- UBA tools have benefits
		- early detection of threats
		- insider threat detection
		- improved incident response
	- UBA is an efficient security tool that identifies potential threats by detecting anomalous behavior


---

## Module 21.10: Selecting Secure Protocols  
**Learning Objectives:**  
- Recognize secure protocol choices  
- Explain their application  

**Key Topics:**  
- Prefer encrypted protocols (HTTPS, SFTP, SSH, TLS, IPSec)  
- Replace insecure ones (HTTP, FTP, Telnet)  
- Ensures confidentiality and integrity of communications  
- protocols, ports, transport methods
- **Protocol:** set of rules or procedures for transmitting data between electronic devices
	- FTP, SFTP
	- use an encrypted version of the same basic protocol
	- **Telnet:** application layer protocol that allows a user on one computer to log onto another computer that is part of the same network
	- **Secure Shell (SSH):** network protocol for securely connecting and communicating with remote devices and systems over an unsecured network
	- always select an encrpytion protocol to protect data during network transfers
		- HTTPS, SFTP, SSH, IMAPS, POP3S, SMPTPS, SNMPS
	- every protocol has both an unencrypted and encrypted version
- **Port:** logical construct that identifies specific processes or services in a given system
	- **Well-known Ports:** used by system processes or services and consist of ports ranging from port 0 to port 1023
	- **Registered Ports:** used by software applications and utilize a port number between 1024 and 49151
	- **Dynamic/Private Ports:** used for client-side conections that range from port number 49152 to port number 65535
	- ensure that port 443 is open while port 80 is closed or blocked
	- POP2, POP3S, IMAP, IMAPS
	- Post Office Protocol 3, Internet Message Access Protocol
	- only open the ports necessary for applications to function, and block all others
	- using default port numbers can be less secure
	- authentication, encryption, security updates
- **Transport Method:** refers to the way data is moved from one place to another, usually using either TCP or UDP to transmit the data
	- **Transmission Control Protocol (TCP):** connection-oriented protocol that ensures data is delivered wwithout any errors
	- **User Datagram Protocol (UDP):** connectionless protocol that doesn't guarantee data delivery
		- UDP is a great choice for streaming video and other near real-time communications

---

## Completion Status  
- All Section 21 materials reviewed  
- [Flashcards created for wireless settings, NAC types, filtering methods, EDR/UBA, and secure protocols](https://jeremyrayjewell-flashcards.netlify.app/security-plus-dion.html#deck=21)    

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
