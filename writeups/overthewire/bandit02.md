# Write-up: Bandit 02 → 03  
**Date:** 2025-07-25  

## Obfuscated password (ROT13) 

`ZAx8XAU3Hfvvb41CEHRbQSCdskYCyFzk`

## OBJECTIVE

>"The password for the next level is stored in a file called spaces in this filename located in the home directory"

## PURPOSE

When a filename contains space, the shell will interpret each space as a separator between arguments. You need to either quote or escape the spaces so that `cat` sees it as a single name.

## SOLUTIONS

- `cat "spaces in this filename"`

- `cat 'spaces in this filename'`

- `cat spaces\ in\ this\ filename`

- TIP: `cat space\` + `TAB` key will often complete the name for you.

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
