# IBM Cybersecurity Analyst Professional Certificate  
## Course 5 – Computer Networks and Network Security  

[Coursera](https://www.coursera.org/learn/network-security-database-vulnerabilities/home/module/1)  
---

## Overview  
Course 5 provides a comprehensive introduction to networking concepts, protocols, and security mechanisms. Learners explore the OSI and TCP/IP models, IEEE standards, and wireless technologies, before moving into IP addressing (IPv4 and IPv6), routing, switching, and subnetting. Practical modules cover DNS, DHCP, syslog, packet analysis, and user behavior monitoring. Security topics include firewalls, intrusion detection and prevention, NAT, DLP, NAC, and EDR/XDR. The course culminates in a project requiring learners to design and secure a branch office network using subnetting, firewall configuration, and traffic analysis with Wireshark.  

---

## Module 1: Networking Fundamentals  
This module introduces the hardware, models, and protocols that form the backbone of networking.  

**Learning Objectives:**  
- Identify and differentiate networking hardware devices  
- Explain the OSI and TCP/IP models and IEEE standards  
- Define common ports and protocols and their functions  
- Describe wireless network types (WPAN, WLAN, WMAN, WWAN) and their standards  

**Key Topics & Details:**  
- **Networking Hardware:** Servers, clients, hubs, switches, routers, modems, bridges, gateways, repeaters, NICs, firewalls, proxy servers, IDS/IPS:contentReference[oaicite:1]{index=1}.  
- **Network Models:** OSI’s 7 layers (application to physical); TCP/IP’s 4 layers (application, transport, internet, network access). Standards organizations: ISO, ITU, DARPA, IEEE (802.x), W3C, IETF (RFC process).  
- **Protocols & Ports:** TCP (reliable), UDP (fast), HTTP (80), HTTPS (443), FTP (21), SFTP/SSH (22), Telnet (23, insecure), RDP (3389), SMTP (25), POP3 (110), IMAP4 (143), DNS (53), DHCP (67/68), SNMP (161), LDAP (389), SMB (137–139):contentReference[oaicite:2]{index=2}.  
- **Wireless Networks:**  
  - WPAN (IEEE 802.15: Bluetooth, Zigbee, IR, short range ~10m)  
  - WLAN (IEEE 802.11 Wi-Fi: homes/offices; now 802.11ax Wi-Fi 6 for VR, 8K streaming)  
  - WMAN (IEEE 802.16 WiMAX: metro/campus networks)  
  - WWAN (4G, 5G, LTE, LoRaWAN for global coverage)  
  - WANET/MANET/VANET – ad hoc mobile networks  
- **Cellular Evolution:** 2G (64 Kbps), 3G (2 Mbps), 4G (100 Mbps), 5G (1 Gbps).  
- **Lab:** Explore Windows Server networking environment and hardware identification.  

---

## Module 2: IP Addressing, Routing, and Switching  
This module covers addressing schemes, subnetting, and routing principles.  

**Learning Objectives:**  
- Convert between binary, decimal, octal, and hex numbering systems  
- Differentiate IPv4 and IPv6 addressing schemas  
- Explain subnet masks, prefixes, and default gateways  
- Configure routing principles and Layer 2 vs Layer 3 addressing  

**Key Topics & Details:**  
- **Number Systems:** Binary (base-2), decimal (base-10), octal (base-8), hex (base-16). Conversion practice for IP addressing:contentReference[oaicite:3]{index=3}.  
- **IPv4:** 32-bit addresses; network/host/subnet portions. Classes A–E, default subnet masks (A: 255.0.0.0; B: 255.255.0.0; C: 255.255.255.0). Limitations: exhaustion, non-hierarchical, complex routing, scalability.  
- **IPv6:** 128-bit addresses, expanded address space.  
- **IP Headers:** version, TTL (prevents endless routing), protocol ID (ICMP=1, TCP=6, UDP=17), source/destination IPs, payload.  
- **Routing Concepts:** ARP, subnet masks, broadcast addresses, default gateway role.  
- **Lab:** Secure a SOHO network by configuring router, switch, and devices.  

---

## Module 3: Network Protocols  
This module explores transport and application protocols with practical configuration labs.  

**Learning Objectives:**  
- Explain the roles of TCP and UDP  
- Configure and secure DHCP and DNS services  
- Analyze traffic using syslog and port mirroring  
- Perform user behavior analysis  

**Key Topics & Details:**  
- **TCP vs UDP:** TCP ensures delivery but is slower (web, email, FTP); UDP is fast, resource-light but unreliable (VoIP, gaming, streaming).  
- **Application Protocols:** HTTP/HTTPS, FTP/SFTP, email protocols (SMTP, POP3, IMAP4).  
- **Network Services:**  
  - DHCP (auto IP assignment, ports 67/68)  
  - DNS (domain resolution, port 53; DNS filtering lab with Windows Defender)  
  - SMB (file/printer sharing, ports 137–139)  
  - SNMP (network monitoring, port 161)  
  - LDAP (directory authentication, port 389):contentReference[oaicite:4]{index=4}  
- **Monitoring & Logging:** Syslog, port mirroring, promiscuous mode, Wireshark packet capture.  
- **Lab:** DHCP setup, DNS filtering, traffic analysis, user behavior monitoring.  

---

## Module 4: Network Security Techniques  
This module presents layered defenses against network threats.  

**Learning Objectives:**  
- Apply firewall rules (stateless vs stateful inspection)  
- Configure IDS and IPS systems  
- Explain NAT, DLP, NAC, and FIM functions  
- Deploy EDR/XDR tools in real-world scenarios  

**Key Topics & Details:**  
- **Firewalls:** Software/hardware, inbound/outbound rules, packet vs stateful inspection.  
- **IDS vs IPS:** IDS detects and alerts; IPS actively blocks threats. Snort (open-source IDS/IPS).  
- **NAT:** Conserves IP addresses, masks internal networks.  
- **Advanced Security:**  
  - DLP (Data Loss Prevention) to prevent unauthorized exfiltration  
  - NAC (Network Access Control) for endpoint compliance  
  - FIM (File Integrity Monitoring) for tamper detection  
  - EDR/XDR (endpoint/extended detection & response) — advanced telemetry and incident correlation:contentReference[oaicite:5]{index=5}.  
- **Lab:** Hands-on Xcitium OpenEDR/XDR open-source lab deployment.  

---

## Module 5: Final Project and Wrap-Up  
This module integrates all networking and security concepts into a peer-reviewed project.  

**Learning Objectives:**  
- Design a secure branch office network architecture  
- Implement subnets and calculate subnet masks  
- Analyze HTTP/HTTPS traffic using Wireshark  
- Configure Windows Defender Firewall rules  

**Key Topics:**  
- **Network Design Benefits:** scalability, security, cost savings, performance.  
- **Consequences of Poor Design:** downtime, inefficiency, overspending, vulnerabilities.  
- **Design Tools:** IBM Netcool, IBM Cloud Pak, IBM SevOne, Cisco Network Assistant, SolarWinds, NetBrain, Microsoft Visio, GNS3, Wireshark:contentReference[oaicite:6]{index=6}.  
- **Project Tasks:**  
  - Design wired/wireless topology using Draw.io  
  - Configure routers, switches, WAPs, and end devices  
  - Set firewall rules in Windows Defender  
  - Capture/analyze packets with Wireshark  

---

## Supplementary Projects  
- **Windows Server Labs** – Explore networking devices, ports, and server management  
- **DHCP/DNS Labs** – Configure DHCP service and implement DNS filtering  
- **Wireshark Labs** – Packet analysis, protocol inspection, and broadcast identification  
- **EDR/XDR Labs** – Deploy open-source EDR/XDR tools to monitor endpoint/network activity  
- **Final Project** – Branch office network design, subnetting, and security recommendations  

---

## Completion Status  
- All modules completed  
- All videos, readings, and hands-on labs completed  
- All graded assignments and final project submitted with perfect scores (100%)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
