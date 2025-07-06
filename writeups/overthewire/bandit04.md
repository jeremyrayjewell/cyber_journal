# BANDIT 4 -> 5

## Obfuscated password (ROT13): 

	4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

## Objective

	"The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command."


## PURPOSE

	Find a command-based method for isolating human-readable from binary files.

## SOLUTIONS

	find . -type f -exec file --mime {} + | grep 'text/'