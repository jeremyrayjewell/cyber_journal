# Write-up: Bandit 13 → 14  
**Date:** 2025-08-05  

## Obfuscated password (ROT13): 

ZH4IJeGyWk8EBof1qqmcOCoYh7lQPCvF

## OBJECTIVE

"The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on"

## PURPOSE

This level introduces us to the basics of ssh keys. This is a common way to authenticate GitHub from the terminal, as well as do many other things. SSH key-pairs are a fundamental tool for password-free workflows.

To make an ssh key pair, we could just use the `ssh-keygen` command to produce the public key and the private key. In this case, the public key is located in `/home/bandit14/.ssh/authorized_keys` where permissions are restricted to `bandit14`. The private key is located in bandit13's home directory, and we can utilize it to connect to bandit14 via `ssh` with the `-i` *identity file* option.

Once we make it to the bandit14 server, we can locate the bandit13 password in the `/etc/bandit_pass` directory.

## SOLUTIONS

- `ssh -i sshkey.private -p 2220 bandit14@bandit.labs.overthewire.org`

- `cat /etc/bandit_pass`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
