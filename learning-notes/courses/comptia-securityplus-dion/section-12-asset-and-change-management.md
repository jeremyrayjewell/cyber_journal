# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 12 – Asset and Change Management  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 12 covers asset and change management practices that ensure IT resources are securely acquired, deployed, maintained, and retired. Learners examine processes for tracking assets, managing mobile devices, and handling procurement and disposal. The section also introduces structured change management frameworks and their technical implications.  

---

## Module 12.1: Asset and Change Management Overview  
**Learning Objectives:**  
- Define asset and change management  
- Explain their role in security and operations  

**Key Topics:**  
- Asset management: tracking and controlling IT resources  
- Change management: structured processes for modifying systems  
- Both support accountability, compliance, and risk reduction  
- **Asset Management:** systematic process of developing, operating, maintaining, and selling assets in a cost-effective manner
- **Acquisution and Procurement:** structured process of sourcing, vetting, and obtaining security technologies and services
- Every change should undergo a strict approval process while considering a lot of different aspects
- Consider the complexities of legacy applications and dependencies

---

## Module 12.2: Acquisition and Procurement  
**Learning Objectives:**  
- Explain secure procurement practices  
- Recognize risks in acquisition  

**Key Topics:**  
- Vendor due diligence and supply chain security  
- Ensure hardware/software integrity before deployment  
- Align purchases with organizational policies and compliance  
- **Procurement:** encompasses the full process of acquiring goods and services, including all preceding steps
	- company credit card, individual purchase, use of purchase orders
	- organizations often permit employees to use company credit cards for small purchases on the organization's behalf
	- an individual purchase entails employees buying on the company's behalf and later seeking reimburdement from their employer
	- an approval process for purchases ensures alignment with the company's goals and needs
- **ITPR: Infromation, Technology, Procurement, Request**
- Ensure financial prudence, enhance operational efficiency, increase security for the organization's enterprise network

---

## Module 12.3: Mobile Asset Deployments  
**Learning Objectives:**  
- Identify challenges in deploying mobile assets  
- Recognize security requirements  

**Key Topics:**  
- BYOD, corporate-owned, and hybrid models  
- Risks: data leakage, theft, unauthorized access  
- Mitigation: MDM solutions, encryption, strong authentication  
- **Bring Your Own Device (BYOD):** permits employees to use personl devices for work
	- employees own and control the security of their devices
	- personal devices must undergo security checks and have specific software for protecting company data
	- organization might not have the ability to manage or update the device for uers, or enforce stricter security configurations
- **Corporate-Owned, Personally Enabled (COPE):** involves the company providing a mobile device to employees for both work and personal use
	- COPE standardizes device management but may be expensive for employers providing devices to staff
- **Choose Your Own Device (CYOD):** offers a middle ground between BYOD and COPE by allowing employees to choose devices from a company-approved list
	- CYOD has higher intial costs for the organization and raises employee data privacy concerns
- *costs, security, employee satisfaction*
	- BYOD is cost-effective, but hidden costs may arise related to security and compatibility
	- COPE and CYOD have higher upfront costs but save on ongoing support due to fewer supported device models
	- CYOD provides optimal control over devices and enables management through the organization's MDM solution
	- BYOD and CYOD models are suitable for prioritizing employees' freedom and choice

---

## Module 12.4: Asset Management  
**Learning Objectives:**  
- Define asset management practices  
- Explain inventory tracking and responsibility  

**Key Topics:**  
- Maintain up-to-date inventory of hardware and software  
- Tagging and tracking devices  
- Assigning ownership and accountability  
- Supports patching, auditing, and lifecycle management  
- **Asset Management:** refers to the systematic approach to governing and maximizing the value of items an entity is responsible for throughout their lifecycle
- **Assignment/Accounting:** every organization should designate individuals or groups as owners for each of its assets
- **Classificiation:* involves categorizing assets based on criteria like function, value, or other relevant parameters as determined by the organization
- **Monitoting/Tracking:** ensures proper accountability and optimal use of each asset
- **Asset Tracking:** involves maintaining a comprehensive inventory with asset specifications, locations, assigned users, and relevant details
- **Enumeration:** involves identifying and counting assets, especially in large organizations or during times of asset procurement or retirement
	- maintains accurate inventory, detects unauthorized devices, informs software update decisions, addresses security vulnerabilities
- **Mobile Device Management (MDM):** lets organizations securely oversee employee devices, ensuring policy enforcement, software consistency, and data protection
	- MDM's centralization boosts security by ensuring all devices comply with the latest standards and protocols
	- MDM lowers risks tied to unsecured or outdated devices
- Asset Management guarantees the organization's assets are optimally utilized, delivering maximum value and security

---

## Module 12.5: Asset Disposal and Decommissioning  
**Learning Objectives:**  
- Explain secure disposal and decommissioning processes  
- Recognize risks of improper disposal  

**Key Topics:**  
- Wiping, degaussing, or physically destroying drives/media  
- Sanitization to prevent data recovery  
- Ensure compliance with regulations and industry standards  
- **Special Publication 800-88**, commonly referred to as the "Guidelines for Media Sanitization"
	- **Sanitization:** the thorough process of making data inaccessible and irretrievable from a storage medium using traditional forensic methods
		- **Overwriting:** replacing the existing data on a storage device with random bits of information to ensure that the original data is obscured
			- single pass, 7 passes, 35 passes
			- each overwrite makes it increasingly difficult for potential adversaries to retrieve any meaningful data using forensic tools
		- **Degaussing:** involves using a machine called a degausser to produce a strong magnetic field that can disrupt the magnetic domains on storage devices like hard drives or tapes
			- after degaussing, a device loses its data storage capability
		- **Secure Erase:** completely deletes data from a storage device while ensuring that it can't be recovered using traditional recovery tools
			- **Cryptographic Erase** was introduced to replace the Secure Erase technique in most modern storage devices
				- one significant advantage of cryptographic erase over traditional erasure methods is speed
		- **Destruction:** ensures the physical device itself is beyond recovery or reuse
			- shredding, pulverizing, melting, incinerating
		- **Certification:** an act of proof that the data or hardware has been securely disposed of
			- organizations should prioritize data security by documenting the sanitization, disposal, or destruction of data
			- data retention is focused on strategically deciding what to keep and for how long
			- regulations may require specific data, such as financial transactions or medical records, to be retained for a set duration
- *The more you store, the more you must secure:* every piece of data, no matter how trivial, needs protection from potential data breaches
	- asset disposal and decommissioning is an important process that must be considered
	- guidelines presented by the National Institute of Standards and Technology

---

## Module 12.6: Change Management  
**Learning Objectives:**  
- Define change management and its goals  
- Recognize need for structured processes  

**Key Topics:**  
- Prevent untested or unauthorized changes  
- Ensure accountability and minimize service disruption  
- Align changes with business and compliance needs  
- **Change Management:** an organization's orchestrated strategy to transition from its existing state to a more desirable future state
	- disruption of existing processes by any kind of change will affect its efficiency and effectiveness
	- change management ensures seamless integration of changes into existing architecture and processes
- **Change Advisory Board (CAB):** body of representatives from various parts of an organization that is responsible for evaluation of any proposed changes
- **Change Owner:** an individual or a team that initiates the change request
- **Stakeholder:** a person who has a vested interest in the proposed change
	- technical stakeholders, business stakeholders, end user-based stakeholders
- **Impacy Analysis:** an integral part of change management process that ivolves understanding of change's potential fallout
	- What could go wrong?
	- What would be the immediate effects?
	- How would the long-term operations be impacted?
	- Are there unforeseen challenges that might cause an issue?
- Change management is a critical process that guides organizations safely through any changes or transformations needed
	

---

## Module 12.7: Change Management Processes  
**Learning Objectives:**  
- Explain key steps in managing changes  
- Recognize documentation and approval requirements  

**Key Topics:**  
- Request → Impact assessment → Approval → Implementation → Review  
- Documenting changes for traceability and accountability  
- CABs (Change Advisory Boards) for approval and oversight
- **Preparation:** involves assessing the current state and recognizing the need for transition
	- gather necessary resources, engage stakeholders, ensure preparedness
- **Vision for Change:** a clear, compelling description of the desired future state that is guiding the transformation process within an organization
	- define future state, explain reasons for change, ensure vivid vision
- **Implementation:** putting the plan into action
	- training, restructuring teams, introducing new technologies, continuous communication
- **Verification:** measuring the change's effectiveness by comparing it to the inittial objectives
	- surveys, performance metrics analysis, stakeholder interviews
- **Documentation:** creating a thorough record of the entire change process
	- reflect on past initiatives, understand decisions, improve practices
- **areas to be considered throughout the change management process:**
	- *use of scheduled maintenance windows:* a scheduled maintenance window does not restrict change implementation as emergencies may require immediate action
	- *creation of a Backout Plan:* predetermined strategy for restoring systems to their intiial state in case a change does not go as expected
	- *testing of results*
	- *use of Stadard Operating Procedures (SOPs):* a step-by-step instruction that guides the carrying out of a specific task to maintain consistency and efficiency 

---

## Module 12.8: Technical Implications of Changes  
**Learning Objectives:**  
- Recognize technical effects of system changes  
- Explain risks if unmanaged  

**Key Topics:**  
- Possible impacts: downtime, incompatibility, vulnerabilities  
- Importance of testing, rollback plans, and monitoring  
- Technical changes must align with security controls and business goals  
- allow and deny lists, restricted activities, complex applications interplay, dependencies
- **Allow List:** permitted entities
- **Deny List:** prevented entities
- **Restricted Activities:** knowing restrictions can prevent data breaches and operational problems
- **Downtime**
- **Service and Application Restarts:** data may be lost in transit and backlog may be created during the associated downtime
- **Legacy Application:** older software or system that is still being used and meets the needs of users; can malfunction or crash from even minor updates in other parts of the system
- **Dependencies:** prior to implementing proposed changes, it is crucial to map existing dependencies to prevent minor tweaks
- technical implications of proposed changes involve understanding and grasping potential impact of changes

---

## Module 12.9: Documenting Changes  
**Learning Objectives:**  
- Explain why documenting changes is critical  
- Recognize what must be recorded  

**Key Topics:**  
- Records: what changed, when, by whom, approval path, test results  
- Enables audits, compliance checks, troubleshooting  
- Ensures accountability and historical tracking  
- Documenting changes provides a clear history of the what, when, and why for accountability and future reference
- **Version control:** tracks and manages changes in documents and software, enabling collaborative work and reverting to prior versions when needed
	- version control ensures continuity and stability in the environment beyond preserving history
	- preoperyl document and record every change
	- update diagrams
	- revise policies and procedures
	- update change requests
	- maintain associated trouble tickets
- updating diagrams, like flowcharts or network diagrams, offers a visual snapshot of the system's architecture
- when encountering implementation issues, revise policies and procedures to prevent future occurrences
- after implementing a change, update the related change request or trouble ticket to indicate completion

---

## Completion Status  
- All Section 12 materials reviewed  
- [Flashcards created for asset lifecycle, disposal methods, and change management processes](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=12)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
