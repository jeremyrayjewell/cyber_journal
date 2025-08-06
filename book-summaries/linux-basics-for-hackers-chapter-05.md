SUMMARY OF 
**LINUX BASICS FOR HACKERS** 
(FIRST EDITION) BY OCCUPYTHEWEB

---

# CHAPTER 5: CONTROLLING FILE AND DIRECTORY PERMISSIONS

---

## Different Types of Users

Linux distinguishes between the **root user** (with unrestricted system access) and **regular users** (with limited rights). Users are grouped by function (e.g., developers, admins) so group permissions can be managed collectively. New users inherit the permissions of their assigned group.

## Granting Permissions

Files and directories have three basic permissions: **read (r)**, **write (w)**, and **execute (x)**. Permissions are assigned separately for the **owner**, the **group**, and **others**.

### Granting Ownership to an Individual User

Use `chown user filename` to transfer file ownership, allowing that user to control its permissions.

### Granting Ownership to a Group

Use `chgrp group filename` to change a file’s group, enabling all members to inherit group-level access.

## Checking Permissions

`ls -l` displays file type (first character) and three sets of `rwx` flags for owner, group, and others, plus owner, group, size, timestamp, and name.

## Changing Permissions

Only root or the file owner can modify permissions using `chmod`.

### Changing Permissions with Decimal Notation

Octal digits (0–7) map to binary `rwx` flags (`r=4, w=2, x=1`). Three digits (`ugo`) set owner, group, and others in one command (e.g., `chmod 774 file`).

### Changing Permissions with UGO

Symbolic method uses `u/g/o` for owner/group/others, operators `+`, `-`, or `=`, and the permission letters (`rwx`). Example: `chmod u-w file` removes write from owner.

### Giving Root Execute Permission on a New Tool

Downloaded scripts default to non-executable; use `chmod` (e.g., `chmod 766 tool`) to grant yourself execute rights.

## Setting More Secure Default Permissions with Masks

`umask` defines which permission bits to remove from default bases (666 for files, 777 for dirs). A `umask` of `022` results in new files having `644` and directories `755`. Users can set personal `umask` in `~/.profile`.

## Special Permissions

Three advanced bits extend basic permissions:
	
### Granting Temporary Root Permissions with SUID

Setting the SUID bit (`chmod 4xxx`) lets users execute a program with the file owner’s privileges (commonly root) for that process only.

### Granting the Root User's Group Permissions [with] SGID

SGID (`chmod 2xxx`) runs a file with owner’s group rights or makes new files in a directory inherit the directory’s group.

### The Outmoded Sticky Bit

Legacy bit ignored by modern Linux for directories; originally controlled file retention in memory.

Special bits can be exploited for privilege escalation (e.g., using SUID binaries like sudo to gain root).
	
### Special Permissions, Privilege Escalation, and the Hacker

Hackers can exploit misconfigured SUID and SGID bits to escalate privileges (e.g., running a SUID binary like `sudo` or `passwd` to gain root access or read `/etc/shadow`). Using `find / -user root -perm -4000` reveals vulnerable SUID executables.

## Summary

Linux enforces fine-grained file and directory permissions for owners, groups, and others. You now know how to view (`ls -l`), set (`chmop`, `chown`, `chgrp`), and secure defaults (`umask`), as well as how special SUID/SGID bits can grant temporary elevated rights—tools both for defending anstems.

## Exercises

- Pick a directory and run `ls -l` to observe permissions.

- Take a non-executable file and grant yourself execute rights using both octal (`chmod 777 file`) and symbolic (`chmod u+x file`) methods.

- Change a file’s owner with `chown`.

- Use `find` to list all files with the SGID bit set (`find / -perm -2000`).

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
