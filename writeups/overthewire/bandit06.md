# BANDIT 6 -> 7

## Obfuscated password (ROT13): 

	zbeoAGQxFJ6wVyHp0lzBqZnYaBySINnw

## Objective

	"The password for the next level is stored somewhere on the server and has all of the following properties:
    	- owned by user bandit7
    	- owned by group bandit6
    	- 33 bytes in size"

## Purpose

	

## Solutions

	find . -group bandit6 -user bandit7 -size 33c



