# Write-up: Natas 09 → 10  
**Date:** 2025-12-09  

## Obfuscated password (ROT13)

`g7V5IUicn14fWGHTI0poRfoLsSC2qzBh`

## OBJECTIVE

> The page displays an input box labeled “Find words containing:”  
> When a search term is entered, the output reflects matches found in a dictionary:
>
> ```
> Output:
> <? 
> if ($key != "") {
>     passthru("grep -i $key dictionary.txt");
> }
> ?>
> ```
> Source code is accessible via a “View sourcecode” link.  
> It reveals that user input is passed directly into `passthru("grep -i $key dictionary.txt");` with no sanitization.

## PURPOSE

This challenge disguises a shell execution vulnerability as a search feature. The server takes whatever the user enters in the search box and inserts it **unquoted** into a `grep` shell command passed to `passthru()`. Since the input is not sanitized or quoted, attackers can **inject arbitrary shell commands** by adding characters like `;` or `|`, allowing access to sensitive files like `/etc/natas_webpass/natas10`. This level teaches a classic **command injection** vulnerability caused by directly embedding user input into a shell command. 

Here it is useful to recall what we learned about the CTF structure in Natas7, that passwords are stored in a `/etc/natas_webpass/natas<x>` structure.

## SOLUTIONS

Enter `; cat /etc/natas_webpass/natas10` or `| cat /etc/natas_webpass/natas10` in the search box. The value is then added as `$key`, and the final shell command therby becomes `grep -i ; cat /etc/natas_webpass/natas10 dictionary.txt` or `grep -i | cat /etc/natas_webpass/natas10 dictionary.txt`. This causes the password to be printed below the search results.

## EXPERIMENTS

I navigated to `cat /etc/passwd` successfully just to confirm that I could. I also attempted full shell injection with `;sh -c 'cat /etc/natas_webpass/natas10'`, which worked. This inspired me to create a [command injection tool](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/cmd-injector) in bash.


___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
