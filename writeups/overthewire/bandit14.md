# BANDIT 14 -> 15

## Obfuscated password (ROT13): 

	8kPwaztbXoTYuUSNMyTR5Gzh4Z2gXWDb

## OBJECTIVE

	"The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost."

## PURPOSE


## SOLUTION

	echo [previous password] | nc localhost 30000
