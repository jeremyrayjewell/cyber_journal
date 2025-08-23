# Write-up: Bandit 20 → 21
**Date:** 2025-08-12

## Obfuscated password (ROT13)
`RrbHYZPen2d0qFxLw561QK7f1PcOhBOg`

## OBJECTIVE
> “There is a setuid binary in the home directory that makes a connection to localhost on the port you specify as a command-line argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).
>
> NOTE: Try connecting to your own network daemon to see if it works as you think.”

## PURPOSE
This level **teaches** a client/server handshake with a **setuid helper**:

- You run a local **server** (listener) that will **send** the bandit20 password.
- The setuid **client** (owned by `bandit21`, named `suconnect`) connects to your port, checks the line, and if correct **sends back** the bandit21 password.

Running `ls -l` shows `./suconnect` with permissions like `-rwsr-x---` (note the **s** = setuid) and owner `bandit21`. That’s why it can read `/etc/bandit_pass/bandit21`.

You’ll use **two terminals/sessions** (both logged in as bandit20) for clarity: one to listen with `nc`, one to run `suconnect`. Netcat flags you’ll care about:
- `-l` listen mode (server)
- `-p <port>` set listen port (needed on GNU nc; OpenBSD nc uses a positional port after `-l`)
- `-v` verbose (optional)

Pick any **unprivileged** port (>1024) that’s **free** (e.g., `3333`). If it’s in use, `nc` will complain—just choose another.

## SOLUTIONS

**Terminal 1 — start a listener**
```bash
# OpenBSD nc (common on Bandit)
nc -l 3333 -v
# or GNU/traditional nc
# nc -l -p 3333 -v
```

**Terminal 2 — run the setuid client**
```bash
./suconnect 3333
```

**Back to Terminal 1 — send the previous password**
```bash
# Paste the contents of /etc/bandit_pass/bandit20 and press Enter
# (Pressing Enter matters: suconnect reads a single newline-terminated line.)
```

You’ll see the **bandit21** password appear in Terminal 1.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
