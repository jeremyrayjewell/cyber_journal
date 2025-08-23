## BANDIT 22 -> 23

# Obfuscated password (ROT13): 

	0Ms11vbVwZIA551wK3PzFgXYLdwx54Tn

# OBJECTIVE

	"A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

	NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints."


# PURPOSE


# SOLUTIONS

	cat /usr/bin/cronjob_bandit23.sh
	echo "I am user bandit23" | md5sum
