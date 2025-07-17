# BANDIT 5 -> 6

## Obfuscated password (ROT13): 

	UJnfaCugd9NIXr0qzx45akl20piHn6RT

## Objective

"The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
- human-readable
- 1033 bytes in size
- not executable"

## Purpose

Now in `/inhere` we see 20 subdirectories titles `maybehereXX` with suffixes `00`-`19`. Each one contains six files: 3 `-fileX` files where X = `1`-`3` and 3 `spaces fileX` files where X = `1`-`3`. Here is an abbreviated visual representation:

<pre markdown>
/home/bandit5/inhere
	        ├──/maybehere00
                │    ├── -file1
	        │    ├── -file2
	        │    ├── -file3
	        │    ├── spaces file1
	        │    ├── spaces file2	     
                │    └── spaces file3
	        ├──/maybehere01
                │    ├── -file1
	        │    ├── -file2
	        │    ├── -file3
	        │    ├── spaces file1
	        │    ├── spaces file2	     
                │    └── spaces file3
                ⋮
	        └──/maybehere19
                     ├── -file1
	             ├── -file2
	             ├── -file3
	             ├── spaces file1
	             ├── spaces file2	     
                     └── spaces file3
</pre>

We can see this structure by porforming a quick recursive dump with `ls -R`. That is a total of 120 possible password locations. Compared to bandit4, manual searching is much less of an option now. Insted of just being human-readable, this time we are told that it must also fit the following additional criteria: *exactly 133 bytes*, *non-executable*.

This time we will have to rely on the filesystem's metadata, and as the file structure contains files buried in different subdirectories we will necessarily need to search *recursively*. The `find` utility we used last time is recursive, but we will need more options. Running `find ./inhere -type f -exec file {} \; | grep 'text'` as before returns 118 items (which we can observe by piping to `wc -l`), a very poor reduction.

If we enter `man find` and either use `/` + `executable` to search or navigate to the `TESTS` section, we see the following regarding the option `-executable`:

<pre markdown>
       -executable
              Matches  files  which  are  executable and directories which are searchable (in a file name resolution sense) by the
              current user.  This takes into account access control lists and other permissions artefacts which the -perm test ig‐
              nores.  This test makes use of the access(2) system call, and so can be fooled by NFS servers which do  UID  mapping
              (or root-squashing), since many systems implement access(2) in the client's kernel and so cannot make use of the UID
              mapping information held on the server.  Because this test is based only on the result of the access(2) system call,
              there is no guarantee that a file for which this test succeeds can actually be executed.
</pre>

Putting the common negation symbol `!` in front of this flag filters for non-executable files. This is confirmed by `find man` in the `OPERATORS` section:

<pre markdown>
       ! expr True if expr is false.  This character will also usually need protection from interpretation by the shell.
</pre>

`find ./inhere -type f ! -executable` thus returns 60 results, and with grepping for text we get 59. More exploration is needed. Are next criterium is the file's size, decribed as 1033 bytes. Looking through `man `find` again, we find this in the `TESTS` section:

<pre markdown>
       -size n[cwbkMG]
              File uses less than, more than or exactly n units of space, rounding up.  The following suffixes can be used:

              `b'    for 512-byte blocks (this is the default if no suffix is used)

              `c'    for bytes

              `w'    for two-byte words

              `k'    for kibibytes (KiB, units of 1024 bytes)

              `M'    for mebibytes (MiB, units of 1024 * 1024 = 1048576 bytes)

              `G'    for gibibytes (GiB, units of 1024 * 1024 * 1024 = 1073741824 bytes)

</pre>

`find ./inhere -type f -size 1033c` actually returns exactly one result, meaning that if we begin our search there we find the solution faster. Herein lies another takeaway from this level: byte count is inherently more selective that the other two criteria, meaning that statistically beginning your filtering with the most selective traits will normally result in faster results. In fact, the file type flag is not even needed here.

## Solutions

- `find inhere -size 1033c`

- `find inhere -type f -size 1033c`

- `find inhere -type f -size 1033c ! -executable`

- `find inhere -type f -size 1033c -exec file {} \; | grep 'text'

- `find inhere -type f -size 1033c ! -executable  -exec file {} \; | grep 'text'` 
