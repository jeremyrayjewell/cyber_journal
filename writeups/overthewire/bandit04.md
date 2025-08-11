# Write-up: Bandit 04 → 05  
**Date:** 2025-07-27  


## Obfuscated password (ROT13) 

`4bDLICxkMBBRBB5cGJ81SO8w8ykKTHDj`

## OBJECTIVE

>"The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command."


## PURPOSE
	
`inhere/` now contains the following files: 

	-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09

The task is to find a command-based method for isolating human-readable from binary files. In Unix-land, "human-readable" (or simply "test") files are sequences of byters meant to be interpreted as characters (usually ASCII or UTF-8. This is in contrast to **binary** files, which contain arbitrary byte values which only programs know how to interpret. A slogan one might hear related to Unix-type systems is "everything is a file", referring to how many system resources are equally exposed to the same open/read/write/close interface that one would expect to use with ordinary disk files. File types are not imposed from outside by the use of suffixes, but by metadata, permissions, and how applications interpret them.

As each file in `inhere/` begins with a `-` followed by another character, it is important to consider that running `cat -file00` will result in `-file00` being treated as an option to be applied to `cat` rather than as a file. So, thinking back to *bandit1*, we must remember to prefix the filename appropriately (i.e. `./-file00`). This leads to the first, and least-efficient solution, which is to `cat` each file one-at-a-time. This can be made more efficient by running a **filename globbing pattern**: `cat ./-file0[0-9]`. As binary files do not end in linebreaks, this may taint the true password with unwanted characters or otherwise make it difficult to read. An improvement would be `strings ./-file0[0-9]`, where `strings` checks the documents for printable characters and prints each one as a string on its own line.

The `file` command exists to read the first bytes of a file and compare them against a database of known signatures. Running `file foo.pdf` will show its identity as a PDF document owing to its contents rather than its suffix, and indeed if one changes its name (`mv foo.pdf foo.bar && file foo.bar`) one will see that `file` continues to identify the document as a PDF. So running `file ./-file0[0-9]` here prints file type descriptions, allowing us to see that only one file is identified as `ASCII text`, meaning it is human-readable. We can then run `cat` on the file.

`find` within the present directory `.` can also be used, and if we had subdirectories to avoid traversing we could add the option `-maxdepth 1`, although that isn't necessary here. We should, however, add the following options: `-type -f`, which filters for *regular/text files*; `-exec` which executes another command on each filtered result produced by `find . -type f`; `file {} \;` to execute on filtered results to place them in a **placeholder** `{}` before exiting the execution with `\;`. If we run the command as-is, we can then see which file is ASCII text. Alternatively, we may also wish to pipe the results into `grep` to isolate for occurences of "text": `| grep "text". 


## SOLUTIONS

- LEAST OPTIMAL: `cat` each file manually

- `cat ./-file0[0-9]`

- `strings ./-file0[0-9]`

- `file ./-file0[0-9]` + `cat ./file07`

- `find . -type f -exec file {} \;`

- `find . -type f -exec file {} \; | grep 'text'`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
