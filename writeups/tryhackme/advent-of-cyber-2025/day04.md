# Advent of Cyber 2025 – Day 4, 2025-12-04
**Room:** AI Cybersecurity Showcase – Van SolveIT  
**Category:** AI in Cybersecurity / Automation  
**Skills Practiced:** Using AI for red-team automation, log triage, vulnerability analysis, exploit generation, and secure coding review.

---

## Summary
TBFC is trialing a new AI cybersecurity assistant, **Van SolveIT**, to accelerate both defensive and offensive workflows. This challenge demonstrates practical applications of AI across three domains:

- **Red Team:** Generate and run an exploit against a deliberately vulnerable web application.
- **Blue Team:** Use the AI agent to triage and interpret Web server logs from an attack.
- **Software Security:** Use AI to review source code and identify vulnerabilities.

The room ends by retrieving two flags:  
1. The main Van SolveIT showcase completion flag  
2. The flag printed by the exploit script when executed against the vulnerable app

---

## Walkthrough Notes

### Connecting to the Machine
Two machines must be started:
- **AttackBox** (where the exploit will be executed)
- **Target VM** (hosts the vulnerable app and the AI assistant)

Van SolveIT is accessed via `http://MACHINE_IP` and the vulnerable web application is accessed via `http://MACHINE_IP:5000`

---

## My Steps


I followed the AI assistant through three stages:
- The AI produced a Python exploit script.
- The script targeted the vulnerable login endpoint.
- I saved it to the AttackBox as `script.py`.

The script originally contained `http://machine_ip:5000/login.php`. I updated it manually to include the actual IP. This allowed the exploit to execute properly. After replacing the placeholder IP:

```bash
python3 script.py
```

The output returned the exploit flag required for the second question.

Van SolveIT analyzed web logs from a simulated attack and provided:

- Suspicious IP enumeration  
- Path traversal and injection indicators  
- Webshell and ransomware execution traces  
- Exfiltration behavior  

This section mirrored real SOC workflows, but automated. ThenVan SolveIT reviewed application code for vulnerabilities and described:

- Input validation issues  
- Missing authentication checks  
- Insecure coding patterns  

After completing all stages, Van SolveIT presented the showcase completion flag.

---

## Key Takeaways

- **AI is now part of real-world SOC and pentest workflows** — this exercise shows exactly how.
- AI-generated exploits can be useful but **must be validated and corrected manually** (e.g., fixing URLs).
- AI can accelerate log analysis and code review, but still requires **human judgement**.
- This room helps reinforce modern expectations for cybersecurity roles: familiarity with AI-augmented investigation and automation.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
