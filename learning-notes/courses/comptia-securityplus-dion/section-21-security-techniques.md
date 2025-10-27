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

---

## Module 21.6: Web and DNS Filtering  
**Learning Objectives:**  
- Explain filtering techniques  
- Recognize benefits  

**Key Topics:**  
- Web filtering: blocks malicious or inappropriate sites  
- DNS filtering: prevents resolution of known malicious domains  
- Helps prevent phishing, malware downloads, and C2 communication  

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

---

## Module 21.9: User Behavior Analytics (UBA)  
**Learning Objectives:**  
- Explain UBA concepts  
- Recognize its benefits  

**Key Topics:**  
- Uses machine learning to detect abnormal activity  
- Identifies insider threats, compromised accounts, and anomalies  
- Complements SIEM and EDR for holistic monitoring  

---

## Module 21.10: Selecting Secure Protocols  
**Learning Objectives:**  
- Recognize secure protocol choices  
- Explain their application  

**Key Topics:**  
- Prefer encrypted protocols (HTTPS, SFTP, SSH, TLS, IPSec)  
- Replace insecure ones (HTTP, FTP, Telnet)  
- Ensures confidentiality and integrity of communications  

---

## Completion Status  
- All Section 21 materials reviewed  
- [Flashcards created for wireless settings, NAC types, filtering methods, EDR/UBA, and secure protocols](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=21)    

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
