# Advent of Cyber 2025 – Day 6 , 2025-12-06
**Room:** Malware Analysis – HopHelper.exe  
**Category:** Static & Dynamic Malware Analysis  
**Skills Practiced:** Static analysis, PE inspection, strings extraction, registry diffing, behavioral monitoring, persistence discovery, network activity analysis.

---

## Summary
Today’s challenge introduced basic malware analysis workflows inside a Windows sandbox VM. The suspicious attachment, *HopHelper.exe*, was sent to TBFC staff via a fake “schedule update” email allegedly from Elf McClause at 3AM — an obvious red flag. Acting as Elf McBlue, I performed both **static analysis** (PeStudio) and **dynamic analysis** (Regshot + ProcMon) to determine:

- how the malware is constructed  
- what artifacts it leaves behind  
- how it persists  
- and what network infrastructure it contacts

This writeup documents the exact process I used, mistakes included, and how each tool contributed to reconstructing the malware’s behavior.

---

## Walkthrough Notes

### 1. Accessing the sandbox
The provided Windows VM launches in split view. Tools preinstalled on the Desktop:

- **PeStudio** (static analysis)
- **Regshot** (registry diffing)
- **ProcMon** (behavioral monitoring)
- Folder: **HopHelper/** containing `HopHelper.exe`

Before doing anything else, I followed the cardinal rule:  
**Never execute malware before doing static analysis.**

---

## 2. Static Analysis (PeStudio)

### 2.1 Obtaining the SHA256 checksum
I launched PeStudio and dragged `HopHelper.exe` into it.  
Under **Indicators → file > sha256**, I recorded the hash required for the Day 6 question.

This checksum is useful because:

- it can be Googled to identify known malware  
- it serves as threat intel (“we’ve seen this sample before”)  
- it fingerprints the exact binary version  

No execution was required to gather this.

---

### 2.2 Extracting strings
Next I clicked **Strings** in PeStudio.  
It took ~2–3 minutes to populate, which is normal for malware containing many embedded resources.

At the bottom of the strings list, I recovered:

`THM{...}`

This embedded flag indicates the challenge authors intentionally placed readable indicators inside the malware — mimicking how analysts sometimes uncover attacker infrastructure, URLs, commands, or encryption keys through simple string inspection.

---

## 3. Dynamic Analysis – Regshot (Registry Persistence)

### 3.1 First snapshot
I opened Regshot and set the output directory to the Desktop.  
Then I clicked:
`1st shot → Shot`

This captured the registry state before executing the malware.

---

### 3.2 Executing HopHelper.exe
Only after the first snapshot did I run the executable from the `HopHelper` folder.

A fake “rota manager” window appeared — clearly a decoy.  
This is common: malware tries to look legitimate to reduce suspicion.

---

### 3.3 Second snapshot & comparison
Back in Regshot:
`2nd shot → Shot → Compare`

The diff file opened in Notepad.

I searched for:

- `"HopHelper"`
- `"Run"`
- `"Startup"`

The persistence mechanism was exactly where expected:  
the malware added a **Run key** under the user’s hive so it launches automatically on reboot.

The full modified path was the answer to Q3.

---

## 4. Dynamic Analysis – ProcMon (Behavior Monitoring)

### 4.1 Capturing behavior
I launched Process Monitor (ProcMon), which immediately began logging thousands of system events per second.

To focus on the malware:

1. I ran HopHelper.exe again.
2. Let ProcMon collect events for ~10 seconds.
3. Stopped capture (Play/Pause button).

---

### 4.2 Filtering for network behavior
Most raw ProcMon output is noise.  
To isolate network activity, I applied the filter:
`Operation contains TCP → Include`

Now only TCP-related actions appeared (TCP Connect, TCP Receive, TCP Send).

This revealed:

- the malware uses **TCP** for outbound communication  
- the destination host likely hosts a command-and-control (C2) web panel  
- the connection is established immediately upon execution  

A panel URL can be derived from the domain/IP revealed here or from PeStudio strings.

---

## Key Takeaways

- **Static analysis** gives quick intel (hashes, strings, imports) before execution.
- **Dynamic analysis** reveals real behavior: persistence keys, file writes, network traffic.
- **Regshot** is ideal for catching registry-based persistence.
- **ProcMon** is essential for tracing malware operations in real time.
- Even simple malware follows a standard pattern: decoy window → persistence → outbound C2 contact.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell



