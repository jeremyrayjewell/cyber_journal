# Write-up: Natas 03 → 04  
**Date (written):** 2025-12-03  

## Obfuscated password (ROT13)

`DelMKp2r0mnuHYqUegUkmlLxw59xHkYD`

## OBJECTIVE

> "There is nothing on this page."

## PURPOSE ##

This level teaches why **robots.txt is not a security mechanism**. Although intended for search engine crawlers, it is publicly accessible and often leaks sensitive directories. Attackers—or curious users—can read it exactly like any other file and follow its “Disallow” paths.

### What `robots.txt` is actually for
- It belongs to the **Robots Exclusion Protocol**, which provides *guidelines* for crawlers.  
- Search engines voluntarily respect `Disallow:` rules to avoid crawling or indexing specific URLs.  
- It **does NOT restrict access**. Every user, script, or bot can still fetch disallowed paths directly.  
- Because of this, placing sensitive files (like credentials or backups) behind a path listed in `robots.txt` is a classic misconfiguration.

### Why the landing page & its source show nothing
- The page’s HTML intentionally contains no hint of the hidden path.  
- `/s3cr3t/` appears **only** inside `robots.txt`, which is not part of the page and must be requested directly.  
- Therefore, “View Source” will never reveal what `/robots.txt` does.

## SOLUTION ##

1. Log in as **natas3**. Here is another opportunity to use my [directory-enumerator](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/directory-enumerator) tool:
```bash
./dir_enum.py http://natas3.natas.labs.overthewire.org   -u natas3 -p '<password>' --common
```
This reveals `robots.txt` is present.

2. Open:  
   `http://natas3.natas.labs.overthewire.org/robots.txt`
   Or fetch:
```
curl -u natas3:<password> \
http://natas3.natas.labs.overthewire.org/robots.txt
```

3. The file reveals:
```
  User-agent: *
  Disallow: /s3cr3t/
```

4. Visit the directory directly:  
`http://natas3.natas.labs.overthewire.org/s3cr3t/`

5. Open `users.txt` to find the next password.  
The plaintext (kept locally) is `natas4:<password>`  
Its ROT13 is recorded above.

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
