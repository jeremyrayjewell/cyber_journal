# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 4 – Physical Security  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 4 examines physical security measures used to deter, delay, and prevent unauthorized access to facilities. Learners study controls such as fencing, bollards, locks, vestibules, and surveillance systems, as well as methods attackers use to bypass them, including brute force entry and access badge cloning.  

---

## Module 4.1: Physical Security Basics  
**Learning Objectives:**  
- Define physical security and its role in cybersecurity  
- Identify categories of physical controls  

**Key Topics:**  
- Physical security: measures taken to protect tangible assets, like buildings, equipment, and people, from harm or unauthorized access 
	- protects people, facilities, and information  
- Examples: fencing and bollards, attacking with brute force, surveillance systems, bypassing surveillance systems, access control vestibules  
- Complements technical and administrative controls

---

## Module 4.2: Fencing and Bollards  
**Learning Objectives:**  
- Explain the purpose of fencing and bollards  
- Identify situations where each is appropriate  

**Key Topics:**  
- **Fencing:** structure that encloses an area using interconnected panels or posts 
	- defines boundaries, deters casual intruders, delays attackers  
	- trespassing, theft, vandalism, unauthorized access
- **Bollards:** robust, short vertical posts, made of steel or concrete, that are designed to manage or redirect vehicular traffic 
	- prevent vehicle-based attacks or forced entry  
	- used to keep vehicles away from buildings so that if an IED explodes nearby, the building and people are safe
	- clear visual reminder of where vehicles are not permitted
	- ASTM F2656-07 M30 P1: can stop a 15,000-pound vehicle traveling at 30 mph and not allow a vehicle to move for more than 1m after hitting
- **Attacking with Brute Force:**
	- forcible entry: gaining unauthorized access to a space by physically breaking or bypassing its barriers, such as windows, doors, or fences
		- use reinforced or laminated windows to provide resistance against brute force attacks
		- use high-strength doors with deadbolt locks, metal frames, or a solid core
	- tampering with security devices: involves manipulating security devices to create new vulnerabilities that can be exploited
		- to protect against tampering with security devices, have redundancy in physical security measures
	- confronting security personnel: involves the direct confrontation or attack of security personnel
		- seucirty personnel undergo rigorous conflict resolution and self-defense training to mitigate risks
	- ramming a barrier with a vehicle: brute force attack that uses a car, truck, or other motorized vehicle to ram into the organization's physical security barriers
		- brute force attacks on physical security are a direct, often violent approach to bypassing security measures

---

## Module 4.3: Access Control Vestibules  
**Learning Objectives:**  
- Describe how vestibules (mantraps) support access control  
- Recognize how they reduce tailgating and piggybacking  

**Key Topics:**  
- Two sets of interlocked doors controlling entry  
- Authentication required at each stage  
- May integrate biometrics or badge readers
- **Access Control Vestibules**: Souble-door system that is designed with two doors that are electronically controlled to ensure that only one door can be opened at a given time
	- combined with other measures to create a comprehensive security framework
	- access control vestibules provide a controlled environment for anyone trying to access an organization's facilities
- **Piggybacking**: person with legitimate access intentionally allows another person without authorization to enter a secure area with them
	- involves an authorized individual allowing an attack into the facility
- **Tailgating**: unauthorized person follows someone with legitimate access to the secure space without their knowledge or consent
	- following an authorized individual through the access control vestibule without consent
- radio-frequency identification (RFID), near-field communication (NFC), magnetic strips
	- every time an access badge is used, the action is logged
- visual deterrent, assistance, check identity, response

---

## Module 4.4: Door Locks  
**Learning Objectives:**  
- Compare lock types and their vulnerabilities  
- Understand use cases for mechanical vs. electronic locks  

**Key Topics:**  
- Types: mechanical deadbolts, electronic locks, biometric locks  
- Weaknesses: picking, brute force, or poor installation; **not all door locks offer the same protection level**  
- Security strengthened when combined with logging or MFA
- **Door Locks**: physical security control that is designed to secure entryways by restricting and regulating access to a particular space or property
	- are often placed on the outside of the building's main entrance, as well as inside of the building on server room doors, network closets, and other areas
	- these padlocks use a pin and tumbler system that is fairly easy to defeat
- more complex types of door locks are available; these locks can be configured so that each person uses their own unique identification number
	- biometrics: facial recognition, fingerprint identification; relies on **physical characteristics** to identify a person properly
	- when talking about biometrics, these are considered to be an inherence factor
	- biometrics challenges: acceptance and rejection rates
		- False Acceptance Rate (FAR): rate that the system authenticates a user as valid, even though that person should not have been granted access to the system; increased sensitivity of scanners, lower FAR
		- False Rejection Rate (FRR): occurs any time the biometrics system denies a user who should have been allowed access to the system			
			- Fale Rejection is just as big of a problem as false acceptance
		- Equal Error Rate (EER): more commonly called Crossover Error Rate (CER), which uses a measure of the effectiveness of a given biometrics system to achieve a balance
			- the lower the CER, the better the lock
	- many of these modern electronic door locks will combine multiple authentication factors before giving access to the area
- a *cipher lock* provides excellent protection using a mechanical locking mechanism with push buttons that are numbered and require a person to enter the correct combination in order to open that door
- the **actual moment of vulnerability** arises when unauthorized individuals gain access to the building's interiors
- combination of multiple authentication methods, such as using both a PIN and fingerprint, can also further increase the physical security posture
	
---

## Module 4.5: Surveillance Systems  
**Learning Objectives:**  
- Explain the role of surveillance in security monitoring  
- Recognize limitations and bypasses  

**Key Topics:**  
- Systems: CCTV, IP cameras, DVR/NVR  
- Sensors: infrared, ultrasonic, microwave, pressure-based  
- Weaknesses: blind spots, tampering, poor resolution  
- Countermeasures: redundancy, proper placement
- **Surveillance Systems:** maintain the security and safety of facilities, including business, home, or commonly used public areas
	- traditional security guards and high-tech sensors both aim to monitor for suspicious or harmful activities
	- video survellance: motion detection, night vision, facial recognition, remote access
		- the benefit of video surveillance systems is the ability to provide real-time visual feedback and the capability to review the recorded footage after an incident
		- a wireless solution relies on Wi0Fi to send its signal back to the central monitoring station
		- indoor/outdoor
		- Pan-Tolt-Zoom (PTZ): can move the camera or its angle to better detect issues during an intrusion
		- data center, telecommunication closets, entrance or exit areas
	- security guards: flexible and adaptable forms of surveillance that organizations use
		- security guards help to reassure staff or customers that they are safe
	- lighting: proper lighting is curcial for conducting effective surveillance using both video and security guards
	- sensors: devices that detect and respond to external changes in the environment and convert the information into readable signals or data
		- infrared: detect changes in infrared radiation that is emitted by warm bodies like humans or animals
		- pressure: activate when a specified minimum amount of weight is detected on the sensor that is embedded into the floor or a mat
		- microwave: detect movement in an area by emitting microwave pulses and measuring their reflection off moving objects
		- ultrasonic: measure the reflection of ultrasonic waves off moving objects
	- Surveillance systems often combine various tools and techniques to monitor, detect, and respond to potential threats or unusual activities
- **Bypassing Surveillance Systems:** 
	- visual obstruction: blocking the camera's line of sight (paint on camera, etc)
	- bland sensors and cameras: overwhelming the sensor or camera with a sudden burst of light to render it ineffective for a limited period of time
	- acoustic interference: jamming or playing loud music to disrupt the microphone's functionality
	- electromagnetic interference (EMI): jamming the signals that surveillance systems rely on to monitor the environment
	- physical environment attack: exploiting the environment around the surveillance equipment to compromise it functionality
		- physical tampering, like cutting wires or physically disabling devices, is an effective strategy to bypass surveillance systems
		- modern systems are equipped with countermeasures to help protect surveillance systems
	- tamper alarms, backup power supplies/UPS, encrypt frequencies 

---

## Module 4.6: Attacks on Physical Controls  
**Learning Objectives:**  
- Identify methods used to bypass physical defenses  
- Understand risks from cloned badges and forced entry  

**Key Topics:**  
- **Brute force:** physically breaking locks or barriers  
- **Badge cloning:** duplicating access cards to bypass authentication  
- **Surveillance evasion:** exploiting blind spots, disabling systems  
- Mitigation: stronger locks, multifactor authentication, redundant surveillance, guards 
- **Access Badge Cloning**: copying the data from RFID or NFC card or badge onto another card or device; **considered a stealthy way to conduct a physical security attack**
	- Radio Frequency Identification (RFID) and Near Field Communication (NFC) are popular technologies used for contactless authentication in various applications
	- one of the most prevalent vulnerabilities you need to be aware of in terms of the RFID and NFC technologies is the ability to easily conduct access badge cloning to bypass your authentication systems
	- scanning, data extraction, writing to a new card, using a cloned access badge
	- an attacker can use a handheld RFID or NFC reader to capture dsts from s victim'd card and store it for further processing
	- once the data is captured, attackers extract the relevant authentication credentials from the card
	- using specialized writing tools, the attacker will then transfer the extracted data into a blank RFID or NFC card
	- now that the attacker has their cloned access badge or device in hand, they can gain unauthorized access to buildings, computer systems, or even make payments
	- ease of execution, ability to be stealthy when conducting the attack, potentially large use in compromising physical security
- **combatting access badge cloning**: implement advanced encryption in card-based authentication systems, implement multi-factor authentication (MFA), regularly update security protocols, educate the users, users should implement the use of shielded wallets or sleeves with RFID access badges, monitor and audit access logs

---

## Completion Status  
- All Section 4 materials reviewed  
- [Flashcards created for physical controls and bypass techniques](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=4)

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
