# Write-up: Bandit 15 → 16  
**Date:** 2025-08-07  

## Obfuscated password (ROT13): 

xFxiHcZD7yOLlPZ4TOCiPiG1OsJEl0Qk

## OBJECTIVE
	
"The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption."

## PURPOSE

The difference between bandit15 and bandit14 is **encryption**. While in bandit14 we sent raw, plain-TCP over the socket, here we will not exchange any data before the client and server perform a **SSL/TLS handshake**. In the real world, SSL (*Secure Sockets Layer*) and TLS (*Transport Layer Security*) cryptographic protocols guarantee confidentiality, integrity, and authentication for network traffic.

Like in the previous challenge, we use `echo` to pipe the previous password to another command. This time the command receiving that output will be `openssl` with the `s_client` subcommand, and we will use the option `-connect` to send our input to `localhost:30001`. `openssl` is the OpenSSL commad line program, `s_client` implements a minimal TLS client, and `-connect host:port` tells it where to open the underlying TCP socket.

We will, however, notice a problem: as `openssl s_client` parses the certificate dump, it ends the TLS session before it reads the server's final response. To get around this, we can also add the `-quiet` flag to supress all of the handshake and session-info chatter. Alternatively, we could forgo piping our previous password via `echo` and instead run the `openssl s_client -connect host:port` command with the `-ign_eof` flag at the end to keep the client open and allow us to enter the previous password over the TLS channel ourselves.

## SOLUTIONS
	
- `echo [previous password] | openssl s_client -quiet -connect localhost:30001`

- `openssl s_client -connect localhost:30001 -ign_eof`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
