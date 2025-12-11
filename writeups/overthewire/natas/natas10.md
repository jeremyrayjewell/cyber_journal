# Write-up: Natas 10 → 11  
**Date:** 2025-12-10  

## Obfuscated password (ROT13)

`HWqdxX1cGh6IYg9HUJNtEMm6fIHM3yRx`

---

## OBJECTIVE

> The web page prompts the user to “Find words containing” an input string.  
> Viewing the source (`index-source.html`) shows the same basic logic as in Natas 9, with a small difference:
>
> ```php
> $key = "";
> if(array_key_exists("needle", $_REQUEST)) {
>     $key = $_REQUEST["needle"];
> }
>
> if($key != "") {
>     if(preg_match('/[;|&]/',$key)) {
>         print "Input contains an illegal character!";
>     } else {
>         passthru("grep -i $key dictionary.txt");
>     }
> }
> ```
>
> The challenge is to **bypass the input filter** (which blacklists certain shell metacharacters) in order to **achieve command injection** and read the password for **natas11** from `/etc/natas_webpass/natas11`.

---

## PURPOSE

This level teaches how **blacklist-based filtering can be bypassed**, and reinforces command injection principles from Natas 9. The input is run through `preg_match('/[;|&]/', $key)` to block three specific characters (`;`, `|`, `&`), but **does not escape or sanitize the shell command itself**. The key lesson is: **blacklists are fragile and incomplete defenses**. There are always alternative ways to express shell commands unless the input is strictly sanitized or escaped.

---

## SOLUTIONS

These inputs can be submitted into the search box:
- `$ /etc/natas_webpass/natas11` — This uses Unix shell variable expansion. Since `$` is treated as an empty or undefined variable, the shell effectively sees `/etc/natas_webpass/natas11` as a standalone argument. This file is then processed by `grep`, revealing its contents in the output.
- `\r /etc/natas_webpass/natas11` — The carriage return character (ASCII 13) causes the shell to treat the input after `\r` as if it starts on a new line. This prematurely ends the original grep command and starts a new one using the file path, allowing direct output of its contents.

Note:
`cat` is not required. Supplying `/etc/natas_webpass/natas11` alone is enough — the shell treats it as a filename, and grep attempts to search it. Because it contains no search pattern, it simply echoes the file's content to the output.

---

## TAKEAWAY

Relying on blacklists is inherently unsafe for command input. If you allow unsanitized user input to be inserted into shell commands, assume it can be weaponized. Always use safe APIs (e.g., `escapeshellarg()` or `proc_open()` with array syntax), and avoid shell invocation entirely if possible.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
