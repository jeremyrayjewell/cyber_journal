# Advent of Cyber 2025 – Day 11, 2025-12-11
**Room:** Leave the Cookies, Take the Payload
**Category:** Web Security / Cross-Site Scripting (XSS)
**Skills Practiced:** Reflected XSS, Stored XSS, payload injection, identifying unsafe rendering, log inspection, basic input sanitization concepts.

---

## Summary
This challenge introduced the concepts of Reflected and Stored Cross-Site Scripting (XSS) through McSkidy’s secure message portal. By testing user-controlled input in both the search functionality (client-side reflection) and the stored messages feature (server-side persistence), I confirmed vulnerabilities that allowed JavaScript execution in the browser. The exercise demonstrates how improperly sanitized input can lead to session hijacking, defacement, or data theft.

---

## Walkthrough Notes

### 1. Testing for Reflected XSS

Navigating to the portal at `http://MACHINE_IP`. The search bar directly reflects user input into the results panel. I injected a simple test payload:

`<script>alert('Reflected Meow Meow')</script>`

Clicking Search Messages triggered a JavaScript alert(), confirming Reflected XSS. The System Logs panel displayed the payload execution, revealing the reflected XSS flag. 

---

### 2. Testing for Stored XSS

Next, I moved to the Send Message form. This input is stored on the backend and displayed whenever the page loads — a classic target for Stored XSS. I submitted the same payload:

`<script>alert('Stored Meow Meow')</script>`

After submission and page reload, the alert triggered on every visit, confirming Stored XSS. The challenge text includes an attacker-style stored XSS payload with a Base64-encoded flag:

`<script>alert(atob("VEhNe0V2aWxfU3RvcmVkX0VnZ30="))</script>`

Decoding the Base64 string provides the next flag.

---

## Key Discovery

- Reflected XSS executes immediately when input is echoed back without sanitization.
- Stored XSS persists on the server and executes for every user viewing the stored content.
- Avoid using innerHTML to render user input; use textContent instead.
- Cookies should be set with HttpOnly, Secure, and SameSite attributes.
- Always sanitize and encode user-supplied data to prevent script injection.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
