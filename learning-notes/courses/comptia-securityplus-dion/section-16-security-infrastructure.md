# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 16 – Security Infrastructure  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 16 covers security infrastructure technologies, protocols, and controls used to protect modern networks. Learners examine firewalls, IDS/IPS, network appliances, port security, secure communications, SD-WAN/SASE, and considerations for selecting infrastructure controls.  

---

## Module 16.1: Security Infrastructure Overview  
**Learning Objectives:**  
- Define security infrastructure and its purpose  
- Recognize key categories of infrastructure controls  

**Key Topics:**  
- Combines hardware, software, and processes for defense-in-depth  
- Controls include preventive, detective, corrective, and compensating measures  
- Infrastructure must support confidentiality, integrity, and availability  
- **Security Infrastructure:** combination of hardware, software, policies, and practices that organizations use to protect information
	- web application firewalls, unified threat management systems, next generation firewalls
	- rules and access control lists, ports and protocols, screened subnets
- **Intrusion Detection Systems (IDS), Intrusion Prevention Systems (IPS)**
- **Network Appliance:** specialized hardware ir siftware device designed to perform specific networking functions or services
- **Port Security:** network security feature that restricts and controls access to a network by allowing only authorized devices to connect
- VPNs, IPSec Tunnels, TLS
- **Software-Defined Wide Area Networking (SD-WAN):** technology that utilizes software-defined networking principles to manage and optimize wide area network (WAN) connections
	- broadband, cellular, MPLS
- **SASE:** network security and connectivity framework that integrates network security and wide area networking into a cloud-based service
- device placement, security zones and screened subnets, attack surfaces, connectivity concerns, device attributes, failure mode options
- how to choose the right controls for the network

---

## Module 16.2: Ports and Protocols  
**Learning Objectives:**  
- Explain common ports and protocols  
- Recognize their security implications  

**Key Topics:**  
- Well-known ports: 20/21 (FTP), 22 (SSH), 25 (SMTP), 80 (HTTP), 443 (HTTPS)  
- Secure alternatives: SFTP, SMTPS, HTTPS  
- Protocol misuse can expose networks to threats  
- **Port:** logical communication endpoint that exists on a computer or server
- **Inbound Port:** logical communication opening on a server that is listening for a connection from a client
- **Outbound Port:** lofical communication opening created on a client in order to call out to a server that is listening for a connection
- Ports can be any number between 0 and 6,535
- **Well-known Ports:** ports 0 to 1023 are considered well-known and are assigned by the Internet Assigned Numbers Authority (IANA)
	- *HTTPS:* port 332, *Telnet:* port 23
- **Registered Ports:** ports 1024 to 49,151 are considered registered and are usually assigned to proprietary protocols
	- *SQL:* port 1433, *RDP:* port 3389
- **Dynamic and Private Ports:** port 49,152 to 65,535 can be used by any application without being registered with IANA
	- commonly used in gaming, instant messaging, and chat for chat connections
- **Protocol:** rules governing device communication and data exchange
	- port number, protocol used, TCP/UDP support, basic description

- **Port 21 (TCP):** File Transfer Protocol (FTP)
	- used to transfer files from host to host
- **Port 22 (TCP):** SSH, SCP,and SFTP
	- provides secure remote terminal access and file transfer capabilities
	- provides secure copy functions
	- provides secure file transfers
- **Port 23 (TCP):** Telnet
	- provides insecure remote control of another machine using a text-based environment
- **Port 25 (TCP):** Simple Mail Trnasfer Protocol (SMTP)
	- provides the ability to send emails over the network
- **Port 53 (TCP and UDP):** Domain Name System (DNS)
	- translates domain names into IP addresses
- **Port 69 (UDP):** Trivial File Transer Protocol (TFTP)
	- used as a lightweight file transfer method for sending configuration files or network booting of an operating system
- **Port 80 (TCP):** Hypertext Transfer Protocol (HTTP)
	- used for insecure web browsing
- **Port 88 (UDP):** Kerberos
	- network authentication protocol
- **Port 110 (TCP):** Post Office Protocol Version Three (POP3)
	- responsible for retrieving email from a server
- **Port 119 (TCP):** Network News Transfer Protocol (NNTP)
	- used for accessing newsgroups
- **Port 135 (TCP and UDP):** Remote Procedure Call (RPC)
	- facilitates sommunication between different system processes
- **Ports 137, 138, and 139 (TCP and UDP):** NetBIOS
	- networking protocol suite
- **Port 143 (TCP):** Internet Message Access Protocol (IMAP)
	- allows access to email messages on a server
- **Port 161 (UDP):** Simple Network Management Protocol (SNMP)
	- manages network devices
- **Port 162 (UDP):** SNMP Trap
	- responsible for sending SNMP trap messages
- **Port 389 (TCP):** Lightweight Directory Access Protocol (LDAP)
	- facilitates directory services
- **Port 443 (TCP):** HTTP Secure (HTTPS)
	- provides secure web communication
- **Port 445 (TCP):** Server Message Block (SMB)
	- used for file and printer sharing over a network
- **Port 465 and 587 (TCP):** SMTP Secure (SMTPS)
	- provides secure SMTP sommunication
- **Port 514 (UDP):** Syslog
	- used for sending log messages
- **Port 636 (TCP):** LDAP Secure (LDAPS)
	- LDAP communication over SSL/TLS
- **Port 993 (TCP):** Internet Message Access Protocol over SSL/TLS (IMAPS)
	- used for secure email retrieval
- **Port 995 (TCP):** Post Office Protocol version 3 over SSL/TLS (POP3S)
	- used for secure email retrieval
- **Port 1433 (TCP):** Micosoft SQL
	- used to facilitate sommunication with Microsoft SQL Server
- **Ports 1645 and 1646 (TCP):** RADIUS TCP
	- used for remote authentication, authorization, and accounting
- **Ports 1812 and 1813 (UDP):** RADIUS TCP
	- used for authentication and accounting as defined by the Internet Engineering Task Force (IETF)
- **Ports 3389 (TCP):** Remote Desktop Protocol (RDP
	- enables remote desktop access
- **Port 6514 (TCP):** Syslog TLS
	- used in a secure syslog that uses SSL/TLS to encrypt the IP packets using a certificate before sending them across the IP network to the syslog collector

---

## Module 16.3: Firewalls  
**Learning Objectives:**  
- Define firewalls and their role  
- Recognize firewall types  

**Key Topics:**  
- Packet-filtering, stateful inspection, next-generation firewalls (NGFWs)  
- Block/allow traffic based on rules  
- Essential for network segmentation and perimeter defense  
- **Firewall:** safeguards networks by monitoring and controlling traffic based on predefined security rules
	- firewalls can be hardware appliances or specialized software installed on a device to control network traffic
- **Screened Subnet (Dual-homed Host):** acts as a security barrier between external untrusted networks and internal trusted networks, using a protected host with security measures like a packet-filtering firewall
	- install a firewall in a network to set up a screened subnet
- a firewall with in-depth inspection may slow down the device due to the time taken for each packet to pass through all the rules
- **Packet Filtering Firewall:** checks packet headers for traffic allowance based on IP addresses and port numbers
	- packet filtering firewalls cannot prevent certain attacks due to limited inspection capabilities in the packet header
- **Stateful Firewall:** monitors all inbound and outbound network connections and requests
- **Proxy Firewall:** acts as an intermediate between internal and external connections, making connections on behalf of other endpoints
- **Circuit Level:** like a SOCKS firewall, operates at the Layer 5 of the OSI model
- **Application Level:** conducts various proxy functions for each type of application at the Layer 7 of the OSI model
- **Kernel Proxy Firewall (Fifth Generation Firewall):** has minimal impact on network performance while thoroughly inspecting packets across all layers
- **Next-Generation Firewall (NGFW):** aims to address the limitations of traditional firewalls by being more aware of applications and their behaviors
	- conducts deep packet inspection for traffic
	- operates fast with minimal network performance impact
	- offers full-stack traffic visibility
	- integrates with various security products
	- organizations become reliant on a single vendor due to firewall configurations tailored to their product line
- **Unified Threat Management Firewall (UTM):** provides the ability to conduct multiple security functions in a single appliance
	- network firewalls, network intrusion prevention systems, gateway antivirus and antispam, virtual private network concentration, content filtering, load balancing, data loss prevention
	- UTM devices are a single point of failure
	- lower upfront costs, maintenance, and power consumption
	- simplified installation and configuration
	- UTM lacks the depth of specialized tools and occasionally exhibits less efficient performance
- **UTM vs NGFW:** UTM = separate individual engines; NGFW = single engine
- **Web Application Firewall (WAF):** focuses on the inspection of the HTTP traffic
	- WAF can function as standalone appliances or as software integrated into web servers
	- *Inline configuration:* device sits between the network firewall and the web servers
	- *Out-of-band confiuguration:* device receives a mirrored copy of web server traffic
- **Layer 4 firewalls, Layer 7 firewalls, NGFW, UTM, WAF**
	- **Layer 4 firewall:** filters based on port numbers and protocols, without inspecting packet content
	- **Layer 7 firewall:** inspects and controls traffic based on data content and application characteristics
	- **Next-Generation Firewall (NGFW):** merges standard firewall functions with advanced threat detection and application awareness
	- **Unified Threat Management Firewall (UTM):** combines security platform that integrates firewall, antivirus, intrusion detection, and content filtering
	- **Web Application Firewall (WAF):** inspects HTTP/HTTPS traffic and applies rule sets to prevent common web-based attacks 

---

## Module 16.4: Configuring Firewalls  
**Learning Objectives:**  
- Explain firewall configuration principles  
- Recognize best practices  

**Key Topics:**  
- Principle of least privilege for rule creation  
- Allowlisting vs. blocklisting approaches  
- Logging, monitoring, and regular review of firewall rules  
- **Access Control List (ACL):** a rule set that is places on firewalls, routers, and other network infrastructure devices that permit or allow traffic through a particular interface
	- web-based interface, text-based command-line interface
	- include a deny all rule at the end of the ACL
	- type, source, destination, action
	- hardware-baed firewall, software-based firewall

---

## Module 16.5: IDS and IPS  
**Learning Objectives:**  
- Compare Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS)  
- Recognize deployment considerations  

**Key Topics:**  
- **IDS:** monitors and alerts on suspicious traffic (passive)  
- **IPS:** actively blocks malicious traffic (inline)  
- Both rely on signatures, heuristics, and anomaly detection 
- *network-based, host-based, wireless*
- **IDS:** logs and alerts
- **IPS:** logs, alerts, takes action
- **Network Intrusion Detection Systems (NIDS):** responsible for detecting unauthorized network access or attacks
	- **Network IDS (NIDS):** monitors the traffic coming in and out of a network
	- **Host-Based IDS (HIDS):** looks at suspicious network traffic going to or from a single server or endpoint
	- **Wireless IDS (WIDS):** detects attempts to cause a denial of service on a wireless network
- **Signature-based IDS:** analyzes traffic based on defined signatures and can only recognize attacks based on previously identified attacks in its database
- **Pattern-matching:** specific pattern of steps; NIDS, WIDS
- **Stateful-matching:** known system baseline; HIDS
- **Anomaly-based/Behavioral-based IDS:** analyzes traffic and compares it to a normal baseline of traffic to determine whether a threat is occuring
	- statistical, protocol, traffic, rule/heuristic, application-based
- **Intrusion Prevention Systems (IPS):** scans traffic to look for malicious activity and takes action to stop it

---

## Module 16.6: Network Appliances  
**Learning Objectives:**  
- Identify specialized network appliances  
- Explain their role in security  

**Key Topics:**  
- Load balancers, proxies, VPN concentrators, DLP appliances, UTMs  
- Provide additional layers of control and visibility  
- Require configuration, updates, and monitoring  
- **Network Appliance:** dedicated hardware device with pre-installed software that is designed to provide specific networking services
	- load balancers, proxy servers, sensors, jump servers
- **Load Balancer:** crucial component in any high-availability network or system that is designed to distribute network or application traffic across multiple servers
	- maintenance window, system failure
	- this dynamic and transparent redirection ensures that services remain uninterrupted
	- SSL termination, HTTP compression, content caching
	- high-traffic wesites, criticial application systems, extensive digital platforms
- **Proxy Server:** intermediary between a client and a server to provide various functions like content caching, request filtering, and login management
	- obscurity is crucial to shield the server from direct attacks
	- proxy servers facilitate the smooth operation of a high-availability network
	- implementing user authentication protocols, providing secure tunnels, routing traffic
	- aiding in performance monitoring, detecting performance anomalies. triggering alerts
- **Sensors**
- *Intrusion Detection Systems (IDS), Intrusion Prevention Systems (IPS)*
- **Jump Server/Box:) dedicated gateway used by system administrators to securely access devicces located in different security sones within the network
	- jump boxes restrict direct access to protected devices or servers
	- a centralized point of access simplifies activity logging
	- jump servers streamline system management and maintenance
	- routine checks, troubleshooting taks
	- jump servers are crucial for ensuring uninterrupted and secure operations

---

## Module 16.7: Port Security  
**Learning Objectives:**  
- Define port security measures  
- Recognize techniques to secure switch ports  

**Key Topics:**  
- Disable unused ports, MAC filtering, port-based authentication (802.1X)  
- Protects against unauthorized devices and rogue access  
- Supports defense-in-depth at access layer  
- **Port Security:** common security feature found on network switches that allows administrators to restrict which devices can connect to a specific port based on the network interface card's MAC address
	- switches use intelligence to prevent collisions on networks
	- switches are more efficient and secure than hubs
- **Contant Adressable Memory (CAM) Table:** used to store information about the MAC addresses that are available on any given port of the switch
	- port security links MAC addresses to specific network interfaces for enhanced network security
- **Persistent (Sticky) MAC Learning:** feature in network port security where the switch automatically learns and associates MAC addresses with specific interfaces
	- **802.1x Authentication:** standardized framework that is used for port-based authentication for both wired and wireless networks
		- **RADIUS:** cross-platform, **TACACS+:** Cisco-proprietary protocol
		- supplicant, authenticator, authentication service 
		- 802.1x is a top-notch defense against unauthorized access on the network
	- **Extensible Authentication Protocol:** 
		- **EAP-MD5:** variant that utilizes simple passwords and the challenge handshake authentication process to provide remote access authentication
		- **EAP-TLS:** form of EAP that uses public key infrastructure with a digital certificate being installed on both the client and the server as the method of authentication
		- **EAP-TTLS:** variant that requires a digital certificate on the server, but not on the client
		- **EAP-FAST:** variant that uses a protected access credential, instead of a certificate, to establish mutual authentication between devices
		- **PEAP:** variant that supports mutual authentication by using server certificates and the Microsoft Active Directory databases for it to authenticate a password from the client
		- **LEAP:** variant of EAP that only works on Cisco-based devices

---

## Module 16.8: Securing Network Communications  
**Learning Objectives:**  
- Explain methods of securing communications  
- Recognize encryption and tunneling protocols  

**Key Topics:**  
- VPNs with IPSec or SSL/TLS  
- Secure protocols: HTTPS, SSH, SFTP  
- Segmentation and tunneling for confidentiality and integrity  
- **Virtual Private Network (VPN):** extends a private network over a public one, enabling users to securely send and receive data
	- **Site-to-site VPN:** establishes secure tunnels over the public Internet for interconnecting remote sites
		- site-to-site VPN secures traffic, but may slow down users due to extra data transfer
	- **Client-to-site VPN:** connects individual devices directly to the organization's headquarters, enabling remote users to access the network
		- **Full Tunnel:** maximizes security by encrypting all traffic to the headquarters while integrating clients with the network
		- **Split Tunnel:** divides traffic and network requests and then routes them to the appropriate network
		- a client-to-site VPN with split tunnel decides which traffic goes through the VPN, encrypting data for headquarters' network access
		- split tunnel combines encrpyted VPN path to headquarters with a direct, unencrypted Internet path for everything else
		- **Full Tunnel** offers more security, **Split Tunnel** offers better performance
	- **Clientless VPN:** secures remote access through browser-based VPN tunnels without needing client software or hardware configuration
- **Transport Layer Security (TLS):** a protocol that provides cryptographic security for secure connections and is used for secure web browsing and data transfer
- **Transmission Control Protocol (TCP):** used by TLS to establish secure connections between a client and a server, but it may slow down the connection
- **Datagram Transport Layer Security (DTLS): a UDP-based version of TLS protocol that offers the same security level as TLS while maintaining faster operations
	- DTLS ensures end-user security and protects against eavesdropping in clientless VPN connections
- **Internet Protocol SEcurity (IPSec):** a protocol suite for secure communication through authentication and data encryption in IP networks
	- confidentiality, integrity, authentication, anti-replay
- **Steps in establishing and using a secure VPN tunnel:**
	- *Request to start Internet Key Exchange (IKE):* PC1 initiates traffic to PC2, triggering IPSec tunnel creation by RTR1
	- *IKE Phase 1:* RTR1 and RTR2 negotiate security associations for the IPSec IKE Phase 1 (ISAKMP) tunnel
	- *IKE Phase 2:* IKE Phase 2 establishes a tunnel within the tunnel
	- *Data transfer:* data transfer between PC1 and PC2 takes place securely
	- *Tunnel termination:*	tunnel termination, including the deletion of IPSec security associations
- **Transport Mode:** employs the original IP header, ideal for client-to-site VPNs, and is advantageous when dealing with MTU contraints
	- **Maximum Transission Unit (MTU):** is set only at 1500 bytes and may cause fragementation and VPN problems
- **Tunneling Mode:** employed for site-to-site VPNs and adds an extra header that can increase packet size and exceed the MTU
	- at the destination site, the VPN concentrator removes the outer header, decrypts the content, and routes it internally
	- in tunneling mode, packets are encapsulated within new ones, potentially exceeding the 1500-byte limit of MTU
	- site-to-site VPNs may require support for jumbo frames above an MTU of 1500 bytes
	- lower the inner router's MTU to ~1400 bytes if jumbo frames cannot be utilized
	- adjusting the MTU to 9000 bytes is feasible in local area networks but not recommended for Internet due to potential issues
- **Authentication Header (AH):** offers connectionless data integrity and data origin authentication for IP datagrams using cryptographic hash and indentification information
- **Encapsulating Security Payload (ESP):** employed for providing authentication, integrity, replay protection, and data confidentiality by enrypting the packet's payload
	- in transport mode, use the authentication header for TCP header integrity, then add ESP to encrypt header and payload
	- in tunneling mode, employ both the authentication header and the encapsulated security payload
---

## Module 16.9: SD-WAN and SASE  
**Learning Objectives:**  
- Define SD-WAN and Secure Access Service Edge (SASE)  
- Recognize benefits for distributed organizations  

**Key Topics:**  
- **SD-WAN:** software-based WAN management, improves performance and flexibility  
- **SASE:** integrates networking and security functions (SWG, CASB, ZTNA)  
- Supports cloud adoption and secure remote access  
- **Software-Defined Wide Area Network (SD-WAN):** virtualized approach to managing and optimizing wide area network connections to efficiently route traffic between remote sites, data centers, and cloud environments
- **Secure Access Service Edge (SASE):** used to consolidate numerous networking and security functions into a single cloud-native service to ensure that secure and access for end-users can be achieved

---

## Module 16.10: Infrastructure Considerations  
**Learning Objectives:**  
- Recognize planning considerations for infrastructure design  
- Explain trade-offs  

**Key Topics:**  
- Performance, scalability, security, and cost must be balanced  
- Redundancy, monitoring, and manageability influence design  
- Business goals shape infrastructure choices  

---

## Module 16.11: Selecting Infrastructure Controls  
**Learning Objectives:**  
- Explain how to choose infrastructure controls  
- Recognize alignment with risk management  

**Key Topics:**  
- Controls should address identified risks and compliance obligations  
- Defense-in-depth: multiple overlapping controls for resilience  
- Selection based on effectiveness, feasibility, and cost-benefit analysis  

---

## Completion Status  
- All Section 16 materials reviewed  
- [Flashcards created for firewalls, IDS/IPS, SD-WAN/SASE, and infrastructure control selection](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=16)   

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
