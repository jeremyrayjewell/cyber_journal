# Advent of Cyber 2025 – Day 16, 2025-12-16 
**Room:** Forensics – Registry Furensics  
**Category:** Windows Forensics  
**Skills Practiced:** Windows Registry analysis, offline hive examination, persistence detection, execution artefact analysis

---

## Summary
Day 16 focused on Windows Registry forensics as part of an incident response investigation on a compromised system, **dispatch-srv01**, a critical server responsible for SOC-mas drone gift deliveries. With abnormal activity beginning on **October 21, 2025**, the objective was to reconstruct attacker behavior by analyzing offline registry hives rather than live system artefacts.

Using **Registry Explorer**, I examined collected registry hives to determine:
- which application was installed prior to the compromise,
- where that application was executed from,
- and how it achieved persistence on system startup.

This investigation demonstrated how registry artefacts alone can reveal installation, execution, and persistence without relying on malware samples or logs.

---

## Walkthrough Notes

### 1. Loading Offline Registry Hives

Registry Explorer was launched on the target machine. Each hive was loaded from:

`C:\Users\Administrator\Desktop\Registry Hives`

To ensure consistency, each hive was opened while holding **SHIFT**, allowing transaction logs to replay and ensuring clean hive states. The following hives were loaded:
- `SYSTEM`
- `SOFTWARE`
- `NTUSER.DAT`

---

### 2. System Verification

To confirm analysis was being performed on the correct system, the hostname was verified by navigating to:

SYSTEM  
└─ ControlSet001  
   └─ Control  
      └─ ComputerName  
         └─ ComputerName  

The hostname **DISPATCH-SRV01** confirmed the correct target.

---

### 3. Identifying the Suspicious Application Installation

To determine which application was installed shortly before the abnormal activity, the SOFTWARE hive was examined at:

SOFTWARE  
└─ Microsoft  
   └─ Windows  
      └─ CurrentVersion  
         └─ Uninstall  

Each application entry was reviewed for:
- DisplayName
- InstallDate
- InstallLocation

An application installed just prior to October 21, 2025 stood out as anomalous compared to baseline server software. This application was identified as the source of subsequent malicious activity.

This answered:
**What application was installed on the dispatch-srv01 before the abnormal activity started?**

---

### 4. Determining Execution Path

To identify where the suspicious application was launched from, execution artefacts were examined within the NTUSER.DAT hive:

NTUSER.DAT  
└─ Software  
   └─ Microsoft  
      └─ Windows  
         └─ CurrentVersion  
            └─ Explorer  
               └─ UserAssist  

The UserAssist key records GUI-launched programs and execution counts. Registry Explorer automatically decoded the ROT13-encoded entries. The same application identified earlier appeared here with its **full execution path**, revealing exactly where the user launched it from.

This answered:
**What is the full path where the user launched the application from?**

---

### 5. Persistence Mechanism Identification

To identify how the application maintained persistence, the SOFTWARE hive was initially examined at the standard location: `ROOT\Microsoft\Windows\CurrentVersion\Run`. Troubleshooting & Resolution: While the hive transaction logs were successfully replayed (incorporating "dirty" data from .log files), the entry was not immediately visible through manual navigation of the folder tree. This suggested a potential UI refresh discrepancy within Registry Explorer. To bypass this, a global search (Ctrl+F) was performed across the hive for the string dronehelper.exe. This search successfully localized the persistence artifact in the memory-resident view of the Run key, confirming the entry existed despite the visual folder tree remaining unpopulated.

Findings:
- Hive: SOFTWARE
- Key Path: `ROOT\Microsoft\Windows\CurrentVersion\Run`
- Value Name: `DroneManager Updater`
- Value Data: `"C:\Program Files\DroneManager\dronehelper.exe" --background`
This entry ensures the "helper" utility executes in a background state upon every system boot, a classic persistence technique.


---

## Key Takeaways
- Windows Registry artefacts can reconstruct attacker behavior even when files and logs are missing.
- Installation, execution, and persistence each leave distinct registry traces.
- Offline registry analysis avoids evidence contamination and allows accurate forensic reconstruction.
- UserAssist and Run keys are especially valuable for timeline and persistence analysis.
- Registry Explorer significantly improves forensic efficiency over native Registry Editor.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
