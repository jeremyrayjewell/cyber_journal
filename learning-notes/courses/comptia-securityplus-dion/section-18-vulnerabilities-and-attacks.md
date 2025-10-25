# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 18 – Vulnerabilities and Attacks  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 18 introduces common vulnerabilities and attack methods across hardware, mobile, operating systems, and applications. Learners examine zero-day flaws, injection attacks, XSS/XSRF, buffer overflows, and race conditions. The section emphasizes identifying these threats and applying defenses to reduce risk.  

---

## Module 18.1: Vulnerabilities and Attacks Overview  
**Learning Objectives:**  
- Define vulnerabilities and attacks  
- Recognize their role in security risks  

**Key Topics:**  
- **Vulnerability:** weakness or flaw in hardware, software, configurations, or processes within a computer system, network, or application 
- **Attack:** active exploitation of vulnerabilities  
- Categories: hardware, software, mobile, network, human factors  
- unauthorized access, data breaches, system disruptions, data theft, malware infections, denial of service attacks, social engineering
- **Attacks:** deliberate actions or activities carried out by threat actors with the intent to exploit vulnerabilities
- hardening the system, patching, enforcing baseline configurations, decommissioning old and insecure assets, creating isolation or segmentation for devices
- servers, workstations, laptops, switches, routers, network appliances, mobile devices, internet of things
- bluesnarfing, bluejacking, bluebugging, bluesmark, bluehorns
- side loading, jailbreaking, insecure connection methods
- patch management, mobile device management solutions, preventing sideloading and rooting of devices
- **Zero-Day Vulnerability:** type of software or hardware vulnerability that is discovered and exploited by malicious actors before a patch is released
- unpatched systems, zero-days, misconfigurations, data exfiltration, malicious updates
- patching, configuration management, encryption of data, installing endpoint protection, utilizing host-based firewalls, implementing host-based IPS, configuring access controls and permisions, requiring the use of application allow lists
- **SQL Injection:** type of cyberattack that exploits vulnerabilities in web applications or data bases
- **XML Injection:** security vulnerability that targers web applications that process XML data
- **Cross-Site Scripting (XSS):** web security vulnerability where malicious scripts are injected into web pages viewed by other users
- **Cross-Site Request Forgery (XSRF):** webs ecurity exploit that focuses on an attacker who attempts to trick a user
- **Buffer Overflow:** software vulnerability that occurs when a program writes more data to a memory buffer
- **Race Condition:** software vulnerability that occurs when multiple processes or threads in a concurrent system access shared resources or data simultaneously
- time of check, target of evaluation, time of use

---

## Module 18.2: Hardware Vulnerabilities  
**Learning Objectives:**  
- Identify hardware vulnerabilities  
- Recognize risks in physical and embedded systems  

**Key Topics:**  
- Firmware flaws, insecure chips, malicious hardware implants  
- Side-channel attacks (e.g., Meltdown, Spectre)  
- Supply chain issues affecting hardware integrity
- **Hardware Vulnerabilities:** security flaws or weaknesses inherent in a device's physical components or design that can be exploited to compromise the integrity, confidentiality, or availability of the system and its data
- kinds of vulnerabilties:
	- device's firmware
	- end-of-life hardware
	- legacy hardware
	- unsupported systems and applications
	- unpatched systems
	- hardware misconfigurations
 - kind of hardware:
	- servers
	- workstations
	- laptops
	- swtiches
	- routers
	- network appliances
	- mobile devices
	- IoT devices
- **Firmware:** specialized form of software stored on hardware device, like a router or a smart thermostat, that provides low-level control for the device's specific hardware
	- vulnerabilities: without security, outdated security
	- mitigation: regular updates, security audits, device hardening
- **End-of-Life Systems:** hardware or software products that have reached the end of their life cycle
- **Legacy Systems:** outdated computing software, hardware, or technologies that have been largely superseded by newer and more efficient alternatives
- **Unsupported Systems:** hardware or software products that no longer receive official technical support, security updates, or patches from their respective vendors or developers
- **Unpatched System:** device, application, or piece of software that has not been updated with the latest security patches so that it remains vulnerable to known exploits and attacks
	- unauthorized access, data compromise, service disruption
	- regularly monitoring for updates, assessing the relevance and impact of patches, deploying patches in a timely manner
- **Hardware Misconfiguration:** occurs when a device's settings, parameters, or options are not optimally set up, and this can cause vulnerabilities to exist, a decrease in performance or unintended behavior of devices or systems
	- conduct regular audits, enforce good configuration management practices, implement automated tools, provide training to the personnel
- *hardening:* involves tightening the security of a system
- *patching:* involves the regular updating of the software, formware, and applications with the latest security patches
- *configuration enforcement:* used to ensure that all devices and systems adhere to a standard secure configuration
- *decommissioning:* means that the system is retired and removed from the network
- *isolation:* used to limit the potential damage that might occur from a potential security breach
- *segmentation:* used to divide the network into segments

---

## Module 18.3: Bluetooth Vulnerabilities and Attacks  
**Learning Objectives:**  
- Explain Bluetooth vulnerabilities  
- Recognize attack types  

**Key Topics:**  
- Exploits: Bluejacking (spam), Bluesnarfing (data theft), Bluebugging (device control)  
- Risks from insecure pairing and weak encryption  
- Mitigation: disable unused Bluetooth, update devices, enforce policies  
- **Bluetooth:** wireless technology standard used for exchanging data between fixed and mobile devices over short distances without the need for an Internet connection
	- **Insecure Device Pairing:** occurs when Bluetooth devices establish a connection without proper authentication
	- **Device Spoofing:** occurs when an attacker impersonates a device to trick a user into connecting
	- **On-Path Attack:** exploits Bluetooth protocol vulnerabilities to intercept and alter communications between devices without either party being aware
- Bluejacking, Bluesnarfing, Bluebugging, Bluesmack, Blueborne
- make calls, send text messages, access the internet
- best practicies:
	- turning off Bluetooth
	- ensuring that devices are set to "non-discoverable" mode
	- regularly updating devices
	- only pairing with known and trusted devices
	- always using unique PINs or passkeys
	- always being cautious of unsolicited connection requests
	- using encryption for sensitive data transfers

---

## Module 18.4: Mobile Vulnerabilities and Attacks  
**Learning Objectives:**  
- Identify mobile-specific risks  
- Recognize common attack methods  

**Key Topics:**  
- Rooting/jailbreaking bypasses controls  
- Malicious apps, insecure Wi-Fi usage  
- Risks of lost or stolen devices  
- Defenses: MDM, strong authentication, app vetting  
- **Sideloading:** the practice of installing applications on a device from unofficial sources which actually bypasses the device's default app store
	- always download apps from an official and trusted source
- **Jailbreaking/Rooting:** process that gives users escalated privileges on the devices and allows users to circumvent the built-in security measures provided by the devices
	- avoid opening Wi-Fi and unknown Bluetooth pairings for security
	- long, strong, and complex password
	- 802.1x authentication methods
- **Mobile Device Management (MDM) Solution:** used to conduct patching of the devices by pushing any necessary updates to the devices to ensure that they are always equipped with the latest security patches
	- disable a device's ability to sideload programs
	- detect if a device has been jailbroken or rooted
	- force each device to use a VPN connection

---

## Module 18.5: Zero-day Vulnerabilities  
**Learning Objectives:**  
- Define zero-day vulnerabilities  
- Recognize their impact  

**Key Topics:**  
- Exploits unknown to vendor and unpatched  
- Highly valuable to attackers  
- Defenses: patch management, threat intelligence, layered defenses  

---

## Module 18.6: Operating System Vulnerabilities  
**Learning Objectives:**  
- Identify OS vulnerabilities  
- Recognize related attack methods  

**Key Topics:**  
- Outdated patches, misconfigurations, privilege escalation  
- Kernel exploits, insecure services  
- Mitigation: patching, secure baselines, least privilege  

---

## Module 18.7: SQL and XML Injections  
**Learning Objectives:**  
- Explain injection attacks  
- Recognize their risks  

**Key Topics:**  
- SQL injection: manipulating queries to extract/modify data  
- XML injection: altering XML structures to manipulate logic  
- Defenses: parameterized queries, input validation, sanitization  

---

## Module 18.8: Conducting an SQL Injection  
**Learning Objectives:**  
- Understand mechanics of SQL injection  
- Recognize exploitation steps  

**Key Topics:**  
- Entering malicious SQL into input fields  
- Bypassing authentication, extracting data, escalating privileges  
- Importance of secure coding and input handling  

---

## Module 18.9: XSS and XSRF  
**Learning Objectives:**  
- Define cross-site scripting (XSS) and cross-site request forgery (XSRF/CSRF)  
- Recognize their impacts  

**Key Topics:**  
- **XSS:** injects malicious scripts into web apps (stored, reflected, DOM-based)  
- **XSRF/CSRF:** tricks authenticated users into executing unwanted actions  
- Defenses: input/output validation, CSRF tokens, same-site cookies  

---

## Module 18.10: Buffer Overflow  
**Learning Objectives:**  
- Explain buffer overflow vulnerabilities  
- Recognize risks  

**Key Topics:**  
- Occurs when data exceeds allocated memory buffer  
- Can overwrite adjacent memory, execute arbitrary code  
- Defenses: input validation, safe coding, DEP/ASLR protections  

---

## Module 18.11: Race Conditions  
**Learning Objectives:**  
- Define race conditions  
- Recognize their risks  

**Key Topics:**  
- Occur when processes depend on timing or order of operations  
- Exploited to gain elevated privileges or bypass checks  
- Mitigation: synchronization, secure coding, testing  

---

## Completion Status  
- All Section 18 materials reviewed  
- [Flashcards created for injection types, OS vulnerabilities, mobile threats, and memory-based attacks](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=18)       

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
