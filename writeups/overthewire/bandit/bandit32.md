# BANDIT 32 -> 33

## Obfuscated password (ROT13): 

	N/A (No level 33)

# Write-up: Bandit 32 → 33
**Date:** 2025-08-24

## Obfuscated password (ROT13) 
`N/A, final level`

## OBJECTIVE
> "After all this git stuff, it’s time for another escape. Good luck!"

## PURPOSE

This level drops you into a **custom “uppercase” shell** instead of a normal `/bin/bash`. Anything you type gets **uppercased** before being handed to a real shell, so common escapes like `sh` become `SH` (not a valid command/path on Linux) and fail.

Key idea: use **shell substitution that doesn’t contain letters** so it **survives uppercasing**, then expands to a real command.

- `$0` is a **special parameter**: when evaluated by the shell, it expands to the **name/path of the current shell** (e.g., `sh`).  
- The uppercase wrapper doesn’t change `$` or digits, so typing `$0` reaches the real shell **unchanged**, then expands to `sh`, effectively launching a **sub-shell** that isn’t filtered by the uppercase wrapper.  
- Once you’re in that sub-shell, you can read the usual password file.

Small checks you can do after escaping:
- `echo $0` → confirm you’re in `sh`.
- `id`, `whoami` → verify effective user before reading the pass file.

## SOLUTIONS
- Type `$0` to spawn an unfiltered shell.
- `echo $0` *(optional: confirm it prints `sh`)*  
- `cat /etc/bandit_pass/bandit33`

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
