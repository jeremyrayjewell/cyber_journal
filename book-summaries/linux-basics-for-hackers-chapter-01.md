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

- not mention here, though useful, is the distinction between relative and absolute locations when using `cd`. Absolute routes are prefixed with `/`, which relative routes lack. As a result, `cd /etc` will take you to the `etc` directory in the root `/` directory from anywhere in the filesystem. `cd etc` would only take you to the same directory if it is executed while working in the `/` directory.

	### Getting Help

	### Referencing Manual Pages with man

## Finding Stuff
	
	### Searching with locate

	### Finding Binaries with whereis

	### Finding Binaries in the PATH Variable with which
	
	### Performing More Powerful Searches with find

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
