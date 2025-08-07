**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 11: THE LOGGING SYSTEM

---

## The rsyslog Logging Daemon

* Linux uses **rsyslog** (a syslogd variant) to record system and application events.
* Configuration and control files live under `/etc/rsyslog.conf`, `/etc/rsyslog.d/`, and related locations.

### The rsyslog Configuration File

* Found at `/etc/rsyslog.conf`.
* Comprised of **modules**, **global directives**, and **rules**, all in plain-text with extensive comments.

### The rsyslog Logging Rules

* **Syntax**: `facility.priority    action`

  * **facility**: source (e.g., `auth`, `kern`, `mail`, `user`, or `*`).
  * **priority**: severity (`debug`, `info`, `notice`, `warning`, `err`, `crit`, `alert`, `emerg`).
  * **action**: destination (e.g., file under `/var/log/`).
* Examples:

  ```text
  auth,authpriv.*    /var/log/auth.log    # All auth messages
  kern.crit          /var/log/kern.log    # Critical kernel errors
  *.emerg            *                    # Emergencies go to all users
  ```

## Automatically Cleaning Up Logs with logrotate

* **logrotate** archives and optionally compresses old logs, preventing disk fill-up.
* Main config: `/etc/logrotate.conf` (includes `/etc/logrotate.d/`).
* Key directives:

  * `weekly` (time unit)
  * `rotate 4` (keep last 4 periods)
  * `create` (start fresh logs)
  * `compress` (enable compression)
* Adjust `rotate` count for retention length (e.g., `rotate 26` for \~6 months).

## Remaining Stealthy

Hackers must cover trails; defenders must know how logs reveal attacks.

### Removing Evidence

* **shred** securely deletes logs by overwriting data:

  ```bash
  shred -f -n 10 /var/log/auth.log.*  # overwrite 10 times
  ```
* Overwrites wildcards to include rotated logs (`auth.log.1`, etc.).

### Disabling Logging

* Stop the rsyslog daemon (requires root):

  ```bash
  service rsyslog stop    # Halts all new log entries
  ```

---

## Summary

Log files record vital system events and security information. You saw how to configure rsyslog rules, automate log rotation with logrotate, and, from an attacker’s perspective, how to shred or disable logs to erase footprints.

## Exercises

1. Use `locate rsyslog` to list all rsyslog-related files.
2. Edit `/etc/logrotate.conf` to rotate logs weekly.
3. Disable logging (`service rsyslog stop`) and observe entries in `/var/log/syslog`.
4. Shred all `kern.log` files using `shred`.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
