# BANDIT 1-> 2

## Obfuscated password (ROT13): 

263WTWCstH6YgqRitsJH1KC5lnp29zSk

## Objective

"The password for the next level is stored in a file called - located in the home directory"

## Purpose

`-` by itself is read as STDIN (Standard Input), the default data stream that s program reads
from (file descriptor 0). When you run a command without supplying a file, or use `-` as a
filename, the program reads from STDIN. If you run `-` as an argument, the program is told to 
read/write from/to the standard input stream instead of a real file.
The STDIN is, by default, your keyboard input. So running `cat -` here results in keyboard 
inputs being printed on the screen until Ctrl+D (default EOF character) is entered.
Prefixing the argument with `./` to focus on the literal file path (`./-`) bypasses this issue,
where `.` indicates the current directory and `/` functions as a separator. Alternatively, 
the full file path could also be used.  
`./` is most often associated with running executables, but as we see here it can also be used
in command-line arguments.

## Solutions

- `cat ./-`

- `cat /home/bandit1/-`

