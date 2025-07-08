# BANDIT 3 -> 4

## Obfuscated password (ROT13): 

2JzeQSEzWVd3VCkarNnZTunc0cSuS3AW

## OBJECTIVE
	
"The password for the next level is stored in a hidden file in the inhere directory."

## PURPOSE

This level requires the user to navigate into a new directory using `cd`, the *change directory* shell builtin command. Then, in the new directory, the user must use the `ls ` *list* utility to see the directory's contents. These contents are, however, hidden. On Unix-like systems, any file whose name begins with a `.` is treated as "hidden" by most tools.

In order to see the hidden file, the use must run the `ls` utility with the flags `-a`/`--all` or `-A`/`--almost-all`. `-a`/`--all` will show all hidden contents, while `-A`/`--almost-all` will exclude the `.` *current directory* and the `..` *parent directory* special entries.

## SOLUTIONS

- `cd inhere`, `ls -a`, `cat ...Hiding-From-You`

- `-a` flag alternatives: `--all` (same function), `-A`/`--almost-all` (excludes special entries)




