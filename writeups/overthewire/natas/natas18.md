# Write-up: Natas 18 → 19  
**Date:** 2025-12-31  

## Obfuscated password (ROT13)  
`gajRE7CqsJxkfT4SAJHgbNM9IlMGWdWe`

---

## OBJECTIVE

> The goal of this level was to obtain the credentials for natas19 by exploiting a weakness in session handling. Unlike previous challenges, no SQL injection or direct input manipulation was possible. Instead, the vulnerability existed in how session identifiers were generated and validated by the application.
> 
---

## PURPOSE

This challenge demonstrates the security risks of predictable session identifiers. Rather than relying on cryptographic randomness, the application generated session IDs using a small numeric range. Because the server trusted any provided session identifier, it was possible to enumerate active sessions and locate one belonging to an authenticated administrator.

The purpose of this exercise was to identify and exploit that weakness by programmatically testing session identifiers until a privileged session was discovered.

---

## SOLUTION

Inspection of the source code revealed that session IDs were generated using a simple numeric range and stored server-side. The application accepted any value provided via the PHPSESSID cookie and did not validate whether the session originated from a legitimate login.
To exploit this, I wrote [an enumeration tool (session_enumerator.py)](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/session_enumerator) that:
- Iterated through all possible session ID values.
- Sent each candidate as the PHPSESSID cookie in an authenticated request.
- Inspected the server response for indicators of admin access.
- Stopped execution when a valid admin session was identified.
Once the correct session ID was discovered, the server returned the credentials for the next level, confirming successful exploitation.
This approach required no brute-force of credentials and no SQL injection, only careful analysis of session handling behavior.

Example command used with [session_enumerator.py](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/session_enumerator) during testing:

```bash
python session_enumerator.py \
  --url http://natas18.natas.labs.overthewire.org \
  --user natas18 \
  --password <REDACTED> \
  --mode numeric
```

---

## TAKEAWAYS

- Session identifiers must be cryptographically unpredictable.
- Trusting client-supplied session values is fundamentally insecure.
- Session management flaws can completely bypass authentication mechanisms.
- Reusable tooling makes it easier to identify recurring vulnerability patterns.

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
