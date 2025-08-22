# Write-up: Bandit 20 → 21
**Date:** 2025-08-12

## Obfuscated password (ROT13) 
`RrbHYZPen2d0qFxLw561QK7f1PcOhBOg`

## OBJECTIVE
>"There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

>NOTE: Try connecting to your own network daemon to see if it works as you think"

## PURPOSE
This level teached a client/server handshake with a **setuid helper**:
- You run a local **server** (listener) that will **send** the bandit20 password.
- The setuid **client** (owned by `bandit21`, named `suconnect`)

The objective tells us what `suconnect` does, and we are told that it takes a port number as an argument. When we inspect the helper `suconnect` by running `ls -l` we see `-rwsr-x---` permissions and we see that its owner is `bandit21`.

We will need to terminals to accomplish our task. First, we neet to run **netcat** (`nc`), a simple network connection tool that can pipe data in (**stdin**) and out (**stdout**). The flag we definitley need is `-l` for **listen mode** (server), and depending on the version of `nc` we may also need the `-p` flag before giving our port number. We may also choose to add `-v` for verbose to see exactly when the client connects and to receive debugging messages. In terms of selecting a port, any high number will probably work. Ports under 1024 require root privleges, and if the port we choose is already in use we should receive an error message letting us know.

Once we run the server in one terminal, we can then access bandit20 from the other terminal in order to run `./suconnect` with the port of our choosing. Then, returning to our first terminal, we can enter the last password in the interactive mode in order to receive the next password in response.

## SOLUTIONS
- First step -- terminal 1 : `nc -l 3333`
- Second step -- terminal 2 : `./suconnect 3333`
- Third step -- terminal 1 : paste password to bandit20, receive password to bandit21

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
