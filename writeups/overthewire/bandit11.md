# BANDIT 11 -> 12

## Obfuscated password (ROT13): 

7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4

## OBJECTIVE

"The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions"

## PURPOSE

Whereas the last level was an encoding challenge, this one is an encryption challenge. Letters having been "rotated by 13" indicates the use of ROT13, a Caesar cipher with a shift of 13. The Caesar cipher is an elementary substitution cipher which works by shifting each letter in a text by a fixed number of position in the alphabet. It is not very secure, but it is easily reversible.

The `tr` command (*translate* or *transliterate*) reads from a standard input, replaces (translates) characters found in the first set with the corresponding character in the second set, and writes to standard output. The arguments which we give to `tr` are first the *search* set and second the *replacement* set:

- *search set*: `A-Za-z` moves through all uppcase letters before moving through all lowercase characters.

- *replacement set*: `N-ZA-Mn-za-m` is also split into uppercase and lowercase, beginning at N (13 characters after A), cycling back through the characters by connecting Z to A before finishing at M (one character before its starting position). Uppercase and lowercase are likewise stitched together, providing a full substitution pattern for the search set.

After these arguments are given, `tr` lines up the characters in the first and second sets in order, replacing characters in the first set with their corresponding character in the second set.



## SOLUTIONS

- `echo "Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4" | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
