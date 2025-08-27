# dir_enum.py

A minimal **directory enumeration tool** written in Python.

Supports:
- HTTP **Basic Auth**
- **Built-in common paths** (`files/`, `images/`, `uploads/`, etc.)
- **Custom wordlists**
- **Detection of directory listings** (Apache, Nginx, etc.)
- **Colorized output** and simple classifications (`DIR-LISTING`, `OK`, `FORBIDDEN`, `NOTFOUND`)
- **Verbose mode** to show response headers and body previews

---

## Installation

Requires Python 3 and `requests`:

    pip install requests

Make the script executable:

    chmod +x dir_enum.py

---

## Usage

    ./dir_enum.py <base_url> [options]

Examples:

    # Quick scan with built-in common paths
    ./dir_enum.py http://target/ --common

    # With Basic Auth
    ./dir_enum.py http://example.com -u user -p 'password' --common

    # With a custom wordlist
    ./dir_enum.py http://target/ -w wordlist.txt

    # Verbose output
    ./dir_enum.py http://target/ --common -v

---

## Output Symbols

- `[+]` **DIR-LISTING** — directory listing detected, previewing found files.
- `[*]` **OK / REDIR** — valid page or redirect.
- `[-]` **FORBIDDEN / NOTFOUND** — blocked or missing paths.
- `[?]` **HTTP XXX** — other status codes.

---

## Options

- `-u`, `--username` → Basic Auth username
- `-p`, `--password` → Basic Auth password
- `-w`, `--wordlist` → Path to custom wordlist
- `--common` → Use built-in list of common paths
- `--timeout` → Request timeout (default: 8s)
- `--delay` → Delay between requests
- `--headers` → Extra headers (e.g., `--headers "User-Agent: X"`)
- `--max-preview` → Max preview items in directory listing (default: 5)
- `-v`, `--verbose` → Verbose mode (headers + body snippet)
- `--color` → Force color output: `auto` (default), `always`, or `never`

---

## Example Run

    ./dir_enum.py http://example.com -u user -p 'password' --common

    [+] http://example.com/files/         DIR-LISTING  -> [pixel.png, users.txt]
    [*] http://example.com/robots.txt     NOTFOUND
    [-] http://example.com/backup/        FORBIDDEN

---

## Notes

- This tool is meant for **educational and authorized use only**.
- Do not run against systems you do not own or have permission to test.

___

Author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
