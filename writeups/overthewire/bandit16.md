# BANDIT 16 -> 17

## Obfuscated password (ROT13): 

	RErInirCYSUgSySfwa3ulmZyiFhFNpEQ

## OBJECTIVE

	"The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it."

## PURPOSE


## SOLUTIONS

	ss -tnlp
	echo [previous password] | openssl s_client -quiet -connect localhost:31790
	chmod 600 bandit17.key
	ssh -i /tmp/santafe2/bandit17.key bandit17@localhost -p 2220
