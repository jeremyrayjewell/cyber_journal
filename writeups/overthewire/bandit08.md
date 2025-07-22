# BANDIT 8 -> 9

## Obfuscated password (ROT13): 

4PXZu1WV91oHVMMCKQdTnany4kiNt0WZ

## Objective
	
"The password for the next level is stored in the file data.txt and is the only line of text that occurs only once"

## Purpose

The `uniq` command allows repeated lines to be reported or ommitted, but it only compares each line with the line *right before it*. Its man page states the following:

<premarkdown>

	Note:  'uniq'  does not detect repeated lines unless they are adjacent.  You may want to sort the input first, or use 'sort
       -u' without 'uniq'.

</pre>

The man page for `sort` clarifies:

<premarkdown>

Write sorted concatenation of all FILE(s) to standard output. 

</pre>

`sort` + `uniq` is a common pairing. Though `sort` does have a `-u` option itself, this option only removes duplicate *runs* after sorting, still keeping one copy of every distinct line, and thus only reducing the 1001 lines to 101. 

## Solutions

- sort data.txt | uniq -u