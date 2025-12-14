# Advent of Cyber 2025 – Day 13, 2025-12-13
**Room:** YARA – Hidden Messages
**Category:** Threat Hunting / Malware Detection
**Skills Practiced:** Writing YARA rules, regex construction, string detection, directory scanning, pattern-based hunting, decoding staged messages.

---

## Summary

In this challenge, McSkidy covertly communicated with the TBFC blue team by embedding hidden messages inside a directory of seemingly innocent image files. Rather than traditional malware detection, the task required **threat hunting using YARA** — identifying specific string patterns across multiple files to reconstruct a message.
The objective was to write a YARA rule that detects a keyword (TBFC:) followed by a code word, extract all matching code words from the image files, and decode McSkidy’s message by ordering them correctly.
This room reinforced how YARA can be used not only for malware detection, but also for **intelligence discovery and post-incident investigation**.

---

## Walkthrough Notes

### Environment Setup

After starting the target VM, the provided directory was located at `/home/ubuntu/Downloads/easter`. This folder contained multiple image files allegedly related to Easter preparations. The images themselves were not malicious executables, but they contained embedded strings relevant to the investigation.

### 1. Understanding the Detection Goal

The challenge specified that:
- Each relevant file contains the keyword `TBFC`:
- The keyword is immediately followed by an **ASCII alphanumeric code word**
- Multiple files may contain different code words
- The final message must be reconstructed after extracting all of them
This made YARA an ideal tool, since it excels at **pattern-based detection across large file sets**.

---

### 2. Designing the YARA Rule

I created a YARA rule focused on:
- Detecting the literal keyword `TBFC`:
- Matching one or more alphanumeric characters after the colon
- Using a **regular expression** for flexibility
The rule included:
- A `meta` section describing the rule’s purpose
- A `strings` section using a regex string
- A `condition` triggering when the pattern was found
Regex was required here because the code words varied between files and could not be hard-coded.

---

### 3. Running the YARA Scan

I executed YARA recursively against the Easter directory:
`yara -r -s rule.yar /home/ubuntu/Downloads/easter`
Flags used:
- `-r` to scan directories recursively
- `-s` to print the matched strings, allowing extraction of the code words
This produced output showing:
- Which image files matched
- The specific `TBFC:<codeword>` strings found inside each file 

---

### 4. Extracting and Reconstructing the Message

After identifying all matching files:
- I collected the extracted code words
- Ordered them as instructed by the challenge
- Decoded the final message sent by McSkidy
The result confirmed that the hidden communication was intentional and successfully recovered.

---

## Key Discovery

- YARA is not limited to malware — it’s a powerful hunting and discovery tool.
- Regex strings enable flexible detection when indicators vary between files.
- Embedded strings can exist in non-executable files such as images.
- Threat hunting often involves pattern recognition, not just known signatures.
- Clear metadata and well-scoped conditions make YARA rules reusable and readable.
- This exercise mirrors real-world scenarios where defenders uncover attacker intent from subtle artifacts.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
