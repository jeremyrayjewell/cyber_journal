# Write-up: Natas 21 → 22  
**Date:** 2026-01-14  

## Obfuscated password (ROT13)  
`q8ejTOy0Kfyt3o76hu3sRoFyaBHOybmm`

---

## OBJECTIVE

> The objective of this level was to obtain the credentials for natas22 by exploiting insecure session sharing between two colocated web applications.  
> The challenge was to demonstrate that session integrity can be broken not only inside a single application, but also across multiple applications that trust the same session storage without proper isolation.

---

## PURPOSE

This level illustrates a critical architectural flaw: multiple applications sharing the same session backend without enforcing strict ownership or trust boundaries. While Natas20 focused on poisoning a session through malformed input inside one application, Natas21 expands the threat model:

- One application is allowed to write arbitrary session values.  
- Another application blindly trusts those values.  
- No authentication boundary exists between the two.  

This models a real-world class of vulnerabilities found in:

- Monolithic PHP deployments with shared session storage  
- Poorly designed SSO systems  
- Microservices that reuse session cookies without validation  

It demonstrates that even a “harmless” auxiliary app can become a privilege-escalation vector.

---

## SOLUTION

The main application (natas21) grants administrative privileges when the session contains:

```
$_SESSION["admin"] == 1
```

The colocated experimenter application (natas21-experimenter) contains this logic:

```
foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
}
```

This means every parameter supplied by the user is written directly into the session.

The exploit chain is:

1. Establish a valid PHP session on the experimenter application.  
2. Send a crafted request including:
   ```
   submit=1
   admin=1
   ```
3. The experimenter writes:
   ```
   $_SESSION["admin"] = "1"
   ```
4. Reuse the same session cookie on the real application.  
5. The real application checks:
   ```
   $_SESSION["admin"] == 1
   ```
   and grants administrative access.  
6. The credentials for natas22 are displayed and extracted.

This was implemented using a generic session poisoning framework that:

- Creates a session on one host  
- Mutates it using attacker-controlled parameters  
- Forces the same session cookie onto another host  
- Reads the protected resource  

The approach required no guessing, brute force, or cryptographic bypass. It relied entirely on broken trust boundaries between colocated applications and improper session ownership design.

### Automation

The exploit was implemented using the unified [session_injector.py](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/session_injector) framework, which supports both single-host and cross-host session poisoning without any challenge-specific logic.

For Natas21, the tool was used in **cross-host mode**, where one application mutates the session and another evaluates it.

Command used:

```bash
python3 session_injector.py \
  --mode cross-host \
  --inject-url http://natas21-experimenter.natas.labs.overthewire.org/index.php \
  --read-url   http://natas21.natas.labs.overthewire.org/index.php \
  --user natas21 \
  --password <PASSWORD> \
  --require-submit \
  --submit-key submit \
  --submit-value 1 \
  --kv admin=1
```

This command performs the following generically:

1. Establishes a session on the injection endpoint.  
2. Captures the session identifier.  
3. Injects attacker-controlled key/value pairs into the session.  
4. Forces reuse of the same session identifier against the target endpoint.  
5. Detects privileged access and extracts protected credentials.  

The framework contains no challenge-specific logic. All behavior is controlled by command-line parameters, making it reusable for:

- Single-application session poisoning  
- Cross-application session poisoning  
- Arbitrary cookie names  
- Arbitrary parameter names  
- Arbitrary session mutation strategies  

---

## TAKEAWAYS

- Session data must never be writable by untrusted applications.  
- Sharing session storage across applications creates an implicit trust relationship.  
- Any application that can write to the session becomes an authentication authority.  
- Cross-application session poisoning is more dangerous than single-app injection because it breaks architectural boundaries.  
- Security must be enforced at the session design level, not only at the application logic level.  
- Insecure auxiliary tools (“experimenters”, dashboards, debug apps) frequently become real attack surfaces.  

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
