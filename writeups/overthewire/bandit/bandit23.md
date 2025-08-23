# BANDIT 23 -> 24

## Obfuscated password (ROT13): 

	to8XEEPffuhMKV0gHhE6lcBSwvMos3T8

## OBJECTIVE

	"A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

	NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

	NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…"

## PURPOSE


## SOLUTIONS

	#!/bin/bash	cat /etc/bandit_pass/bandit24 > /tmp/mybandit24pass