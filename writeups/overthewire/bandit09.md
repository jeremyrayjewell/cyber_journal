# Write-up: Bandit 09 → 10  
**Date:** 2025-08-01  


## Obfuscated password (ROT13): 

STHJ5vyYIWekK9xZLZzyA4ZtocsZvdrl

## OBJECTIVE

"The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters."

## PURPOSE

The `strings` command prints the sequences of printible characters in a file. A **printable character** is any byte or multi-byte sequence that the system's current locale says can be drawn visibly on the screen **plus the space character**. This is a category that overlaps with "human-readable" text, as human-readable text is generally printable. Printability, however, is a strict byte-level test. A "string", in computer languages, is an ordered sequence of characters. We can, in general think of `strings` as a low-level, brute-force way to recover possible high-level strings from any file by filtering on "printable" bytes, which is the common denominator between raw storage and human-meaningful text.

If we run `strings` on `data.txt` we ought to be able to see the password, but if we grep for `===` then we can complete for the "several ‘=’ characters" criteria and reveal a complete message from the OTW admins.

## SOLUTIONS

- `strings data.txt`

- `strings data.txt | grep "==="`

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)

