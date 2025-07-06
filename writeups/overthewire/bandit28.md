# BANDIT 28 -> 29

## Obfuscated password (ROT13): 

	4cG1g5QRAnLhdadinqLf1bR4DYPqwzW7

## OBJECTIVE

	"There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

	Clone the repository and find the password for the next level."

## PURPOSE


## SOLUTIONS

	bandit28@bandit:/tmp/santafe2$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo

	git log --reverse --skip=1 -n1

	git rev-list --reverse HEAD

	SECOND_HASH=$(git rev-list --reverse HEAD | sed -n '2p')

	git show $SECOND_HASH
