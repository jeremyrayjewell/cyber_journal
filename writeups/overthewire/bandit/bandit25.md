# BANDIT 25 -> 26

## Obfuscated password (ROT13): 

	f0773kkxx0ZKsqdBsCEIe9Y3wWOHBtPM

## OBJECTIVE

	"Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

	NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead."


## PURPOSE


## SOLUTIONS

	minimize terminal screen to below 6px high

	ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220
	v and :e /etc/bandit_pass/bandit26

	

	:set shell=/bin/bash
	:shell

