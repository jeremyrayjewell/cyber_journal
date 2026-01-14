# Microsoft 365 Messaging Admin Exchange Online
**Course by John Christopher**

* **Course Link:** https://www.udemy.com/course/microsoft-365-messenger-administrator-exchange-course  
* **Section:** 10 – Manage compliance
* **Date:** 2026-01-14  
* **Notes Author:** Jeremy Ray Jewell  

---

## Overview  
Section 10 focuses on compliance operations in Microsoft 365. It shows how retention, auditing, investigations, and legal preservation are all managed through **Microsoft Purview**, turning Exchange into part of a broader compliance and evidence system rather than just an email platform.

---

## Module 10.1: Configure Messaging Records Management (MRM) retention for a specific mailbox  
**Learning Objectives:**  
- Understand what MRM (Messaging Records Management) is  
- Know where MRM is now managed (Microsoft Purview)  
- Understand the difference between MRM and modern Microsoft 365 retention policies  
- Create and configure MRM retention tags  
- Create and apply MRM retention policies to mailboxes  
- Assign MRM policies to individual or multiple users  

**Key Topics:**  
- **What MRM Is:**  
  - Legacy Exchange retention system  
  - Controls how long emails are kept, archived, or deleted  
  - Works through:
    - Retention **tags**
    - Retention **policies**
- **Where MRM Lives Now:**  
  - `admin.microsoft.com → Compliance → Microsoft Purview`  
  - Under **Data lifecycle management**  
  - Two options shown:
    - **Microsoft 365** (modern method, recommended)
    - **Exchange (Legacy)** (MRM, limited use cases)
- **Microsoft’s Recommendation:**  
  - Use **Microsoft 365 retention policies and labels** for:
    - Exchange  
    - SharePoint  
    - OneDrive  
    - Microsoft 365 Groups  
  - Use **MRM only** for:
    - Moving items from primary mailbox → archive mailbox  
    - Applying retention to default Exchange folders  
- **MRM Retention Tags:**  
  - Define what happens to messages:
    - Delete after X time  
    - Move to archive after X time  
  - Can apply to:
    - Entire mailbox  
    - Default folders (Inbox, Sent Items, etc.)  
    - User-selected items  
  - Example:
    - “Archive Inbox after 7 years”  
- **Archive Mailbox Concept:**  
  - Separate mailbox storage  
  - Lower-cost storage tier  
  - Improves performance of primary mailbox  
  - Acts as long-term email storage  
- **Creating a Retention Tag:**  
  - Choose:
    - Automatic vs user-applied  
    - Target (entire mailbox, folder, or items)  
    - Time period  
    - Action:
      - Move to Archive  
      - Delete  
- **Retention Policies:**  
  - Tags do nothing by themselves  
  - They must be attached to a **retention policy**  
  - A policy is a collection of tags  
- **Applying Retention Policies:**  
  - Go to Exchange Admin Center  
  - Recipients → Mailboxes → Select user  
  - Assign the desired MRM policy  
  - Can apply:
    - To a single mailbox  
    - To multiple mailboxes at once  
- **Why You Still Need to Know MRM:**  
  - Many organizations still use it  
  - Legacy environments rely on it  
  - Exam expects awareness of:
    - Retention tags  
    - Retention policies  
    - Archive behavior  
    - Exchange vs Microsoft 365 retention models  

---

## Module 10.2: Configure retention policies for Microsoft 365 services including Exchange Online  

**Learning Objectives:**  
- Understand why retention policies are required for compliance and data lifecycle management  
- Know where retention is managed in Microsoft Purview  
- Understand the difference between retention policies and retention labels  
- Configure static vs adaptive retention policies  
- Create, publish, and apply retention labels  
- Understand how labels override retention policies  
- Understand manual vs automatic label application  

**Key Topics:**  
- **Why Retention Exists:**  
  - Controls how long data is kept or deleted  
  - Required for:
    - Legal compliance  
    - Privacy regulations  
    - Storage governance  
    - Audit readiness  
- **Where Retention Is Managed:**  
  - `admin.microsoft.com → Compliance → Microsoft Purview`  
  - Data lifecycle management → **Microsoft 365**  
- **Retention Policies (Baseline Rules):**  
  - Apply globally to content locations:
    - Exchange Online  
    - SharePoint  
    - OneDrive  
    - Microsoft 365 Groups  
  - Define:
    - Retain for X years  
    - Delete after X years  
    - Retain forever  
  - Can be:
    - **Static** → applied to fixed locations  
    - **Adaptive** → applied based on attributes (users, properties, connectors)  
- **Retention Timing Logic:**  
  - Based on:
    - Date created (email)  
    - Date modified (documents)  
  - Important compliance behavior:
    - Content already older than the period is deleted when policy activates  
- **Retention Labels (Exceptions to Policies):**  
  - Used to override retention policies  
  - Applied to specific items  
  - Can:
    - Extend retention  
    - Prevent deletion  
    - Retain forever  
    - Enforce special handling  
- **Labels Do Nothing Until Published:**  
  - A label must be:
    1. Created  
    2. Published through a **Label Policy**  
  - Until then:
    - Users cannot see or apply it  
- **Publishing Labels:**  
  - Publish manually or via label policies  
  - Can be:
    - Static (fixed locations)  
    - Adaptive (attribute-based)  
- **Manual Labeling:**  
  - Users apply labels themselves  
  - Used for:
    - Legal holds  
    - Special-case records  
    - Compliance exceptions  
- **Automatic Labeling:**  
  - Labels applied based on:
    - Sensitive information types  
    - Keywords  
    - Trainable classifiers  
    - Content properties  
  - Example:
    - Apply label if content contains:
      - SSN  
      - Financial data  
      - Government-regulated information  
- **Label Enforcement Options:**  
  - Retain forever  
  - Retain for X years  
  - Delete after X years  
  - Just classify (no retention enforcement)  
- **Propagation Delay:**  
  - Policies and labels can take:
    - Several hours  
    - Up to 24 hours  
  - Trial tenants may show temporary errors  
- **Core Model:**  
  - Retention Policy = Default rule  
  - Retention Label = Exception  
  - Label Policy = Makes label usable  
Retention policies define the *baseline*,  
labels define the *exceptions*,  
and label policies make those exceptions *active*.

---

## Module 10.3: Configure retention policies using Microsoft 365 for a specific mailbox folder  
**Learning Objectives:**  
- Understand how to scope a retention policy to a single mailbox  
- Know how to create mailbox-specific retention using static policies  
- Understand how adaptive scopes enable user-based targeting  
- Recognize when to use static vs adaptive retention  
- Understand policy propagation timing  

**Key Topics:**  
- **Where This Is Configured:**  
  - `admin.microsoft.com → Compliance → Microsoft Purview`  
  - Data lifecycle management → **Microsoft 365** → Retention policies  
- **Static Retention for a Single Mailbox:**  
  - Create a new retention policy  
  - Choose **Static**  
  - Limit scope to:
    - Exchange Online  
    - Included mailboxes → select one user  
  - Used when:
    - You want direct, manual targeting  
    - Simple one-off mailbox control  
- **Adaptive Retention for a Single Mailbox:**  
  - Requires creating an **Adaptive Scope** first  
  - Adaptive scopes live under:
    - Roles & scopes → Adaptive scopes  
  - Scope example:
    - Users where EmailAddress = `jc@examlabpractice.com`  
- **Using an Adaptive Scope in Retention:**  
  - Create retention policy  
  - Choose **Adaptive**  
  - Add the adaptive scope  
  - Apply only to:
    - Exchange mailboxes  
  - Used when:
    - You want dynamic targeting  
    - Policies should update automatically if user attributes change  
- **Why Adaptive Is Powerful:**  
  - Automatically follows users that match the rule  
  - Useful for:
    - Executives  
    - Legal staff  
    - High-risk roles  
    - Compliance exceptions  
- **Retention Action Examples:**  
  - Retain forever  
  - Retain for X years  
  - Delete after X years  
  - Based on:
    - Created date (email)  
    - Modified date (documents)  
- **Policy Activation Delay:**  
  - Can take:
    - Several hours  
    - Up to 24 hours  
  - Normal behavior  
- **Design Rule:**  
  - Static = manual, fixed targeting  
  - Adaptive = rule-based, automatic targeting  

---

## Module 10.4: Enable and configure archive mailboxes  
**Learning Objectives:**  
- Understand what an archive mailbox (In-Place Archive) is  
- Know that archive mailboxes are disabled by default  
- Enable an archive mailbox for a user in the Exchange Admin Center  
- Understand performance and storage behavior of archive mailboxes  
- Enable archive mailboxes in bulk using PowerShell  

**Key Topics:**  
- **What an Archive Mailbox Is:**  
  - Also called *In-Place Archive*  
  - A secondary mailbox used to store older email  
  - Typically populated by:
    - Retention policies  
    - Manual user moves  
  - Uses lower-priority storage:
    - Slower access  
    - Optimized for long-term retention  
- **Why Use Archive Mailboxes:**  
  - Keeps primary mailbox small and fast  
  - Supports compliance retention  
  - Works with MRM and Microsoft 365 retention policies  
  - Acts as long-term storage for aged mail  
- **Archive Mailboxes Are Disabled by Default:**  
  - Must be explicitly enabled per user  
  - Not active unless turned on  
- **Enable for a Single User (GUI):**  
  - `admin.microsoft.com → Exchange Admin Center`  
  - Recipients → Mailboxes  
  - Select user → **Others** → Manage mailbox archive  
  - Enable archive mailbox  
- **Storage Limits:**  
  - Archive mailbox has a quota  
  - Not unlimited, but significantly large  
- **Bulk Enable Requires PowerShell:**  
  - GUI only supports one user at a time  
  - Example concepts:
    - Enable for one user:
      ```powershell
      Enable-Mailbox -Identity user@domain.com -Archive
      ```
    - Enable for all users without archives:
      ```powershell
      Get-Mailbox -Filter {ArchiveStatus -Eq "None" -and RecipientTypeDetails -Eq "UserMailbox"} |
      Enable-Mailbox -Archive
      ```
- **Design Rule:**  
  - GUI = single user  
  - PowerShell = bulk operations  

---

## Module 10.5: Manage inactive mailboxes  
**Learning Objectives:**  
- Understand what an inactive mailbox is and when it is used  
- Know how inactive mailboxes are created  
- View inactive mailboxes in Microsoft Purview  
- Understand the role of Litigation Hold  
- Know that PowerShell is required to restore or attach inactive mailboxes  

**Key Topics:**  
- **What an Inactive Mailbox Is:**  
  - A mailbox preserved after a user is deleted  
  - Used for:
    - Legal investigations  
    - Compliance retention  
    - Forensics and eDiscovery  
  - Cannot be logged into directly  
- **How Inactive Mailboxes Are Created:**  
  1. Apply **Litigation Hold** to a mailbox  
  2. Delete the user  
  3. The mailbox becomes **inactive** and is permanently preserved  
- **Where to View Inactive Mailboxes:**  
  - `admin.microsoft.com → Compliance (Microsoft Purview)`  
  - Data lifecycle management → Microsoft 365  
  - Retention → **Inactive mailboxes**  
- **Litigation Hold:**  
  - Applied in Exchange Admin Center  
  - User → Others → **Manage litigation hold**  
  - Options:
    - Duration (days or unlimited)  
    - Notes and documentation links  
  - Prevents mailbox data from ever being deleted  
- **Restoring or Accessing an Inactive Mailbox:**  
  - Must be done using **PowerShell**  
  - Requires:
    - Creating a new mailbox  
    - Using:
      ```powershell
      New-MailboxRestoreRequest
      ```
  - There is no GUI option for this  
- **PowerShell Is Mandatory:**  
  - Searching inactive mailboxes  
  - Restoring mailbox data  
  - Attaching mailbox content to a new user  
- **Use Case Summary:**  
  - Inactive mailboxes are for:
    - Compliance  
    - Legal preservation  
    - Historical recordkeeping  
  - Not for normal user access  


---

## Module 10.6: Analyze audit logs  
**Learning Objectives:**  
- Know where audit logs are managed (Microsoft Purview)  
- Understand that auditing is unified across all Microsoft 365 services  
- Search and filter audit events  
- Export audit data for analysis  
- Recognize the PowerShell alternative  
- Understand audit log retention policies  

**Key Topics:**  
- **Audit Logs Are Now in Microsoft Purview:**  
  - Moved from Exchange Admin Center  
  - Centralized for:
    - Exchange  
    - SharePoint  
    - Teams  
    - OneDrive  
    - Azure activities  
  - Path:  
    `admin.microsoft.com → Compliance → Microsoft Purview → Audit`
- **Unified Auditing Model:**  
  - One audit system for all Microsoft 365 workloads  
  - No longer separate per product (Exchange, SharePoint, Teams, etc.)
- **Searching Audit Logs:**  
  You can filter by:
  - Date range  
  - Workload (Exchange, SharePoint, Teams, etc.)  
  - User(s)  
  - Operation type (mail accessed, file modified, login, etc.)  
  - Record type  
  - Keywords  
  - Administrative units  
- **Audit Results Show:**  
  - Timestamp  
  - User  
  - IP address  
  - Operation performed  
  - Success or failure  
  - Detailed JSON record for forensic review  
- **Viewing Detailed Events:**  
  - Each log entry can be expanded  
  - Shows raw audit metadata  
  - Used for:
    - Security investigations  
    - Compliance audits  
    - Insider threat detection  
- **Exporting Logs:**  
  - Search results can be exported  
  - Output format:
    - CSV  
  - Used for:
    - Excel analysis  
    - Reporting  
    - Legal evidence  
- **PowerShell Option:**  
  - Cmdlet:
    ```powershell
    Search-AdminAuditLog
    ```
  - Used for:
    - Automation  
    - Scripted investigations  
    - Advanced filtering  
  - Not required to memorize syntax  
  - Just know it exists  
- **Audit Log Retention Policies:**  
  - Control how long audit logs are kept  
  - Configurable in Purview  
  - Retention:
    - Up to 10 years  
  - Policies can be scoped by:
    - Users  
    - Record types  
    - Workloads  
  - Priority-based when multiple policies exist  
- **Purpose of Audit Logging:**  
  - Security investigation  
  - Compliance verification  
  - Legal discovery  
  - Insider activity tracking  
  - Change accountability  

---

## Module 10.7: Manage journal rules  
**Learning Objectives:**  
- Understand what Exchange journaling is and why it is used  
- Know that journaled mail must be sent to an external address  
- Configure journal rule prerequisites  
- Create and remove journal rules  
- Understand when journaling is appropriate vs modern retention  

**Key Topics:**  
- **What Journaling Is:**  
  - Copies emails to an external mailbox  
  - Used for:
    - Legal compliance  
    - Regulatory archiving  
    - External investigations  
    - Backup-style storage  
  - Destination address must be:
    - Outside Microsoft 365  
    - Example: on-prem server, Gmail, external archive service  
- **Microsoft’s Recommendation:**  
  - Prefer:
    - Retention policies  
    - Litigation holds  
    - Archive mailboxes  
  - Journaling is legacy and used only when external copies are required  
- **Where Journaling Is Managed:**  
  - `admin.microsoft.com → Compliance → Microsoft Purview`  
  - Data lifecycle management → **Exchange (Legacy)**  
  - **Journal Rules**
- **Required First Step (Settings):**  
  - You must configure a **journal report email address**  
  - Used for:
    - Undeliverable journal messages  
  - Rule creation fails if this is not set  
- **Creating a Journal Rule:**  
  - Specify:
    - External email address (journal recipient)  
    - Rule name  
    - Scope:
      - Everyone  
      - Or specific user(s)  
    - Message type:
      - All messages  
      - Internal only  
      - External only  
- **What the Rule Does:**  
  - Every matching email:
    - Is delivered normally  
    - AND copied to the external mailbox  
- **Example Use Case:**  
  - User: Tom Williamson  
  - Journal destination: Gmail account  
  - Result:
    - Any email sent to or from Tom  
    - Is duplicated externally  
- **Verification:**  
  - Send a test email  
  - Confirm copy arrives in external mailbox  
- **Cleanup:**  
  - Journal rules can be:
    - Disabled  
    - Deleted  
  - Takes effect immediately  
- **Important Characteristics:**  
  - Real-time duplication  
  - Cannot target internal mailboxes  
  - Powerful but invasive  
  - Must be used carefully due to:
    - Privacy  
    - Legal implications  
    - Data exposure risk  

---

## Module 10.8: Introduction to content search and eDiscovery  

**Learning Objectives:**  
- Understand what Content Search is and when it is used  
- Understand what eDiscovery is and how it differs from Content Search  
- Distinguish between eDiscovery Standard and eDiscovery Premium  
- Know where Content Search and eDiscovery live in Microsoft Purview  
- Understand the role of legal holds in investigations  

**Key Topics:**  
- **Content Search:**  
  - Simple searching across Microsoft 365 data:
    - Exchange  
    - SharePoint  
    - OneDrive  
    - Teams  
  - Used to:
    - Find content  
    - Export content  
  - Does *not* support:
    - Legal holds  
    - Forensic preservation  
  - Requires minimal licensing  
- **eDiscovery:**  
  - Used for:
    - Legal investigations  
    - Compliance cases  
    - Forensics  
    - Evidence collection  
  - Supports:
    - Legal holds (prevents deletion)  
    - Case management  
    - Controlled data export  
- **eDiscovery Types:**  
  - **Standard:**  
    - Create cases  
    - Run searches  
    - Export data  
    - Apply legal holds  
  - **Premium:**  
    - Advanced indexing  
    - Tagging and analytics  
    - Predictive coding (AI)  
    - Legal hold notifications  
    - External reviewer access  
    - Advanced export to Azure storage  
- **Relationship Between Tools:**  
  - Content Search = searching only  
  - eDiscovery Standard = searching + legal preservation  
  - eDiscovery Premium = full legal forensics platform  
- **Licensing:**  
  - Content Search:
    - Included with most Microsoft 365 plans  
  - eDiscovery Standard:
    - Requires higher compliance licensing  
  - eDiscovery Premium:
    - Requires advanced compliance licensing  
- **Where These Are Located:**  
  - `admin.microsoft.com → Compliance (Microsoft Purview)`  
  - Under **Solutions**:
    - Content search  
    - eDiscovery (Standard & Premium)  
- **Purpose Summary:**  
  - Content Search = *find and export*  
  - eDiscovery = *find, preserve, and legally defend*  

---

## Module 10.9: Manage content search  
**Learning Objectives:**  
- Understand required permissions for Content Search  
- Know where Content Search is located in Microsoft Purview  
- Create and run a basic content search  
- Interpret search results and statistics  
- Export search results for reporting or review  

**Key Topics:**  
- **Required Permissions:**  
  - Global Administrator alone is not sufficient  
  - Roles needed:
    - **eDiscovery Manager**
    - (Optional higher level) **eDiscovery Administrator**
  - Assigned in:
    - `Microsoft Purview → Roles & scopes → Permissions → Microsoft Purview solutions → Roles`
- **Where Content Search Lives:**  
  - `admin.microsoft.com → Compliance (Microsoft Purview)`  
  - Under **Solutions → Content search**
- **Creating a Content Search:**  
  1. Click **New search**  
  2. Name the search (e.g., `Payroll`)  
  3. Select locations:
     - Exchange mailboxes  
     - SharePoint  
     - OneDrive  
     - Teams  
  4. Define query:
     - Simple keyword (e.g., `payroll`)  
     - Or advanced KQL (Kusto Query Language)  
  5. Add optional conditions:
     - Date  
     - Sender / recipient  
     - Subject  
     - Size  
     - Retention labels  
  6. Submit search  
- **Search Results:**  
  - Shows:
    - Number of items found  
    - Number of locations  
    - Total data size  
  - Displays:
    - Which mailboxes or sites contained matches  
  - Search reports can be downloaded as CSV  
- **Exporting Results:**  
  - From **Actions → Export**  
  - Options:
    - Export all items  
    - Export only unindexed/encrypted items  
    - Export normal indexed items  
  - Uses an **Export Key**:
    - Required to download results  
    - Must be protected (anyone with it can download data)  
  - Uses the **eDiscovery Export Tool** to download files  
- **Export Output:**  
  - Downloaded as folders with:
    - CSV reports  
    - Metadata  
    - Search result files  
  - CSV shows:
    - Subject  
    - Sender / recipient  
    - Original path  
    - Timestamp  
    - File identifiers  
- **Purpose of Content Search:**  
  - Used to:
    - Find content  
    - Review content  
    - Export content  
  - Not used for:
    - Legal holds  
    - Forensics  
    - Case management  
- **Difference from eDiscovery:**  
  - Content Search = visibility and reporting  
  - eDiscovery = investigation and legal preservation  

---

## Module 10.10: Manage standard eDiscovery cases  

**Learning Objectives:**  
- Understand what an eDiscovery case is  
- Know required roles for eDiscovery  
- Create and manage an eDiscovery Standard case  
- Run searches inside a case  
- Place legal holds on data  
- Export evidence from a case  

**Key Topics:**  
- **Permissions Required**
  - Global Admin is not enough  
  - Must be assigned:
    - **eDiscovery Manager**
  - Path:
    - `Purview → Roles & scopes → Permissions → Microsoft Purview solutions → Roles`
- **eDiscovery Types**
  - **Content Search**  
    - Search + export only  
  - **eDiscovery Standard**
    - Search  
    - Export  
    - Case management  
    - Legal holds  
  - **eDiscovery Premium**
    - Advanced analytics  
    - Custodian management  
    - Legal team workflows  
    - Requires higher licensing  
- **Create an eDiscovery Case**
  1. Go to:
     - `Purview → eDiscovery → Standard`
  2. Click **Create case**
  3. Name it (e.g., `Payroll Keyword Case`)
  4. Save and open the case  
- **Create a Search Inside a Case**
  1. Open the case  
  2. Go to **Searches → New search**  
  3. Choose locations:
     - Exchange mailboxes  
     - SharePoint  
     - Teams / M365 Groups  
  4. Enter query:
     - Simple keyword (e.g., `payroll`)  
     - Or KQL  
  5. Add optional filters:
     - Sender  
     - Date  
     - Subject  
     - Size  
  6. Submit  
- **Search Results**
  - Shows:
    - Items found  
    - Data size  
    - Locations  
  - Can:
    - Edit search  
    - Export results  
    - Review keyword samples  
- **Create a Legal Hold**
  1. Inside the case go to **Holds → Create**
  2. Name the hold  
  3. Choose location:
     - Exchange mailboxes  
  4. Select users (e.g., Tom Williamson)
  5. Define query (e.g., keyword `payroll`)
  6. Submit  
  Result:
  - Matching content cannot be deleted  
  - Preserves evidence for investigation  
- **Case Management**
  - Case Settings:
    - Case name  
    - Case number  
    - Description  
  - Access control:
    - Grant other users access to the case  
    - They must be in your tenant  
- **Difference from Content Search**
  - Content Search:
    - Visibility + export  
  - eDiscovery:
    - Evidence preservation  
    - Holds  
    - Case organization  
    - Legal defensibility  

## Assignment 7: SIMULATION  
**Create a retention policy for `JC@elp` using an adaptive scope. Retention: Forever**
Steps:
1. Go to:
   - `Purview → Roles & scopes → Adaptive scopes`
2. Create new scope:
   - Name: `JC Scope`
   - Type: **Users**
   - Condition:
     - `Email address equals JC@elp`
3. Go to:
   - `Purview → Data lifecycle management → Microsoft 365 → Retention policies`
4. Click **New retention policy**
   - Name: `JC Retention Policy`
5. Choose:
   - **Adaptive**
   - Add scope: `JC Scope`
6. Select location:
   - Exchange mailboxes only
7. Retention settings:
   - **Retain items forever**
8. Submit  
Effect:
- All email for `JC@elp` is preserved permanently  
- Overrides global retention behavior  
- Useful for executives, legal subjects, or compliance cases  

---

## KEY TAKEAWAYS
- Microsoft Purview is the central hub for compliance:
  - Retention
  - Auditing
  - Inactive mailboxes
  - Content search
  - eDiscovery
- MRM is legacy; Microsoft 365 retention policies and labels are the modern standard.
- Retention model:
  - Policy = baseline  
  - Label = exception  
  - Label policy = activation  
- Archive mailboxes store older email in lower-priority storage and must be enabled.
- Inactive mailboxes preserve data for legal and compliance reasons and require PowerShell to restore.
- Audit logs are unified across all Microsoft 365 services and are critical for investigations.
- Journaling is a legacy feature used only when external email copies are legally required.
- Content Search = find and export data.  
  eDiscovery = find, preserve, and legally protect data.
- eDiscovery introduces:
  - Cases
  - Legal holds
  - Evidence management
- Proper permissions are required:
  - eDiscovery Manager role is mandatory.
- Adaptive scopes allow retention to follow users automatically based on rules.
  
---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
