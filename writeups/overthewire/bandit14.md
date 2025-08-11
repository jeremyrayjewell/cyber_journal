# Write-up: Bandit 14 → 15  
**Date:** 2025-08-06  

## Obfuscated password (ROT13) 

`8kPwaztbXoTYuUSNMyTR5Gzh4Z2gXWDb`

## OBJECTIVE

>"The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost."

## PURPOSE

Despite entering this level via ssh key, we can see now that we need the bandit13 password in order to retrieve the bandit14 one. This level is all about speaking directly to a network service on a given port. In particular, we must understand basic TCP client tools, "localhost" and ports, and how to pipe data into a socket.

Piping `echo` into the `nc` *Netcat* utility with `localhost` and port `30000` specified wires the input into a raw TCP connection. As promised, we receive the next password as a response.

As for the mechanism that causes the response, we can infer that it is an *xinetd*-managed service.

## SOLUTION

`echo [previous password] | nc localhost 30000`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
