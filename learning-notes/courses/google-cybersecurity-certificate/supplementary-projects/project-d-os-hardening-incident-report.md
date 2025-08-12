# Annex D — OS Hardening Incident Report

## Incident Summary

**Date/Time of Incident:** Not specified (observed during investigation)  
**Organization:** YummyRecipesForMe.com  
**Analyst:** Jeremy Ray Jewell (Cybersecurity Analyst)  
**Incident Type:** Brute force attack leading to website compromise, malware injection, and malicious redirection  
**Impact:** Unauthorized access to administrative panel, modification of source code, malware distribution, user redirection to a malicious domain

---

## Network Protocol Identified

- **DNS (Domain Name System):** Used to resolve domain names (`yummyrecipesforme.com` and `greatrecipesforme.com`) to their respective IP addresses.
- **HTTP (HyperText Transfer Protocol):** Used to request and deliver webpage content and initiate file downloads.

---

## Detailed Incident Description

A disgruntled former employee executed a **brute force attack** on the administrative account of the company’s web host, exploiting the fact that the account password was still set to the **default password**. This attack consisted of repeated login attempts using known default credentials until the correct password was found.

Upon gaining administrative access, the attacker:

1. Accessed the website's **admin panel**.
2. Modified the website’s **source code**.
3. Embedded a **JavaScript function** that prompted users to download and run an executable file under the pretext of a browser update.
4. Changed the administrative password to prevent legitimate access.

When users visited the compromised site:

- The browser issued a **DNS request** for `yummyrecipesforme.com`.
- DNS replied with the correct IP address.
- The browser sent an **HTTP request** to load the website.
- The website prompted users to download the malicious executable.
- Upon execution, the file caused the browser to issue a **DNS request** for `greatrecipesforme.com`.
- DNS returned the IP address for `greatrecipesforme.com`.
- The browser sent an **HTTP request** to this malicious domain, which hosted further malware.

Customer complaints indicated:
- Slow computer performance post-infection.
- Visible domain name change after running the downloaded file.

The incident was confirmed through a **sandbox test** and **tcpdump network capture**.

---

## Root Cause

- **Weak authentication controls**: Administrative password left at factory default.
- **No brute force protection**: No lockout mechanism or rate limiting in place to prevent repeated login attempts.

---

## Recommendations

**Primary Security Measure to Prevent Brute Force Attacks:**
- **Implement strong authentication controls**:
  - Enforce **complex, unique administrative passwords**.
  - Deploy **account lockout policies** or **CAPTCHA challenges** after a set number of failed login attempts.
  - Use **multi-factor authentication (MFA)** for administrative accounts.

**Additional Hardening Measures:**
- Remove all default credentials upon deployment.
- Monitor authentication logs for unusual login patterns.
- Limit administrative panel access by IP address when possible.
- Conduct periodic **penetration testing** to identify and remediate vulnerabilities.

---

## References

- Google Cybersecurity Certificate – *Connect and Protect: Networks and Network Security*, Module 4
- NIST Cybersecurity Framework – Identify, Protect, Detect, Respond, Recover
