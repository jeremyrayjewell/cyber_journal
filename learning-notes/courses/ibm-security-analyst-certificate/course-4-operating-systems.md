# IBM Cybersecurity Analyst Professional Certificate  
## Course 4 – Operating Systems: Overview, Administration, and Security  

[Coursera](https://www.coursera.org/learn/operating-systems-overview-administration-security/home/module/1)  
---

## Overview  
Course 4 explores the architecture, features, and security mechanisms of modern operating systems (Windows, Linux, and macOS), along with concepts of virtualization and containers. Learners gain practical skills in managing file systems, user accounts, directory structures, and kernel/user mode operations. The course emphasizes securing Windows through Active Directory, Microsoft Defender, Kerberos authentication, patching, and auditing. Linux modules cover CLI vs GUI, common shell commands, file system navigation, and user management. macOS instruction includes Apple IDs, system preferences, and secure configurations. The course concludes with virtualization, containerization, and cloud deployment concepts, supported by hands-on labs.  

---

## Module 1: Windows Operating Systems  
This module introduces the fundamentals of Microsoft Windows, including architecture, file systems, and administrative tools.  

**Learning Objectives:**  
- Identify Windows OS editions (Windows 10/11 variants) and their features  
- Describe FAT vs NTFS file systems and metadata functions  
- Navigate Windows directory structures, 32-bit vs 64-bit architectures, and WoW64 compatibility  
- Differentiate user mode vs kernel mode and their impact on stability and security  
- Explore Windows Server roles, Active Directory, and group management  

**Key Topics & Details:**  
- **OS Generations:** Four historical stages (1945–present), from batch processing to multitasking (Windows, Linux, macOS, ChromeOS). UNIX (1969) pioneered portability and timesharing. Linux (1991) became a robust server OS; Android (2013) captured 75% of mobile OS market.  
- **Windows Editions:**  
  - Windows 10 Home (OneDrive, Defender, Cortana)  
  - Windows 10 Pro (BitLocker, Remote Desktop, domain joining)  
  - Windows 10 Enterprise (AppLocker, BranchCache, kiosk customization)  
  - Windows 10 Pro for Workstations (supports 4 CPUs, 6TB RAM, ReFS file system)  
  - Windows 11 Home/Pro/Enterprise/Workstation — enhanced security (Hello, Secure Boot, BitLocker, Autopatch).  
- **File Systems:**  
  - FAT (simple, cross-platform, limited to 4GB files, 2TB partitions)  
  - NTFS (permissions, encryption, disk quotas, journaling, MFT, hard links)  
- **Directory Structures:** User, Windows, Program Files (x86/64), hidden system files (pagefile.sys, hiberfil.sys, PerfLogs).  
- **User vs Kernel Mode:** Applications run in isolated user mode; kernel mode allows direct hardware interaction. Crashes in kernel mode can destabilize the entire OS. Communication is handled via system calls.  
- **Windows Server:** Provides Active Directory, file/storage services, IIS web hosting, Remote Desktop Services, Hyper-V virtualization, Storage Spaces Direct (S2D). Includes DNS, DHCP, VPN services, and security mechanisms like AD RMS, RBAC, BitLocker.  
- **Administration Tools:** Command Prompt (dir, md, del, ipconfig, ping, shutdown, robocopy), MMC snap-ins (Disk Management, Event Viewer, Group Policy, Task Scheduler, Performance Monitor, Certificate Manager).  
- **Active Directory:** Hierarchy of domains, trees, and forests; administrative features include OUs, security groups, folder redirection, and home folders. Provides centralized authentication and Group Policy enforcement.  

---

## Module 2: Windows Security  
This module focuses on securing Windows OS and Windows Server environments.  

**Learning Objectives:**  
- Configure Active Directory accounts and security policies  
- Identify risks associated with default local accounts  
- Apply patch management and updates through Microsoft Update  
- Configure Microsoft Defender Antivirus and firewall rules  
- Implement Kerberos authentication for domain-based systems  
- Audit systems for vulnerabilities and weaknesses  

**Key Topics & Details:**  
- **Active Directory Accounts:** Domain Admins (full privileges, must be safeguarded), Guest (disabled by default), KRBTGT (Kerberos ticketing), HelpAssistant (remote assistance).  
- **Security Practices:** Enable User Account Control (UAC), enforce role-based access control (RBAC), disable unnecessary default accounts, use least privilege.  
- **Microsoft Defender:** Real-time protection, firewall rules (hands-on lab), integration with Windows Security Center.  
- **Kerberos Authentication:** Uses tickets for secure domain authentication, reduces password transmission.  
- **Patch Management:** Critical for preventing exploits; use Microsoft Update.  
- **Auditing:** Log analysis, vulnerability scanning, and account monitoring.  

---

## Module 3: Linux Operating System  
This module introduces Linux distributions, file systems, and administration.  

**Learning Objectives:**  
- Differentiate Linux Desktop editions and common distributions  
- Compare CLI vs GUI environments  
- Execute common Linux/Unix commands  
- Navigate Linux directory structure and file systems  
- Manage users, groups, and permissions  

**Key Topics & Details:**  
- **Distributions:** Ubuntu, Red Hat, Fedora, Debian; adoption in enterprise, government, and cloud computing.  
- **File Systems:** Hierarchical root structure, run levels, ext4 format.  
- **Commands:** `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `chmod`, `chown`, `ps`, `grep`.  
- **User Management:** Adding/removing users, modifying groups, setting permissions.  
- **Hands-On Labs:** Ubuntu terminal navigation, user creation, updates and upgrades, system maintenance.  

---

## Module 4: macOS, Virtualization, and Containers  
This module explores Apple operating systems and virtualization technologies.  

**Learning Objectives:**  
- Identify macOS editions, features, and security tools  
- Manage Apple IDs (personal vs managed)  
- Configure macOS preferences for privacy and updates  
- Describe virtualization, containers, and cloud computing  
- Deploy Docker containers and IBM Cloud resources  

**Key Topics & Details:**  
- **macOS:** Based on UNIX; includes Time Machine, FileVault encryption, Gatekeeper, and iCloud integration. Transition from Intel to Apple Silicon (M1, 2020).  
- **Mobile OS:** iOS and Android overview, interface navigation.  
- **Virtualization:** Hyper-V (Windows), VirtualBox, VMware; benefits include scalability, resource optimization, isolation.  
- **Containers:** Docker, Kubernetes basics, container challenges, hands-on IBM Cloud deployment.  

---

## Module 5: Final Project and Course Wrap-Up  
This culminating module integrates Windows and Linux skills in a peer-graded project. Learners apply security configuration, directory navigation, and command-line skills to practical scenarios.  

**Learning Objectives:**  
- Apply Windows and Linux administration tasks in a lab environment  
- Demonstrate security configuration through Defender, firewall, and Active Directory  
- Execute Linux shell commands for user management and system maintenance  
- Explore container deployment on cloud infrastructure  

**Key Topics:**  
- Windows + Linux combined lab  
- System hardening and account management  
- Virtualization and container security considerations  

---

## Supplementary Projects  
- **Windows Server Lab** – Manage Active Directory, group policies, and firewall rules  
- **Command Prompt & MMC Labs** – File/directory management, user accounts, system maintenance  
- **Linux Terminal Exercises** – User management, updates, permissions  
- **macOS Customization Project** – Security preferences and Apple ID management  
- **Virtualization & Containers Labs** – Docker deployment and IBM Cloud integration  
- **Final Peer-Graded Project** – Applied Windows/Linux administration and security  

---

## Completion Status  
- All modules completed  
- All videos, readings, and hands-on labs completed  
- All graded assignments and final project submitted with high scores (90%)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
