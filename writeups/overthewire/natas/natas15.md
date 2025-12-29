# Write-up: Natas 15 → 16  
**Date:** 2025-12-28  

## Obfuscated password (ROT13)  
`uCxwXLivYDpgRJ33DzhKY6rQIsZJ4fTb`

---

## OBJECTIVE

> Use blind SQL injection to extract the password for the user `natas16`, even though the application does not display any direct SQL results.

---

## PURPOSE

This level demonstrates a **blind SQL injection scenario**. Unlike earlier levels, the application does not output database results directly. Instead, it only indicates whether a query returned *any* rows.

By observing this binary response, it becomes possible to infer sensitive information one character at a time.

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
natas16" AND BINARY SUBSTRING(password,1,1)="a" --
```

If the first character of the password is `'a'`, the query evaluates to true, and we get confirmation. Otherwise, we try another character.

Using this idea, we brute-force the password character by character. I automated the process with my reusable script [`blind_sqli_extractor.py` (stored under my `cyber_journal/experiments/` tooling)](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/blind_sqli_extractor).

Command used to extract the Natas16 password:

```bash
python3 blind_sqli_extractor.py \
  --url "http://natas15.natas.labs.overthewire.org/" \
  --user natas15 \
  --password <NATAS15_PASSWORD> \
  --param username \
  --true-string "This user exists" \
  --max-length 32
```

- The script iterates through a known character set (letters and digits).
- The `BINARY` keyword enforces case sensitivity.
- It advances position-by-position until the full 32-character password is recovered.

Once complete, the password for `natas16` is revealed.


---

## TAKEAWAYS

- Blind SQL injection does not require visible query output  
- Boolean responses are sufficient to extract sensitive data  
- Parameterized queries completely prevent this vulnerability  
- Automation is essential for practical exploitation  

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
