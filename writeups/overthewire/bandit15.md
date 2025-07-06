# BANDIT 15 -> 16

## Obfuscated password (ROT13): 

	xFxiHcZD7yOLlPZ4TOCiPiG1OsJEl0Qk

## OBJECTIVE
	
	"The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption."

## PURPOSE


## SOLUTIONS
	
	echo [previous password] | openssl s_client -quiet -connect localhost:30001
	(sleep 3; echo [previous password]) | openssl s_client -connect localhost:30001
