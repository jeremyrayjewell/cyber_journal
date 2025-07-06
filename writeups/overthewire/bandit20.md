# BANDIT 20 -> 21

## Obfuscated password (ROT13): 

	RrbHYZPen2d0qFxLw561QK7f1PcOhBOg

## OBJECTIVE

	"There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

	NOTE: Try connecting to your own network daemon to see if it works as you think"

## PURPOSE


## SOLUTIONS

	terminal 1 : nc -l -p 3333
	terminal 2 : ./suconnect 3333
