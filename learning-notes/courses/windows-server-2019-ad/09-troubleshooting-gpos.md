# Windows Server 2019 Admin: Active Directory, DNS, GPO, DHCP
**Course by Emilio Aguero, Palwasha Khan**

* **Course Link:** [https://www.udemy.com/course/windowsserver2019/](https://www.udemy.com/course/windowsserver2019/)
* **Section:** 9 – Troubleshooting GPOs
* **Date:** 2026-02-05
* **Notes Author:** Jeremy Ray Jewell

---

## Overview  

Section 9 covers basic methods for troubleshooting Group Policy application issues using built-in Windows tools.

---

## Module 9.1: Introduction to Troubleshooting GPOs  

**Learning Objectives:**  
- Understand common causes of Group Policy application failures  
- Apply a basic troubleshooting approach for GPO issues  

**Key Topics:**  
- Common GPO failure scenarios  
- GPO processing and application dependencies  
- Role of DNS and domain connectivity in GPO application  
- High-level troubleshooting workflow for GPO issues  
- Impact of misapplied policies on users and systems  

---

## Module 9.2: Using the MMC (rsop.msc)  

**Learning Objectives:**  
- Use Resultant Set of Policy (RSoP) to diagnose applied GPOs  
- Identify which policies are affecting a given user or computer  

**Key Topics:**  
- Launching and using rsop.msc  
- Viewing applied and denied policies  
- Understanding policy precedence in RSoP output  
- Using RSoP to troubleshoot unexpected behavior  
- Limitations of RSoP for GPO diagnostics  

---

## Module 9.3: Using the Command Prompt (gpresult /r and gpupdate /force)  

**Learning Objectives:**  
- Use gpresult to view applied Group Policy settings  
- Use gpupdate to force immediate policy refresh  

**Key Topics:**  
- Running gpresult /r to inspect applied policies  
- Forcing policy updates with gpupdate /force  
- Interpreting gpresult output for troubleshooting  
- Common scenarios where manual policy refresh is needed  
- Basic command-line troubleshooting workflow for GPO issues  

---

## KEY TAKEAWAYS

- RSoP and gpresult help identify which policies are applied.  
- gpupdate forces immediate policy refresh for testing.  
- GPO troubleshooting starts with verifying scope and connectivity.

---

**Notes Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  

