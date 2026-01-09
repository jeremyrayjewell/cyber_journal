# Microsoft 365 Messaging Admin Exchange Online Course w/ SIMS
## by John Christopher  
## Section 3 – Manage organizational and client access settings in Exchange Online

**Date:** 2026-01-09 
[Notes on the Udemy course **Microsoft 365 Messaging Admin Exchange Online Course w/ SIMS** by  **John Christopher**](https://www.udemy.com/course/microsoft-365-messenger-administrator-exchange-course)  
---

## Overview  

Section 3 focuses on **controlling visibility, access, and sharing behavior in Exchange Online**. It moves beyond basic mailbox setup into how organizations **structure address visibility**, **segregate users**, **support offline access**, and **secure collaboration**—both internally and with external partners.

The section explains how Exchange dynamically builds and manages address data through the **Global Address List (GAL)**, how that data can be **filtered and segmented** using **Address Book Policies (ABPs)**, and how users continue working through **Offline Address Books (OABs)** when disconnected. It also covers **external sharing controls** (organization-wide and per-user), **Outlook on the Web (OWA) policies** for browser-based access control, and the **practical realities of managing all of this almost entirely through PowerShell**.

Overall, this section emphasizes **architecture, governance, and access control**, showing how Exchange Online scales from a single directory into a **multi-organization, policy-driven environment** without spinning up separate tenants.

---

## Module 3.1: Understanding the Global Address List (GAL)

**Learning Objectives:**  
- Understand what the Global Address List (GAL) is and its role in Exchange  
- Identify the types of recipient objects included in the GAL  
- Distinguish between the GAL, custom address lists, and offline address books  
- Understand visibility, filtering, and management considerations  

**Key Topics:**  
- Definition and purpose:
	- The Global Address List (GAL) is a **dynamically generated directory** of mail-enabled recipient objects  
	- Includes users, contacts, groups, rooms, and other mail-enabled objects  
	- Used by Outlook, Outlook on the web, and other Exchange clients for address resolution  
- Dynamic nature:
	- The GAL is automatically built and updated by Exchange  
	- New recipients are added automatically; no manual maintenance is required for defaults  
- Types of address lists in Exchange:
	- **Global Address List (GAL):** Default, organization-wide address list  
	- **Custom Address Lists:** Filtered subsets (e.g., Sales, Marketing, partner organizations)  
	- **Offline Address Book (OAB):** Cached version of address lists for offline use  
		- By default, the GAL is included in the OAB  
- Multiple GALs:
	- Most organizations use a single GAL  
	- Multiple GALs are possible in complex or multi-organization scenarios  
	- Users can only see **one GAL**, even if multiple exist  
- Visibility and policies:
	- Users do not see the GAL’s name—only its contents  
	- Access is controlled using **Address Book Policies (ABPs)**  
	- If misconfigured, Exchange may automatically assign the largest GAL  
- Management and administration:
	- GAL creation and modification require **Exchange Online PowerShell**  
	- Limited graphical management options  
	- Unique names are required for multiple GALs  
- Default GAL views:
	- All Users  
	- All Groups  
	- All Contacts  
	- All Rooms  
	- Distribution Lists  
	- Public Folders  
	- Offline Global Address List  
- Filtering and privacy:
	- Certain recipients can be hidden or restricted from general visibility  
	- Used for executives, service accounts, or sensitive roles  
	- Controlled via permissions and address book policies  

---

## Module 3.2: Manage a Global Address List (GAL)

**Learning Objectives:**  
- Understand how the Global Address List is populated in Exchange Online  
- Learn how permissions and roles affect GAL management  
- Create, modify, and manage GALs using Exchange Online PowerShell  

**Key Topics:**  
- How the GAL is populated:
	- Any user with an Exchange-enabled license is automatically added to the GAL  
	- Microsoft 365 groups are mail-enabled by default and appear in the GAL  
	- Groups can be emailed directly, delivering messages to all members  
- Default behavior:
	- All users are assigned the default GAL unless address book policies are applied  
	- GAL contents appear in Outlook and Outlook on the web under People  
- Permissions and roles:
	- Managing GALs requires specific Exchange permissions  
	- An admin role group must include the **Address Lists** role  
	- Only mail-enabled users can be assigned this role  
	- Role changes may take up to ~30 minutes to propagate  
- Exchange Online PowerShell setup:
	- PowerShell is required; no full graphical management exists  
	- Execution policy may need to be set to allow scripts  
	- Install and import the `ExchangeOnlineManagement` module  
	- Connect using `Connect-ExchangeOnline`  
- GAL management via PowerShell:
	- `Get-GlobalAddressList` to view existing GALs  
	- `New-GlobalAddressList` to create a new GAL  
	- `Set-GlobalAddressList` to modify an existing GAL  
	- Commands and syntax are documented in Microsoft Docs  
- Recipient filtering:
	- GAL membership is controlled using **Recipient Filters**  
	- Filters can target properties such as:
		- Recipient type (e.g., UserMailbox)  
		- Department, company, or custom attributes  
	- Supports operators and wildcards (`-like`) for flexible matching  
- Custom attributes:
	- User accounts can be tagged with custom attributes  
	- These attributes are commonly used to separate users across multiple GALs  
- Limitations:
	- GALs cannot be fully managed through the admin UI  
	- PowerShell remains the only supported method  
	- Address Book Policies (ABPs) are required to assign GALs to users (covered later)  

---

## Module 3.3: Understanding Offline Address Books (OABs)

**Learning Objectives:**  
- Understand what an Offline Address Book (OAB) is and why it exists  
- Identify when and how OABs are downloaded and updated  
- Recognize scenarios that trigger full OAB downloads in Outlook  

**Key Topics:**  
- Definition and purpose:
	- Offline Address Books (OABs) are downloadable copies of address lists  
	- Allow users to search recipients and compose emails while offline  
	- Common use case: users without internet access (e.g., airplane travel)  
- User experience:
	- Emails composed offline are queued and sent once connectivity is restored  
	- OAB enables recipient lookup even without a live Exchange connection  
- Administrative control:
	- Admins decide which address lists are available offline  
	- By default, the GAL is associated with the OAB  
- Update behavior:
	- OABs are generated and updated automatically (approximately every 8 hours)  
	- Outlook checks for changes during send/receive operations  
- Manual download:
	- Outlook → File → Account Settings → Download Address Book  
	- Users can download updates or select specific address books  
- Full OAB download triggers:
	- No existing OAB on the client (first-time setup)  
	- Version mismatch between server and client OAB  
	- Missing OAB files on the client  
	- Previous full download failure  
	- Multiple MAPI profiles using Cached Exchange Mode on the same client  
- Supporting concepts:
	- MAPI (Messaging Application Programming Interface) handles Exchange communication  
	- Cached Exchange Mode stores mail and address data locally for offline use  
- Exam and practical focus:
	- Know the acronym **OAB**  
	- Understand its purpose, benefits, and common download conditions  

---

## Module 3.4: Add or Remove an Offline Address Book (OAB)

**Learning Objectives:**  
- Understand how Offline Address Books are managed in Exchange Online  
- Learn how to create and remove OABs using PowerShell  
- Recognize the permissions and tools required for OAB administration  

**Key Topics:**  
- Required permissions:
	- Admin must have the **Address Lists** role assigned  
	- Permissions are configured in Exchange Admin Center → Admin Roles  
	- Same role used for managing Global Address Lists  
- Management method:
	- OABs are managed primarily through **Exchange Online PowerShell**  
	- No full graphical interface exists for OAB creation or removal  
- Creating an OAB:
	- Use the `New-OfflineAddressBook` PowerShell cmdlet  
	- Specify:
		- Name of the OAB  
		- Address lists to include  
	- OAB creation may take a short time to propagate  
- Removing an OAB:
	- Use the `Remove-OfflineAddressBook` cmdlet  
	- Target the OAB by its identity  
	- Removal is immediate after confirmation  
- PowerShell tooling:
	- Requires the `ExchangeOnlineManagement` module  
	- Admin must connect using `Connect-ExchangeOnline`  
	- Available cmdlets include:
		- `Get-OfflineAddressBook`  
		- `New-OfflineAddressBook`  
		- `Set-OfflineAddressBook`  
		- `Remove-OfflineAddressBook`  
- Client-side usage:
	- Users download OABs through Outlook:
		- File → Account Settings → Download Address Book  
	- Outlook must be installed locally to use OABs  
- Customization:
	- OAB parameters (included lists, schedules, etc.) can be modified via PowerShell  
	- Full parameter options are documented in Microsoft Docs  
- Practical emphasis:
	- OAB administration is PowerShell-driven  
	- Understanding cmdlet usage is more important than memorizing syntax  

—

## Module 3.5: Manage Address Book Policies (ABPs)

**Learning Objectives:**  
- Understand the purpose of Address Book Policies in Exchange Online  
- Learn how ABPs control which address lists users can see  
- Create and assign ABPs using Exchange Online PowerShell  

**Key Topics:**  
- Purpose of Address Book Policies (ABPs):
	- ABPs control visibility of address lists, GALs, room lists, and OABs  
	- Used to logically separate users within the same Exchange organization  
	- Common in multi-company or multi-tenant-style scenarios (e.g., Contoso vs. Fabrikam)  
- Management approach:
	- ABPs are created and managed primarily through **Exchange Online PowerShell**  
	- Minimal graphical support exists for creation; PowerShell is required  
- Prerequisites:
	- Existing Global Address Lists (GALs)  
	- Custom Address Lists (user subsets)  
	- Room Lists  
	- Offline Address Books (OABs)  
- Creating ABPs:
	- Use `New-AddressBookPolicy`  
	- Policy defines:
		- Which GAL is visible  
		- Which address lists are available  
		- Which room list is used  
		- Which OAB is associated  
- Example use case:
	- Two companies in one tenant (Contoso and Fabrikam)  
	- Each company has:
		- Its own GAL  
		- Its own address lists  
		- Its own room lists  
		- Its own OAB  
		- Its own ABP  
- Assigning ABPs at scale:
	- Use `Get-Recipient` with filters (e.g., Company attribute)  
	- Pipe results into `Set-Mailbox -AddressBookPolicy`  
	- Allows automatic assignment based on user properties  
- Assigning ABPs individually (GUI option):
	- Exchange Admin Center → Recipients → Mailboxes  
	- Select user → Mailbox settings → Address Book Policy  
	- Only assignment (not creation) is supported graphically  
- Cleanup and removal:
	- ABPs, OABs, GALs, and address lists can be removed using `Remove-*` cmdlets  
	- Useful for lab cleanup or policy redesign  
- Practical considerations:
	- ABPs are powerful but add complexity  
	- Most commonly used in large or segmented organizations  
	- Proper planning of attributes and filters is critical  

—

## Module 3.6: Plan and Configure Organization Relationships and Individual Sharing

**Learning Objectives:**  
- Understand how Exchange Online supports calendar and information sharing with external organizations  
- Differentiate between organization-wide sharing and individual mailbox sharing  
- Configure sharing policies for specific external domains  

**Key Topics:**  
- Purpose of sharing policies:
	- Allow controlled sharing of mailbox information with external domains  
	- Commonly used to support collaboration with partner organizations  
	- Typical use case: sharing calendar free/busy information  
- Types of sharing in Exchange Online:
	- **Organization sharing**:
		- Applies globally to the entire Exchange organization  
		- Allows or restricts sharing with external domains at a high level  
	- **Individual sharing policies**:
		- Applied on a per-mailbox basis  
		- More granular and restrictive than organization-wide sharing  
- Accessing sharing settings:
	- Microsoft 365 Admin Center → Exchange Admin Center  
	- Organization → Sharing  
- Creating an individual sharing policy:
	- Define a policy name (e.g., partner organization name)  
	- Specify allowed external domain(s)  
	- Choose what information can be shared:
		- Free/busy time only  
		- Subject and location  
		- Subject, location, and title  
		- Optional contact folder sharing  
- Assigning sharing policies:
	- Navigate to Recipients → Mailboxes  
	- Select a user mailbox  
	- Mailbox settings → Sharing policy  
	- Assign the appropriate policy to the user  
- Default behavior:
	- Exchange includes a default sharing policy  
	- Default policy may allow broad sharing unless restricted  
- Security and control considerations:
	- Sharing can be tightly limited to specific domains  
	- Policies help prevent unintended information exposure  
	- Different users can have different sharing permissions  
- Practical usage:
	- Useful for B2B collaboration scenarios  
	- Balances usability with security by limiting visibility to trusted partners  

---

## Module 3.7: Configure Outlook on the Web Policies  
**+ Assignment 1: Simulation – Create an Individual Sharing Policy**

**Learning Objectives:**  
- Understand how Outlook on the Web (OWA) policies control user functionality  
- Learn how to create and configure custom OWA mailbox policies  
- Apply OWA policies to individual mailboxes  
- Recognize policy propagation timing considerations  

**Key Topics:**  
- Purpose of Outlook on the Web (OWA) policies:
	- Control which features users can access in Outlook on the Web  
	- Used to restrict or enable functionality for security, compliance, or usability reasons  
- Accessing OWA policies:
	- Microsoft 365 Admin Center → Exchange Admin Center  
	- Roles → Outlook Web App Policies  
- Default vs custom policies:
	- A default OWA policy exists and can be modified  
	- Custom policies can be created for specific user groups or scenarios  
- Creating a custom OWA policy:
	- Define a policy name  
	- Enable or disable features such as:
		- Information management features  
		- Time management features  
		- Password change options  
	- Use built-in tooltips to understand each setting  
- Attachment access controls:
	- Separate rules for public/shared computers vs private computers  
	- Control whether users can open or download attachments  
- Assigning OWA policies:
	- Exchange Admin Center → Recipients → Mailboxes  
	- Select user → Manage email app settings  
	- Assign the desired Outlook Web App mailbox policy  
- Propagation behavior:
	- Policy changes are not immediate  
	- Can take 15–45 minutes to apply across the service  
- Practical usage:
	- Common in environments with shared workstations  
	- Useful for tightening security in browser-based email access  

**Assignment: Simulation – Create an Individual Sharing Policy**  
- Task:
	- Create an individual sharing policy for the Contoso domain  
	- Assign the policy to the user *John Christopher*  
- Goal:
	- Reinforce understanding of sharing policies through guided simulation  
	- Practice assigning policies at the mailbox level  
- Notes:
	- Simulation is browser-based and does not require a live tenant  
	- Assignment completion is optional and not required for course certification  

---


## Module 3.8: DO NOT SKIP – Redoing Simulations in the Course

**Learning Objectives:**  
- Understand how to reaccess completed Udemy simulations  
- Learn the exact steps to reopen assignment instructions and simulation links  

**Key Topics:**  
- Udemy limitation:
	- Once an assignment is completed, Udemy does **not** provide a visible “restart” option  
- Common confusion:
	- Returning to a completed assignment shows a summary screen with no obvious way to relaunch the simulation  
- How to redo a simulation:
	1. Open the completed assignment  
	2. Click **Go to Summary** (lower-left)  
	3. Click **Back to Assignment** (lower-right)  
	4. Click **Instructions** (upper-left)  
	5. Use the simulation link again  
- Key takeaway:
	- The simulation link is always accessible via the **Instructions** view  
	- Simulations can be repeated unlimited times using this method  
- Course-wide relevance:
	- This applies to **all** assignments across the instructor’s courses  
	- Assignment names may differ, but the process is identical  

---

## KEY TAKEAWAYS

- The **Global Address List (GAL)** is a **dynamic, automatically maintained directory** of all mail-enabled objects; admins don’t manually populate it.
- Exchange supports **multiple GALs**, but users can only see **one**, controlled via **Address Book Policies (ABPs)**.
- **PowerShell is mandatory** for managing GALs, OABs, and ABPs—there is no full graphical alternative.
- **Recipient filters and custom attributes** are the foundation for separating users into different address views.
- **Offline Address Books (OABs)** allow users to work without connectivity and are automatically refreshed; admins decide what data is available offline.
- **ABPs are the enforcement layer** that ties together GALs, address lists, room lists, and OABs into a single user-visible experience.
- **Sharing policies** allow controlled calendar and information sharing with external domains, either globally or per mailbox.
- **Outlook on the Web (OWA) policies** restrict browser-based email functionality and attachment access, especially useful in shared or untrusted environments.
- Policy changes often **do not apply immediately**; propagation delays (15–45 minutes) are normal and expected.
- Udemy simulations can always be redone—even after completion—by navigating back through **Summary → Assignment → Instructions**.
- From an admin perspective, **Exchange Online is policy-first**: visibility, access, and collaboration are shaped by configuration—not user choice.


---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  



