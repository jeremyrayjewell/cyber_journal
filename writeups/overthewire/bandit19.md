# BANDIT 19 -> 20

## Obfuscated password (ROT13): 

	0dKnuT8MwBIZA9Tuf7vBJfPsMlKBHoLB

## OBJECTIVE

	"To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary."

## PURPOSE

## SOLUTIONS

	find / -user bandit20 -perm -4000 2>/dev/null
	./bandit20-do cat /etc/bandit_pass/bandit20
