# Write-up: Bandit 21 → 22
**Date:** 2025-08-13

## Obfuscated password (ROT13): 
`gEnr0HsO9i0HmoPqa9pL0tDaqf9TS58D`

## OBJECTIVE
>"A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed."

## PURPOSE
This level teaches you to read **system cron jobs** (`/etc/cron.d/...`), trace the **command** a cron job runs (often a small script), and infer where the script writes the **target secret**, then read it.

A **cron job** is a scheduled task on Unix/Linux that runs **automatically** at times you specify. It's handled by the **cron daemon** (`cron`), which wakes up every minute, checks its schedules, and launches any jobs that are due. Trivia: its named is derived from rhe Greek *chronos*, meaning "time". While some systems now favor **systemd timers** for scheduling (unit files + `systemd`), **cron** remains ubiquitous for its simplicity and portability.

We need to inspect the cron entry that is running. Normayll we would first need to find out where it lives, but our objective tells us it it `/etc/cron.d`. Once we navigate there we can run `ls -l` to see `cronjob_bandit22`. Running cat on that gives us the following:

```
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

That us know that cron is running `/usr/bin/cronjob_bandit22.sh`. Next, when we cat that, we get:

```
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/	
```

We see that this script is performing two actions: `chmod` sets permissions on the file and then `cat` copies the next password to it. We can then cat that file to receive the next password.


bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
bandit21@bandit:/etc/cron.d$ 


## SOLUTIONS

- `ls -l /etc/cron.d`
- `cat /etc/cron.d/cronjob_bandit22`
- `cat /usr/bin/cronjob_bandit22.sh`
- `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`


---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
	

	
