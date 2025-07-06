# BANDIT 18 -> 19

## Obfuscated password (ROT13): 

	pTJcZnXKIjQHAtCNIWoJLhTUIa9my3w8

## OBJECTIVE

	"The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH."

## PURPOSE

## SOLUTIONS

	ssh -p 2220 bandit18@bandit.labs.overthewire.org ls -la  [Remote command execution via SSH]
	ssh -p 2220 bandit18@bandit.labs.overthewire.org cat readme
