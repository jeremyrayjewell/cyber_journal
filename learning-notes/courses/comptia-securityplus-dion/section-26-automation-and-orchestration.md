# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 26 – Automation and Orchestration  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 26 introduces automation and orchestration as methods to improve efficiency, consistency, and responsiveness in cybersecurity operations. Learners review benefits, use cases, and integrations of automation across support, onboarding, development, and security functions.  

---

## Module 26.1: Automation and Orchestration Overview  
**Learning Objectives:**  
- Define automation and orchestration  
- Recognize their differences  

**Key Topics:**  
- **Automation:** use of scripts or tools to handle repetitive tasks  
- **Orchestration:** coordinated use of multiple automated tasks into workflows  
- Both improve speed, consistency, and resource efficiency  
- **Automation:** automatic execution of taks without manual involvement; individual tasks
- **Orchestration:** coordination of the automated tasks for a spceific outcome or workflow; multiple automated tasks
- **SOAR:** Security, Orchestration, Automation, Response
	- SOAR's automation capabilities make it serve in incident response primarily
	- SOAR integrates with SIEM and creates a next-generation SIEM
	- incident response may be performed immediately to provision resources
- **Playbook:** checklist of actions for specific incident responses
	- playbook typically focuses on the outlined actions
- **Runbook:** automated versions of playbooks with human interaction points
- when to automate and orchestrate, benefits of automation and orchestration, automating support tickets, automating onboarding process, automating security, automating application development, integrations and APIs

---

## Module 26.2: When to Automate and Orchestrate  
**Learning Objectives:**  
- Recognize when automation is beneficial  
- Explain orchestration needs  

**Key Topics:**  
- Automate repetitive, high-volume, rule-based tasks  
- Orchestrate tasks requiring coordination across multiple systems or tools  
- Example: automated alert triage vs. orchestrated incident response playbooks  
- automation and orchestration are vital in modern IT and cyber-security environments
= streamline complex processes, enhance security meaures, improve operational efficiency
- complexity, cost, single points of failure, technical debt, ongoing supportability
	- **Complexity:** works best in repetitive tasks, ensuring a better return on investment
		- the initial step involves assessing the complexity and resource commitment needed for the process
		- isolate infected machine, image storage drive, analyze drive with forensics, format workstation, install clean OS image, validate workstation, reconnect to network
	- **Cost:** requires a large upfront initial investment to hire a service provider or a team of developers for implementation
		- hardware, software, personnel, ongoing support cost
	- **Single Points of Failure:** identify during automation or orchestration implementation in the network
		- inadequately designed automation can disrupt critical business processes if issues arise
		- redundancy involves backup systems or manual processes to ensure continuity in case of failures
	- **Technical Debt:** can accumulate if not regularly maintained or updated; cost and complexity of poorly implemented software needing future adjustments
		- regular reviews and updates help reduce technical debt in automation and orchestration systems
	- **Ongoing Supportability:** long-term supportability is crucial for adapting automation to evolving technology
- automation depends on the connection of systems via APIs and webhooks
- automation and orchestration work best for stable, repeatable tasks
	- **

---

## Module 26.3: Benefits of Automation and Orchestration  
**Learning Objectives:**  
- Explain advantages of automation and orchestration  
- Recognize their impact  

**Key Topics:**  
- Reduces human error and response times  
- Improves scalability and resource allocation  
- Frees analysts for higher-level work  
- Provides consistency across security operations  
- automation and orchestration enhance organizational efficiency, securrity, and effectiveness
- increasing efficieny and time savings, enforcing baselines, implementing standard infrastructure configurations, scaling in a secure manner, increasing employee retention, increasing reaction times, being a workforce multiplier
	- **Increasing efficiency and time savings:** automating tasks frees up employee time
	- **Enforcing baselines:** streamlined security and compliance through automation
		- enforce industry standards through automated policies
	- **Implementing standard infrastructure configurations:** standardized configurations for security and stability
	- **Scaling in a secure manner:** dynamic resource scaling with securiity compliance
	- **Increasing employee retention:** automating tasks unlocks job fulfillment
	- **Increaing reaction times:** respond more quickly to security incidents and anomalies through automation
	- **Being a workforce multiplier:** amplifying staff capabilities with automation
- embrace automation and become a process engineer
- automation streamlines incident response
- automated tools flag suspicious network activity

---

## Module 26.4: Automating Support Tickets  
**Learning Objectives:**  
- Explain ticket automation  
- Recognize its use cases  

**Key Topics:**  
- Automates creation, assignment, and routing of support tickets  
- Reduces delays in incident handling  
- Integrates with SIEM alerts for rapid response  
- support ticket management is a critical function for customer support teams
- delays in issue resolution, increased workloads, decreased customer satisfaction scores
- efficiency, consistency, scalability
- **Automation:** process of using technology and machinery to perform tasks or processes with minimal human intervention
	- ticket creation, ticket escalation
- **Ticket Creation:** involves the automatic generation of tickets when users or customers report issues or requests
	- users or customers will submit support requests through various channels
	- an automation tool monitors incoming requests and generates support tickets based on predefined criteria
	- the automation system captures essential user-submitted information
		- description, contact details, metadata
	- automation categorizes tickets based on content or source
	- tickets are prioritized based on predefined rules and criteria
	- automated notifications are sent to the relevant support team or technician
		- captured, categorized, assigned
- **Ticket Escalation:** critical aspect of support ticket management that ensures that complex or high-priority issues are addressed promptly and by the appropriate personnel
	- escalation criteria are defined by the organization based on issue nature, urgency, and service level agreements
	- automation rules for escalation are created
		- priority level, response time, unresolved status
	- automation system executes predefined actions for escalation
	- automation will continuously monitor and track the progress of escalated tickets
	- automation system triggers ticket closure and notifesi the user or customer
		- transparency, accountability

---

## Module 26.5: Automating Onboarding  
**Learning Objectives:**  
- Define automation in onboarding  
- Recognize benefits  

**Key Topics:**  
- Automates account creation, access provisioning, and policy assignment  
- Ensures new employees meet security requirements from day one  
- Reduces administrative overhead  
- **Automation:** use of technology to execute repetitive tasks without continuous human intervention in order to increase overall efficiency
	- overall productivity, employee satisfaction, retention rates
	- eliminate any tedious manual tasks; reduce the likelihood of errors; provide new employees with a structures, consistent experience
- automating the onboarding process is crucial for businesses
- creating documentation records, scheduling training, provisioning equipment, managing access rights, distributing various checklists, collecting feedback
- **User Provisioning:** involves the creation and management of user accounts and access rights to internal systems
	- create the user's account, assign the account the correct roles and access,, send out the proper notifications and confirmations, conduct continuous synchornization and updates
		- email, work management platforms, internal communication tools
		- workstations, software licenses, communication tools
- **Resource Provisioning:** allocating the necessary tools and resources that new employees need to perform their jobs
	- requirements analysis, resource allocation, configuration and customization, verification and audting, gathering feedback
	- workstation, providing a smartphone, granting a license
	- the verification process ensures the automation was successful
	- speed up the process, reduce errors, ensure compliance, save time and resources

---

## Module 26.6: Automating Security  
**Learning Objectives:**  
- Explain automation of security tasks  
- Recognize benefits  

**Key Topics:**  
- Automates patch deployment, malware removal, log analysis  
- Supports continuous monitoring and compliance checks  
- Enables faster containment of incidents  
- **Security Automation:** involves use of technology to handle repetitive security tasks and maintain consistent defenses
	- **Guardrails:** automated safety controls to protect against insecure infrastructure configurations
		- guardrails enforce security policies, monitor infrastructure, and automatically act on security violations
		- revoke permissions, reconfigure components, isolate infected workstation
	- **Security Groups:** act as cloud-based server firewalls that control incoming and outgoing network traffic
		- automation assigns instances to security groups with predefined rules
		- systems adapt security groups to evolving threats
		- automated traffic analysis ensures compliance with security settings
	- **Service Access Management:** a crucial area to prioritize in security automation for risk reduction and operational efficiency
		- automatic access review
		- automatic monitoring of unusual activities for quick time response
		- automatic restriction of access when needed
		- automatic enabling/disabling of services for security
	- **Managing Permissions:** involves ensuring that individuals have the correct access level corresponding to designated role
- **Role-based Access Control (RBAC):** used to assign and manage system permissions
	- manages user permissions for onboarding, transfers, and departures
	- ensures protection of sensitive information
	- allows automated compliance checks and adjustments

---

## Module 26.7: Automating Application Development  
**Learning Objectives:**  
- Recognize automation in DevOps/DevSecOps  
- Explain its role in secure development  

**Key Topics:**  
- Automated testing, builds, and deployments  
- Integrates security checks (static/dynamic analysis) into pipelines  
- Improves software quality and reduces vulnerabilities  
- automating development enhances software quality
- automation involves the use of technology to manage, test, and deploy new apps or features with minimal human intervention
- features developed and released rapidly with continuous integration
- **Continuous Integration** and **Continuous Deployment (CI/CD)** enhances efficiency, consistency, and overall quality of software spplications
- **Continuous Integration (CI):** practice in software development where developers merge code changes frequently in one place
	- automated tests follow code integration for efficiency
	- **Release:** process of finalizing and preparing new software or updates; enabling software installation and usage
	- **Deployment:** involves automated process of software releases to users; installing software to a new environment
- **Continuous Delivery:**maintains deployable code with automation
	- continuous delivery is part of the release process
	- in continuous delivery, the full deployment process is automated only up to a certain stage
	- continuous delivery allows manual control of deploying changes to the live production environment
- **Continuous Deployment:** automates the process of deploying code changes from testing to production after completion of the build stage
- automation ensures consistent error-free deployments and accelerates the deployment process
- rollback capability is crucial for ensuring service continuity in a continuous deployment model
- in CI/CD, developers take responsibility for code testing and deployment, moving away from the traditional hand-off approach
- **Continuous Integration and Continuous Delivery**
- **Continuous Integration and Continuous Deployment**

---

## Module 26.8: Integrations and APIs  
**Learning Objectives:**  
- Define the role of APIs in automation  
- Recognize integration benefits  

**Key Topics:**  
- APIs connect security tools for orchestration  
- Example: SIEM, ticketing, and endpoint systems sharing data  
- Enables seamless automation workflows across platforms  
- **Integration:** procecss of combining different subsystems or components into one comprehensive system to ensure that they function properly together
- **Application Programming Interface (API):** set of rules and protocols that are used for building and integrating application software
	- administration, management, monitoring
	- REST, SOAP
- **Representational State Transfer (REST):** architectural style that uses standard HTTP methods and status codes, uniform resource identifiers, and MIME types
- **Simple Object Access Protocol (SOAP):** protocol that defines a strict standard with a set structure for the message, usually in XML format
- REST is more straightforward and adaptable to utilize
- SOAP provides higher level of security and transactional integrity
- provisioning, configuration, deprovisioning
- how to overcome this limitation
- Udemy has an API that allows anyone to programmatically read and respond to any Q&A posts
- get the new Q&As, create the trouble tickets, post the responses back
- email, Q&A section
- video lessons, quizzes, study guide, practice exams
- a thrid-party partner will integrate the labs into the course experience
	- no need for another username and password
	- no need to go to a different website
	- no need to figure out which lab to use
	- which of the students is taking the lab
	- which lesson are students at in the course
	- which lab needs to be run
	- authorization token
- how to test if a given API is working propery
- **CURL:** tool to transfer data to or from a server using one of the supported protocols
	- HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, DICT, TELNET, LDAP, FILE
- integrations and APIs are used to create interconnections between different services

---

## Completion Status  
- All Section 26 materials reviewed  
- [Flashcards created for automation vs. orchestration, benefits, and automation use cases](https://jeremyrayjewell-flashcards.netlify.app/security-plus-dion.html#deck=26)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
