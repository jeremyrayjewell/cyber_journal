# Write-up: Natas 06 → 07  
**Date:** 2025-12-06  

## Obfuscated password (ROT13)

`ozt8FiH1YvmhJwk3l7kxARExUkTer0TF`

## OBJECTIVE

> The page prompts for a “secret” value. If the submitted value matches the server-side `$secret`, the page reveals the password for **natas7**. The source code is available via a “View sourcecode” link.

## PURPOSE
This level teaches a simple but important lesson: **hiding a file is not the same as securing it**. The `View sourcecode` button is an obvious breadcrumb, and viewing the sourcecode exposes the following inline PHP embedded in the HTML:
```
include "includes/secret.inc";

if(array_key_exists("submit", $_POST)) {
    if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
}
```
Here we see that `$secret` is defined inside `includes/secret.inc` with nothing protecting the `includes/` directory. This is essentially an **IDOR** (Insecure Direct Object Reference) issue: a sensitive server-side file is exposed simply because it lives inside the web-accessible document root. The violated principle is clear: **security by obscurity is not security**.

## SOLUTIONS

The simplest solution is in the browser, where we only need to navigate to the file being referenced (`http://natas6.natas.labs.overthewire.org/includes/secret.inc`) to reveal the secret that in turn exposes the password to Natas7. Copy the value assigned to `$secret`, return to the main page, paste the secret into the form, and submit it. 

Alternatively, if enjoy a CLI challenge, you could `curl` the destination with the Natas6 username and password via the `-u` flag and submit it to the main page via POST. First, retrieve the secret:
`curl -u natas6:'<password-for-natas6>' http://natas6.natas.labs.overthewire.org/includes/secret.inc`
Then, submit the secret via POST:
`curl -u natas6:'<password-for-natas6>' -d "secret=<retrieved-secret>" -d "submit=1" http://natas6.natas.labs.overthewire.org/`

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
