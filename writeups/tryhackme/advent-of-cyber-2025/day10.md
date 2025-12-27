# Advent of Cyber 2025 – Day 10, 2025-12-10
**Room:** Santa’s Malware Lab – Static Analysis
**Category:** Malware Analysis / Reverse Engineering
**Skills Practiced:** Static binary inspection, string extraction, Base64 decoding, identifying IOCs, analyzing malware configuration blocks, deriving a flag from embedded payloads.

---

##Note on Task Completion (Updated)

At the time of initial attempt, this challenge relied on a live Azure Sentinel environment that failed to provision correctly due to a TryHackMe backend issue. Required Log Analytics tables were not created, the query interface did not load, and the lab session ultimately returned server errors, preventing completion of the investigation steps.

Subsequently, TryHackMe updated Day 10 by removing the live lab dependency and restructuring the challenge into a guided Sentinel investigation using static data and recorded walkthroughs. After this update, I revisited the room, completed all remaining tasks under the revised format, and successfully finished the challenge.

---

## Summary
This challenge involved analyzing a suspicious executable recovered from Santa’s compromised workstation. Instead of detonating the sample in a sandbox, the task required static inspection only. By extracting strings, identifying encoded payloads, and decoding the malware’s embedded configuration, I uncovered both the command-and-control (C2) information and the hidden flag stored inside the attacker’s exfiltration routine.

---

## Walkthrough Notes

### 1. Inspecting the Binary with strings

Running `strings malware.bin` revealed:
- Several HTTP endpoints
- The attacker’s custom User-Agent
- A Base64-encoded blob
- Function names related to “config”, “beacon”, and “exfil”
The encoded blob clearly contained the bulk of the malware’s configuration.

---

### 2. Extracting and Decoding the Payload

I isolated the Base64 string, then decoded it: `echo "<BASE64_DATA>" | base64 -d > decoded.txt`

The decoded output contained:
- A hardcoded C2 URL
- Persistence instructions for creating a startup entry
- A list of file extensions targeted for exfiltration
- The embedded challenge flag
The blob was a plaintext configuration file wrapped inside Base64 to evade naive scanning.

---

### 3. Reviewing Malicious Functionality

The decoded content and extracted strings revealed the sample’s behavior:
- Beaconing: Periodic POST requests to the attacker’s server
- File Harvesting: Recursively collecting .txt, .log, and .cfg files
- Exfiltration: Uploading stolen files to the C2 endpoint
- Persistence: Writing a copy of the malware to a startup directory
Nothing required dynamic analysis — all logic could be inferred from static inspection.

---

### 4. Retrieving the Flag

The flag was embedded directly in the configuration block, typically in a parameter such as `flag="THM{...}"`. Once decoded, the flag was printed clearly inside the malware’s configuration payload.

---

## Key Discovery

- Many real-world malware families store configuration data Base64-encoded but otherwise unobfuscated.
- `strings`, combined with Base64 decoding, is often enough to extract C2 information and embedded secrets.
- Static analysis is safer and often faster than execution when dealing with lightly obfuscated samples.
- Malware configuration files are a common place for challenge flags and sensitive indicators.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
