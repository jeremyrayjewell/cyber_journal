# Advent of Cyber 2025 – Day 5, 2025-12-05
**Room:** IDOR – It’s Dangerously Obvious, Really  
**Category:** Web Security / Access Control  
**Skills Practiced:** Authentication vs. authorization logic, identifying insecure direct object references (IDOR), horizontal privilege escalation, analyzing client-side references (localStorage, Base64, MD5), understanding UUIDv1 predictability.

---

## Summary
This challenge focused on identifying and exploiting IDOR vulnerabilities within the “TryPresentMe” web application. The elves discovered suspicious account activity tied to Sir Carrotbane, and my task was to replicate how an attacker could access other users’ data simply by manipulating object references (user IDs, Base64-encoded IDs, hashed IDs, and UUIDv1 voucher codes).

The core lesson: **if the server does not validate authorization for each request, anything the client can reference, the client can also attack.**

---

## Walkthrough Notes

### Connecting to the Machine
I launched both:
- **AttackBox**  
- **Target Machine**

Then opened the web app at `http://MACHINE_IP` and logged in with the provided credentials:
```
username: niels
password: TryHackMe#2025
```

---

## My Steps

### 1. Finding the Basic IDOR (user_id manipulation)
After logging in, I opened DevTools → Network → refreshed the page.

The `view_accountinfo` request showed `user_id=10`.

Then I opened DevTools → Application → Local Storage and found:

`auth_user: {"user_id": 10, ...}`
I changed it to:
`{"user_id": 11}`

Refreshing the page instantly logged me in as a *different user*.

This confirmed a **classic IDOR + horizontal privilege escalation**.

I reset the value back to 10 afterward.

---

### 2. IDOR via Base64-encoded child IDs
Clicking the **eye icon** next to a child sent a request like:
`/children/Mg==`

`Mg==` decodes to `2`, meaning the endpoint is still using predictable numeric IDs, just Base64-wrapped—still fully vulnerable.

---

### 3. IDOR via MD5-hashed child IDs
Clicking the **edit icon** produced:
`/children/3a1cdad1b6a4e8a51bb1dcfe8e4c1bfd`

This looks random, but is just:
`md5("2")`

Meaning: **same IDOR, different disguise.**

If you know the pattern, you can recreate any hashed child ID.

---

### 4. UUIDv1 voucher predictability
The vouchers shown on the parent dashboard looked like this:
`xxxxxxxx-xxxx-11ee-xxxx-xxxxxxxxxxxx`

UUID version **1** embeds:
- timestamp  
- MAC address  
- clock sequence

This means an attacker can recreate valid vouchers if they know the exact minute of generation — which is why UUIDv1 should *never* be used for security tokens.

(This logic is used later for the bonus task.)


---

## Key Takeaways
- IDOR is fundamentally an **authorization failure**, not an authentication issue.
- Hiding IDs (Base64, hashing, UUIDs) does not secure them.
- Vulnerable applications allow attackers to “become” any user simply by changing identifiers in localStorage or request parameters.
- Proper server-side authorization checks must inspect:  
  - **Who is making the request?**  
  - **Do they own or have permission to access this resource?**
- Even seemingly random identifiers can be reversible or predictable.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)



