# Write-up: Natas 22 → 23  
**Date:** 2026-01-15  

## Obfuscated password (ROT13)  
`qVHDpV3hFhf1WRBFFJENRKOT8XoE8gEf`

---

## OBJECTIVE

> The objective of this level was to obtain the credentials for natas23 by exploiting a control-flow vulnerability where a redirect was incorrectly treated as an access control mechanism.  
> The challenge was to demonstrate that sending a redirect header does not stop program execution and does not prevent sensitive data from being included in the HTTP response.

---

## PURPOSE

This level illustrates a fundamental mistake in web application security: confusing client-side behavior with server-side enforcement.

The developer assumed that:

    header("Location: /");

was equivalent to:

    deny access and stop execution

But in HTTP, a redirect is only an instruction to the browser.  
It does not stop PHP from continuing to execute code or from sending sensitive data in the response body.

This models a real-world class of vulnerabilities where:

- Access control is implemented with redirects instead of program termination  
- Sensitive content is generated even after “blocking” logic is triggered  
- Security depends on client behavior rather than server enforcement  

It demonstrates that redirects are not security controls.

---

## SOLUTION

The vulnerable logic was:

    if(array_key_exists("revelio", $_GET)) {
        if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {
            header("Location: /");
        }
    }

Later in the same request, the application prints the protected credentials:

    if(array_key_exists("revelio", $_GET)) {
        print "You are an admin...";
    }

The problem is that after issuing the redirect header, the script never calls:

    exit;

So execution continues and the sensitive data is still written into the response body.

Browsers automatically follow the redirect and hide the body.  
But the body is already present in the HTTP response.

The exploit is therefore:

1. Request the protected endpoint:
       /index.php?revelio=1
2. Use a client that does not follow redirects.
3. Read the response body directly.

Command used:

    curl -u natas22:<password> -i http://natas22.natas.labs.overthewire.org/index.php?revelio=1

This returns:

    HTTP/1.1 302 Found
    Location: /

    You are an admin. The credentials for the next level are:
    Username: natas23
    Password: <PASSWORD>

No session manipulation, no privilege escalation, and no injection was required.  
The server leaked the credentials in the same response that attempted to redirect the user.

---

## TAKEAWAYS

- A redirect is not a security control.  
- Access control must be enforced by terminating execution, not by client instructions.  
- Sensitive data should never be generated if access checks fail.  
- Browsers hide dangerous behavior by following redirects automatically.  
- Security must not rely on how clients behave.  

The correct secure pattern is:

    header("Location: /");
    exit;

This level demonstrates that control flow is part of security, and mistakes at that layer can be just as catastrophic as cryptographic or authentication failures.

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
