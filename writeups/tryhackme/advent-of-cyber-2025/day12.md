# Advent of Cyber 2025 – Day 12, 2025-12-12
**Room:** Phishing – Email Threat Triage
**Category:** Incident Response / Email Security
**Skills Practiced:** Phishing detection, email header analysis, impersonation spotting, spoofing identification, typosquatting and punycode recognition, attachment risk analysis, distinguishing spam from phishing.

---

## Summary
With TBFC’s Email Protection Platform offline, the SOC team was forced to manually triage suspicious emails using the **Wareville Email Threat Inspector**. The objective of this challenge was to correctly classify incoming messages as either **phishing or non-threatening spam**, while identifying the specific techniques used by attackers attempting to compromise TBFC users.

This task emphasized analyst judgement rather than tooling, requiring careful inspection of sender details, message intent, headers, domains, and attachments. Each phishing message contained multiple indicators that had to be identified correctly to proceed.
---

## Walkthrough Notes

### Accessing the Email Threat Inspector

After starting the target machine, I accessed the Wareville Email Threat Inspector via the provided web interface. The platform displayed a set of emails that needed to be individually reviewed and classified. For each email, the task was to:
- Decide whether the message was phishing or not
- Identify multiple concrete indicators supporting that classification

### 1. Distinguishing Spam vs. Phishing

Before diving into individual emails, I established a clear mental distinction:
- **Spam**: Unwanted or promotional content with no clear malicious intent
- **Phishing**: Targeted deception intended to steal credentials, deliver malware, or manipulate user behavior
The intent behind the message mattered more than whether it was merely annoying.. 

---

### 2. Identifying Impersonation

Several emails attempted to impersonate trusted TBFC personnel or departments. I evaluated impersonation by checking:
- Sender display name versus actual email domain
- Whether the sender domain matched TBFC’s internal naming conventions
- Use of free or external email providers
Any mismatch immediately raised suspicion.
---

### 3. Social Engineering Indicators

Phishing emails consistently relied on psychological pressure. Common patterns included:
- Urgent language (“urgent”, “immediately”, “action required”)
- Requests to bypass normal communication channels
- Appeals to authority or emergency situations
Messages attempting to rush or isolate the recipient were treated with high suspicion. 

---

### 4. Typosquatting and Punycode Abuse

Some emails used visually deceptive domains. I carefully inspected:
- Slight misspellings of legitimate domains
- Unicode characters masquerading as Latin letters
- The Return-Path and header encoding to reveal punycode usage
Checking headers proved essential for uncovering these techniques.

---

### 5. Spoofing via Header Analysis

Certain emails appeared legitimate at first glance but failed authentication checks. I reviewed:
- SPF results
- DKIM signatures
- DMARC enforcement
Failures across these controls confirmed spoofed messages, even when the visible sender looked trustworthy.

---

### 6. Malicious Attachments and Modern Phishing Trends

Attachments and links were evaluated based on:
- File type (HTML/HTA vs. PDFs or documents)
- Whether the email attempted to move the user to a third-party platform
- Use of legitimate services (OneDrive, document sharing portals) as lures
The challenge highlighted how modern phishing avoids direct malware delivery in favor of credential theft via fake login pages.

---

## Key Discovery

- Phishing is defined by intent, not just appearance.
- Display names are meaningless without verifying domains and headers.
- Typosquatting and punycode are increasingly common and easy to miss.
- SPF, DKIM, and DMARC failures are strong indicators of spoofing.
- HTML attachments remain dangerous due to lack of browser sandboxing.
- Many modern phishing attacks rely on legitimate platforms to bypass defenses.
- Manual triage requires patience, skepticism, and consistency.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
