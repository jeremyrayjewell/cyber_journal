# Write-up: Bandit 26 → 27
**Date:** 2025-08-18

## Obfuscated password (ROT13) 
`hcfAPp7imnEQk6bMP6TvE6REjr1ZbjTO`

## OBJECTIVE
> "Good job getting a shell! Now hurry and grab the password for bandit27!"

## PURPOSE
Now that we have an interactive shell as **bandit26**, the next password is available via a **setuid helper** in the home directory. The binary (commonly named `bandit27-do`) runs a command **as user `bandit27`**. We’ll use it to read the usual password file at `/etc/bandit_pass/bandit27`.

1. List the home directory to discover the helper and check its mode (you’ll notice the setuid bit `s` on the owner):
   ```
   ls -la
   ```
2. Run the helper without arguments to see usage, then execute `cat` as bandit27:
   ```
   ./bandit27-do
   ./bandit27-do cat /etc/bandit_pass/bandit27
   ```
That prints the **bandit27** password, which you can then use to log in to the next level.

## SOLUTIONS
- `ls -la`
- `./bandit27-do`
- `./bandit27-do cat /etc/bandit_pass/bandit27`

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)

