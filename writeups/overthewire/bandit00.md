# BANDIT 0 -> 1 #

## Obfuscated password (ROT13): ##

MwYwGzZ6SiilEaeo2esAJBMBGn6vc5Vs

## Objective ##

"The password for the next level is stored in a file called readme 
located in the home directory. Use this password to log into bandit1 
using SSH. Whenever you find a password for a level, use SSH (on 
port 2220) to log into that level and continue the game."

## Purpose ##
	
This first level is a simple introduction. The user must first be
able to use `ssh` to connect to the server via port 2220, then be
familiar with the basic `ls` (list directory contents) and `cat` 
(concatenate files and print on the standard output) commands.

- The `ssh` command runs the OpenSSH client program to connect to
an SSH server on a remote host. The command opens a TCP connection
on a port. It is port 22 by default, or another via flag (command-
line option) `-p` or `--port`. The command takes a minimum argument
of `host`, though its use without a specified `user` will result in
its using your current local username. Specified user name input is
given as `user@host`. SSH is a cryptographic network protocol.
OpenSSH is Linux's defacto SSH suite.  

- `ls` shows the contents of the present working directory. It is
one of the oldest and most fundamental Unix utilities.  
	
- The name of the `cat` command is derived from its original Unix
purpose: to con*cat*enate one or more files and to print the result
to the terminal. `cat` predates all screen-based editors. Thus, 
while its name reflects its original primary functionality, its use 
today is very often as a quick pager (or text viewer).

	

## Solutions ##
	
- `ssh -p 2220 bandit0@bandit.labs.overthewire.org`
- This same command format must be used to connect to all subsequent
levels.
- The password for user bandit0 is given as `bandit 0`.
- User can run `ls` in home directory to reveal readme.
- `cat readme` reveals the password.