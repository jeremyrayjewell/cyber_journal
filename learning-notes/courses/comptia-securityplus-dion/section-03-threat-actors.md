# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 3 – Threat Actors  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 3 examines the types of threat actors, their attributes, and the motivations driving their activities. Learners also review vectors and attack surfaces and study methods for deceiving and disrupting adversaries. The focus is on understanding who the attackers are, how they operate, and why they engage in malicious activity.  

---

## Module 3.1: Threat Actors and Motivations  
**Learning Objectives:**  
- Identify categories of threat actors  
- Explain motivations for different types of attacks  

**Key Topics:**  
*Threat Actor*: individual or entity responsible for incidents that impact security and data protection
*Intent* (specific objective) vs *Morivation* (underlying reasons)
- Threat actors: nation-states, organized crime, hacktivists, insider threats, unskilled attackers  
- Motivations: 
	- *financial gain*: one of the most common motivations for cybercriminals
		- ransomeware attacks
		- banking trojans
	- *data exfiltration*: the unauthorized transfer of data from a computer
		- selling it on the dark web
		- using it for identity theft
		- leveraging it for a competitive advantage
	- *blackmail*: attacker obtains sensitive or compromising information about an individual/organization and threatens to release this information to the public unless certain demands are met
		- reputational damage, legal repercussions, financial loss
		- ransomware, doxxing, sextortion
	- *service disruption*: often achieved by conducting a Distributed Denial of Service (DDoS) attack to overwhelm a network, service, or server with excessive amounts of traffic so that it becomes unavailable to its normal users
		- financial and reputational damage
	- *espionage*: spying on individuals, organizations, or nations to gather sensitive or classified information
		- motivated by national security reasons or for strategic advantage when conducted by a nation state
		- to gain competitive advantage when conducted by a rival company
		- to gain political advantage when conducted by hacktivists or nation-state actors
	- *revenge*: an employee who is disgruntled, or one who has recently been fired or laid off, might want to harm their current or former employer by causing a data breach, disrupting services, or leaking sensitive information
		- causing data breach, distrupting services, leaking sensitive information
		- former or current employee, or anyone who believed a targeted entity has wronged them in some way 
	- *philosophical or political beliefs*: individuals or groups use hacking to promote a political agenda, social change, or to protst against organizations they perceive as unethical
		- "hacktivist" motivation
		- website defacement, data leaks
		- targets political, financial, and media industries
	- *ethical reaons*: ethical hackers, also known as *authorized hackers*, are motivated by a desire to improve security
		- pen testers, bounty hunters
	- *disruption or chaos*: often referred to as *unauthorized hacker*, these actors engage in malicious activities for the thrill of it, to challenge their skills, or simply to cause harm
		- for thrill, to challenge their skills, or simply to cause harm
		- creating/spreading malware, launching sophisticated cyber attacks against critical infrastrucre
	- *war*:  cyberattacks have increasingly become a tool for nations to attack each other both on and off the battlefield
		- disrupt a country's infrastructure, compromise national security, and to cause economic damage
		- most common actor behind attacks with geopolitical objectives


- Threat vectors and attack surfaces: message-based, image-based, file-based, voice calls, removable devices, use of unsecured networks

---

## Module 3.2: Threat Actor Attributes  
**Learning Objectives:**  
- Recognize attributes that distinguish threat actors  
- Assess relative sophistication and capability  

**Key Topics:**  
- Internal vs. external threats and their relative risk
	- *internal threat actors*: individuals or entities within an organization who pose a threat to its security
		- angry employees, contractors, business associates
		- have legitimate access but use it in an unauthorized way
		- may be motivated by revenge, financial gain, or coercion by external entitites
	- *external threat actors*: individuals or groups outside an organization who attempt to breach its cybersecurity defenses
		- cyber criminals, hacktivists, competitors, state-sponsored actors
		- tpically do *not* have authorized access, use malware or social engineering to gain access
- Resources and funding: the tool, skills, and personnel at the disposal of a given threat actor
	- can influence scale, frequency, and sophistication
- Level of sophistication and capability: technical skill, the complexity of the tools and techniques used, and the ability to evade detection and countermeasures
	- low level of sophistication and capability: use widely available tools and techniques, such as common malware or phishing attacks
		- "Script Kiddies"
	- high level of sophistication and capability: possess advanced technical skills and use sophisticated tools and techniques, like custom-developed malware, zero day exploits, and advanced evasion techniques
		- APT (advanced persistent threats)

- Unskilled attackers (“script kiddies”): limited technical skills, reliance on tools 
	- script kiddie (unskilled attacker): an individual who lacks the technical knowledge to develop their own hacking tools or exploits
	- can still cause significant damage using readily available toold and exploits to victimize systems with unpatched, known vulnerabilites
	- many are motivated by a desire for recognition or the thrill of causing disruption to an organization's network
	- less likely to be motivated by financial gain or political ideologies 
- Advanced actors: well-funded, custom malware, long-term campaigns  
- Attributes: resources, stealth, persistence, access, sophistication

---

## Module 3.3: Hacktivists  
**Learning Objectives:**  
- Define hacktivism and its role in cyberattacks  
- Identify tactics used by hacktivists  

**Key Topics:**  
- Hacktivitsts: individuals or groups that use their technical skills to promote a cause or drive social change instead of for personal gain
	- fairly high levels of sophistication
	- target organiations or individuals that they perceive as acting out against their cause
	- Anonymous, LulzSec
- Politically or ideologically motivated attackers  
- Techniques: DDoS, defacement, data leaks, doxing  
- Aim: visibility for a cause, disruption of targets

---

## Module 3.4: Organized Crime  
**Learning Objectives:**  
- Explain how organized crime groups operate  
- Recognize financially motivated attacks  

**Key Topics:**
- Organized Cyber Crime Groups: sophisticated and well-structured entities that leverage resources and technical skills for illicit gain
	- typically well-structured, with members having specific roles based on skills/expertise
	- transnational nature can create increased complexity for law enforcement
	- possess a very high level of technical capability, often emplying custom malware, ransomware, sophisticated phishing campaigns
	- known to exploit emerging technologies like cryptocurrencies, dark web, cellular collection devices
	- motivation is almost always financial gain, using data breaches, identity theft, online fraud, ransomware attacks
	- targets: small- to medium-sized business and high net worth individuals
	- though not ideologically motivated, they may be hired by other entities, including governments
	- FIN7, Carbanak  
- Structured criminal groups engaging in cyberattacks  
- Common activities: ransomware, phishing, identity theft, fraud  
- Goal: financial profit, sometimes outsourcing capabilities

---

## Module 3.5: Nation-State Actors  
**Learning Objectives:**  
- Describe the objectives of nation-state attackers  
- Recognize tactics and strategies used  

**Key Topics:**  
- Nation-State Actors: Groups that are sponsored by a government to conduct cyber operations against other nations, organizations, or individuals
	- false flag attack: orchestrated in such a way that it appears to rogiinate
	- some of the most highly sophisticated and capable
	- techniques: creating custom malware, using zero-day exploits, becoming an advanced persistent threat
	- Advanced Persistent Threat (**APT**): once synonymous with nation-state actor because of their long-term persistence and stealth
	- motivated to achieve long-term strategic goals: gathering intelligence, disrupting critical infrastructure, influencing political processes
	- North Korea, Stuxnet Worm (US/Israel), Russia (US elections)
- State-sponsored operations against organizations or countries  
- Use of APT campaigns, zero-day exploits, long-term infiltration  
- Motivations: espionage, disruption, geopolitical advantage  
- Techniques: false flag operations to obscure attribution

---

## Module 3.6: Insider Threats  
**Learning Objectives:**  
- Identify the risks of insider threats  
- Differentiate malicious and unintentional insiders  

**Key Topics:**  
- Insider Threats: cybersecurity threats that originate from within the organization
	- have an intimate knowledge of infrastructure
	- have varying levels of capabilities, largely determined by role and level of access
	- forms: data theft, sabotage, misuse of access privileges
	- can also help to facilitate external attack, installing malware or backdoors
	- financial gain, revenge, unintentional (result of carelessness or lack of awareness)
	- Edward Snowden, Twitter attack of 2020
- Malicious insiders: data theft, sabotage, revenge  
- Unintentional insiders: negligence, poor training  
- Mitigation: monitoring, access controls, user training 

---

## Module 3.7: Shadow IT  
**Learning Objectives:**  
- Explain the concept of Shadow IT  
- Understand risks created by unauthorized systems  

**Key Topics:**  
- Shadow IT: the use of information technology systems, devices, software, applications, and services without explicit organizational approval (a.k.a . "stealth IT", "client IT")
	- use of personal devices for work purposes, installation of unapproved software, use of cloud services that have not been approved by the organization
	- exists because a security posture is too high/complex, when employees want to gain efficiency
	- USB drive, external hard drive, keyboard, wired mouse, network adapter, cloud services
	- leads to a lack of standardization
- Unapproved apps, services, or devices used without IT approval  
- BYOD (Bring Your Own Device) as a common source of Shadow IT  
- Causes: overly strict policies, desire for convenience  
- Risks: data leakage, unmanaged vulnerabilities 

---

## Module 3.8: Threat Vectors and Attack Surfaces  
**Learning Objectives:**  
- Differentiate threat vectors from attack surfaces  
- Identify common vectors and methods of exploitation  

**Key Topics:**  
- Vectors: phishing, smishing, vishing, malicious files, removable media, unsecured Wi-Fi, Bluetooth exploits  
- Attack surfaces: exposed services, unpatched systems, misconfigurations  
- Reduction: patching, disabling unused services, limiting access 

---

## Module 3.9: Outsmarting Threat Actors  
**Learning Objectives:**  
- Explain methods for deceiving or disrupting attackers  
- Recognize common deception tools  

**Key Topics:**  
- Honeypots, honeynets, honeyfiles, honeytokens  
- Bogus DNS entries, decoy directories, fake telemetry  
- Goal: mislead adversaries, collect intelligence, slow attacks 

---

## Completion Status  
- All Section 3 materials reviewed  
- Flashcards created for threat actor types, motivations, attributes, and vectors  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
