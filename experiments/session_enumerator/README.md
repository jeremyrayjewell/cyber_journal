# session_enumeratorr

A lightweight Python utility for enumerating predictable session identifiers in web applications.
Designed for educational use, CTF challenges, and controlled security testing.

![Session Enumerator Screenshot](session_enumerator.png)

---

## Overview

`session_enumerator` targets applications that rely on predictable or insecure session identifiers.
Instead of brute-forcing credentials, it tests possible session values directly to identify authenticated or privileged sessions.

This technique is commonly applicable when:
- Session IDs are numeric or low-entropy
- The application trusts client-supplied session identifiers
- Authentication state is tied directly to the session ID
The tool was developed while solving OverTheWire Natas Level 18, where the application relied on predictable PHP session IDs.

---

## How It Works

Sends HTTP requests using a supplied authentication context.
- Iterates through a range of possible session identifiers.
- Injects each candidate as a session cookie.
- Detects successful authentication by matching a known response string.
- Stops when a valid session is discovered.
The approach avoids brute-forcing credentials and instead exploits flawed session management logic.

---

## Usage

```
python3 session_enumerator.py \
  <url> \
  <username> \
  <password> \
  [options]

```
---

## Arguments

| Option          | Description                                          |
| --------------- | ---------------------------------------------------- |
| `--cookie-name` | Name of the session cookie (default: PHPSESSID)      |
| `--start`       | Starting session ID (default: 1)                     |
| `--end`         | Ending session ID (default: 640)                     |
| `--match`       | Response string indicating successful authentication |
| `--delay`       | Delay between requests (seconds)                     |

---

## Ethical Notice

This tool is intended solely for educational use and authorized security testing.
Do not use it against systems you do not own or have permission to test.

---

## Author

Jeremy Ray Jewell  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
