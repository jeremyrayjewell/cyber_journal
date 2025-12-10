# Advent of Cyber 2025 – Day 8, 2025-12-08
**Room:** Evil Elf Login Portal – SQL Injection 
**Category:** Web Exploitation / SQL Injection
**Skills Practiced:** Input fuzzing, SQLi login bypass, analyzing backend query behavior, privilege escalation through authentication flaws.

---

## Summary
This challenge introduced a deliberately insecure login system used by the elves. The username and password fields were directly concatenated into a backend SQL query without parameterization, making the authentication process vulnerable to SQL injection. By injecting a condition that always evaluates to TRUE, I bypassed the login entirely and accessed the admin area, where the final flag was displayed.
---

## Walkthrough Notes

### 1.Initial Page Inspection
Navigating to the portal revealed a basic login page with two fields:
- Username
- Password

There were no rate limits, no account lockouts, and no visible server-side validation.

Viewing the source confirmed no client-side filtering or obfuscation — a strong indication the challenge expected SQL injection.

---

### 2. Testing for SQL Injection

I began by entering a single quote (`'`) into the username field. Many applications will error on this if the string is improperly escaped.
The page responded with a generic “invalid login,” but not a full SQL error.
Still, the structure suggested a simple query like:
```
SELECT * FROM users 
WHERE username = '<input>' AND password = '<input>';
```
---

### 3. Performing the Authentication Bypass

The classic SQL injection payload that forces authentication to always succeed is `' OR 1=1--`.
I entered it into the username field and left the password blank.
The appended logic terminates the original string, then injects a universal TRUE condition, and comments out the remainder.

Submitting this payload granted immediate access to the admin dashboard.

---

### 4. Retrieving the Flag

Once authenticated, the admin page displayed configuration information, an access log, and the challenge flag.
No further exploitation was necessary — the SQLi bypass was the only required vulnerability.

---

## Key Discovery

- Login forms that concatenate user input into SQL queries without escaping or prepared statements are trivially bypassed.
- A Boolean-based injection (`OR 1=1`) is often enough to trick the backend into treating an attacker as a valid user.
- Authentication bypasses often require **no password at all** — the application simply evaluates the injected logic.
- SQLi remains one of the most common and impactful vulnerabilities, especially where authentication and access control are involved.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
