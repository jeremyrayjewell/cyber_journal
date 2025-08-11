# Write-up: Bandit 17 → 18  
**Date:** 2025-08-10  

## Obfuscated password (ROT13): 

pTJcZnXKIjQHAtCNIWoJLhTUIa9my3w8

## OBJECTIVE

"The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH."

## PURPOSE

Here we must bypass an interactive shell trap using non-interactive commands. You will find such "print a message and exit" behaviors that you may see in the wild: 

- service/automation accounts (backup, deploy, CI runners)

- bastion/jump hosts with a menu

- HPC clusters / build farms

- SFTP-only users / chrooted accounts

- Incident response / quarantine

- Honeypots / tripwires

The mere fact that we are kicked out before we can interact with the shell suggests interference in the interactive login path. The primary culprit would be a shell startup file. We could inspect the problem by navigating to bandit18's home directory while still logged in as bandit17. There, running `ls -la`, we can find the `.bashrc` startup script, but we cannot read it. 

Fortunately for us, non-interactive shell commands are an intended feature of SSH which allows automation. They allow SSH to run one specific command on the remote host without giving you a shell prompt. As such, we can test to see if our non-interactive commands get through by running: `ssh -p 2220 bandit18@bandit.labs.overthewire.org echo ok`. Non-interactive commands follow our SSH options and the target host. If we see the non-interactive command execute before we are given the boot then we know that they will work. We can then run `ssh -p 2220 bandit18@bandit.labs.overthewire.org cat readme` to retrieve the password.


## SOLUTIONS

- ssh -p 2220 bandit18@bandit.labs.overthewire.org cat readme

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
