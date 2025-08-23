# BANDIT 30 -> 31

## Obfuscated password (ROT13): 

	so5F2ko7oElSzNiDLDTRdfouIlWduaQl

## OBJECTIVE

	"There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

	Clone the repository and find the password for the next level."

## PURPOSE


## SOLUTIONS

	git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
	git tag
	git show secret
