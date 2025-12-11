# Advent of Cyber 2025 – Day 1 , 2025-12-01 
**Room:** Linux CLI – Shells Bells  
**Category:** Linux Fundamentals  
**Skills Practiced:** Navigating Linux filesystems, working with hidden files, reading logs, using grep, using find, reading shell scripts, switching users, inspecting /etc/shadow, accessing bash history, SSH tunneling, and interpreting clues.

---

## Summary
This challenge introduces the Linux command-line interface in the context of investigating the disappearance of McSkidy. The TBFC team suspects HopSec Island attackers tampered with the Christmas wishlist server (`tbfc-web01`). My goal was to follow McSkidy’s clues, inspect the system, uncover malicious changes, and collect flags along the way.

This writeup includes the actual commands I entered, the incorrect attempts and misunderstandings I resolved, and the full investigative process, including the optional Side Quest hidden in McSkidy’s home directory.

---

## Walkthrough Notes

### Connecting to the Machine
You can connect in two ways:

1. THM split-view terminal (auto-loaded)
2. SSH from your own machine:

```bash
ssh mcskidy@MACHINE_IP
# password: AoC2025!
```

Useful commands for this room:

```bash
ls -la
pwd
cd /path
cat filename
grep -r "keyword" .
```

---

## My Steps

### 1. Connecting to the machine
I connected via SSH: `ssh mcskidy@10.65.130.60`

---

## 2. Locating McSkidy’s hidden guide
`ls` inside the `Guides` directory. Nothing showed until I listed hidden files, `la -a`. I then read the guide with `cat`. It revealed a hint to check `/var/log/` using `grep` the first flag.

**Mistakes made:**

I attempted invalid syntax a few times. Oops!

---

## 3. Inspecting logs for suspicious activity

```bash
cd /var/log
grep "Failed password" auth.log
```

This revealed repeated failed login attempts from HopSec-controlled IPs.

---

## 4. Hunting for “Eggsploit” files

```bash
find /home/socmas -name *egg*
```

Result:

```
/home/socmas/2025/eggstrike.sh
```

---

## 5. Analyzing the Eggstrike script

```bash
cat /home/socmas/2025/eggstrike.sh
```

The script:

- sorted wishlist entries to `/tmp/dump.txt`
- deleted the original wishlist
- replaced it with EASTMAS data

And revealed another flag:

```
THM{sir-carrotbane-attacks}
```

---

## 6. Exploring system utilities and privilege boundaries

Attempting to read `/etc/shadow`, returned "Permission denied." To inspect further, changed to root. I

---

## 7. Digging through root’s Bash history

Inside `/root`:

```bash
cat .bash_history
```

One of the final lines contained the key for the main objective.

---

# Side Quest 1 — Optional Advanced Puzzle

McSkidy left an extra message in her Documents directory:

```bash
cd /home/mcskidy/Documents
cat read-me-please.txt
```

This unlocked a new set of credentials and hinted at three hidden passcode fragments.

## Egg #1

Clue:

> “I ride with your session… open the little bag your shell carries.”

Meaning: environment variables... `env` returned password fragment #1.

## Egg #3 (found before #2)

Searching recursively with `grep -Ri "frag" ~/` returned password fragment #3. Oops!

---

## Egg #2

Deduced password fragment #2 from the contents of the other two fragments.

---

## Key Takeaways

- Hidden files frequently contain relevant clues (`ls -a`)
- Environment variables can store secrets (`env`)
- `grep` is essential for triage and searching logs
- `find` is valuable for locating suspicious files
- Bash history often reveals attacker behavior
- Privilege escalation changes visibility drastically
- Optional side quests reinforce real-world investigative techniques  
- Understanding users, permissions, and logs is core SOC analyst competency

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
