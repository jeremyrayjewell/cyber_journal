# Advent of Cyber 2025 – Day 18, 2025-12-18 
**Room:** Obfuscation – The Egg Shell File  
**Category:** Malware Analysis / Obfuscation  
**Skills Practiced:** Obfuscation analysis, PowerShell script inspection, XOR encoding, safe deobfuscation, tooling-assisted decoding

---

## Summary
Day 18 focused on identifying and reversing obfuscation techniques used within a malicious PowerShell script delivered via a phishing email impersonating northpole-hr. The investigation centered on a suspicious attachment extracted from a PDF and analyzed in an isolated virtual machine. The objective was twofold:
  1. Deobfuscate a command-and-control (C2) URL embedded in the script to understand its behavior.
  2. Correctly re-obfuscate an attacker API key using XOR, as instructed by the script, to trigger additional execution logic.
This exercise reinforced practical distinctions between encoding, encryption, and obfuscation, and demonstrated how layered or simple obfuscation is commonly used to evade casual inspection rather than provide cryptographic security.

---

## Walkthrough Notes

### 1. Script Identification and Initial Inspection

The extracted PowerShell script, `SantaStealer.ps1`, was located on the Desktop of the target VM and opened in Visual Studio. At the top of the file, a clearly marked “Start here” section provided guided instructions indicating:
- which variables contained obfuscated data,
- how the obfuscation should be reversed,
- and how to safely execute the script once modifications were complete.
This structured layout allowed analysis without executing unknown logic prematurely.

---

### 2. Deobfuscating the C2 URL

Within the script, the C2 endpoint was stored in an obfuscated format intended to obscure network indicators from casual review. Using pattern recognition and the hints provided in the comments, the obfuscation method was identified and reversed. Once decoded, the plaintext C2 URL was restored in the appropriate variable. This step demonstrated a common attacker tradeoff: lightweight obfuscation sufficient to bypass basic detection, but easily reversible once identified.

---

### 3. Script Execution and First Flag Retrieval

After restoring the decoded C2 value, the script was executed from PowerShell:
```
cd .\Desktop\
.\SantaStealer.ps1
```
With the deobfuscation performed correctly, the script completed execution and returned the first flag.

This answered:
**What is the first flag you get after deobfuscating the C2 URL and running the script?**

---

### 4. XOR Obfuscation of the API Key

A second challenge required re-obfuscating an attacker API key using XOR, reversing the analyst’s usual role. Following the Part 2 instructions embedded in the script:
- the provided API key was XOR-encoded using the specified key and format,
- the resulting output was inserted back into the script in place of the original value.
This step reinforced how XOR obfuscation works symmetrically and why key reuse makes it especially weak against analysis.

---

### 5. Persistence Mechanism Identification

With the API key correctly XOR-obfuscated, the script was executed again: `.\SantaStealer.ps1`. The modified logic path was triggered, and the script returned the second flag.

This answered:
**What is the second flag you get after obfuscating the API key and running the script again?**

---

## Key Takeaways
- Obfuscation is primarily used to delay analysis and evade simple detection, not to provide true secrecy.
- XOR obfuscation is trivial to reverse once the key or pattern is known.
- Pattern recognition (ROT, Base64, XOR) significantly accelerates deobfuscation.
- Script comments and structure can unintentionally aid defenders during analysis.
- Safe, isolated execution environments are critical when handling unknown scripts.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
