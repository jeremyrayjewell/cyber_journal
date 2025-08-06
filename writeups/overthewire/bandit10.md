# BANDIT 10 -> 11

## Obfuscated password (ROT13): 

qgE173sMXo0EEfQSFTft2EJacAIw3dEe

## OBJECTIVE

"The password for the next level is stored in the file data.txt, which contains base64 encoded data"

## PURPOSE

Here we are given the password for the next level in **Base64 encoding**. Encoding is distinct from encryption or compression in that it's *reversible*. Base64 encoding turns raw binary data into printable text so that it can travel safely through channels that expect only ASCII characters. We are given a `data.txt` file that includes the Base64 encoding of the password, and we must decode it.

The man page for the `base64` command tells us that option `-d` is to be used to decode. We could run that command on `data.txt`, or alternatively we could join the contents of the file to the end of the command with the `<<<` operator, also known as Bash's "here-string". That creates a temporary, one-line input stream connected to the command's **stdin**.

## SOLUTIONS

- `base64 -d data.txt1`

- `base64 -d <<< VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==`
