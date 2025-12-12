# Write-up: Natas 11 → 12  
**Date:** 2025-12-11  

## Obfuscated password (ROT13)  
`?`

---

## OBJECTIVE

> The site sets a cookie called `data`, which is a **base64-encoded blob**. The source reveals:
>
> ```php
>$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
>
>function xor_encrypt($in) {
>    $key = '<censored>';
>    $text = $in;
>    $outText = '';
>
>    // Iterate through each character
>    for($i=0;$i<strlen($text);$i++) {
>    $outText .= $text[$i] ^ $key[$i % strlen($key)];
>    }
>
>    return $outText;
>}
>
>function loadData($def) {
>    global $_COOKIE;
>    $mydata = $def;
>    if(array_key_exists("data", $_COOKIE)) {
>    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
>    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
>        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
>        $mydata['showpassword'] = $tempdata['showpassword'];
>        $mydata['bgcolor'] = $tempdata['bgcolor'];
>        }
>    }
>    }
>    return $mydata;
>}
>
>function saveData($d) {
>    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
>}
>
>$data = loadData($defaultdata);
>
>if(array_key_exists("bgcolor",$_REQUEST)) {
>    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
>        $data['bgcolor'] = $_REQUEST['bgcolor'];
>    }
>}
>
>saveData($data);
> ```
>
> Our goal is to craft a cookie that sets `"showpassword": "yes"`, using the XOR-based symmetric encryption logic.

---

## PURPOSE

In the source code we can find this `$defaultdata = array("showpassword"=>"no", "bgcolor"=>"#ffffff");`, and later in the code we see `setcookie("data", base64_encode(xor_encrypt(json_encode($d))));`. This tells us the cookie is storing a `base64`-encoded value and that that value is a result of applying an **XOR cipher** to a **JSON-encoded varsion of `$d`**. `$d` is based on `$defaultdata`, unless the user changes it via input. In short, if we don't send any input, then the cookie is just the XOR-encrypted version of `{"showpassword":"no","bgcolor":"#ffffff"}`

This level teaches how to exploit **XOR encryption** when both the plaintext and ciphertext are partially known — an example of **known plaintext attack**. XOR is symmetric: `A ^ B = C` implies `C ^ B = A` and `C ^ A = B`. If we know both the plaintext and ciphertext, we can deduce the key. Likewise, if we know the key, we can encrypt any value (e.g. `{"showpassword":"yes","bgcolor":"#ffffff"}`)

The easiest thing to do was to make a script, [so I did.](../../../experiments/xor-cookie-tool)

---

## SOLUTION

1. Copy the `data` cookie from your browser and base64-decode its value, `HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAydnTRg=`. In bash we can achieve this with `base64 -d <<< 'HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAydnTRg='`
2. XOR the decoded blob against the known JSON string it encrypts:
   ```json
   {"showpassword":"no","bgcolor":"#ffffff"}
   ```
   This gives us the XOR key.
3. Replace `"no"` with `"yes"` in the plaintext and re-XOR with the key.

Browser: Base64-encode the result and set it as the new `data` cookie, refresh the page to get the password.
Bash:

`HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAycJA0c5`

---

## TAKEAWAYS

- This was a **classic XOR known-plaintext attack**: if you know any portion of the original message, XOR lets you recover the key and craft arbitrary messages.
- Repeating XOR keys should never be used for encryption. They are trivially breakable if the attacker knows or can guess part of the plaintext.
- This is also a lesson in tampering with encoded session data.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
