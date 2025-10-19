# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 14 – Cyber Resilience and Redundancy  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 14 focuses on ensuring continuity of operations through resilience and redundancy. Learners study high availability, data redundancy, RAID, capacity planning, backup strategies, redundant sites, and resilience testing. Emphasis is placed on planning, preparation, and infrastructure support to ensure critical services remain available during disruptions.  

---

## Module 14.1: Cyber Resilience and Redundancy Overview  
**Learning Objectives:**  
- Define cyber resilience and redundancy  
- Explain their importance in security operations  

**Key Topics:**  
- **Resilience:** ability to maintain operations during disruptions  
- **Redundancy:** duplication of critical systems and data  
- Both aim to reduce downtime and data loss  
- **Cyber Resilience:** entity's ability to continuously deliver the intended outcome despite adverse syber events
	- power supplies, connections, servers, services, providers
	- **R.A.I.D.:** Redundant Array of Independent Disks
	- people technology, infrastructure
	- generators, UPSs, line conditioner, power distribution centers
	- **BCDR:** Business, Continuity, Disaster, Recovery
	- hot sites, cold sites, warm sites, geographic dispersion, virtual sites, platform diversity
	- tabletop exercises, failover techniques, simulation, parallel processing

---

## Module 14.2: High Availability  
**Learning Objectives:**  
- Explain the concept of high availability (HA)  
- Recognize design elements for HA  

**Key Topics:**  
- System design to minimize downtime  
- Use of clustering, load balancing, and failover systems  
- Requires monitoring, patching, and preventive maintenance  
- **High Availability:** the ability of a service to be continuously available by minimizing the downtime to the lowest amount possible
- **Uptime:** the number of minutes or hours that the system remains online over a given period, and this uptime is usually expressed as a percentage
	- 99.9999% equated to only 31 seconds of downtime each and every year
- **Load Balancing:** the process of distributing workloads across multiple computing resources
- **Clustering:** the use of multiple computers, multiple storage devices, and redundant network connections that all work together as a single system to provide high levels of availability, reliability, and scalability
	- clustering provides redundancy in the event of system failure to ensure that continuity of service is maintained
- **Redundancy:** the duplication of critical components or functions of a system with the intention of increasing the reliability of the system
	- adding multiple power supplies, network connections, servers, software services, service providers
	- this type of power supply redundancy can be achieved by installing two power supply units inside of a server or network device
	- maintain multiple network connections or pathways by using multiple cabled connections
	- servers and services can be configured to operate in a load balanced or clustered architecture
	- to safeguard the organization against outages, use two or more service providers to ensure a constant backup
	- it's important that each design decision is considered to decide if redundancy is required for a particular piece of hardware
	- utilize multi-cloud systems to distribute data, applications, and services across several different cloud-based environments
	- using a multi-cloud system also provides some additional flexibility for scaling operations and for optimizing costs
	- *vendor lock-in*
	- data management, threat management, policy management

---

## Module 14.3: Data Redundancy  
**Learning Objectives:**  
- Define data redundancy  
- Explain its role in resilience  

**Key Topics:**  
- Duplicate storage of data to protect against loss  
- Implemented through backups, replication, RAID  
- Balance between cost, performance, and protection
- **Redundant Array of Independent Disks (RAID):** combines multiple physical storage devices into a recognized single logical storage device
	- **RAID 0:** provides data striping across multiple disks to increase performance
		- RAID 0 is for performance without fault tolerance concerns
		- enhances performance by spreading data across multiple drives without fault tolerance
	- **RAID 1:** mirrors data for redundancy across two drives or SSDs; *Mirroring*
		- mirrors data across drives for increased read performance and data integrity
	- **RAID 5:** stripes data with parity, using at least three storage devices
		- spreads data and parity across disks for performance and fault tolerance
	- **RAID 6:** uses data striping across multiple devices with two pieces of parity data
		- enhances RAID 5 by using double parity across multiple drives for better fault tolerance
	- **RAID 10:** combines RAID 1 and RAID 0, featuring mirrored arrays in a striped setup
		- combines RAID 1 and RAID 0 for performance, fault tolerance, and data redundancy
- **Failure-resistant:** use of redundant storage to withstand hardware malfunctions without data loss
	- filure-resistant systems include RAID 1 and RAID 10, using mirroring for data redundancy
- **Fault-tolerant:** use of RAID 1, 5, 6, and 10 for uninterrupted operation during hardware failures
- **Disaster-tolerant:** protects data from catastrophic events
- *RAID combines multiple drives into one recognized by the OS   

---

## Module 14.4: Configuring a RAID  
**Learning Objectives:**  
- Identify RAID levels and their purposes  
- Explain advantages and trade-offs  

**Key Topics:**  
- RAID 0: striping, performance, no redundancy  
	- provides more speed and performance
- RAID 1: mirroring, high redundancy  
	- allows for having two hard disks operating in a mirror
- RAID 5: striping with parity, balance of performance and protection  
- RAID 10: nested, combining mirroring and striping  


---

## Module 14.5: Capacity Planning  
**Learning Objectives:**  
- Explain the importance of capacity planning  
- Recognize factors that influence planning  

**Key Topics:**  
- Ensure resources meet current and future needs  
- Consider growth, peak usage, and failover capacity  
- Includes CPU, memory, storage, bandwidth  
- **Capacity Planning:** crucial strategic planning to meet future demands cost-effectively
	- **People:** involves analyzing current skills and forecasting future needs for hiring or training
		- focus on having the correct number of skilled individuals to meet organizational goals through capacity planning
	- **Technology:** involves assessing current resources, utilization, and anticipating future technological needs
		- evaluate if current technology can accommodate future growth or if additional/new solutions are required for the expected demand
	- **Infrastrucutre:** involves considering physical space and utilities to support organizational operations
	- **Process:** aims to optimize business processes to handle demand fluctuations
		- enhancing workflows, efficiency through automation, and third-party support ensure adaptable processes
- planning for telemedicine services should meet demand, maintain quality, and aid staff and patient transition	

---

## Module 14.6: Powering Data Centers  
**Learning Objectives:**  
- Recognize requirements for reliable power  
- Explain protections against outages  

**Key Topics:**  
- Redundant power supplies, generators, UPS systems  
- Cooling systems to prevent overheating  
- Physical design for resilience  
- **Surge:** a small and unexpected increase in the amount of voltage that is being provided
- **Spike:** a short transient coltage that is usually caused by a shirt circuit, a tripped circuit breaker, a power outage, or a lightning strike
- **Sag:** a small and unexpected decrease in the amount of voltage that is being provided
	- it is common to see sags that drop the voltage from 120 volts to 117 or 115 volts instead
- **Undervoltage Event:** occurs when the coltage is reduced to lower levels and usually occur for a longer period of time
- **Power Loss Event:** occurs when there is a total loss of power for a given period of time
	- with a complete power loss event, it is important to be aware that when power is restored it can also cause a power spike
- **Line Conditioners:** used to overcome any minor fluctuations in the power being recceived by the given system
	- automatically adjust the power signal being received as an undervoltage or overvoltage condition and change it back to the standard power level
- **Uninterruptible Power Supply (UPS):** a device that provides emergency power to a system when the normal input power source has failed
- **Generator:** machine that converts mechanical energy into electrical energy for use in an external circuit through the process of electromagnatic induction
	- portable gas-engine, permanently installed, battery-inverter
- **Power Distribution Center (PDC):** acts as a central hub where power is received and then distributed to all systems in the data center
	- most large data centers will use a rack mounted uninterrupted power supply to provide line conditioning and battery backup
	- the data center should use power distribution units for line conditioning and load balancing from the main utility power source to each server rack

---

## Module 14.7: Data Backups  
**Learning Objectives:**  
- Explain backup strategies  
- Recognize differences in methods and frequency  

**Key Topics:**  
- Types: full, differential, incremental  
- Storage options: onsite, offsite, cloud  
- Backup frequency determined by RPO (Recovery Point Objective)  
- Testing backups critical to ensure usability  
- *Never keep all the data on a single device or server*
- **Data Backup:** the process of creating duplicate copies of digital information to protect against data loss, corruption, or unavailability
	- **Onsite or Offsite Backup:** where the backups of the data are physically being stored
		- it's important to remember that the backed up data might be vulnerable to destruction
	- **Offsite Backup:** the practice of storing duplicate copies of data at a geographically separate location from the primary data source to provide protection against physical disasters and to ensure data continuity
	- **Frequency:** how much data is the company willing to lose?
		- consider the RPO of the organization to confirm that the backup plan preserves the necessary data mount
		- another consideration is how frequently the data will be changed inside of the business
- **Encryption on Backups:** fundamental safeguard that protects the backup data from unauthorized access and potential breaches
	- Data-at-rest Encryption, Data-in-transit Encryption
- **Snapshots:** point-in-time copies of the data that capture a consistent state that is essentially a frozen in time copy of the data
- **Recovery:** used to regain access to the data in the event of a data loss or a system failure
	- selection of the backup, initiating the recovery process, data validation, testing and validation, documentation and reporting, notification
- **Replication:** making real-time, or near-real-time, copies of the data
- **Journaling:** maintaining a meticulous record of every change made to an organization's data over time
- selecting the appropriate data tracking granularity
- managing the journal's size and retention policies
- ensuring its security to prevent any kind of tampering
- data backups are focused on creating a robust, multi-layered strategy to combat any potential data loss

---

## Module 14.8: Continuity of Operations Plan (COOP)  
**Learning Objectives:**  
- Define COOP and its purpose  
- Recognize its key elements  

**Key Topics:**  
- Planning to continue mission-essential functions  
- Includes communications, alternate sites, and succession planning  
- Supports recovery time objectives (RTOs) and RPOs  
- **Continuity of Operations Plan (COOP):**  ensures an organization's ability to recover from disruptive events or disasters
- **Business Continuity Plan (BCP):** addresses responses to disruptive events
	- BCP involves preventative actions and recovery steps for various threats, not limited to technical disruptions
	- switching to backup credit card processors to maintain payment processing during a disruption may become a part of BCP
	- the need for remote work in a business affected by protests, which are beyong technical issues, may be included in BCP
- **Disaster Recovery Plan (DRP):** considered as a subset of BC Plan, it focuses on how to resume operations swiftly after a disaster
	- DRP focuses on how to resume operations after a disaster
	- what can an organization do to continue operations during disasters?
	- DRP may include cloud-based solutions
	- geographic dispersal of staff may also be included in DRP to prepare for natural disasters
- *BCP and DRP differe only in the type of event to respond to:* BCP = Incident ; DRP = Disaster
- senior management takes charge of BCP/DRP development
- a Business Contiuity Coordinator is appointd to lead a Business Continuity Committee
- Business Continuity Committee should include representatives from different departments to address the scope of planning
- BCP/DRP covers everything in the business so the committee must compromise people from across the organization
- define the scope of the BCP/DRP to prevent scope creep, consider the organization's risk appetite and tolerance, structure the BCP/DRP by business function or geographical area

---

## Module 14.9: Redundant Site Considerations  
**Learning Objectives:**  
- Explain different types of redundant sites  
- Recognize trade-offs of each  

**Key Topics:**  
- **Hot site:** fully operational, fastest recovery, highest cost  
- **Warm site:** partially equipped, moderate recovery and cost  
- **Cold site:** basic space, slowest recovery, lowest cost  
- **Redundant Site:** alternative sites for backup in case the primary location encounters a failure or interruption
	- **Hot Site:** a fully equipped backup facility ready to swiftly take over in case of a primary site failure or disruption
		- cloud computing makes hot sites more accessible, however, it does not encompass all of its needs
		- a cloud hot site offers fast data recovery but is better suited for mission-critical functions
	- **Warm Site:** a partially equipped backup site that can become operational within days of a primary site disruption
		- warm sites may provide essentials like power, phone lines, and network connectivity
		- in a hybrid model, critical employees go to a hit site, while the rest relocate to a warm or cold site as part of the DRP
	- **Cold Site:** a site with no immediate equipment or infrastructure but can be transformed into a functional backup facility
- **Mobile Site:** a versatile site that utilizes independent and portable unites like trailers or tents to deliver recovery capabilities
	- the key benefit of a mobile recovery site is its self-sufficiency
	- choosing the appropriate site/sites is a decision for senior managers, considering various business needs and scenarios
	- a full hot site may be use for servers and not for employees
	- microwave link, local cable connection, cellular modem
	- in addition to the four main types of redundant sites, there is a fifth type that has been added recently
- **Virtual Site:** utilizes cloud-based environments and offers highly flexible approach to redundancy
	- **Virtual Hot Site:** fully replicated and instantly accessible
	- **Virtual Warm Site:** prtially replicated and scalable
	- **Virtual Cold Site:** minimal activation to minimize costs
	- *scalability, cost-effectiveness, easy maintenance*
- **Platform Diversity:** a vital aspect in redundant site design that uses different platforms to prevent single points of failure in disaster recovery
	- **Cloud-Provider Platform Diversity:** entails spreading resources across multiple cloud providers or regions, reducing the risk of a single platform outage
	- platform diversity also includes using different systems and infrastructure
- weigh the risks and rewards to determine the best approach for the organization
- when selecting the backup site, consider both the tech stack and the employee workspace support
- continuity of operations is critical to maintaining essential functions and services during disruptions

---

## Module 14.10: Resilience and Recovery Testing  
**Learning Objectives:**  
- Explain the importance of testing resilience measures  
- Recognize testing approaches  

**Key Topics:**  
- Regular testing ensures reliability of backups, failovers, COOP  
- Types: tabletop exercises, simulation, full-scale drills  
- Identifies gaps and validates procedures  
- **Recovery Testing:** evaluates the system's ability to return to regular functioning following to regular functioning following a disruptive incident
	- resilience and recovery testing serves as "fire drill" for enterprise networks and operations
	- **Tabletop Exercise:** a simulated discussion to imrpove crisis readiness without deploying resources
		- tabletop exercises promote team-building and identify gaps in response plans
	- **Failover Test:** verifies seamless system transition to a backup for uninterrupted functionality during disasters
		- plans to shift business operations to an alternative hot site, due to a large-scale disaster, can be verified through failover tests
		- failover tests require more resources, time, and energy but verify planned actions will work
	- **Simulation:** computer-generated representations of real-world scenarios
		- simulations allow responders to perform actions in a virtualized environment
	- **Parallel Processing:** replicates data and processes onto a secondary system running both in parallel
		- parallel processing aims to check the reliability and stability of the secondary setup
- **In resilience testing:** tests ability to handle multiple failure scenarios
- **In recovery testing:** tests efficiency to recover from multiple failure points
- plan for the worst and learn how to overcome any obstacles

---

## Completion Status  
- All Section 14 materials reviewed  
- [Flashcards created for RAID levels, site types, and resilience testing methods](https://jeremyrayjewell.neocities.org/security-plus-dion#deck=14)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
