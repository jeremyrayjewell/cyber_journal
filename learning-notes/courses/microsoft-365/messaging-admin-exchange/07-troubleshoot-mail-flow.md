# Microsoft 365 Messaging Admin Exchange Online
**Course by John Christopher**

* **Course Link:** https://www.udemy.com/course/microsoft-365-messenger-administrator-exchange-course  
* **Section:** 7 – Troubleshoot Mail Flow 
* **Date:** 2026-01-13  
* **Notes Author:** Jeremy Ray Jewell  

---

## Overview  


---

## Module 7.1: Configure and manage alert policies  
**Learning Objectives:**  
- Understand what alert policies are and why they are used  
- Identify the different types of mail flow alerts available in Exchange Online  
- Learn how to create and configure custom alert policies  
- Know how alerts are delivered and monitored  

**Key Topics:**  
- Alert policies monitor abnormal or risky mail flow behavior  
- Managed in Exchange Admin Center → Mail flow → Alert policies  
- Alerts can be:
  - Viewed in the portal  
  - Sent to admins by email  
- Severity levels:
  - Low, Medium, High  
  - Used to prioritize response  
- Notification limits:
  - Prevent inbox flooding during repeated incidents  
- Common built-in alerts:
  - Reply-all storms  
  - Message delivery delays  
- Custom alert triggers:
  - Mail loops  
  - Slow transport rules  
  - New users forwarding externally  
  - Forwarding to new or suspicious domains  
  - Certificate expiration  

---

## Module 7.2: Trace a message and analyze a message trace  
**Learning Objectives:**  
- Understand what Message Trace is and why it is used in Exchange Online  
- Know who is authorized to run message traces (Global Admin and Exchange Admin)  
- Learn how to perform message traces through the Exchange Admin Center  
- Recognize common delivery statuses and what they mean  
- Understand how message trace integrates with Microsoft Defender for investigation  

**Key Topics:**  
- **Purpose of Message Trace:**  
  - Track email as it moves through Exchange Online  
  - Determine whether a message was delivered, failed, delayed, quarantined, or blocked  
  - Used for troubleshooting mail flow and security issues  
- **Access Requirements:**  
  - Only Global Administrators and Exchange Administrators can run traces  
  - High-privilege administrative feature  
- **Where Message Trace Is Located:**  
  - Microsoft 365 Admin Center → Exchange Admin Center  
  - Mail flow → Message trace  
- **Query Types:**  
  - Default queries (prebuilt searches)  
  - Custom queries (user-defined searches)  
  - Auto-saved queries (recent searches)  
  - Downloadable reports  
- **Search Filters:**  
  - Sender and recipient  
  - Date range (up to 90 days)  
  - Delivery status  
  - Message ID (GUID / client ID)  
  - Direction (inbound or outbound)  
  - IP address  
- **Delivery Status Values:**  
  - Delivered  
  - Failed  
  - Pending  
  - Quarantined  
  - Filtered as spam  
  - Getting status  
  - Expanded (distribution group expansion)  
- **Message ID:**  
  - Unique identifier assigned to every message  
  - Used for precise troubleshooting and PowerShell tracing  
  - Appears in message headers  
- **Report Types:**  
  - Summary (quick results)  
  - Enhanced (adds routing and IP data)  
  - Extended (full transport and event history)  
- **Integration with Microsoft Defender:**  
  - View message in Threat Explorer  
  - Submit message for analysis  
  - Hunt for message in advanced threat hunting  
- **PowerShell Support:**  
  - `Get-HistoricalSearch` and `Get-MessageTrace` commands  
  - Used for automation or advanced reporting  
  - Message ID can be queried directly  
- **Default Queries:**  
  - Messages sent from domain  
  - Messages received by domain  
  - Pending delivery  
  - Quarantined messages  
  - Failed messages  
- **Exporting Data:**  
  - Results can be exported as CSV  
  - Used for auditing and documentation  
- **Strategic Importance:**  
  - Message trace is the primary tool for diagnosing mail flow problems  
  - Essential for security incident investigation  
  - Provides visibility into how Exchange and EOP handled a message  

---

## Module 7.3: Analyze message headers  
**Learning Objectives:**  
- Understand what email message headers are and what information they contain  
- Learn how to view message headers in Outlook (Web and Desktop)  
- Recognize how headers help verify message legitimacy and security  
- Understand how SPF, DKIM, and TLS results appear in headers  
- Use online tools to simplify header analysis  

**Key Topics:**  
- **What Message Headers Are:**  
  - Technical metadata added to every email  
  - Shows routing, authentication, encryption, and delivery details  
  - Used for troubleshooting, security analysis, and validation  
- **Viewing Headers in Outlook on the Web:**  
  - Open email → Three dots (…) → View → View message details  
  - Displays:  
    - Message ID  
    - Sender and receiving servers  
    - TLS encryption status  
    - SPF, DKIM, and DMARC results  
- **Viewing Headers in Outlook Desktop:**  
  - Open email → File → Properties  
  - Internet headers section shows full raw header data  
- **What to Look For in Headers:**  
  - Authentication results:
    - SPF = Pass/Fail  
    - DKIM = Pass/Fail  
    - DMARC = Alignment results  
  - TLS encryption version used  
  - Message ID and routing path  
  - X-Headers (Exchange-added processing metadata)  
- **X-Headers:**  
  - Custom headers added by mail systems (like Exchange)  
  - Indicate filtering, spam checks, routing, and security processing  
- **Header Analysis Tools:**  
  - Online “Email Header Analyzer” websites  
  - Paste full header text for automated breakdown  
  - Makes routing paths, spam rules, and auth results easier to read  
- **Why Header Analysis Matters:**  
  - Confirms if an email is legitimate  
  - Helps investigate phishing, spoofing, and delivery problems  
  - Complements Message Trace for full email investigation  
- **Cross-Platform:**  
  - Header analysis works in any email system:
    - Outlook  
    - Gmail  
    - Others  
  - Only the method of accessing headers changes  


---

## Module 7.4: Analyze non-delivery reports (NDRs)
**Learning Objectives:**  
- Understand what a Non-Delivery Report (NDR) is and why it is generated  
- Learn how to read and interpret NDR status codes  
- Know how to use Microsoft documentation to troubleshoot NDRs  
- Use Message Trace to investigate failed messages  
- Identify common causes of NDRs  

**Key Topics:**  
- **What an NDR Is:**  
  - An automatic response when email delivery fails  
  - Sent back to the sender explaining why the message was not delivered  
  - Contains diagnostic information and status codes  
- **Where to Find NDR Information:**  
  - Directly in the NDR email itself  
  - Full message headers are included automatically in NDRs  
  - Message Trace in Exchange Admin Center:
    - Mail flow → Message trace  
    - Filter by failed messages  
- **NDR Status Codes:**  
  - Numeric codes describe the exact failure reason  
  - Common reasons:
    - Recipient does not exist  
    - Typo in email address  
    - Domain does not exist  
    - Message blocked by policy or filtering  
  - Microsoft provides full lookup tables for all NDR codes  
- **Using Microsoft Documentation:**  
  - Search “Exchange Online NDR codes”  
  - Tables explain:
    - Code meaning  
    - Root cause  
    - Recommended fix  
- **Troubleshooting Workflow:**  
  1. Open the NDR email  
  2. Identify the status code  
  3. Look it up in Microsoft documentation  
  4. Check Message Trace for confirmation  
  5. Fix:
     - Typo  
     - User existence  
     - Domain configuration  
     - Mail flow rules or filtering  
- **Message Trace Integration:**  
  - Confirms:
    - Message failed  
    - Exact failure point  
    - Transport rule involvement  
    - Policy enforcement  
  - Avoids relying only on user-provided NDRs  
- **Most Common Cause:**  
  - Misspelled or non-existent recipient address  
- **Big Idea:**  
  - NDRs are diagnostic tools, not just error messages  
  - They provide structured data that leads directly to the root cause  
  - Message Trace + NDR = complete delivery failure analysis  

---

## Module 7.5: Troubleshoot by using the Microsoft Remote Connectivity Analyzer + Assignment: SIMULATION: Create a Mail Loop alert policy
**Learning Objectives:**  
- Understand what the Microsoft Remote Connectivity Analyzer is used for  
- Know where to access the tool and what services it supports  
- Use it to test Exchange Online and Outlook connectivity issues  
- Identify common troubleshooting scenarios for SMTP, Outlook, and DNS  
- Create a Mail Loop alert policy with proper severity and notifications  

**Key Topics:**  
- **Microsoft Remote Connectivity Analyzer:**  
  - Web-based troubleshooting platform:  
    - https://testconnectivity.microsoft.com  
  - Used to validate Microsoft 365, Exchange, Outlook, SMTP, and DNS connectivity  
  - Helps diagnose real-world mail and client connection problems  
- **Common Test Categories:**  
  - Outlook connectivity (Autodiscover, MAPI, authentication)  
  - Inbound and outbound SMTP tests  
  - Reverse DNS and blacklist checks  
  - Exchange ActiveSync tests  
  - IMAP / POP server tests  
  - SSL certificate validation  
  - DNS and security configuration tests  
- **Outlook Connectivity Test:**  
  - Enter user email address  
  - Optionally authenticate with credentials  
  - Tests:
    - Autodiscover  
    - Exchange Online connection  
    - MAPI connectivity  
    - Authentication success  
  - Confirms whether Outlook should function correctly  
- **SMTP Tests:**  
  - Validate outbound mail server reputation  
  - Reverse DNS validation  
  - Real-time blacklist checks  
  - Sender ID verification  
  - Confirms mail server trustworthiness  
- **Use Case:**  
  - Ideal when users report:
    - Outlook connection failures  
    - Email send/receive issues  
    - Authentication problems  
    - SMTP relay problems  
- **Strategic Value:**  
  - Eliminates guesswork  
  - Provides authoritative diagnostics directly from Microsoft  
  - Often used before deeper Exchange or Defender investigations  

### Assignment: SIMULATION  
**Create a Mail Loop alert policy**
- Location:  
  - Exchange Admin Center → Mail Flow → Alert Policies  
- Policy Settings:  
  - **Name:** Mail Loop Alert  
  - **Trigger:** Mail loop  
  - **Severity:** High  
  - **Email Notification:** JC  
  - **Daily Notification Limit:** 100  
  - **Enable policy after creation**  
- Purpose:  
  - Detect and alert when Exchange mail loops occur  
  - Prevent runaway mail storms  
  - Protect system stability  
  - Provide immediate admin awareness  

---

## KEY TAKEAWAYS


---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
