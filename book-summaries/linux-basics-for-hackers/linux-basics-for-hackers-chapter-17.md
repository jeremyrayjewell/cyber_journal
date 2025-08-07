**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 17: PYTHON SCRIPTING BASICS FOR HACKERS

---

## Adding Python Modules

### Using pip

* Install Python 3 package manager:  `apt-get install python3-pip`
* Download modules:  `pip3 install <package>`
* Locate package:  `pip3 show <package>`

### Installing Third‑Party Modules

* Download tarball (e.g., via `wget`).
* Extract:  `tar -xzf name.tar.gz`
* Install:  `python setup.py install`

## Getting Started Scripting with Python

### Variables

* Dynamically typed: no declaration needed.
* Common types: string, integer, float, list (`[]`), dictionary (`{'key':value}`).

### Comments

* Single line: start with `#`.
* Multi‑line: enclose in `"""`.

### Functions

* Built‑in examples:

  * `print()`, `len()`, `int()`, `float()`, `sorted()`, `help()`.
* Importable modules provide extra functions.

## Lists

* Ordered, iterable collections.
* Zero‑based indexing: `mylist[0]` is first element.

## Modules

* Code organized in files; import with `import <module>`.
* Essential for reusing functionality (e.g., `socket`, `ftplib`, `nmap`).

## Object‑Oriented Programming (OOP)

* Objects have attributes (properties) and methods (actions).
* Classes are blueprints; subclasses inherit behavior.

## Network Communications in Python

### Building a TCP Client

* Use `socket.socket()` to create client socket.
* Connect:  `s.connect((host, port))`.
* Receive banner:  `s.recv(1024)`.
* Close socket:  `s.close()`.

### Creating a TCP Listener

* Bind server socket:  `s.bind((IP, port))`.
* Listen:  `s.listen(1)`, accept connections, then `conn.recv()`.

## Dictionaries, Loops, and Control Statements

### Dictionaries

* Unordered key\:value stores, iterable with `for key in dict`.

### Control Statements

* `if`, `if...else` for branching based on conditions.
* Indentation defines code blocks.

### Loops

* `for` iterates over iterables.
* `while` repeats while condition is true.

## Improving Our Hacking Scripts

* Use lists and `for` loops to iterate through ports/services.
* Example: multi‑port banner grabber using list of ports.

## Exceptions and Password Crackers

* `try/except` to handle errors or invalid inputs.
* Example: FTP password cracker with nested `try` blocks and wordlist iteration.

## Summary

Python’s readability, built‑in and third‑party modules, and network libraries make it a powerful choice for automating reconnaissance and brute‑force tasks. You built basic hacking tools: banner grabbers, TCP listeners, and an FTP cracker.

## Exercises

1. Build and modify the SSH banner grabber for port 21.
2. Prompt for IP address instead of hardcoding.
3. Update TCP listener to prompt for listen port.
4. Enhance FTP cracker to read usernames from a wordlist.
5. Add exception handling to banner grabber for closed ports (`"no answer"`).

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
