# BANDIT 5 -> 6

## Obfuscated password (ROT13): 

	UJnfaCugd9NIXr0qzx45akl20piHn6RT

## Objective

	"The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
	- human-readable
	- 1033 bytes in size
    	- not executable"

## Purpose

## Solutions

	ls -lahR | awk '/:$/ {dir=$0; next}$5 == "1.3K" {print dir "\n" $0}'  [doesn't work because bytes can't be specified]
	find . -type f -size 1033c -exec ls -l {} \;  [works]

