# Write-up: Bandit 22 → 23
**Date:** 2025-08-14

## Obfuscated password (ROT13)
`0Ms11vbVwZIA551wK3PzFgXYLdwx54Tn`

# OBJECTIVE

>"A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

>NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints."


# PURPOSE

The primary purpose of this level, aside from building on our experience with cron, is learning to read scripts. Once again we need to start by looking at `/etc/cron.d/`. There we find `cronjob_bandit231`, which directs us to the script `bandit23 /usr/bin/cronjob_bandit23.sh` which contains the following:

```
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget

```

This script is taking the current username (the output of `whoami`) and assigning it to the shell variable `myname`. Then it assigns to the variable `mytarget` the hashed **32-hex MD5 digest** of a string using `md5sum`. The string is defined as `I am user $myname`, where `$` interpolates the value of `myname` into the string. `md5sum` provides us with the hash, but also appeads it with `  -`. This is because its print template is `<32-hex-digest><space><space><filename>`, and `-` stands for **stdin** in our case. To eliminate those, the `cut` command uses the `-d` delimiter flag with a value of `' '` and the `-f` fields flag with a value of `1`. This delimits fields by spaces and returns the first field. Altogether, that is what makes the name of the file which we seek, as we can see that the next line cats the password into a tmp file with the name of `mytarget`. If we run `echo "I am user bandit23" | md5sum` we will receive the file name.


# SOLUTIONS

- `cat /usr/bin/cronjob_bandit23.sh`
- `echo "I am user bandit23" | md5sum`
- `cat /tmp/8ca319486bfbbc3663ea0fbe81326349`

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
	