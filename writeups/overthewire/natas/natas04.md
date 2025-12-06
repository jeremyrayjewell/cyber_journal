# Write-up: Natas 04 → 05  
**Date:** 2025-12-04  

## Obfuscated password (ROT13)

`0a35CxttNCz2moRcBH802p0k0Zfa1GbX`

## OBJECTIVE

> "Access disallowed. You are visiting from \"\" while authorized users should come only from \"http://natas5.natas.labs.overthewire.org/\""

## PURPOSE ##

This level teaches that **HTTP headers cannot be trusted for access control**. The page checks the value of the `Referer` header and only grants access if it matches the expected origin:  
`http://natas5.natas.labs.overthewire.org/`.

The `Referer` header is interesting. Its spelling is historically incorrect (the correct English spelling being *referrer*). Investigating things like this are much-appreciated opportunities to play cyber etymologist for me. What is it supposed to be used for? Analytics/logging, debugging, and perhapd CSFR mitigation. Client-supplied metadata should never be considered trustworthy. In Natas 4, however, this header is being used for authentication checking. Because the browser sends `Referer` only during real navigation events, loading the URL directly produces an empty string (`""`), causing the access-denied message.

The key lesson:  
**HTTP request headers such as Referer can be forged easily.**  
Any client—browser plugins, scripts, proxies, or command-line tools—can send arbitrary header values. Using them as an authentication gate is a fundamental security mistake.

## SOLUTION ##

You can spoof the `Referer` header using a browser extension, but the easiest thing to use is `curl` with the `-u` and `-H` flags. The `-u` or `--user` flag is used for HTTP Basic Authentication, supplying  `username:password`, and `-H` or `--header` passes custom headers to the server. 

```bash
curl -u natas4:'<password-for-natas4>' \
-H "Referer: http://natas5.natas.labs.overthewire.org/" \
http://natas4.natas.labs.overthewire.org/
```

This returns a `200-OK` HTML page containing the credential

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
