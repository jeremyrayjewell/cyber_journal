# Write-up: Natas 20 → 21  
**Date:** 2026-01-02  

## Obfuscated password (ROT13)  
`OCui63pXR1yxDy04pR5PhSGmKr15AsvU`

---

## OBJECTIVE

> The objective of this level was to obtain the credentials for natas21 by exploiting insecure session handling logic.  
> Unlike previous challenges, the vulnerability did not rely on guessing or predicting session identifiers, but on manipulating how session data itself was stored and interpreted by the server.

---

## PURPOSE

This challenge demonstrates the dangers of trusting user-controlled input within server-side session storage.  
Although the application used PHP’s session mechanism, it failed to properly sanitize or isolate user-provided values before writing them to the session file.

As a result, it was possible to inject arbitrary session variables by abusing the way the server serialized session data. This allowed full privilege escalation without authentication, brute force, or session ID prediction.

Natas20 models a classic **single-application session poisoning** vulnerability, where the same application both writes and later trusts unsafe session content.

---

## SOLUTION

The application accepted a `name` parameter and stored it directly in the session file using a custom session handler. Because newline characters were not filtered, a crafted value could inject additional key–value pairs into the session storage.

By submitting a payload containing a newline followed by `admin 1`, the server wrote a forged administrator flag into the session file. On subsequent requests, the application trusted this value and granted administrative access.

Conceptually, the attack is:

1. Establish a valid session.
2. Inject a crafted value containing a newline.
3. Force the session file to contain:
   ```
   admin 1
   ```
4. Reuse the same session.
5. Trigger privilege escalation.

This was implemented using the unified [session_injector.py](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/session_injector) framework, configured in **single-host mode**.

In this mode, the same application is responsible for:

- Writing session data
- Reading session data
- Enforcing authorization

### Automation

Command used:

```bash
python3 session_injector.py \
  --mode single-host \
  --inject-url http://natas20.natas.labs.overthewire.org/index.php \
  --read-url   http://natas20.natas.labs.overthewire.org/index.php \
  --user natas20 \
  --password <PASSWORD> \
  --param name \
  --payload $'anyone\nadmin 1'
```

This command performs the following generically:

1. Establishes a valid session with the target application.  
2. Injects attacker-controlled input into the session via the `name` parameter.  
3. Exploits newline-based session file injection.  
4. Re-enters the same application using the poisoned session.  
5. Detects privileged access and extracts protected credentials.

The framework contains no challenge-specific logic.  
All behavior is controlled by command-line parameters, making it reusable for any application vulnerable to single-host session poisoning.

---

## UPDATE: Unified Session Injector Framework

This level was originally solved using a purpose-built script. It has since been fully integrated into the unified [session_injector.py](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/session_injector) framework, which now supports both:

- Single-host session poisoning (Natas20 style)
- Cross-host session poisoning (Natas21 style)

This update reflects a shift from challenge-specific tooling to a generic session exploitation framework that models real-world session integrity failures. Natas20 maps directly to the **single-host mode** of the framework, where one application both writes and trusts its own session data. Updated command using the unified tool:

```bash
python3 session_injector.py \
  --mode single-host \
  --inject-url http://natas20.natas.labs.overthewire.org/index.php \
  --read-url   http://natas20.natas.labs.overthewire.org/index.php \
  --user natas20 \
  --password p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw \
  --param name \
  --payload $'anyone\nadmin 1'
```
This command performs the following generically:
1. Establishes a valid session with the target application.
2. Injects attacker-controlled input into the session via the name parameter.
3. Exploits newline-based session file injection.
4. Re-enters the same application using the poisoned session.
5. Detects privileged access and extracts protected credentials.
The framework contains no challenge-specific logic. All behavior is controlled entirely through configuration parameters. This update demonstrates that Natas20 is not an isolated trick, but an instance of a broader vulnerability class: single-application session poisoning, which is commonly found in applications that treat session storage as a trusted data serialization layer rather than an integrity-protected security boundary.

---

## TAKEAWAYS

- Session data must never be constructed directly from unsanitized user input.  
- Newline injection in session files can lead to full privilege escalation.  
- Session poisoning is more dangerous than session ID guessing because it compromises trust, not randomness.  
- Applications must strictly validate how session data is written and parsed.  
- Custom session handlers are especially dangerous when they treat session files as line-based key/value stores.  
- Session security is a data integrity problem, not just an authentication problem.  

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
