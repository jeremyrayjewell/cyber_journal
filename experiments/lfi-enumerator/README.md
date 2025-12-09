# LFI Enumerator

`lfi_enum.py` is a lightweight Python 3 script for automating Local File Inclusion (LFI) testing against web applications. It supports optional HTTP Basic Authentication, custom or built‑in payloads, and automatic detection of responses that resemble password file leaks.

## Features

- Tests for LFI vulnerabilities using:
  - Built‑in common payloads  
  - Custom payloads from a file or command line
- Supports HTTP Basic Authentication via `-u` and `-p`
- Highlights likely `/etc/passwd` or sensitive file disclosures
- Optional delay between requests to avoid rate‑limiting
- Simple output for easy parsing and inspection

## Usage

`python3 lfi_enum.py <base_url> [OPTIONS]`


### Positional Argument

- `base_url` — The URL up to the LFI parameter (e.g., `http://target.com/index.php?page=`)

### Optional Flags

| Flag                   | Description                                    |
|------------------------|------------------------------------------------|
| `-u`, `--username`     | HTTP Basic Auth username                       |
| `-p`, `--password`     | HTTP Basic Auth password                       |
| `--payload <string>`   | Test a single custom payload                   |
| `--payloads <file>`    | Load payloads from a file (one per line)       |
| `--common`             | Use built‑in common payload list               |
| `--delay <float>`      | Delay between requests (seconds)               |

If no payload flag is provided, the script defaults to the built‑in payloads.

## Examples

Use built‑in payloads with authentication:

`./lfi_enum.py http://target/index.php?page=
 -u admin -p password`


Test a single custom payload:

`./lfi_enum.py http://target/index.php?page=
 --payload ../../../../etc/passwd`

Test with payloads from a file:

`./lfi_enum.py http://target/index.php?page=
 --payloads payloads.txt --delay 0.25`


## Built‑in Payloads

- `etc/passwd`
- `../etc/passwd`, `../../etc/passwd`, `../../../etc/passwd`, etc.
- `....//....//etc/passwd`
- `php://filter/convert.base64-encode/resource=index.php`
- `/var/log/apache2/access.log`
- `/var/log/auth.log`

## Detection Logic

A response is flagged as `LIKELY_PASSWD` if the body contains indicators such as:

- `root:x:0:0:`  

## Dependencies

- Python 3.6+
- `requests` library

Install with:

`pip install requests`


## License

MIT License

## Author

Jeremy Ray Jewell  
[Github](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyyrayjewell
