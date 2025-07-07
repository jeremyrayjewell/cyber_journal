SUMMARY OF 
**LINUX BASICS FOR HACKERS** 
(FIRST EDITION) BY OCCUPYTHEWEB

---

# CHAPTER 1: GETTING STARTED WITH THE BASICS

---

- This chapter aims at providing some fundamental skills to begin hands-on engagement

## Introductory Terms and Concepts

- **Binaries**: executable files, including utilities and applications, often in */usr/bin* or *usr/sbin*.

- **Case sensitivity**: Linux filesystem does not recognize uppercase letters as their lowercase ounterparts, nor vice versa. Like Python.

- **Directory**: hierarchically-organized location within the filesystem. Like Windows' *folders*.

- **Home**: a directory holding directories belonging to each individual user; */home/user*. A default location for each user's files. 

- **Kali**: a Debian-based Linux distribution focused on penetration testing with many pre-installed tools for that purpose. 

- **root**: the system administrator (not to be confused with the *root* directory `/` nor the *root user* directory `/root`).

- **Script**: commands run via interpreters; may be bash, Pyhton, Perl, etc.  

- **Shell**: command-running environment and interpreter. Most typical for Linux, and that used in the book, is *bash* (*Bourne-again shell*)

- **Terminal**: the text-based command line interface (CLI) you find inside a terminal emulator. The terminal interfaces with the shell to implement the CLI commands.

## A Tour of Kali

- After logging in you will want to understand the terminal interface and file structure.

### The Terminal

- In Kali you can open the terminal via its icon on the desktop (top left). The terminal opens the shell. At this point the user may opt to change their password using `passwd`.

### The Linux Filesystem

- The Linux filesystem is distinct from others. It doesn't priotize physical media like Windows does.

- It is advisable *not* to login as root user unless it is necessary so as to avoid having your system compromised with administrator-level permissions enabled. For the exercises in the book, however, the learner can remain in root.  

- The top of the system structure is *root*, or `/`. Here is a lay out of the root directory and its most important subdirectories:

<pre markdown>
	/
	├──/root [Confusingly, NOT the `/` root, but rather the home directory of the root user]
	├──/boot [Kernel image]
	├──/etc  [System configuration files]
	├──/home [User directories]
	├──/mnt  [General-purpose mount point]
	├──/media[CD/USB mount point]
	├──/proc ["Processes"; view of internal kernal data]
	├──/sys	 ["System"; kernel's view of internal hardware]
	├──/dev	 ["Devices"; special device files]
	├──/bin  [Binaries]
	├──/sbin [Binaries]
	├──/lib  [Libraries[
	└──/usr  ["Second tier" for shareable, read-only userland programs/files]
	    ├──/bin  [Binaries]
	    ├──/sbin [Binaries]
	    └──/lib  [Libraries]
</pre>

## Basic Commands in Linux

### Finding Yourself with pwd

- `pwd`: *present/print working directory*. 

### Checking Your Login with whoami

- `whoami`: prints your working user name

### Navigating the Linux Filesystem

- `cd`: *change directory*. `cd /` will take you to *root* `/`, `cd /etc` will take you to `/etc`.

- `cd` then `pwd`: running `pwd` after changing directories with `cd` helps reiterate your path and location.

- `cd ..` takes you up one level from where you are, `cd ../..` takes you up two levels, `cd ../../..` three, etc.

- not mentioned here, though useful, is the distinction between relative and absolute locations when using `cd`. Absolute routes are prefixed with `/`, which relative routes lack. As a result, `cd /etc` will take you to the `etc` directory in the root `/` directory from anywhere in the filesystem. `cd etc` would only take you to the same directory if it is executed while working in the `/` directory.

- `ls`: *list* prints the contents of a directory.

- `ls -l`: *list* with a `-l` short option/flag/switch displays more details (*long-listing format*). Interchangeable with `--long`. 	

- `ls -la`: The addition of the `-a`flag shows *all* contents, including hidden ones. Interchangeable with `--all`, and similar to `-A`/`--almost-all` which exclude the `.` and `..` special entries. 

### Getting Help

- Dedicated help files: conventionally, but not universally, `-h`, `--help`, or `-?` flags.

### Referencing Manual Pages with man

- `man`: Manual pager utils - an interface to the system reference manuals. Run `man` plus the command/utility/application (i.e. `man ls`, `man cat`, `man man`).

- Scroll through entries using `ENTER`, `PG UP`/`PG DM`, or the arrow keys. Press `q` to quit.

## Finding Stuff
	
### Searching with locate

- `locate`: searches filenames anywhere on the system using a periodically updated database (typically `/var/lib/mlocate/mlocate.db`). The database can be updated manually using `sudo updatedb`, which may be necessary if a file you are looking for is newer than the last automatic indexing.

- `locate` is very fast, but susceptible to errors in relation to databse updates.

### Finding Binaries with whereis

- `whereis`: searches binaries, source, and man pages via a small set of predefined system paths (i.e. `/bin`, `/usr/bin`, `/usr/share/man`).

- `whereis` is non-recursive and checks only standard system locations, and as such is non-exhaustive. It also ignores aliases, functions, and built-in commands.

### Finding Binaries in the PATH Variable with which

- `which`: searches executables in your `$PATH`; walks through each directory in your shell's `PATH` until it finds a matching executable. In other terms, it looks to see what is executed when a term is invoked.

- `which` is limited to your `PATH`, and is best to use when confirming which binary is being invoked.	

### Performing More Powerful Searches with find

- `find /`: recursively traverses the live filesystem descending from a starting point of `/` evaluating expressions on the fly to find files that match their criteria. The most flexible, up-to-the-minute search type. `/` can be substituted for any other starting point (i.e. `/etc`)

- `find` is always up-to-date, but can be slow on large trees.

- Use case: `find / -type f -name apache2`, where `/` is the starting directory, `-type f` specifies file type *file*, and `-name apache2` specifies name *apache2*.

- Limiting the scope by choosing a nested directory can save time, i.e. `find /etc -type f -name apache2`.

### NOTE: A Quick Look at Wildcards
<pre markdown>

- `*`: *match zero or more characters*, i.e. `ls *.txt` lists all files ending in ".txt", `ls foo*` lists all files beginning with "foo"

- `?`: *match exactly one character*, i.e. `ls file?.sh` lists "file1.sh", "filaA.sh", but not "file10.sh".

- Not mentioned here: `[...]`: *character classes*, i.e. `ls report[0-9].pdf` lists "report0.pdf ... report9.pdf". `ls report[!0-9]` excludes digits 0-9, returning "reportA.pdf"

</pre>

	### Filtering with grep

## Modifying Files and Directories
	
	### Creating Files

	### Creating a Directory

	### Copying a File

	### Renaming a File

	### Removing a File

	### Removing a Directory

## Go Play Now!

## Exercises

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
