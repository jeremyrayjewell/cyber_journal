# Advent of Cyber 2025 – Day 2, 2025-12-02
**Room:** Phishing – The Red Team Strikes Back  
**Category:** Social Engineering / Offensive Security  
**Skills Practiced:** Social engineering concepts, phishing fundamentals, fake login page hosting, credential harvesting, Social-Engineer Toolkit (SET), SMTP routing, red-team operational flow, credential reuse verification.

---

## Summary
This challenge focused on phishing from a red-team perspective. As part of TBFC’s scheduled penetration testing, my task was to create and deliver a phishing email containing a fake TBFC login page, capture any credentials entered, and verify whether those credentials were reused on the organization’s mail portal. This writeup documents each step I performed, including the full operational workflow, mistakes made, and the commands used.

---

## Walkthrough Notes

### Connecting to the Machines
Two virtual machines were required:
- AttackBox (used for SET and hosting the phishing login page)
- Target Machine (hosting the email portal)

Both must be started before beginning the exercise.

---

## My Steps

### 1. Hosting the Fake TBFC Login Portal
The challenge provided a credential-capturing phishing server. On the AttackBox, I ran:
```
cd ~/Rooms/AoC2025/Day02
./server.py
```
The output indicated:
```
Starting server on http://0.0.0.0:8000
```
I verified the page using Firefox.
The cloned login page rendered correctly.

---

### 2. Using the Social-Engineer Toolkit (SET) to Send the Phishing Email
I launched SET:
```
setoolkit
```

Then navigated:
```
    1 → Social-Engineering Attacks
    5 → Mass Mailer Attack
    1 → E-Mail Attack Single Email Address
```

SET prompted for details, which I filled as follows:
```
    Send email to: factory@wareville.thm
    Delivery method: Use your own server or open relay
    From address: updates@flyingdeer.thm
    From name: Flying Deer
    Open-relay username: (blank)
    Open-relay password: (blank)
    SMTP server: MACHINE_IP
    Port: 25
    High priority: no
    Attach file: n
    Attach inline file: n
    Subject: Shipping Schedule Changes
    Body: includes http://ATTACKBOX_IP:8000
    End with: END
```
Mistakes made:
- Initially used the AttackBox IP instead of MACHINE_IP as the SMTP server.
- Restarted SET via Ctrl+C after misformatting the email body once.

Successful send confirmed:
```
[*] SET has finished sending the emails
```
---

### 3. Monitoring the Fake Login Page for Harvested Credentials
With server.py still running, I waited for output. The captured credentials appeared.
This answered the first question, password to access the TBFC portal.

---

### 4. Checking for Credential Reuse in the Mail Portal
On the AttackBox’s browser, I visited `http://MACHINE_IP`. I attempted login as `factory` with the credentials received for `admin`. The login succeeded. Inside the mailbox I located a shipping schedule email listing to find the total number of toys expected for delivery.

---

## Key Takeaways
- Social engineering exploits human tendencies, not software vulnerabilities.
- Effective phishing requires both a realistic lure and a functional trapping mechanism.
- SET provides structured tooling for red-team email campaigns.
- Credential harvesting must be monitored in real time.
- Credential reuse remains a critical organizational security weakness.
- This exercise reinforces core offensive and defensive concepts relevant to SOC and red-team operations.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
