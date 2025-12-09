# Write-up: Natas 08 → 09  
**Date:** 2025-12-08  

## Obfuscated password (ROT13)

`MR1px82yzqTVbReyuDtJAQ6w2Jmm6o6g`

## OBJECTIVE

> The page contains an input box asking for a “secret.”  
> The source code reveals:
> ```
><?
>$encodedSecret = "3d3d516343746d4d6d6c315669563362";
> function encodeSecret($secret) {
>    return bin2hex(strrev(base64_encode($secret)));
>}
> if(array_key_exists("submit", $_POST)) {
>    if(encodeSecret($_POST['secret']) == $encodedSecret) {
>    print "Access granted. The password for natas9 is <censored>";
>    } else {
>    print "Wrong secret";
>    }
>}
>?>
> ```
> The challenge is to reverse `encodeSecret()` and supply the correct secret so the page prints the password for **natas9**.

## PURPOSE

This level teaches **reversing a custom encoding routine**. The developer implemented a reversible transformation made of three steps, each of which being PHP built-ins:

  1. `base64_encode($secret)` - encodes the input in base64
  2. `strrev()` — reverse the resulting string, easily guessable even without PHP experience
  3. `bin2hex()` — hex‑encode it... the "binary" reference threw me off until I learned that in PHP a "binary string" just means raw bytes

Since all three operations are reversible, we can invert them to discover the original secret. The key principle on display here is **if you can see the encoder, you automatically have the decoder.** Encoding is not encryption.

## SOLUTIONS

In bash we can reverse the encoding by first running `echo '3d3d516343746d4d6d6c315669563362' | xxd -r -p`, `echo '<previous result>' | rev`, and finally `base64 -d <<< '<previous result'`. Note that the result of base64 encoding will differ from those of decoding, and bin to hex will differ from hex to bin. The PHP encoded with base64, so we will be *decoding*. The PHP also converted bin to hex, so we will be going *from hex to bin*. The `xxd` utlity will perfom bin to hex with just the flag `-p` ("plain mode" for a clean hex string output of hexadecimal byte values) but will perform hex to bin with `-p` and `-r` ("reverse") together. For its part, `base64` encooding and decoding syntices vary significantly.

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)

