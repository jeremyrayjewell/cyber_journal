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
- **Zero-Day Vulnerability:** any vulnerability that's discovered or exploited before the vendor can issue a patch for it (original definition of "zero-day")
- **Zero-Day Exploit:** any unknown exploit in the wild that exposes a previously unknown vulnerability in the software or hardware
- **Zero-Day Attack**
- on exam, **Zero-Day** ,ay fer to vulenrability, exploit, *or* malware
- Zero-day malware is a *major threat*
- identify, patch, fix
- government agencies, law enforcement agencies, criminals
- Zero-Day vulnerabilities and exploits are *big business*
- akways keep antivirus software up-to-date


---

## Module 18.6: Operating System Vulnerabilities  
**Learning Objectives:**  
- Identify OS vulnerabilities  
- Recognize related attack methods  

**Key Topics:**  
- Outdated patches, misconfigurations, privilege escalation  
- Kernel exploits, insecure services  
- Mitigation: patching, secure baselines, least privilege  
- **Unpatched Systems:** operating systems that have not been updated with the latest security patches or fixes
- **Zero-Day Vulnerabilities:** represent vulnerabilities in software or hardware that are unknown to the developer and in essence, they are newly discovered vulnerabilities that have not been publicaly disclosed yet
- **Misconfiguration:** occurs when the system's settings are not properly configured and this leaves the system vulnerable to exploitation
- **Data Exfiltration:** unauthorized data transfers from within an organization to an external location
- **Malicious Updates:** occur when an attacker has been able to craft a malicious update to a well-known and trusted program in order to compromise the systems of the program's end users

---

## Module 18.7: SQL and XML Injections  
**Learning Objectives:**  
- Explain injection attacks  
- Recognize their risks  

**Key Topics:**  
- SQL injection: manipulating queries to extract/modify data  
- XML injection: altering XML structures to manipulate logic  
- Defenses: parameterized queries, input validation, sanitization  
- **Code Injection:** the insertion of additional information or code through a data input form from a client to an application
- **SQL (Structured Query Language) Injection:** Select, Insert, Delete, Update
	- `Select * from Users where user_id = 'Jason' and password = 'Pass123'`
	- `SELECT * FROM users WHERE login = $name AND password = $pwd`
	- `Select * from Users where user_id = 'Jason' and password = ''OR 1=1;'`
	- URL parameter, entering data, modifying cookies, changing POST data, using HTTP headers
	- use input validation, sanitize data
	- use web application firewall
	- databases use SQL as the way to read and write information
- **Extensivle Markup Language (XML):** used by web applications for authentication, authorization, and other types of data exchange
	- input validation, input sanitization
	- snooping, spoofing, request forgery, injection of arbitrary code
```
<?xml version="1.0" encoding="UTF-8"?>
<question>
	<id>SECURITY-002-0001</id>
	<title>Is this an XML vulnerability?</title>
	<choice1>Yes</choice1>
	<choice2>No</choice2>
</question>
</xml>
```
- **XML Bomb (Billion Laughs Attack):** XML encodes entities that expand to exponential sizes, consuming memory on the host and potentially crashing it
```
<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
 <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
 <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
 <!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
 <!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
 <!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>
```
- **XML External Entity (XXE):** an attack that embeds a request for a local resource
```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
	<!ELEMENT foo ANY>
	<!ENTITY xxe SYSTEM "file:///etc/shadow">]>
<foo>&xxe;</foo>
```
- *input validation prevents a lot of security issues*
- XML vulnerability, XML exploitation, XML injection
- on the exam, determine if a code sample is HTML, JavaScript, of XML

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
- **Cross-Site Scripting (XSS):** injects a malicious script into a trusted site to compromise the site's visitors
	- attacker identifies an input validation vulnerability within a trusted website
	- attacker crafts a URL to perform code injection against the trusted website
	- the trusted siite returns a page containing the malicious code injected
	- malicious code runs in the client's browser with permission level as the trusted site
		- defacing the trusted website
		- stealing the user's data
		- intercepting the data or communications
		- installing malware on client's system
- **XSS** breaks the browsers security and trust model
	- `https://www.diontraining.com/search?q=<script%20type='application/javascript'> alert ('xss')</script>`
	- **Non-Persistent XSS:** this type of attack only occurs when it's launched and happens once
	- **Persistent XSS:** allows an attacker to insert code into the backend database used by that trusted website
	- **Document Object Model (DOM) XSS:** exploits the client's web browser using client-side scripts to modify the content and layout of the web page
		- `https://diontraining.com/index.html# default<script>alert(document.cookie)</script>
		- document.write, document.location
- **Session Management:** enables web applications to uniquely identify a user across several different actions and requests
- **Cookie:** text file used to store information about a user when they visit a website
	- **Non-Persistent:** known as a session cookie, which resides in memory and is used for a very short period of time
	- **Persistent:** stored in the browser cache until either deleted by a user or expired
- **Session Hijacking:** type of spoofing attack where the attacker diconnects a host and then replaces it with his or her own machine by spoofing the original host IP
	- session tokens need to be generated using a non-predictable algoritm
- **Cross-Site Request Forgery (XSRF):** malicious script is used to exploit a session started on another site within the same web browser
	- how to prevent cross-site request forgery:
		- use user-specific tokens in all form submissinos
		- add randomness and prompt for additional information
		- require users to enter their current password when changing their password
---

## Module 18.10: Buffer Overflow  
**Learning Objectives:**  
- Explain buffer overflow vulnerabilities  
- Recognize risks  

**Key Topics:**  
- Occurs when data exceeds allocated memory buffer  
- Can overwrite adjacent memory, execute arbitrary code  
- Defenses: input validation, safe coding, DEP/ASLR protections  
- **Buffer Overflow:** occurs when data exceeds allocated memory, potentially enabling unauthorized access or code execution
	- **Buffer:** a temporary storage area where a program stored its data
	- Buffer overflow attacks in IT are being used as the initial vector, causing 85% of data breaches
	- there is a sequence of memory buffers after Buffer A in the contact list application
- **Stack:** a memory region where a program stores the return addresses from function calls
	- **"Smashing the Stack":** occurs when an attacker can execute their malicious code by overwriting the return address
- **Address Space Layout Randomization (ASLR):** a security measure that randomizes memory addresses, making buffer overflow attacks harder for attackers

---

## Module 18.11: Race Conditions  
**Learning Objectives:**  
- Define race conditions  
- Recognize their risks  

**Key Topics:**  
- Occur when processes depend on timing or order of operations  
- Exploited to gain elevated privileges or bypass checks  
- Mitigation: synchronization, secure coding, testing  
- **Race Condition:** software vulnerability where the outcome depends on the timing of events not matching the developer's intended order
	- race conditions occur when multiple threads write to the same variable or object in the same memory location simultaneously
- **Dereferencing:** software vulnerability that occurs when the code attempts to remove the relationship between a pointer and the thing that pointer was pointing to in the memory
- **Dirty Cow:** popular 2016 exploit, showcasing a race condition exploitation
	- **COW:** Copy On Write
- **Time-of-Check (TOC):** type of race condition where an attacker can alter a system resource after an application checks its state but before the operation is performed
- **Time-of-Use (TOU):** type of race condition that occurs when an attacker can change the state of a system resource between the time it is checked and the time it is used
- **Time-of-Evaluation (TOE):** type of race condition that involves the manipulation of data or resources during the time window when a system is making a decision or evaluations
- *to protect against a race condition, users can use locks and mutexes to lock resources while a process is being run*
- **Mutex:** mutually exclussive flag that acts as a gatekeeper to a section of code so that onl one thread an be processed at a time
_ **Deadlock:** occurs when a lock remains in place because the process it's waiting for is terminated crashes, or doesn't finish properly, despite the processing being complete

---

## Completion Status  
- All Section 18 materials reviewed  
- [Flashcards created for injection types, OS vulnerabilities, mobile threats, and memory-based attacks](https://jeremyrayjewell-flashcards.netlify.app/security-plus-dion.html#deck=18)       

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
