# Write-up: Natas 00 → 01  
**Date:** 2025-08-24   

## Obfuscated password (ROT13)

`0amPvtNd7g2vNYliH9kpUyLA4ZyxVjyd` 

## OBJECTIVE

> "The username is `natas0` and the password is `natas0`. The goal is to log into http://natas0.natas.labs.overthewire.org and find the password for `natas1`. All Natas level passwords are also stored in `/etc/natas_webpass/` but only accessible to the relevant level."
> "You can find the password for the next level on this page."

## PURPOSE ##

This first Natas level is a simple introduction to web-security challenges. Unlike Bandit (SSH, filesystem, POSIX tools), Natas focuses on how websites deliver information to the client and how careless coding can leak secrets.

- **HTTP Basic Auth**: the browser sends a base64-encoded `username:password` in the `Authorization` header for each request after you authenticate.  
- **View Source**: HTML delivered to the client may include developer comments or hidden elements that are not visible in the rendered page but are still fully retrievable.

## SOLUTIONS ##

- Navigate to the level in a browser:  
  URL: `http://natas0.natas.labs.overthewire.org`  
  Username: `natas0`  
  Password: `natas0`

- The page states: “You can find the password for the next level on this page.” Nothing obvious appears in the rendered content, so inspect the **page source** (Ctrl+U / ⌘+Option+U).

- In the HTML, an embedded comment reveals the credential for the next level:

  <!--The password for natas1 is [REDACTED] --> 

- Use that password to authenticate as **natas1** on the next level.

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
