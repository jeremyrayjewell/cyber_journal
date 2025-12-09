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

The links present on the landing page, `index.php?page=home` and `index.php?page=about`, indicate that the application builds what to include based on the `page` query parameter. This level teaches **Local File Inclusion (LFI)** (and, depending on the exact implementation, path traversal) caused by unsafe use of a user-controlled parameter.

The filename or path comes directly from user input (`$_GET["page"]`). There is no proper whitelist, sanitization, or restriction on which file may be loaded. PHP’s `include()` can often be tricked into loading arbitrary files, including files outside the intended directory, if absolute paths or traversal sequences are accepted.

**If user input controls which server-side file gets included, you have an LFI risk.** Even if the developer thinks only “safe” pages will be requested, an attacker can manipulate the parameter to reach more sensitive locations.

## SOLUTIONS

Browser: Navigate to `http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8`

Curl: `curl -u natas7:'<password-for-natas7>' "http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"`

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
