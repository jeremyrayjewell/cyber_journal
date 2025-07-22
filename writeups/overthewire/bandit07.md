# BANDIT 7 -> 8

## Obfuscated password (ROT13): 

qsjimSDv4zH0jsAoSBr9EbJfxZYt7rRp

## Objective

"The password for the next level is stored in the file data.txt next to the word millionth"

## Purpose

This level is a simple introduction to the concept of "grepping", or piping the output of a command into the `grep` command. We follow our `cat` command with the `|` pipe symbol and the literal text pattern of our choice.

If we run `grep man` we will find the following explanation under the `DESCRIPTION` section:

<premarkdown>

       grep searches for PATTERNS in each FILE.  PATTERNS is one or more patterns separated by newline characters, and grep prints
       each line that matches a pattern.  Typically PATTERNS should be quoted when grep is used in a shell command.

</pre>

## Solutions

- `cat data.txt | grep "millionth"`
