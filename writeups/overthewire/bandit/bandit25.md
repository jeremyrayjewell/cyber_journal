# Write-up: Bandit 25 → 26
**Date:** 2025-08-17

## Obfuscated password (ROT13) 
`<add after solving>`

## OBJECTIVE
> "Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.  
>
> NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead."

## PURPOSE

First, identify **which shell** bandit26 uses, then learn **how that shell behaves** and **escape** it to read the next password.

1) **See bandit26’s login shell**
   ```bash
   grep '^bandit26:' /etc/passwd
   ```
   You’ll see a non-bash shell (typically `/usr/bin/showtext`).

2) **Understand what that shell does**
   It shows a text file via a pager (e.g., `more`) and then exits. If the pager detects a **small terminal**, it becomes **interactive** and shows a `--More--` prompt with extra keys enabled (like opening `vi`).

3) **Log in as bandit26 using the provided key (from bandit25)**
   ```bash
   # Adjust the key path/name if different on your box
   ssh -i /home/bandit25/.ssh/id_rsa bandit26@localhost -p 2220
   ```
   > If your terminal is too tall, the pager may dump output and disconnect immediately. **Shrink your terminal height** (e.g., ~10 lines) *before* you connect so you get the `--More--` prompt.

4) **Break out via the pager → vi → shell**
   - At `--More--`, press **v** to open the file in **vi**.
   - In `vi`, spawn a real shell:
     ```
     :set shell=/bin/bash
     :shell
     ```
   - You now have a normal shell **as bandit26**. Confirm and read the password:
     ```bash
     id
     whoami
     cat /etc/bandit_pass/bandit26
     ```

   *(Alternate inside vi: `:e /etc/bandit_pass/bandit26` to view the password without spawning a shell.)*

> Windows note (from the level text): If you connect from Windows, prefer **Command Prompt** (or WSL/SSH) instead of **PowerShell**, which can interfere with the interactive pager behavior.

## SOLUTIONS
- `grep '^bandit26:' /etc/passwd`
- `ssh -i /home/bandit25/.ssh/id_rsa bandit26@localhost -p 2220` *(shrink terminal height first to trigger `--More--`)*
- At `--More--` press **`v`** (opens `vi`)
- In `vi`: `:set shell=/bin/bash` → `:shell`
- `cat /etc/bandit_pass/bandit26`

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
