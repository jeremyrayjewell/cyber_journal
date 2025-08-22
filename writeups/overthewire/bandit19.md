# Write-up: Bandit 19 → 20
**Date:** 2025-08-11

## Obfuscated password (ROT13)
`0dKnuT8MwBIZA9Tuf7vBJfPsMlKBHoLB`

## OBJECTIVE
>"To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary."

## PURPOSE
This level teaches us how a **setuid** executable runs with the **owner's privileges** (not yours). The setuid helper in `~` is owned by **bandit20**, so any command it runs executes as **bandit20**, letting you read `/etc/bandit_pass/bandit20`.

First, we must locate and inspect the setuid helper by running `ls -l` in the **bandit19** home directory. There we will see permissions `-rwsr-x---`, the `s` indicating the setuid bit. We also see in the file owner column that the file belongs to `bandit20`. Those are the permissions which we would gain by running the executable.

If we execute `./bandit20-do`, we thereby achieve **bandit20** permissions, which we can then use to read the password for the next level stored in its customary location, `/etc/bandit_pass/bandit20`.

## SOLUTIONS
- `./bandit20-do cat /etc/bandit_pass/bandit20`

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
