**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 8: BASH SCRIPTING

---

## A Crash Course in Bash

* **Shell**: CLI interface to OS; bash is the default on most Unix/Linux.
* **Built-ins**: `echo`, `read`, plus numerous utilities.
* **Shebang**: `#!/bin/bash` tells the system to use bash interpreter.

## Your First Script: “Hello, Hackers-Arise!”

1. Create file starting with:

   ```bash
   #!/bin/bash
   # This is my first bash script.
   echo "Hello, Hackers-Arise!"
   ```
2. **Setting Execute Permissions**:

   ```bash
   chmod 755 HelloHackersArise
   ```
3. **Running HelloHackersArise**:

   ```bash
   ./HelloHackersArise
   ```

### Adding Functionality with Variables and User Input

* Prompt and read into variables:

  ```bash
  echo "What is your name?"
  read name
  echo "What chapter are you on?"
  read chapter
  echo "Welcome $name to Chapter $chapter of Linux Basics for Hackers!"
  ```

## Your Very First Hacker Script: Scan for Open Ports

### Our Task

* Automate `nmap` scans for port availability across IP ranges.

### A Simple Scanner

* Script (`MySQLscanner.sh`):

  ```bash
  #!/bin/bash
  # Find hosts with MySQL (port 3306) on local LAN
  nmap -sT 192.168.181.0/24 -p 3306 >/dev/null -oG MySQLscan
  cat MySQLscan | grep open > MySQLscan2
  cat MySQLscan2
  ```

### Improving the MySQL Scanner

* Add prompts and variables:

  ```bash
  #!/bin/bash
  echo "Enter starting IP (e.g. 192.168.181.0):"
  read firstIP
  echo "Enter ending IP (last octet):"
  read lastOctet
  echo "Enter port to scan for:"
  read port
  nmap -sT $firstIP-$lastOctet -p $port >/dev/null -oG MySQLscan
  grep open MySQLscan > MySQLscan2
  cat MySQLscan2
  ```
* Prompts user, builds range, hides raw output, filters for open ports.

## Common Built-in Bash Commands

| Command    | Function                                               |
| ---------- | ------------------------------------------------------ |
| `bg`       | Move job to background                                 |
| `break`    | Exit current loop                                      |
| `cd`       | Change directory                                       |
| `echo`     | Display arguments                                      |
| `exec`     | Execute command without new process                    |
| `export`   | Make variable or function available to child processes |
| `getopts`  | Parse script arguments                                 |
| `pwd`      | Print working directory                                |
| `read`     | Read input into variable                               |
| `readonly` | Declare variable read-only                             |
| `shift`    | Shift positional parameters                            |
| `test`     | Evaluate conditional                                   |
| `trap`     | Catch signals                                          |
| `umask`    | Set default file-create permissions                    |
| `unset`    | Remove variable or function                            |
| ...        | *(and others)*                                         |

## Summary

Bash scripting automates repetitive tasks and orchestrates tools. You learned to write, permission, and run basic scripts; incorporate variables and user input; and build simple scanners. Mastery of these foundations paves the way for more powerful scripting in Python and beyond.

## Exercises

1. Write a greeting script similar to `HelloHackersArise`.
2. Create `MSSQLscanner.sh` to find SQL Server instances (port 1433) on your LAN.
3. Enhance `MSSQLscanner` by prompting for IP range and port, then display only open ports.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
