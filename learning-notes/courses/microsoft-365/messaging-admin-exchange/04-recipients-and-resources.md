# Microsoft 365 Messaging Admin Exchange Online Course w/ SIMS
## by John Christopher  
## Section 4 – Manage recipients and resources

**Date:** 2026-01-09 
[Notes on the Udemy course **Microsoft 365 Messaging Admin Exchange Online Course w/ SIMS** by  **John Christopher**](https://www.udemy.com/course/microsoft-365-messenger-administrator-exchange-course)  
---

## Overview  

Section 4 focuses on **how Exchange Online represents people, roles, and resources as directory-backed objects**, and how those objects are managed, licensed, and delegated. Instead of treating email as a single mailbox-per-user concept, this section shows how Exchange uses **different recipient types** to support collaboration, scheduling, delegation, and external communication without unnecessary licensing or security risk.  
The section explains how **mailboxes are created implicitly through licensing**, how **shared and resource mailboxes** enable role-based and scheduling workflows, and how **contacts, mail users, and groups** extend Exchange beyond the tenant boundary. It also covers **modern versus legacy constructs**, emphasizing Microsoft 365 groups over older distribution models and SharePoint/OneDrive over public folders.  
Overall, Section 4 reframes Exchange administration as **identity- and policy-driven**, where the correct recipient type matters more than simply “creating an email address,” and where clean design decisions directly impact usability, security, and cost.

---

## Module 4.1: Understanding Recipients and Resources
**Learning Objectives:**  
- Understand what recipients and resources are in Exchange Online  
- Identify the different recipient, resource, and group object types  
- Distinguish licensing, functionality, and use cases for each type  

**Key Topics:**  
- Recipients and resources overview:
	- Exchange Online recipients and resources are objects that can receive or relay email  
	- These objects define how email delivery, scheduling, and collaboration operate  
- User mailboxes:
	- Standard individual mailboxes tied to user accounts  
	- Support email, calendar, contacts, and tasks  
	- Require an Exchange license  
- Shared mailboxes:
	- Designed for multiple users (e.g., helpdesk@company.com)  
	- Do not require their own Exchange license  
	- Accessed by licensed user mailboxes  
- Mail contacts:
	- Represent external email addresses inside the GAL  
	- Do not have user accounts or mailboxes in the tenant  
	- Used for partners, vendors, or frequent external contacts  
- Mail-enabled users:
	- Have user accounts without Exchange mailboxes  
	- Email is delivered to an external address  
	- Common for contractors or consultants  
	- Do not require an Exchange license  
- Room mailboxes:
	- Represent physical rooms or meeting spaces  
	- Used for scheduling and availability management  
	- Naming conventions vary by organization  
- Equipment mailboxes:
	- Represent shared equipment (e.g., projectors)  
	- Used for reservation and scheduling  
	- Prevents conflicts over shared resources  
- Distribution groups:
	- Basic email distribution lists  
	- Deliver messages to all members  
	- No calendars, permissions, Teams, or SharePoint integration  
- Mail-enabled security groups:
	- Receive email like distribution groups  
	- Can also be assigned permissions to resources  
	- Do not create Teams or SharePoint sites  
- Dynamic distribution groups:
	- Membership determined by attribute-based rules  
	- Automatically updated as user attributes change  
	- Considered a legacy approach in modern environments  
- Microsoft 365 groups:
	- Modern, recommended group type  
	- Support email, shared calendars, Teams, SharePoint, and Planner  
	- Designed for collaboration and project-based work  
- Mail-enabled public folders:
	- Legacy collaboration feature from early Exchange versions  
	- Still supported but no longer actively developed  
	- Microsoft recommends SharePoint and OneDrive instead  


—

## Module 4.2: Manage User Mailboxes
**Learning Objectives:**  
- Understand how user mailboxes are created in Exchange Online  
- Learn how licensing controls mailbox provisioning  
- Identify common mailbox management options in the Exchange Admin Center  

**Key Topics:**  
- Mailbox creation model:
	- User mailboxes are not created manually in Exchange Online  
	- Mailboxes are automatically provisioned when a user is assigned an Exchange-capable license  
	- This replaces on-premises mailbox creation via EAC or Active Directory  
- Licensing dependency:
	- A valid Exchange Online license is required for every user mailbox  
	- Licenses may be Exchange Online–only or bundled in Microsoft 365 plans  
	- Common options include Exchange Online Plan 1/2, Microsoft 365 Business, E3, and E5  
	- License availability and pricing vary and change over time  
- License assignment behavior:
	- Once a license is assigned, the mailbox is created automatically  
	- Users can immediately access email via Outlook or Outlook on the web  
- Shared mailbox exception:
	- Shared mailboxes can be created directly without licenses  
	- Shared mailboxes rely on licensed users for access  
- Managing existing mailboxes:
	- Exchange Admin Center → Recipients → Mailboxes  
	- Selecting a mailbox exposes configuration tabs  
- General mailbox settings:
	- View and edit contact information  
	- Hide mailbox from the Global Address List if needed  
	- Monitor mailbox storage usage  
- Mailbox permissions and delegation:
	- Send As permissions  
	- Send on Behalf permissions  
	- Full access (read and manage mailbox)  
- Mail flow and delivery controls:
	- Message size restrictions  
	- Email forwarding settings  
	- Message delivery restrictions (allowed/blocked senders)  
- Policy and organization settings:
	- Assign sharing policies and role assignments  
	- Manage mailbox policies (not deeply covered here)  
- Advanced and administrative options:
	- Custom attributes for filtering and dynamic policies  
	- Group membership visibility  
	- Automatic replies (out of office)  
	- Recover deleted items  
	- Convert mailbox to shared mailbox  
	- Litigation hold and archive options  
	- Recipient limits and mail tips  
- Alternative creation methods:
	- Users created via PowerShell also receive mailboxes when licensed  
	- Licensing remains the only required trigger for mailbox creation  

—

## Module 4.3: Manage Resource Mailboxes
**Learning Objectives:**  
- Understand what resource mailboxes are and when they are used  
- Learn how to create and configure room and equipment mailboxes  
- See how users interact with resource mailboxes in Outlook  

**Key Topics:**  
- Purpose of resource mailboxes:
	- Resource mailboxes represent physical or logical resources  
	- Used primarily for scheduling and availability management  
	- Common examples include meeting rooms and shared equipment  
- Types of resource mailboxes:
	- Room mailboxes:
		- Represent conference rooms or meeting spaces  
		- Can include capacity, location, and contact details  
	- Equipment mailboxes:
		- Represent shared equipment (e.g., projectors)  
		- Used to prevent scheduling conflicts for limited resources  
- Creating resource mailboxes:
	- Exchange Admin Center → Recipients → Resources  
	- Choose Add room resource or Add equipment resource  
	- Specify name and email address  
	- Define capacity, location, department, company, and address details  
- Scheduling configuration:
	- Control booking behavior:
		- Allow or restrict recurring meetings  
		- Limit scheduling to work hours  
		- Automatically decline meetings outside booking limits  
	- Define booking window and maximum meeting duration  
	- Configure optional automatic response messages  
- Approval and delegation:
	- Automatically accept or decline meeting requests  
	- Optionally assign delegates to manually approve bookings  
- User experience in Outlook:
	- Users schedule resources directly from the Outlook calendar  
	- Resources appear in the room or resource picker  
	- Availability and capacity are visible during scheduling  
	- Booking places the resource on the calendar automatically  
- Managing existing resource mailboxes:
	- Resource mailboxes expose similar settings to user mailboxes  
	- Manage resource details and contact information  
	- Hide resource from the Global Address List if needed  
	- Review and adjust booking options and delegates  
- Permissions and access:
	- Support Send As and Send on Behalf permissions  
	- Grant full access for administrative management  
- Additional settings:
	- Configure mail tips to guide users during booking  
	- Apply custom attributes for filtering or policy use  
- Administrative takeaway:
	- Resource mailboxes are simple to manage  
	- Consistent behavior across admin and user interfaces  
	- Essential for structured scheduling in Exchange environments  

—

## Module 4.4: Manage Shared Mailboxes
**Learning Objectives:**  
- Understand what shared mailboxes are and when to use them  
- Learn how to create and configure shared mailboxes in Exchange Online  
- Assign permissions and delegate access to shared mailboxes  
- See how users send mail from a shared mailbox  

**Key Topics:**  
- Purpose of shared mailboxes:
	- Used for mailboxes accessed by multiple users  
	- Common examples include Help Desk, Support, or Info addresses  
	- Not tied to a single user identity  
- Licensing behavior:
	- Shared mailboxes do **not** require an Exchange Online license  
	- Users accessing the shared mailbox must have licensed user mailboxes  
- Creating a shared mailbox:
	- Exchange Admin Center → Recipients → Mailboxes  
	- Select Add shared mailbox  
	- Specify name, email address, and alias  
	- Mailbox is created immediately but permissions take time to apply  
- Managing shared mailbox settings:
	- General settings:
		- Contact information  
		- Hide from Global Address List (GAL)  
		- Email app and mobile device access  
	- Email addresses:
		- Shared mailboxes can have multiple email aliases  
	- Organization tab:
		- Department, company, and other organizational attributes  
- Delegation and permissions:
	- Send As:
		- Allows users to send email appearing directly from the shared mailbox  
	- Send on Behalf:
		- Email shows sender acting on behalf of the shared mailbox  
	- Full Access:
		- Allows users to open and manage the mailbox contents  
	- Permission changes may take several minutes to propagate  
- Mail flow controls:
	- Message size restrictions  
	- Email forwarding  
	- Message delivery restrictions  
- Additional configuration:
	- Mail tips for user guidance  
	- Custom attributes for filtering and automation  
- User experience in Outlook on the web:
	- Users enable the From field when composing a message  
	- Shared mailbox can be selected or typed manually  
	- Sent messages appear as coming from the shared mailbox address  
- Administrative takeaway:
	- Shared mailboxes centralize communication  
	- Easy to configure and manage  
	- Widely used for role-based or team-based email workflows  

—

## Module 4.5: Create and Manage Mail Contacts and Mail Users
**Learning Objectives:**  
- Understand the difference between mail contacts and mail users  
- Learn how to create mail contacts in Exchange Online  
- Learn how to create mail-enabled users  
- Understand how external email delivery and visibility work  

**Key Topics:**  
- Mail contacts:
	- Represent external users outside the organization  
	- Do not have a user account in Microsoft 365  
	- Appear in the Global Address List (GAL)  
	- Used for frequently contacted external partners  
	- Email is delivered directly to the external address  
- Creating a mail contact:
	- Exchange Admin Center → Recipients → Contacts  
	- Select Add a mail contact  
	- Specify name, display name, alias, and external email address  
	- Optional contact information can be added  
	- Mail contact appears in the GAL after propagation  
- Mail users (mail-enabled users):
	- Have a user account in Microsoft 365  
	- Do not have an Exchange mailbox  
	- Email is forwarded to an external email address  
	- Commonly used for contractors or consultants  
- Creating a mail user:
	- Exchange Admin Center → Recipients → Contacts  
	- Select Add a mail user  
	- Specify display name, alias, and external email address  
	- Create a Microsoft 365 user account with credentials  
	- No Exchange license is required  
- Directory behavior:
	- Mail contacts do not appear as users in Active Users  
	- Mail users appear as Active Users in Microsoft 365  
	- Mail users can sign in and access assigned resources  
- Email flow:
	- Messages sent to the internal address of a mail user are forwarded externally  
	- No mailbox storage exists in Exchange Online  
- Managing contacts and users:
	- Edit contact information and external addresses  
	- Hide entries from the GAL if needed  
	- Configure mail tips and custom attributes  
- Outlook visibility:
	- Mail contacts and mail users appear in the GAL  
	- Mail contacts appear under Contacts  
	- Mail users appear as directory users  
- Administrative takeaway:
	- Mail contacts are directory-only external references  
	- Mail users bridge identity access with external email delivery  
	- Both simplify collaboration without mailbox licensing  

—

## Module 4.6: Manage Groups, Including Distribution Lists, Microsoft 365 Groups, and More

**Learning Objectives:**  
- Understand the different group types available in Exchange Online  
- Learn when to use Microsoft 365 groups versus legacy group types  
- Create and manage groups through the Exchange Admin Center  
- Understand static versus dynamic group membership  

**Key Topics:**  
- Group management locations:
	- Groups can be created in Microsoft 365 Admin Center or Exchange Admin Center  
	- Exchange Admin Center provides the full set of Exchange-related group options  
	- Recommended path: Exchange Admin Center → Recipients → Groups  
- Microsoft 365 groups:
	- Recommended and default group type  
	- Provide the most functionality and collaboration features  
	- Include:
		- Distribution list functionality  
		- Shared calendar  
		- SharePoint site  
		- Optional Microsoft Teams team  
		- Integration with Planner and other Microsoft 365 services  
	- Can be public or private  
	- Require an owner to manage membership  
- Creating a Microsoft 365 group:
	- Specify group name and description  
	- Assign one or more owners  
	- Add members  
	- Configure email address  
	- Choose public or private visibility  
	- Optionally create an associated Microsoft Teams team  
- Distribution groups (distribution lists):
	- Used solely for email distribution  
	- Do not have a mailbox, calendar, or collaboration tools  
	- Email sent to the group is delivered to all members  
	- Can allow or block external senders  
	- Membership can be open, closed, or owner-approved  
- Mail-enabled security groups:
	- Function like distribution groups for email delivery  
	- Can also be assigned permissions to resources  
	- Commonly used for SharePoint or OneDrive access control  
	- Do not create Teams or SharePoint sites automatically  
- Dynamic distribution groups:
	- Membership is rule-based and evaluated automatically  
	- Updated approximately every 24 hours  
	- Do not allow manual member management  
	- Membership is based on recipient attributes such as:
		- Department  
		- Company  
		- Recipient type  
	- Useful for automatically targeting users by role or attribute  
- Dynamic group behavior:
	- Users are added or removed automatically as attributes change  
	- Requires consistent directory attribute management  
	- Best suited for large or frequently changing organizations  
- Azure AD / Microsoft Entra considerations:
	- Dynamic membership is also supported for Microsoft 365 groups via Microsoft Entra ID  
	- Configuration differs from Exchange dynamic distribution groups  
	- Covered outside the scope of this module  
- Administrative guidance:
	- Microsoft 365 groups are preferred for most use cases  
	- Legacy group types still exist for backward compatibility  
	- Dynamic groups reduce administrative overhead but require careful planning  

—

## Module 4.7: Manage mailbox permissions, including delegation

**Learning Objectives:**  
- Understand the different types of mailbox permissions in Exchange Online  
- Distinguish between Full Access, Send As, and Send on Behalf permissions  
- Learn how mailbox delegation is configured and used in practice  

**Key Topics:**  
- Where mailbox permissions are managed:
	- Microsoft 365 Admin Center → Exchange Admin Center  
	- Recipients → Mailboxes → Select mailbox → Delegation  
	- Applies to user mailboxes and shared mailboxes  
- Full Access permission:
	- Allows a delegate to open and fully manage another mailbox  
	- Delegate can read, send, delete, and manage all mailbox content  
	- Common use case: administrators accessing mailboxes of departed or unavailable users  
	- Does not require password reset  
- Send As permission:
	- Allows a delegate to send email **as** the mailbox owner  
	- Recipient sees the message as coming directly from the mailbox owner  
	- No indication of delegation in the email  
- Send on Behalf permission:
	- Allows a delegate to send email **on behalf of** another mailbox  
	- Email clearly indicates: “Sent by [delegate] on behalf of [mailbox owner]”  
	- Used when transparency about delegation is required  
- User experience in Outlook on the web:
	- Delegate enables the **From** field when composing email  
	- Delegate selects or types the mailbox address  
	- Permissions may take several minutes to propagate  
- Opening another mailbox:
	- Users with Full Access can open delegated mailboxes directly in Outlook  
	- Outlook → Profile menu → Open another mailbox  
- Practical considerations:
	- Permission changes are not instant (propagation delays are normal)  
	- Delegation avoids shared credentials and improves auditability  
	- Choosing between Send As and Send on Behalf is often a policy decision  

—

## Module 4.8: Manage mailbox mail flow settings

**Learning Objectives:**  
- Understand mailbox-level mail flow controls in Exchange Online  
- Configure message size limits, forwarding, and delivery restrictions  
- Distinguish mailbox mail flow settings from transport (Mail Flow) rules  

**Key Topics:**  
- Where mail flow settings are managed:
	- Microsoft 365 Admin Center → Exchange Admin Center  
	- Recipients → Mailboxes → Select mailbox → Mail flow settings  
	- Applies per mailbox (user or shared)  
- Message size restrictions:
	- Set maximum size for messages **sent** and **received** by the mailbox  
	- Enforced at the mailbox level, within Exchange-supported limits  
	- Useful for controlling storage usage and large attachments  
- Email forwarding:
	- Forward all incoming messages to another recipient  
	- Can forward to:
		- Internal mailboxes  
		- External email addresses  
	- Common use cases:
		- Temporary coverage during absence  
		- Redirecting mail for contractors or role-based accounts  
- Message delivery restrictions:
	- Accept messages from:
		- All senders (default)  
		- Only specified senders  
	- Require sender authentication:
		- Blocks unauthenticated (external) senders  
	- Block messages from specific senders:
		- Explicit deny list at the mailbox level  
- Scope clarification:
	- These settings affect **only the selected mailbox**  
	- They are separate from organization-wide **Mail Flow (transport) rules**  
- Practical considerations:
	- Mail flow settings are simple, per-user controls  
	- Useful for targeted restrictions without global impact  
	- Changes may take a short time to propagate  

—

## Module 4.9: Create and manage public folders  
**+ Simulation: Create an HR Department Dynamic Distribution Group**

**Learning Objectives:**  
- Understand what public folders are and their role in Exchange Online  
- Learn how to create and manage public folder mailboxes and folders  
- Recognize Microsoft’s recommended alternatives to public folders  
- Create a dynamic distribution group based on user attributes  

**Key Topics:**  
- Public folders overview:
	- Legacy Exchange feature used to share data and emails within an organization  
	- Designed primarily for smaller organizations and legacy workflows  
	- Microsoft is **deprecating feature development** in favor of SharePoint and OneDrive  
- Public folder architecture:
	- Requires a **Public Folder Mailbox** to store folder data  
	- Individual public folders live under the mailbox  
	- Public folders can be **mail-enabled**, allowing emails to be delivered into them  
- Creating public folders:
	- Exchange Admin Center → Public Folders  
	- Create a public folder mailbox first  
	- Add public folders beneath the mailbox  
	- Optional settings:
		- Mail-enabled / external email access  
		- Storage quotas and retention limits  
		- Hide from GAL  
- Permissions and access:
	- Assign folder permissions (Reviewer, Contributor, Author, Owner, etc.)  
	- Permissions control read/write/delete capabilities  
	- Managed separately from mailbox permissions  
- Client behavior:
	- Public folders may take **up to an hour** to appear in Outlook  
	- Not heavily emphasized or optimized in modern Exchange environments  
- Strategic guidance:
	- Public folders are **legacy** and should not be a design priority  
	- Microsoft recommends **SharePoint and OneDrive** for collaboration and file sharing  

**Assignment: Simulation – Create an HR Department Dynamic Distribution Group**  
- Task:
	- Create a dynamic distribution group for the HR department  
	- Assign *John Christopher* as the group owner  
- Key concepts reinforced:
	- Dynamic membership based on user attributes (e.g., Department = HR)  
	- Automatic membership updates (evaluated periodically)  
	- Difference between static groups and dynamic distribution groups  
- Notes:
	- Membership is not immediate; evaluation can take up to 24 hours  
	- Simulation is browser-based and does not require a live tenant  

---

## KEY TAKEAWAYS

- Exchange Online treats **recipients and resources as distinct object types**, each with specific behaviors, permissions, and licensing rules.
- **User mailboxes are created automatically by license assignment**; admins no longer manually create mailboxes as in on-prem Exchange.
- **Shared mailboxes do not require licenses** and are the preferred solution for team or role-based email addresses.
- **Resource mailboxes (rooms and equipment)** provide structured scheduling and prevent conflicts without manual coordination.
- **Mail contacts** represent external people only, while **mail users** combine internal identity with external email delivery.
- **Microsoft 365 groups are the modern default**, replacing most legacy distribution and collaboration patterns.
- **Dynamic distribution groups** automate membership but rely on consistent directory attributes and legacy evaluation cycles.
- **Mailbox delegation (Full Access, Send As, Send on Behalf)** enables secure access without shared credentials.
- **Mailbox-level mail flow settings** provide targeted controls separate from global transport rules.
- **Public folders are legacy**: still supported, but no longer a strategic solution compared to SharePoint and OneDrive.
- Effective Exchange administration is about **choosing the right object type**, not just enabling email.

---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
