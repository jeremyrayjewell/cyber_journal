# XOR Cookie Tool 

A small Python utility for decoding and encoding XOR-encrypted cookies, built to solve the [OverTheWire Natas11](http://overthewire.org/wargames/natas/) challenge (see my writeup [here](https://github.com/jeremyrayjewell/cyber_journal/blob/main/writeups/overthewire/natas/natas11.md))

This script performs XOR decryption and encryption using a known-plaintext attack or a user-supplied repeating key. It supports both **cookie decoding** (to extract the XOR key and plaintext) and **cookie encoding** (to craft a new encrypted value).

---

## Features

- Decode a base64-encoded, XOR-encrypted cookie using known plaintext.
- Recover repeating XOR keys from known plaintext/ciphertext pairs.
- Encode arbitrary JSON values into new encrypted cookies using a known key.
- Easily integrates with bash/CTF workflows.

---

## Installation

No dependencies. Requires **Python 3.6+**.

---

## Usage

### Decode a cookie using known plaintext

```bash
python3 xor_cookie_tool.py decode \
  --cookie <base64_cookie_value> \
  --known '<known_plaintext_json>'
```

**Example:**

```bash
python3 xor_cookie_tool.py decode \
  --cookie HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAydnTRg= \
  --known '{"showpassword":"no","bgcolor":"#ffffff"}'
```

This will output the raw XOR key and decrypted JSON payload.

---

### Encode a new cookie using a known key

```bash
python3 xor_cookie_tool.py encode \
  --json '<modified_json>' \
  --key <xor_key>
```

**Example:**

```bash
python3 xor_cookie_tool.py encode \
  --json '{"showpassword":"yes","bgcolor":"#ffffff"}' \
  --key eDWoeDWoeDWoeDWo
```

This will output a new base64-encoded encrypted cookie value.

---

## How It Works

- XOR is symmetric: `plaintext ^ key = ciphertext`, and `ciphertext ^ key = plaintext`
- If you know both plaintext and ciphertext, you can derive the key.
- This script exploits that to:
  - **Recover the key** from a known JSON structure
  - **Craft new encrypted cookies** by XORing arbitrary JSON with the recovered key

---

## License

MIT License.  
Use responsibly. Educational/CTF purposes only.

---

## Author

**Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)


