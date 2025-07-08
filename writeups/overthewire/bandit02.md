# BANDIT 2 -> 3

## Obfuscated password (ROT13): 

ZAx8XAU3Hfvvb41CEHRbQSCdskYCyFzk

## Objective

"The password for the next level is stored in a file called spaces in this filename located in the home directory"

## Purpose

When a filename contains space, the shell will interpret each space as a separator between arguments. You need to either quote or escape the spaces so that `cat` sees it as a single name.

## Solutions

- `cat "spaces in this filename"`

- `cat 'spaces in this filename'`

- `cat spaces\ in\ this\ filename`

- TIP: `cat space\` + `TAB` key will often complete the name for you.
