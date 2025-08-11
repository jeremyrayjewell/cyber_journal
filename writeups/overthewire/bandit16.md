# Write-up: Bandit 16 → 17  
**Date:** 2025-08-08  

## Obfuscated password (ROT13) 

`RErInirCYSUgSySfwa3ulmZyiFhFNpEQ`

## OBJECTIVE

>"The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it."

## PURPOSE

This level allows us to explore SSH key pairs once again, along with discovering unknown services. First thing's first, we must find the correct port. `ss` is a modern replacement for `netstat` that lets you inspect sockets. We will use it with the following flags:

- `-t` "TCP": only show TCP sockets

- `-n` "numeric": show port numbers and IPs directly (do not resolve names)

- `-l` "listening": only including listening sockets

`ss -tnl` presents us with a list of 48 sockets, which we could search manually. We could also use *filter expressions* to only show ports within the range we're looking for: `'( sport >= :31000 and sport <= :32000 )'`

An easier solution would be to use `nmap`: `nmap -Pn -p 31000-32000 localhost`, where `-Pn` means "no ping" in order to forgo the initial host-discovery phase and `-p` means port, followed by our range.

Once we have found our target port, we can send our previous password to it the way we did before. In response this time we are sent an RSA private key. RSA refers to the algorithm type; this key is the same tool as we used with SSH previously. `ssh -i` expects a file, so we must save the RSA key to a temp file.

First, let's create a temporary directory: `mkdir -p /tmp/foo2` or `mktemp -d`. Next, recall Bandit15's `-ign_eof` flag that allows us to keep the client open. We can then use the **stdout redirection operator** `>` to write the output to a file. 

`echo kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx | openssl s_client -quiet -connect localhost:31790 -ign_eof 2>/dev/null > /tmp/foo2/rsa.key`  

We may also choose to include Bandit6's `2>/dev/null` before the final `>` to discard error messages. Finally, now that we have out key file, we must change its mode with `chmod 400` (`400` to keep it readable only to us). After that we ought to be able to enter the next level with no issues.


## SOLUTIONS

- `ss -tnl` or  `ss -tnl '( sport >= :31000 and sport <= :32000 )'` or `nmap -Pn -p 31000-32000 localhost`

- `echo [previous password] | openssl s_client -quiet -connect localhost:[port] -ign_eof 2>/dev/null > /tmp/foo2/rsa.key`  	

- `chmod 400 /tmp/foo2/rsa.key`

- `ssh -i /tmp/foo2/rsa.key bandit17@localhost -p 2220`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
