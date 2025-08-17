# Automate Cybersecurity Tasks with Python – Notes  

## Google Cybersecurity Certificate – Cybersecurity Foundations (Course 7 of 9) 

[Coursera](https://www.coursera.org/learn/automate-cybersecurity-tasks-with-python/home/welcome)

---

### **Course Overview**  
This course teaches how to use **Python** to automate common cybersecurity tasks. It begins with foundational programming concepts (data types, variables, conditionals, and loops), then moves into **functions**, **modules/libraries**, and **readability** practices. You then work with **strings** and **lists** (including **regular expressions** for pattern matching), and finish by **opening/reading/parsing files** and **debugging** to put Python into practice for security workflows.

---

## Core Structure  
1. Introduction to Python  
2. Write effective Python code  
3. Work with strings and lists  
4. Put Python into practice (files, parsing, debugging)

---

## Key Cybersecurity Concepts & Acronyms  
- **Regex** – Regular expressions for pattern matching in logs/text  
- **PEP 8** – Python style guidelines for readable, maintainable code  
- **I/O** – Input/Output; reading from and writing to files  
- **PSL** – Python Standard Library (e.g., `re`, `csv`, `os`, `datetime`, `statistics`)  
- **SOC** – Security Operations Center; Python aids detection/analysis/response automation  
- **CLI** – Command-line interface (Linux shell usage alongside Python)

---

## Core Skills Introduced  

**Transferable Skills:**  
- Analytical problem-solving with programmatic logic  
- Clear documentation (comments, docstrings, naming conventions)  
- Workflow design and reproducibility for team handoffs  

**Technical Skills:**  
- Writing basic Python scripts and using built-in functions  
- Creating reusable **functions** with parameters and return values  
- Importing and using **modules/libraries**  
- Applying **regular expressions** to extract indicators from text/logs  
- **File handling** (read/write/append) and basic parsing strategies  
- **Debugging** techniques and error handling

---

## Python Environments
- **Notebooks** (Jupyter, Google Colab)
  - *Code cells* run Python and show output.
  - *Markdown cells* document code (markdown language).
- **IDEs** (with GUI): editing, linting, debugging.
- **Command line (CLI)**: run scripts, navigate files/dirs, open editors.

**Key takeaway:** In this course you’ll mainly use **notebooks**.

---

## Core Data Types
- **String**: ordered characters in quotes, e.g., `"updates needed"`, `""` (empty string).
- **List**: ordered, mutable collection `[12, "ok", True, 4.5]`, `[]` (empty list).
- **Integer**: whole numbers `-100`, `0`, `500`.
- **Float**: decimals `-2.2`, `0.0`, `0.34`.  
  - `/` returns float: `1/4 -> 0.25`
  - `//` floor division (keeps type): `1//4 -> 0`, `1.0//4.0 -> 0.0`
- **Boolean**: `True`, `False` (no quotes).
- **Tuple**: ordered, **immutable** `(46, 2, 13)`. Memory-efficient.
- **Dictionary**: key–value pairs `{1: "East", 2: "West"}`.
- **Set**: unordered unique values `{"jlanksy", "drosas"}`.

---

## Variables (Assign & Reassign)
- Assign: `username = "nzhao"`
- Reassign: `username = "zhao2"`
- Assign variable to variable:  
  `old_username = username` (copies current value).
- **Naming rules**
  - Use letters/numbers/underscores; start with letter or `_`.
  - Case-sensitive: `time`, `Time`, `TIME` are different.
  - Don’t use keywords/built-ins (`True`, `if`, etc.).
  - Prefer `snake_case`: `login_attempts`, `device_id`.
  - Be descriptive, not overly long; avoid confusingly similar names.

---

## Conditionals
- **Comparison ops**: `>`, `<`, `>=`, `<=`, `==`, `!=`
- **Logic ops**: `and`, `or`, `not`
- **Syntax**
    if status == 200:
        print("OK")
    elif status == 400:
        print("Bad Request")
    elif status == 500:
        print("Internal Server Error")
    else:
        print("check other status")

- Parentheses are optional for a single condition, but required to group with `not`:  
  `if not(status >= 200 and status <= 226): ...`
- `elif` chain stops at first `True`; multiple independent `if` all run if true.

---

## Loops
### for loops
- Iterate sequence:
    for i in ["elarson", "bmoreno", "tshah", "sgilmore"]:
        print(i)
- Loop over list variable:
    computer_assets = ["laptop1", "desktop20", "smartphone03"]
    for asset in computer_assets:
        print(asset)
- Loop over string (character-by-character):
    for ch in "security":
        print(ch)
- `range(start, stop, step)`—`stop` is **exclusive**:
    for i in range(5):   # 0..4
        print(i)

### while loops
- Iterate while condition is `True`:
    i = 1
    while i < 5:
        print(i)
        i = i + 1

- Integer-controlled condition:
    login_attempts = 0
    while login_attempts < 5:
        print("Login attempts:", login_attempts)
        login_attempts += 1

- Boolean-controlled condition:
    count = 0
    login_status = True
    while login_status == True:
        print("Try again.")
        count += 1
        if count == 4:
            login_status = False

### Managing loops
- `break` exits loop early:
    for asset in ["laptop1", "desktop20", "smartphone03"]:
        if asset == "desktop20":
            break
        print(asset)

- `continue` skips current iteration:
    for asset in ["laptop1", "desktop20", "smartphone03"]:
        if asset == "desktop20":
            continue
        print(asset)

- **Infinite loops**: interrupt with `CTRL-C`/`CTRL-Z` when needed.

---

## Functions
### Built-in vs. User-defined
- Built-in examples: `print()`, `len()`, `type()`, `max()`, `min()`, `sorted()`.
- Define your own:
    def display_investigation_message():
        print("investigate activity")

- Call:
    display_investigation_message()

- Use in conditionals:
    application_status = "potential concern"
    if application_status == "potential concern":
        print("application_log:")
        display_investigation_message()

- **Avoid unintended recursion** (can cause infinite loop):
    def func1():
        func1()  # bad without exit logic

### Parameters, Arguments, Return
- Parameters are variables in function **definition**:
    def remaining_login_attempts(maximum_attempts, total_attempts):
        return maximum_attempts - total_attempts

- Arguments are values in the **call**:
    remaining_attempts = remaining_login_attempts(3, 3)

- `return` exits the function immediately; no parentheses after `return`.

### Global vs Local Variables
- **Global**: defined outside functions; accessible everywhere.
    device_id = "7ad2130bd"

- **Local**: parameters and variables inside a function; not accessible outside.
    def greet_employee(name):
        total_string = "Welcome " + name
        return total_string

- Shadowing (same name local vs global) can confuse; prefer passing via parameters.

**Best practice:** keep function logic self-contained; avoid relying on globals for inputs.

---

## Built-in Functions (Details & Tips)
- `print(*args)`: prints any number of args.
    month = "September"
    print("Investigate failed login attempts during", month, "if more than", 100)

- `type(obj)`: returns data type (accepts **one** argument).
    print(type("security"))  # str

- **Function chaining / nesting**:
    print(type("This is a string"))  # passes type() output into print()

- `max(iterable or values...)` / `min(...)`:
    time_list = [12, 2, 32, 19, 57, 22, 14]
    print(min(time_list))  # 2
    print(max(time_list))  # 57

- `sorted(iterable)` returns a **new** list; original unchanged.
    time_list = [12, 2, 32, 19, 57, 22, 14]
    print(sorted(time_list))  # sorted copy
    print(time_list)          # original

  *Note:* cannot sort heterogeneous types, e.g., `[1, 2, "hello"]` raises error.

---

## Modules & Libraries
### Python Standard Library (PSL)
- Examples: `re` (regex), `csv` (CSV files), `glob`/`os` (filesystem/CLI), `time`/`datetime` (timestamps), `statistics` (mean/median).
- Import entire module:
    import statistics
    mean_failed = statistics.mean([20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19])
    median_failed = statistics.median([20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19])

- Import specific functions:
    from statistics import mean, median
    mean_failed = mean(monthly_failed_attempts)
    median_failed = median(monthly_failed_attempts)

### External Libraries
- Install in notebooks:
    %pip install numpy
- Import after install:
    import numpy

---

## PEP 8, Comments, & Syntax Hygiene
- **Comments**
  - Single-line: start with `#` (keep lines ≤ 79 chars).
      # Print elements of 'computer_assets' list
      for asset in computer_assets:
          print(asset)
  - Multi-line: multiple `#` lines, or **docstrings** (`""" ... """`) not assigned to a variable.

- **Indentation**
  - 4 spaces per level; nested blocks add 4 more (e.g., while + inner if = 8 spaces).

- **Common syntax checks**
  - Strings in quotes: `username = "bmoreno"`
  - Don’t quote ints/floats/bools: `login_attempts = 5`, `percentage_successful = 0.8`, `login_status = True`
  - Lists in brackets with commas: `username_list = ["bmoreno", "tshah"]`
  - Colons at end of headers: `if ...:`, `while ...:`, `for ...:`, `def ...:`

---

## Strings for Security Work
- Store IPs, usernames, URLs, IDs (non-numeric operations).
- **Indexing** (0-based), also negative indices (`-1` last char).
  - `"h32rb17"[0] -> "h"`
  - `"h32rb17"[0:3] -> "h32"` (stop index excluded)

- Helpful functions/methods:
  - `str(obj)` → string conversion (e.g., numeric IDs to search/slice).
  - `len(s)` → length
  - `"dept".upper()` / `"Dept".lower()`
  - `"h32rb17".index("r") -> 3`  
    - Raises error if not found; returns **first** match.
    - Substrings allowed: `"tsnow, tshah".index("tshah") -> 7` (be precise—`"ts"` matches earlier).

---

## Lists for Security Work
- Store usernames/IPs/URLs/device IDs.
- Index/slice like strings:
    username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
    username_list[2]       # "tshah"
    username_list[0:2]     # ["elarson", "fgarcia"]

- Lists are mutable (change elements):
    username_list[1] = "bmoreno"

- Common methods:
    # insert at index
    username_list.insert(2, "wjaffrey")
    # remove first matching element
    username_list.remove("elarson")
    # append to end
    username_list.append("btang")
    # find index of first occurrence
    idx = username_list.index("tshah")  # 2

*Note:* `.index()` returns first match only.

---

## Regular Expressions (re)
- Import:
    import re

- Find all matches: `re.findall(pattern, string)` → list of matches.

- **Character classes / escapes**
  - `\w` word char (alnum + underscore)
  - `\d` digit `[0-9]`
  - `\s` whitespace (space, etc.)
  - `.` any char
  - `\.` literal dot

- **Quantifiers**
  - `+` one or more
  - `*` zero or more
  - `{n}` exactly n times
  - `{n,m}` between n and m times

- Examples:
    re.findall(r"\w", "h32rb17")         # all 7 characters
    re.findall(r"\d", "h32rb17")         # ['3','2','1','7']
    re.findall(r"\d+", "h32rb17")        # ['32','17']
    re.findall(r"\d*", "h32rb17")        # includes empty-string matches
    re.findall(r"\d{2}", "h32rb17 k825t0m c2994eh")    # ['32','17','82','29','94']
    re.findall(r"\d{1,3}", "h32rb17 k825t0m c2994eh")  # lengths 1..3

- Pattern construction (username + colon + space + digits):
    pattern = r"\w+:\s\d+"
    s = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
    re.findall(pattern, s)  # ['bmoreno: 12', 'tshah: 7', 'sgilmore: 5']

*Note:* Regex matches scan left→right and return first valid matches per pattern progression.

---

## File Handling (Read/Write)
- Open with context manager (**auto-closes file**):
    with open("update_log.txt", "r") as file:
        updates = file.read()
    print(updates)  # .read() returns a string

- Absolute path example (when not in same directory):
    with open("/home/analyst/logs/access_log.txt", "r") as file:
        data = file.read()

- Modes: `"r"` read, `"w"` write (overwrite or create), `"a"` append.
    # overwrite or create
    with open("update_log2.txt", "w") as file:
        file.write("Created new log\n")

    # append line
    line = "jrafael,192.168.243.140,4:56:27,True\n"
    with open("access_log.txt", "a") as file:
        file.write(line)

*Tip:* File paths and names are **strings** and must be quoted.

---

## Automation Patterns (Putting It Together)
- **Variables** store working state (counters, flags, IDs).
- **Conditionals** gate actions (status checks, thresholds).
- **Loops** iterate datasets (log lines, usernames).
- **Functions** encapsulate reusable checks/transformations.
- **Strings/Lists** are the primary structures for log parsing.
- **Files** provide input logs and output reports.

### Example: Count all logins by a flagged user
    def count_logins(flagged_user, usernames):
        count = 0
        for name in usernames:
            if name == flagged_user:
                count += 1
        return count

---

## Quick Reference / Key Takeaways
- Master Python **types, variables, conditionals, loops, functions**—these are the backbone of SOC automation.
- Use built-ins (`print`, `type`, `min`, `max`, `sorted`) to simplify common tasks; remember `sorted()` returns a **new** list.
- Import PSL modules (`re`, `csv`, `os`, `glob`, `time`, `datetime`, `statistics`) and external libs (install first with `%pip install ...`).
- Follow **PEP 8**: 4-space indentation, helpful comments/docstrings, clear names, lines ≤ 79 chars.
- **Regex** + **file I/O** are essential for parsing/searching logs and writing results.

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
