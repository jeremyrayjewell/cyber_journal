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

## UPDATE 2025-08-13

The file name is now `--spaces in this filename--`, adding an additional layer of complexity as the `--` is interepreted by `cat` as a sign to end command option parsing. We must now add an intentional `--` in front of our quotation-mark encapsulation in order to prevent the parsing of our filename as a command option: `cat --   "--spaces in this filename--"`.

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
