# Microsoft 365 Messaging Admin Exchange Online
**Course by John Christopher**

* **Course Link:** https://www.udemy.com/course/microsoft-365-messenger-administrator-exchange-course  
* **Section:** 8 – Manage role-based permissions in Exchange Online 
* **Date:** 2026-01-13  
* **Notes Author:** Jeremy Ray Jewell  

---

## Overview  
Section 8 covers how Exchange Online uses RBAC to control permissions, how PIM adds temporary and controlled elevation, and how Administrative Units scope admin power to specific parts of the organization. Together, these tools enforce least privilege and reduce permanent admin access.

---

## Module 8.1: Plan and manage RBAC roles  
**Learning Objectives:**  
- Understand what Role-Based Access Control (RBAC) is and why Microsoft uses it  
- Distinguish RBAC from other access control models (DAC and MAC)  
- Understand how roles simplify permission visibility and auditing  
- Apply the principle of least privilege when assigning roles  
- Understand how Privileged Identity Management (PIM) enhances RBAC  

**Key Topics:**  
- **Access Control Models:**  
  - **DAC (Discretionary Access Control):**  
    - Based on ownership  
    - Owners decide who gets access  
    - Common in traditional file systems and older Active Directory models  
  - **MAC (Mandatory Access Control):**  
    - Based on classification levels  
    - Common in military and high-security environments  
    - Uses labels like *Secret*, *Top Secret*  
  - **RBAC (Role-Based Access Control):**  
    - Access is granted based on organizational roles  
    - Central model used by Azure and Microsoft 365  
- **Why RBAC Is Better Than Group-Based Security:**  
  - Roles clearly document all permissions they contain  
  - Permissions are stored directly in the role definition (JSON-based, which is JavaScript although the course mistakenly refers to it as Java)  
  - Eliminates “permission sprawl” caused by unmanaged groups  
  - Makes auditing and security reviews far easier  
- **Role Assignment Model:**  
  - Define a role → Assign permissions to the role → Assign identities to the role  
  - Users can have multiple roles  
  - Permissions are cumulative  
  - Enables precise access control  
- **Principle of Least Privilege:**  
  - Always grant the minimum permissions required  
  - Avoid powerful roles like Global Administrator unless absolutely necessary  
  - Exam rule: *Assume least privilege is always the correct choice*  
- **Role Scope:**  
  - Roles apply to:
    - Azure resources  
    - Microsoft 365 services  
  - Different portals manage different role sets:
    - Azure portal  
    - Microsoft 365 admin center  
- **Global Administrator:**  
  - Most powerful role  
  - Full control over Azure and Microsoft 365  
  - Should be tightly restricted  
- **Privileged Identity Management (PIM):**  
  - Adds **Just-In-Time (JIT)** administration  
  - Allows:
    - Temporary role assignments  
    - Scheduled access  
    - Approval-based elevation  
    - Automatic expiration of privileges  
  - Reduces standing administrative risk  
- **Security Impact:**  
  - RBAC + Least Privilege + PIM = modern secure administration model  
  - Prevents excessive access  
  - Limits damage from compromised admin accounts  
  - Enforces clean, auditable privilege boundaries  

---

## Module 8.2: Manage default and custom admin role groups  

**Learning Objectives:**  
- Understand how admin roles are used to control access in Exchange Online  
- Identify key built-in Microsoft 365 and Exchange-specific administrator roles  
- Distinguish between full Exchange administration and limited recipient management  
- Learn how to view role permissions and assigned members  
- Create and manage custom role groups for granular delegation  

**Key Topics:**  

- **Microsoft 365 Global Roles (Portal Roles):**  
  - **Global Administrator:**  
    - Full control over all Microsoft 365 and Azure services  
    - Highest privilege level  
    - Should be tightly restricted  
  - **Billing Administrator:**  
    - Manages subscriptions, licensing, and billing  
  - **Password Administrator:**  
    - Resets user passwords (not full admins)  
  - **Security Administrator:**  
    - Manages security policies, including Exchange-related protections  
  - **Exchange Administrator:**  
    - Full administrative control of Exchange Online only  
    - No control over other Microsoft 365 services  
  - **Exchange Recipient Administrator:**  
    - Manages mailboxes and recipients  
    - Can handle migrations  
    - Limited compared to Exchange Administrator  

- **Exchange Admin Center (EAC) Role Groups:**  
  Located at: `Exchange Admin Center → Roles → Admin roles`
  Key Exchange-specific role groups include:
  - **Organization Management:**  
    - Full administrative control of Exchange Online  
    - Does *not* include discovery permissions  
  - **View-Only Organization Management:**  
    - Read-only version of Organization Management  
  - **Recipient Management:**  
    - Create, modify, and delete mail recipients  
  - **Help Desk:**  
    - Manage user mailbox settings  
    - Reset passwords  
    - Modify user profile information  
  - **Hygiene Management:**  
    - Manage:
      - Anti-spam  
      - Anti-malware  
      - Email filtering policies  
  - **Records Management:**  
    - Manage:
      - Retention policies  
      - Classification rules  
      - Transport rules  
  - **Discovery Management:**  
    - Perform mailbox searches  
    - Access eDiscovery features  
  - **Compliance Management:**  
    - Access Microsoft Purview  
    - Manage compliance and regulatory features  
- **Role Group Inspection:**  
  - Each role group shows:
    - Description  
    - Assigned members  
    - Exact permissions granted  
  - Permissions are fully transparent and auditable  
- **Custom Role Groups:**  
  - Built by copying an existing role group  
  - Allows granular delegation  
  - Example:
    - Create **Help Desk Tier 2** from Help Desk  
    - Add extra permissions:
      - Transport rules  
      - Mailbox searches  
      - Audit logs  
      - Mail tips  
  - Workflow: `Select role → Copy role group → Customize permissions → Assign members`
- **Why Custom Roles Matter:**  
- Prevent over-permissioning  
- Enforce least privilege  
- Match real organizational job functions  
- Improve security posture  
- **Big Picture:**  
- Microsoft 365 provides:
  - High-level tenant-wide roles  
  - Exchange-specific admin roles  
  - Fully customizable role groups  
- Together, they form a precise RBAC model for Exchange administration  

---

## Module 8.3: Using PowerShell to search for RBAC information  
**Learning Objectives:**  
- Understand how PowerShell can be used to query Exchange RBAC roles  
- List and search existing role groups  
- Identify which roles grant specific permissions  
- Determine who is assigned to a given role group  
- Recognize PowerShell as a faster auditing tool than the GUI  

**Key Topics:**  
- **Connecting to Exchange Online with PowerShell:**  
  - Uses the Exchange Online Management module  
  - Command example:  
    Connect-ExchangeOnline  
  - Authenticates and connects to the tenant  
- **Viewing All Role Groups:**  
  - Command:  
    Get-RoleGroup  
  - Lists all built-in and custom role groups  
  - Confirms groups such as:  
    - Organization Management  
    - Recipient Management  
    - Custom groups (e.g., Help Desk Tier 2)  
- **Finding a Specific Role Group:**  
  - Command:  
    Get-RoleGroup "Recipient Management"  
  - Quickly validates that a role exists  
- **Finding Which Roles Grant a Specific Permission:**  
  - Command:  
    Get-ManagementRoleEntry "*\New-Mailbox"  
  - Shows all roles that include the New-Mailbox permission  
  - Answers questions like:  
    - “Which roles can create mailboxes?”  
- **Filtering Output for Readability:**  
  - Command:  
    Get-ManagementRoleEntry "*\New-Mailbox" | Format-List Name,Role,Parameters  
  - Displays only the most relevant permission fields  
- **Finding Members of a Role Group:**  
  - Command:  
    Get-RoleGroupMember -Identity "Organization Management"  
  - Shows which users or groups are assigned  
  - Used to audit privileged access  
- **Searching for Role-Related Commands:**  
  - Commands:  
    Get-Command *Role*  
    Get-Command *RoleGroup*  
  - Lists all RBAC-related PowerShell commands  
- **Creating Role Groups with PowerShell:**  
  - Command:  
    New-RoleGroup  
  - Used for:  
    - Automating RBAC setup  
    - Large-scale tenant administration  
- **Why PowerShell Matters for RBAC:**  
  - Faster and more complete than the GUI  
  - Essential for:  
    - Security reviews  
    - Privilege discovery  
    - Compliance documentation  
  - Makes RBAC transparent and searchable  
- **Big Idea:**  
  - PowerShell is the authoritative method to:  
    - Discover permissions  
    - Audit roles  
    - Validate least-privilege design  
    - Manage RBAC at scale  

---

## Module 8.4: Understanding the use of Privileged Identity Management (PIM) with RBAC  
**Learning Objectives:**  
- Understand what Privileged Identity Management (PIM) is and why it is used  
- Explain how PIM extends RBAC with time-based and controlled access  
- Identify licensing requirements for PIM  
- Understand Just-In-Time (JIT) administration  
- Recognize PIM security controls such as MFA, approval, and auditing  
- Understand key PIM terminology (eligible, active, assigned, permanent, expiring)  

**Key Topics:**  
- **What PIM Is:**  
  - PIM = Privileged Identity Management  
  - Advanced security layer on top of RBAC  
  - Controls *when*, *how*, and *for how long* admin roles are used  
  - Used across:
    - Azure (IaaS)  
    - Microsoft services (PaaS / SaaS, including Microsoft 365)  
- **Just-In-Time (JIT) Administration:**  
  - Users do not have permanent admin power  
  - They request and activate roles only when needed  
  - Access automatically expires after a set time  
  - Prevents forgotten or lingering admin privileges  
- **Common PIM Use Case:**  
  - Temporarily grant admin rights when:
    - An admin is on vacation  
    - A task requires elevated permissions  
  - Role automatically removed after expiration  
- **Licensing Requirement:**  
  - Requires **Azure AD Premium P2**  
  - Not available in:
    - Azure AD Free  
    - Azure AD Premium P1  
- **Core PIM Security Controls:**  
  - Time-bound access  
  - Approval workflows  
  - MFA enforcement during activation  
  - Mandatory justification  
  - Notification when roles are activated  
  - Full audit history of role usage  
  - Periodic access reviews  
- **Who Can Manage PIM:**  
  - Global Administrator  
  - Privileged Role Administrator  
  - Others can be delegated limited PIM management rights  
- **PIM Terminology:**  
  - **Eligible:**  
    - User can activate the role but must request it  
  - **Active:**  
    - Role is currently enabled and usable  
  - **Assigned:**  
    - The role exists for the user (either active or eligible)  
  - **Permanent Eligible:**  
    - User can always request activation  
  - **Permanent Active:**  
    - User always has the role (traditional model)  
  - **Expire Eligible:**  
    - Role is eligible only within a time window  
  - **Expire Active:**  
    - Role is active but will automatically expire  
  - **JIT Access:**  
    - Temporary, controlled, auditable elevation  
- **Principle of Least Privilege:**  
  - Always grant the minimum permissions needed  
  - Never assign Global Administrator unless required  
  - PIM enforces least privilege by design  
- **Big Idea:**  
  - PIM turns static admin accounts into:
    - Temporary  
    - Audited  
    - Approved  
    - Secure privilege sessions  
  - It is one of the strongest controls Microsoft provides for protecting administrative access  

---

## Module 8.5: Using PIM to manage role-based access control in Azure  
**Learning Objectives:**  
- Navigate to Privileged Identity Management (PIM) in the Azure portal  
- Understand the PIM interface and role views  
- Assign role eligibility to users  
- Configure activation settings and security controls  
- Activate roles as an end user  
- Verify role-based permissions after activation  

**Key Topics:**  
- **Accessing PIM:**  
  - Portal: https://portal.azure.com  
  - Search: *Privileged Identity Management*  
  - Can be starred for quick access  
  - Central location for managing time-based admin access  
- **PIM Interface Sections:**  
  - **My Roles:**  
    - Shows roles assigned to *your* account  
    - Split into:
      - Eligible roles  
      - Active roles  
      - Expired roles  
  - **My Requests:**  
    - Shows roles you requested  
  - **Approve Requests:**  
    - Used when approval workflows are enabled  
  - **Review Access:**  
    - Used for periodic access reviews  
- **Azure AD Roles Section:**  
  - Used to manage role assignments for all users  
  - Options:
    - Assign eligibility  
    - Activate roles  
    - Approve requests  
    - View audit history  
- **Role Assignment Methods:**  
  - Method 1:
    - Azure AD Roles → Roles → Select role → Add assignment  
  - Method 2:
    - Azure AD Roles → Assignments → Add assignment → Select role  
  - Both produce the same result  
- **Role Settings Configuration:**  
  - Maximum activation duration (e.g., 8 hours)  
  - Require:
    - MFA  
    - Justification  
    - Ticket number (optional)  
    - Approval  
  - Allow or deny:
    - Permanent active roles  
    - Permanent eligibility  
  - Role behavior is customizable per role  
- **Assigning Eligibility (Admin Side):**  
  - Select role (e.g., User Administrator)  
  - Select user (e.g., Chris Jones)  
  - Choose:
    - Permanent eligibility, or  
    - Time-limited eligibility with expiration date  
  - User becomes *eligible*, not active yet  
- **User Activation Flow (End User):**  
  1. Log in to Azure portal  
  2. Open Privileged Identity Management  
  3. Go to **My Roles**  
  4. Select eligible role  
  5. Click **Activate**  
  6. Complete MFA  
  7. Provide justification  
  8. Role becomes active  
- **Role State Verification:**  
  - Eligible role → Active role after activation  
  - Active role grants actual permissions  
  - Example:
    - Without activation → Cannot create users  
    - After activation → Can create users  
- **Expiration Behavior:**  
  - Role automatically deactivates after set time  
  - No need for admin to manually remove access  
  - Prevents privilege creep  
- **Audit and History:**  
  - All activations are logged  
  - Includes:
    - Who activated  
    - When  
    - Duration  
    - Justification  
    - MFA usage  
- **Big Idea:**  
  - PIM converts static admin roles into:
    - Temporary  
    - Audited  
    - Secure  
    - Purpose-driven privilege sessions  
  - It enforces:
    - Least privilege  
    - Time-bound control  
    - Zero-trust administration  

---

## Module 8.6: Activating a PIM role as a user  
**Learning Objectives:**  
- Understand what it means to be *eligible* vs *active* in PIM  
- Learn how a user activates an assigned PIM role  
- Recognize the security controls involved in role activation  
- Verify that permissions only work after activation  
- Understand how PIM enforces time-limited administrative access  

**Key Topics:**  
- **Initial State (Before Activation):**  
  - User logs in as Chris Jones  
  - Attempts to perform admin task (create a user)  
  - Action fails because role is only *eligible*, not active  
  - Confirms that eligibility alone grants no permissions  
- **Finding PIM as a User:**  
  - Azure Portal → All Services → Privileged Identity Management  
  - Go to **My Roles**  
  - Shows:
    - Eligible roles  
    - Active roles  
    - Expiration dates  
- **Role Eligibility:**  
  - Chris Jones is eligible for:
    - **User Administrator**  
  - Role has:
    - Expiration date  
    - Max activation time (8 hours)  
- **Role Activation Process:**  
  1. Select eligible role  
  2. Click **Activate**  
  3. Choose activation duration (up to 8 hours)  
  4. Complete MFA verification  
  5. Enter justification:
     - Example: *Needed to create new employee user accounts*  
  6. Click **Activate**  
- **Security Controls Enforced:**  
  - Multi-factor authentication  
  - Justification required  
  - Time-limited activation  
  - Audit logging  
- **After Activation:**  
  - Role moves from:
    - **Eligible** → **Active**  
  - User now has real permissions  
  - Admin tasks succeed  
- **Verification of Access:**  
  - Go to:
    - Azure AD → Users  
  - Create new user successfully  
  - Confirms:
    - PIM role is active  
    - Permissions are working  
- **Role State Clarity:**  
  - Eligible ≠ Active  
  - Only *Active* roles grant power  
  - “Active roles” view confirms real access  
- **Automatic Deactivation:**  
  - Role expires after:
    - Selected activation time  
  - Access is removed automatically  
  - Prevents forgotten admin privileges  
- **Big Idea:**  
  - PIM ensures:
    - Admin power is temporary  
    - Justified  
    - Audited  
    - Secure  
  - Users only have high privilege *when they actively request and prove they need it*  

---

## Module 8.7: Using administrative units to help with controlling access  
**Learning Objectives:**  
- Understand what Administrative Units (AUs) are and why they exist  
- Compare Administrative Units to on-prem Active Directory OUs  
- Learn how Administrative Units enable scoped delegation of admin roles  
- Understand licensing requirements for Administrative Units  
- Recognize how Administrative Units support least-privilege administration  

**Key Topics:**  
- **What Administrative Units Are:**  
  - A way to group users and resources in Azure AD  
  - Used to delegate admin permissions over *only part* of the directory  
  - Cloud equivalent of on-premises Organizational Units (OUs)  
  - Managed in:
    - Azure Portal → Azure Active Directory → Administrative Units  
- **Purpose:**  
  - Limit administrative scope  
  - Prevent admins from having tenant-wide control  
  - Apply RBAC roles only to specific sets of users  
- **Common Use Cases:**  
  - Geographic separation
  - Departmental separation
  - Organizational segmentation
- **Licensing Requirement:**  
  - Requires **Azure AD Premium P1 or higher**  
  - Without P1:
    - Administrative Units can be created  
    - But cannot contain members (functionally useless)  
- **Creating Administrative Units:**  
  1. Azure Portal → Azure Active Directory  
  2. Administrative Units → Add  
  3. Name unit (e.g., NYC, ATL)  
  4. Create unit  
  5. Add users to unit  
- **Assigning Users:**  
  - Users can be added to one or more Administrative Units  
  - Example:
    - Bob Jones → NYC  
    - Larry Thomas → ATL  
- **Delegating Admin Roles:**  
  - Roles (like **User Administrator**) can be scoped to an Administrative Unit  
  - Admin can manage only users in their assigned unit  
  - Example:
    - NYC Admin → manages only NYC users  
    - ATL Admin → manages only ATL users  
- **Difference from On-Prem OUs:**  
  | Feature | OUs (On-Prem AD) | Administrative Units (Azure AD) |
  |------|----------------|------------------------------|
  | User membership | Only one OU | Can belong to multiple AUs |
  | Delegation | Folder-style hierarchy | Role-based delegation |
  | Scope | Physical AD structure | Logical grouping |
  | Cloud support | No | Yes |
- **Multiple Membership:**  
  - A user *can* belong to multiple Administrative Units  
  - Useful for:
    - Cross-department roles  
    - Shared responsibilities  
- **Security Value:**  
  - Supports:
    - Least privilege  
    - Reduced blast radius  
    - Clear administrative boundaries  
  - Prevents giving broad roles like Global Admin unnecessarily  
- **Big Idea:**  
  - Administrative Units let you say:  
    > “You are an admin — but only for *this* part of the organization.”  
  - They provide precise, scalable, and secure delegation of authority in Azure AD  

---

## Module 8.8: Manage user roles + Assignment 5: SIMULATION – Create a role that gives "Address List" admin rights to JC and Tom
**Learning Objectives:**  
- Understand what user roles (role assignment policies) are in Exchange Online  
- Distinguish user roles from admin roles  
- Learn how to create custom user role policies  
- Know how to assign user role policies using PowerShell  
- Grant limited, task-specific permissions without making users full admins  

**Key Topics:**  
- **What User Roles Are:**  
  - User roles allow *end users* to perform specific mailbox and profile tasks  
  - They are not full administrators  
  - Managed in:
    - Exchange Admin Center → Roles → User roles  
  - Based on **Role Assignment Policies**  
- **Default Role Assignment Policy:**  
  - Applied to all users by default  
  - Allows:
    - Outlook on the web options  
    - Profile management  
    - Mailbox configuration  
  - Does *not* allow mailbox delegation by default  
- **Why Create Custom User Roles:**  
  - To give limited administrative capabilities without full admin access  
  - Example uses:
    - Managers managing delegation  
    - Users managing address list settings  
    - HR managing contact information  
- **Creating a Custom User Role Policy (GUI):**  
  1. Exchange Admin Center → Roles → User roles  
  2. Create new role assignment policy  
  3. Name it (e.g., **Address List Admins**)  
  4. Enable:
     - **Address List** role  
  5. Save policy  
- **Assigning the Role Policy (PowerShell Required):**  
  GUI cannot assign role policies to users. PowerShell must be used.
  Connect to Exchange:
  ```powershell
  Connect-ExchangeOnline

### Assignment: SIMULATION  
Create a role that gives **“Address List”** admin rights to **JC** and **Tom Williamson**.
1. Exchange Admin Center → Roles → User roles  
2. Create new Role Assignment Policy:  
   - Name: Address List Admins  
   - Enable: Address Lists  
3. PowerShell:
Set-Mailbox -Identity JC -RoleAssignmentPolicy "Address List Admins"  
Set-Mailbox -Identity Tom.Williamson -RoleAssignmentPolicy "Address List Admins"

---

## KEY TAKEAWAYS
- RBAC defines all permissions through clear, auditable roles  
- Least privilege is always the correct design choice  
- PIM adds temporary, MFA-protected, and audited admin access  
- Eligible ≠ Active in PIM (only Active grants power)  
- Administrative Units limit *where* an admin has control  
- User roles give limited powers without creating admins  

---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
