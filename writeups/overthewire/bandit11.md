# BANDIT 11 -> 12

## Obfuscated password (ROT13): 

	7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4

## OBJECTIVE

	"The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions"

## PURPOSE


## SOLUTIONS

	echo "Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
