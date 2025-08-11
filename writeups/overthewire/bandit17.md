# Write-up: Bandit 16 → 17  
**Date:** 2025-08-09  

## Obfuscated password (ROT13): 

k2tYGGwSjZBuD8bJAoZA362DXksEdTyB

## OBJECTIVE

"There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19"

## PURPOSE

The `diff` command compares two files line-by-line. The output will show us our password.


## SOLUTIONS

- `diff passwords.new passwords.old`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
