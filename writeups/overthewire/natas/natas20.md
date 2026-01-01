# Write-up: Natas 20 → 21  
**Date:** 2026-01-02  

## Obfuscated password (ROT13)  
`OCui63pXR1yxDy04pR5PhSGmKr15AsvU`

---

## OBJECTIVE

>The objective of this level was to obtain the credentials for natas21 by exploiting insecure session handling logic. Unlike previous challenges, the vulnerability did not rely on guessing or predicting session identifiers, but on manipulating how session data itself was stored and interpreted by the server.
 
---

## PURPOSE

This challenge demonstrates the dangers of trusting user-controlled input within server-side session storage.
Although the application used PHP’s session mechanism, it failed to properly sanitize or isolate user-provided values before writing them to the session file.

As a result, it was possible to inject arbitrary session variables by abusing the way the server serialized session data. This allowed elevation of privileges without authentication or brute-force techniques.

---

## SOLUTION

The application accepted a name parameter and stored it directly in the session file using a custom session handler. Because newline characters were not filtered, a crafted value could inject additional key–value pairs into the session storage.
By submitting a payload containing a newline followed by admin 1, the server wrote a forged administrator flag into the session file. On subsequent requests, the application trusted this value and granted administrative access.
To automate this process, a [dedicated script (session_injector.py)](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/session_injector) was used to:
- Establish a valid session
- Inject a crafted session payload (`name=anyone\nadmin 1`)
- Reuse the same session to trigger privilege escalation
- Extract the credentials for the next level
This approach required no guessing or brute-force and relied entirely on flawed session handling logic.

---

## TAKEAWAYS

- Session data must never be constructed directly from unsanitized user input.
- Session poisoning is a powerful attack vector when session storage is improperly designed.
- Trusting session contents without strict validation can fully compromise authentication.
- Separation of session logic and user input handling is critical for secure application design.

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
