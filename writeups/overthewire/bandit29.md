# BANDIT 29 -> 30

## Obfuscated password (ROT13): 

	dc30rk3IYm5ZQT1a91LbjGi4D8y7PQMY

## OBJECTIVE

	"There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

	Clone the repository and find the password for the next level."


## PURPOSE


## SOLUTIONS

	git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo

	git branch -a

	git checkout -t origin/dev -b dev

	cat README.md