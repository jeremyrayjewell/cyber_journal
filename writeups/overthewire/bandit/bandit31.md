# BANDIT 31 -> 32

## Obfuscated password (ROT13): 

	3B9EsudlNyIORMcIo6YLFgfuMbdbFk5X

## OBJECTIVE

	"There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

	Clone the repository and find the password for the next level."

## PURPOSE


## SOLUTIONS

	git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
	cat README.md
	echo 'May I come in?' > key.txt
	git add -f key.txt [.gitignore ignores key.txt]
	git commit -m "adding key"
	git push origin master
