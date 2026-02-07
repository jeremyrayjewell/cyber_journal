# Windows Server 2019 Admin: Active Directory, DNS, GPO, DHCP
**Course by Emilio Aguero, Palwasha Khan**

* **Course Link:** [https://www.udemy.com/course/windowsserver2019/](https://www.udemy.com/course/windowsserver2019/)
* **Section:** 8 – Common Group Policies
* **Date:** 2026-02-04
* **Notes Author:** Jeremy Ray Jewell

---

## Overview  

Section 8 covers common Group Policy use cases for enforcing security and configuration settings on domain-joined systems.

---

## Module 8.1: Enforce Domain Password Complexity  

**Learning Objectives:**  
- Configure domain password complexity requirements  
- Understand how password policies improve account security  

**Key Topics:**  
- Domain password policy settings (complexity, length, history)  
- Enforcing password policies via Group Policy  
- Security impact of weak vs strong password policies  
- Default domain policy scope and limitations  
- Operational considerations when changing password policies  

---

## Module 8.2: Set Desktop Background  

**Learning Objectives:**  
- Configure desktop background settings using Group Policy  
- Apply user-level policies across targeted OUs  

**Key Topics:**  
- Setting desktop background via GPO  
- Scoping user configuration policies  
- Applying policies to specific users or OUs  
- Testing GPO application on client machines  
- Using simple visual policies to validate GPO functionality  

---

## Module 8.3: Disable Control Panel  

**Learning Objectives:**  
- Restrict user access to Control Panel using Group Policy  
- Enforce basic endpoint configuration controls  

**Key Topics:**  
- Disabling Control Panel and Settings via GPO  
- User vs computer policy scope  
- Use cases for restricting local configuration changes  
- Testing and verifying policy enforcement  
- Balancing usability with administrative control  

---

## Module 8.4: Setup User Login Warning Messages  

**Learning Objectives:**  
- Configure login warning banners for users  
- Understand compliance and security use cases for login messages  

**Key Topics:**  
- Setting interactive logon warning messages via GPO  
- Legal and compliance motivations for login banners  
- User vs computer policy scope for logon messages  
- Testing banner display on domain-joined clients  
- Common formatting and deployment considerations  

---

## Module 8.5: Disable Guest Account and Local Administrator Accounts  

**Learning Objectives:**  
- Disable insecure default accounts on domain-joined systems  
- Reduce attack surface by limiting local administrator access  

**Key Topics:**  
- Disabling the Guest account via Group Policy  
- Managing and restricting local Administrator accounts  
- Security risks of default and shared local admin credentials  
- Applying account restrictions through GPO  
- Hardening endpoints as part of baseline security policy  

---

## Module 8.6: Deny Execute Access on Removable Disks  

**Learning Objectives:**  
- Restrict execution of programs from removable media  
- Reduce malware risk from USB and external storage devices  

**Key Topics:**  
- Configuring software restriction or execution policies via GPO  
- Controlling removable storage behavior  
- Security risks associated with removable media  
- Applying and testing execution restrictions on client systems  
- Balancing security controls with operational usability  

---

## Module 8.7: Windows Update  

**Learning Objectives:**  
- Configure Windows Update behavior via Group Policy  
- Understand the role of patch management in endpoint security  

**Key Topics:**  
- Managing Windows Update settings with GPO  
- Update scheduling and deferral policies  
- Importance of timely patching for security  
- Impact of updates on system stability and uptime  
- Basic considerations for update rollout in domain environments  

---

## Module 8.8: Disable Command Prompt & Registry Editor  

**Learning Objectives:**  
- Restrict user access to Command Prompt and Registry Editor  
- Reduce risk of unauthorized system changes  

**Key Topics:**  
- Disabling Command Prompt via Group Policy  
- Restricting access to Registry Editor  
- Use cases for limiting local administrative tools  
- Security vs usability trade-offs  
- Verifying enforcement on domain-joined clients  

---

## KEY TAKEAWAYS

- Group Policy is a primary mechanism for enforcing baseline security settings.  
- Many endpoint hardening controls can be centrally managed via GPOs.  
- Policy changes should be tested before broad deployment.

---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  

