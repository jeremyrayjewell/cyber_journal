# blind_sqli_extractor

A reusable blind SQL injection automation tool designed for controlled security testing and educational use.
This script was developed while solving OverTheWire Natas (levels 15 and 17) and is written to support both boolean-based and time-based blind SQL injection techniques.

![Blind SQLi Extractor Screenshot](blind_sqli_extractor.png)

---

## Overview

Many vulnerable applications do not return query results directly. Instead, they reveal information indirectly through response behavior such as timing differences or conditional output.

This tool exploits those behaviors to extract sensitive values one character at a time in a reliable and repeatable way.

The primary goals are clarity, correctness, and reusability.

---

## How It Works

- A crafted SQL payload is injected into a vulnerable parameter.
- The payload evaluates a condition on a specific character of the target value.
- The application’s response indicates whether the condition evaluated to true.
- The script iterates through characters until the full value is recovered.
- The tool supports both boolean-based and time-based inference techniques.

---

## Usage

```
python3 blind_sqli_extractor.py \
  url \
  user \
  password \
  target \
  mode
```
---

## Arguments

--url
Target URL
--user
HTTP authentication username
--password
HTTP authentication password
--target
Target username whose value is being extracted
--mode
Extraction method: boolean or time

---

## Use Case

This tool was used to solve the OverTheWire Natas challenges where application responses reveal only boolean conditions or timing differences. By systematically testing each possible character, the full secret value can be reconstructed.

---

## Ethical Notice

This tool is intended solely for educational use and authorized security testing.
Do not use it against systems you do not own or have permission to test.

---

## Author

Jeremy Ray Jewell  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
