**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 16: AUTOMATING TASKS WITH JOB SCHEDULING

---

## Scheduling an Event or Job to Run Automatically

Linux uses the **cron daemon** (`crond`) and the **cron table** (`crontab`) to run recurring tasks.

* **Crontab Format**: Seven fields per line:

  ```text
  ┌Minute (0–59)
  │ ┌Hour (0–23)
  │ │ ┌Day of Month (1–31)
  │ │ │ ┌Month (1–12)
  │ │ │ │ ┌Day of Week (0–7, Sun=0/7)
  │ │ │ │ │ ┌User
  │ │ │ │ │ │ ┌Command (absolute path)
  * * * * * user /path/to/script.sh
  ```
* Use `crontab -e` to edit your personal crontab, or directly edit **`/etc/crontab`** for system-wide jobs (includes username field).
* **Ranges** (`-`), **lists** (`,`), and **wildcards** (`*`) control scheduling granularity.

### Scheduling a Backup Task

* Run system backup at 2 AM every Sunday (hour `2`, day-of-week `0`):

  ```text
  0 2 * * 0 backup /bin/systembackup.sh
  ```
* Multiple dates (15th & 30th):

  ```text
  0 2 15,30 * * backup /bin/systembackup.sh
  ```
* Weeknights at 11 PM (Mon–Fri):

  ```text
  0 23 * * 1-5 backup /bin/systembackup.sh
  ```

### Using crontab to Schedule Your MySQLscanner

* To run `MySQLscanner.sh` daily at 9 AM as user “hacker”:

  ```text
  0 9 * * * hacker /usr/share/MySQLscanner.sh
  ```
* Weekends (Sat=6, Sun=0) at 2 AM in summer (Jun–Aug):

  ```text
  0 2 * 6-8 0,6 hacker /usr/share/MySQLscanner.sh
  ```

### crontab Shortcuts

* @yearly  (once a year)
* @monthly (once a month)
* @weekly  (once a week)
* @daily   (once a day)
* @midnight (00:00)
* @noon    (12:00)
* @reboot  (at startup)

**Example**: Run scanner at midnight daily:

```text
@midnight hacker /usr/share/MySQLscanner.sh
```

## Using `rc` Scripts to Run Jobs at Startup

Linux’s **`init`** system executes scripts in `/etc/init.d/rc` based on **runlevels**:

| Runlevel | Meaning          |
| :------: | :--------------- |
|     0    | Halt             |
|     1    | Single-user mode |
|    2–5   | Multi-user modes |
|     6    | Reboot           |

### Adding Services to `rc.d`

* Use `update-rc.d` to enable or disable services at boot:

  ```bash
  update-rc.d postgresql defaults    # start PostgreSQL on boot
  update-rc.d postgresql remove      # remove from startup
  ```
* Dependencies and runlevel symlinks are managed automatically.

## Adding Services at Boot via a GUI

* Install **`rcconf`** for a text‑based GUI:

  ```bash
  apt-get install rcconf
  rcconf
  ```
* Toggle services on/off at specific runlevels and press Enter to save.

---

## Summary

Cron and **`crontab`** enable periodic task automation for backups, scans, and maintenance.
The **`rc`** scripts and **`update-rc.d`** allow services and scripts to launch at system startup.
Together, these tools let admins and hackers schedule jobs and ensure critical services run automatically.

## Exercises

1. Schedule `MySQLscanner.sh` to run every Wednesday at 3 PM.
2. Run your scanner on the 10th of April, June, and August:

   ```text
   0 9 10 4,6,8 * hacker /usr/share/MySQLscanner.sh
   ```
3. Schedule it Tue–Thu at 10 AM:

   ```text
   0 10 * * 2-4 hacker /usr/share/MySQLscanner.sh
   ```
4. Use a crontab shortcut to run at noon daily:

   ```text
   @noon hacker /usr/share/MySQLscanner.sh
   ```
5. Add PostgreSQL to start on boot with `update-rc.d`.
6. Install `rcconf` and enable both MySQL and PostgreSQL at boot.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
