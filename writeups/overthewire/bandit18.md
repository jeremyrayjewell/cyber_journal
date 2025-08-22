# Write-up: Bandit 18 → 19
**Date:** 2025-08-10

## Obfuscated password (ROT13)
`pTJcZnXKIjQHAtCNIWoJLhTUIa9my3w8`  

## OBJECTIVE
> “The password for the next level is stored in a file `readme` in the home directory. Unfortunately, someone has modified `.bashrc` to log you out when you log in with SSH.”

## PURPOSE
We must bypass an **interactive shell trap** using **non-interactive SSH commands**.

Situations like this (“print a message and exit”) do occur in the wild, e.g.:

- Service/automation accounts (backup, deploy, CI runners)
- Bastion/jump hosts that present a menu
- HPC clusters / build farms disallowing interactive shells
- SFTP-only or chrooted users
- Incident response / quarantine accounts
- Honeypots / tripwires

**Clue:** You’re kicked out before getting a prompt → interference in the **interactive login** path, usually a shell startup file. From bandit17 you can list `~bandit18` (dir is `r-x`), see `.bashrc`, but **can’t read it** (files are typically `640`: owner+group readable, others none). So you infer: “interactive is trapped; try non-interactive.”

**Non-interactive SSH** is an intended SSH feature: anything you place **after** the host runs **as a single remote command** without starting an interactive shell. Because Bash doesn’t treat this as interactive, `.bashrc` won’t execute (or it returns immediately at its guard).

Test first:
```bash
ssh -p 2220 bandit18@bandit.labs.overthewire.org 'echo ok'
```
If you see `ok`, non-interactive works. Then retrieve the password:
```bash
ssh -p 2220 bandit18@bandit.labs.overthewire.org 'cat /home/bandit18/readme'
```

(Use single quotes so your **local** shell doesn’t expand anything. Absolute path is just explicit; `~/readme` also works.)

If you want to be extra explicit about bypassing startup files:
```bash
ssh -p 2220 bandit18@bandit.labs.overthewire.org \
  'bash --noprofile --norc -c "cat ~/readme"'
```

You can also copy the file non-interactively:
```bash
scp -P 2220 bandit18@bandit.labs.overthewire.org:/home/bandit18/readme .
```

## SOLUTIONS
- **Test non-interactive path**
  ```bash
  ssh -p 2220 bandit18@bandit.labs.overthewire.org 'echo ok'
  ```
- **Get the password**
  ```bash
  ssh -p 2220 bandit18@bandit.labs.overthewire.org 'cat /home/bandit18/readme'
  ```
- **(Optional) Bypass startup files explicitly**
  ```bash
  ssh -p 2220 bandit18@bandit.labs.overthewire.org 'bash --noprofile --norc -c "cat ~/readme"'
  ```
- **(Optional) Copy locally**
  ```bash
  scp -P 2220 bandit18@bandit.labs.overthewire.org:/home/bandit18/readme .
  ```

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
