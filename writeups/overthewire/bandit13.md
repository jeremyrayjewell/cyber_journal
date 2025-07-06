# BANDIT 13 -> 14

## Obfuscated password (ROT13): 

	MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

## OBJECTIVE

	"The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on"

## PURPOSE


## SOLUTIONS

	ssh -i sshkey.private -p 2220 bandit14@bandit.labs.overthewire.org
