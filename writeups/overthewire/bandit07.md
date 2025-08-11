# Write-up: Bandit 07 → 08  
**Date:** 2025-07-30  


## Obfuscated password (ROT13) 

`qsjimSDv4zH0jsAoSBr9EbJfxZYt7rRp`

## OBJECTIVE

>"The password for the next level is stored in the file data.txt next to the word millionth"

## PURPOSE

This level is a simple introduction to the concept of "grepping", or piping the output of a command into the `grep` command. We follow our `cat` command with the `|` pipe symbol and the literal text pattern of our choice.

If we run `grep man` we will find the following explanation under the `DESCRIPTION` section:

<premarkdown>

       grep searches for PATTERNS in each FILE.  PATTERNS is one or more patterns separated by newline characters, and grep prints
       each line that matches a pattern.  Typically PATTERNS should be quoted when grep is used in a shell command.

</pre>

## SOLUTIONS

- `cat data.txt | grep "millionth"`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
