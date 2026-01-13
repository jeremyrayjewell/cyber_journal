# Microsoft 365 Messaging Admin Exchange Online
**Course by John Christopher**

* **Course Link:** https://www.udemy.com/course/microsoft-365-messenger-administrator-exchange-course  
* **Section:** 5 – Manage Exchange hybrid settings and migration  
* **Date:** 2026-01-11  
* **Notes Author:** Jeremy Ray Jewell  

---

## Overview  

Section 5 explains how hybrid Exchange enables mailbox migrations and coexistence between on-premises Exchange and Exchange Online, focusing on synchronization, endpoints, and selecting the right migration type.

---

## Module 5.1: Concepts of virtual directories and URLs for Hybrid Exchange configuration
**Learning Objectives:**  
- Understand the core components involved in an Exchange hybrid migration (on-prem AD DS, DNS, on-prem Exchange, Microsoft 365, and Entra ID)  
- Explain what IIS virtual directories are in on-prem Exchange and why their URL configuration matters in hybrid  
- Understand why Exchange-related sync (metadata) must be enabled in Microsoft Entra ID Connect for hybrid scenarios  
- Distinguish common migration approaches (cutover vs staged vs long-term hybrid coexistence) at a conceptual level  
- Understand, at a high level, what an Exchange migration endpoint is and why Exchange Online needs it  

**Key Topics:**  
- Hybrid baseline architecture (conceptual):
	- On-prem AD DS domain (users/groups controlled on-prem)
	- Internal DNS (internal name resolution)
	- Internet-facing DNS (public records for the domain, can be hosted anywhere)
	- On-prem Exchange Server (version varies; older versions possible)
	- Microsoft Entra ID (formerly Azure AD) as the cloud identity directory
- Microsoft Entra ID Connect (formerly Azure AD Connect):
	- Syncs on-prem identities to the cloud (one-way: on-prem → cloud)
	- Must be configured to sync Exchange-related attributes/settings (Exchange “metadata”)
	- If not enabled initially, you can rerun/reinstall and enable Exchange sync
- IIS virtual directories and URLs (on-prem Exchange):
	- Exchange on-prem uses IIS to publish Exchange web services
	- IIS creates virtual directories that contain Exchange service configuration and URL info
	- These URLs/virtual directory settings are part of the metadata Exchange Online must know for hybrid
- Why the URL/virtual directory metadata matters in hybrid:
	- Exchange Online needs correct service endpoints and naming/auth details to communicate with on-prem Exchange
	- Missing metadata makes hybrid migration/coexistence difficult because Exchange Online cannot “discover” on-prem configuration
- Migration strategy context:
	- Cutover migration: move all mailboxes at once
	- Staged migration: move mailboxes in phases (e.g., 500 now, 500 later)
	- Long-term hybrid coexistence: keep some users on-prem while others are in Exchange Online for months/years
	- The longer coexistence lasts, the more critical accurate hybrid metadata/endpoints become
- Endpoints (conceptual):
	- In the cloud, “endpoints” represent how Exchange Online authenticates to and connects with the on-prem Exchange environment
	- Endpoints depend on the on-prem virtual directory/URL configuration being known and correct

---

## Module 5.2: Hybrid Migrations using the Exchange Admin Center in Exchange Online
**Learning Objectives:**  
- Understand where and how hybrid migrations are initiated in Exchange Online  
- Identify the Migration blade and Migration Batches feature in the Exchange Admin Center  
- Recognize the available migration types selectable in the wizard  
- Understand the difference between the modern EAC migration workflow and the older Hybrid Configuration Wizard  
- Know that most required knowledge is conceptual rather than hands-on for this course  

**Key Topics:**  
- Migration entry point:
	- admin.microsoft.com → Show All → Exchange  
	- Exchange Admin Center → Migration  
	- Migration Batches is the primary interface for migrations  
- Modern migration workflow:
	- Uses a graphical wizard built directly into Exchange Online  
	- Replaces the older downloadable Hybrid Configuration Wizard for most scenarios  
	- Provides a centralized interface for all supported migration types  
- Creating a migration batch:
	- Click **Add migration batch**  
	- Assign a batch name  
	- Choose migration direction:
		- Migrate **to** Exchange Online  
		- Migrate **from** Exchange Online  
- Migration types available:
	- Remote move migration  
	- Staged migration (retired since course was made)
	- Cutover migration  
	- Cross-tenant migration  
	- Google Workspace migration  
	- IMAP migration  
- Migration wizard behavior:
	- Each migration type has:
		- Prerequisites  
		- Required authentication configuration  
		- Specific setup constraints  
	- The wizard enforces correct configuration order  
	- Microsoft Learn documentation provides detailed setup steps  
- Conceptual emphasis:
	- The course focuses on:
		- Understanding which migration type to choose  
		- Knowing where migrations are configured  
		- Recognizing terminology and workflow  
	- Hands-on hybrid environments are not required for mastery  
- Comparison to older method:
	- Older approach: Hybrid Configuration Wizard (downloadable tool)  
	- Newer approach: Built-in Migration blade in Exchange Online  
	- The built-in wizard is now the preferred and primary method  
- Administrative takeaway:
	- All Exchange hybrid migrations begin in the Exchange Admin Center  
	- Migration Batches represent the operational unit of mailbox movement  
	- Choosing the correct migration type is the most important decision point  

---

## Module 5.3: Exchange Hybrid Migration Types including cross-tenant migration batch  
**Learning Objectives:**  
- Understand all Exchange Online hybrid migration types and when to use each  
- Distinguish between legacy and modern migration approaches  
- Know which migration type applies based on mailbox count and Exchange version  
- Understand how endpoints enable authentication between environments  
- Recognize when cross-tenant and IMAP migrations are required  
- Memorize the functional limitations of IMAP migrations  

**Key Topics:**  
- Overview of migration types:
	- Exchange Online supports **six** hybrid migration types:
		- Remote move migration  
		- Staged migration  
		- Cutover migration  
		- Google Workspace migration  
		- Cross-tenant migration  
		- IMAP migration  
- Remote move migration:
	- Used to move mailboxes from **on-prem Exchange to Exchange Online**
	- Uses:
		- Migration endpoints  
		- Migration batches  
	- Endpoint:
		- Stores authentication data between on-prem Exchange and Microsoft 365  
		- Allows the two systems to communicate securely  
	- Moves **existing mailboxes directly**
	- Does not require creating new mailboxes before importing data  
	- Fastest and cleanest migration method  
	- Requires modern Exchange versions (e.g., Exchange 2016/2019)  
- Staged migration (since retired):
	- Used when migrating mailboxes gradually over time  
	- Recommended for:
		- Exchange 2003  
		- Exchange 2007  
		- Environments with **more than 2000 mailboxes**  
	- Microsoft’s modern migration model assumes:
		- Exchange 2010+ on-prem
		- Hybrid configuration
		- Remote Move migrations
	- Remote Move completely replaces what staged migration used to do, but better:
		- It moves existing mailboxes directly
		- It supports true hybrid coexistence
		- It allows partial migrations
		- It keeps identities intact
		- It is more reliable and more secure
- Cutover migration:
	- Moves **all mailboxes at once**
	- Recommended when:
		- Mailbox count is **2000 or fewer**
		- Exchange Server version is 2003 or later  
	- Simple and fast but disruptive  
	- Entire organization transitions simultaneously  
- Relationship between remote move and cutover:
	- Remote move is the **newer and preferred method**
	- Cutover is mainly for **older Exchange versions**
	- Remote move allows direct mailbox movement without recreation  
- Google Workspace migration:
	- Used to migrate mailboxes from **Google Workspace (Gmail)**  
	- Requires:
		- Intra ID Connect (formerly Azure AD Connect)  
	- Allows:
		- Pre-provisioning users before migration  
		- Selecting exactly which users to migrate  
	- Used when organizations move from Google ecosystem to Microsoft 365  
- Cross-tenant migration:
	- Migrates mailboxes from **one Microsoft 365 tenant to another**
	- Common use case:
		- Mergers and acquisitions  
		- Tenant consolidation  
	- Requires:
		- Intra ID services (formerly Azure AD)  
		- Azure Key Vault in target tenant  
		- Organizational relationship between tenants  
		- Migration endpoint with authentication credentials  
	- Azure Key Vault:
		- Stores credentials, certificates, and encryption keys  
		- Secured using Hardware Security Modules (HSMs)  
	- Enables secure trust between tenants during mailbox transfer  
- Migration endpoints:
	- Required for:
		- Remote move migration  
		- Cross-tenant migration  
	- Store:
		- Authentication credentials  
		- Communication metadata between environments  
- IMAP migration:
	- Used for:
		- Legacy mail systems  
		- Third-party providers (e.g., GoDaddy, generic IMAP servers)  
		- Very old Exchange versions (Exchange 5.5, Exchange 2000)  
	- Migrates:
		- Email messages only  
	- Does **not migrate**:
		- Contacts  
		- Calendar items  
		- Tasks  
	- Most important limitation to remember  
- Administrative emphasis:
	- Choosing the correct migration type is critical  
	- Migration type depends on:
		- Exchange version  
		- Mailbox count  
		- Source platform  
		- Tenant architecture  
	- This module contains the **most test-relevant facts** in the migration section  

---

## Module 5.4: Maintain and expand the configuration by using the Hybrid Configuration Wizard  
**Learning Objectives:**  
- Understand the difference between the modern migration workflow and the legacy Hybrid Configuration Wizard  
- Know when and why the Hybrid Configuration Wizard is still used  
- Understand what the wizard configures automatically in a hybrid environment  
- Recognize PowerShell version requirements for hybrid configuration  
- Identify which migration options are supported by the wizard and which are not  

**Key Topics:**  
- Two approaches to Exchange hybrid migration:
	- Modern method:
		- Portal: portal.microsoft.com  
		- Show all → Exchange Admin Center  
		- Use the **Migration** blade  
		- Create migration batches  
		- Select migration direction and migration type  
		- Preferred and current Microsoft approach  
	- Legacy method:
		- Uses the **Exchange Hybrid Configuration Wizard (HCW)**  
		- Downloadable standalone tool  
		- Still functional but considered older workflow  
- Hybrid Configuration Wizard overview:
	- Long-standing Microsoft tool for hybrid deployments  
	- Automatically:
		- Verifies prerequisites  
		- Detects Exchange on-prem environment  
		- Configures hybrid connectivity  
		- Enables hybrid features by default  
	- Hybrid features include:
		- Free/busy sharing  
		- Mail flow configuration  
		- Authentication trust  
		- Mail tips integration  
	- These features can be disabled if only mailbox migration is desired  
- PowerShell requirements:
	- Wizard executes PowerShell commands in the background  
	- Requires **Windows PowerShell 5.5**  
	- PowerShell 7 is **not supported** for this process  
	- Most Windows systems already include PowerShell 5.x  
- Installation and execution:
	- Download from Microsoft using:
		- “Download Exchange Hybrid Configuration Wizard”  
	- Install on an **on-prem Exchange server**  
	- Launch the wizard:
		- Click Next  
		- Choose automatic Exchange server detection or specify one manually  
		- Select Exchange version (e.g., 2010, 2013)  
		- Choose Microsoft 365 organization region  
		- Sign in with Microsoft 365 admin credentials  
		- Wizard attempts to connect on-prem Exchange to Exchange Online  
- Exchange version expectations:
	- Wizard references older Exchange versions:
		- Exchange 2010  
		- Exchange 2013  
	- Reflects its legacy design and original purpose  
- Migration capabilities supported:
	- Cutover migration  
	- Staged migration  
	- IMAP migration  
- Migration capabilities **not supported**:
	- Remote move migration  
	- Cross-tenant migration  
- Comparison summary:
	- Exchange Admin Center:
		- Newer  
		- Supports all modern migration types  
		- Includes cross-tenant and remote move migrations  
	- Hybrid Configuration Wizard:
		- Older  
		- Still functional  
		- Limited migration options  
		- Primarily used for legacy or traditional hybrid deployments  
- Administrative takeaway:
	- The Hybrid Configuration Wizard is a legacy but still useful tool  
	- Exchange Admin Center migration blade is the preferred modern solution  
	- Understanding both helps when working with older Exchange environments  
	- Hybrid administration requires awareness of tooling evolution  

---

## KEY TAKEAWAYS

- Hybrid Exchange depends on syncing **identity and Exchange metadata** to Microsoft 365 using Intra ID Connect.
- Virtual directories in IIS store URL and authentication data that Exchange Online must see for hybrid to work.
- Migrations are now started from the **Exchange Admin Center migration blade**, not mainly the old wizard.
- Different migration types exist for different scenarios (remote move, staged, cutover, cross-tenant, IMAP, Google).
- Cross-tenant migrations require **Intra ID + Azure Key Vault + migration endpoints**.
- IMAP migrations move **email only** (no calendar, contacts, or tasks).
- The Hybrid Configuration Wizard is **legacy** and supports fewer options.
- Hybrid migration is about choosing the **right method**, not just moving mail.

---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
