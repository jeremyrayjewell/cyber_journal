# BANDIT 6 -> 7

## Obfuscated password (ROT13): 

zbeoAGQxFJ6wVyHp0lzBqZnYaBySINnw

## Objective

"The password for the next level is stored somewhere on the server and has all of the following properties:
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size"

## Purpose

In the last level we learned to narrow a search by size and executability. Now we need to search by size again, but also by ownership metadata. We must find a file that has a byte count of 33, but also user owner `bandit7` and group owner `bandit6`. This time the password is not located inside the user's home directory, so our search must include the whole server.

If we return to `man find` and search for `group` and `user`, we see the following lines within the `TESTS` section:
	
<premarkdown>

       -group gname
              File belongs to group gname (numeric group ID allowed).

</pre>
<premarkdown>

       -user uname
              File is owned by user uname (numeric user ID allowed).

</pre>

Putting those options together with the size option from last time, `-size` with the `c` unit suffix for bytes, we can find our file within the root, `/`. We may wish to add another snippet, though, as the basic command `find / -group bandit6 -user bandit7 -size 33c` to search throughout the server returns a large number of "Permission denied" messages.

Because we are starting in `/root`, our `find` command is coming across many entries that are not world-searchable. It calls system call `stat()` on all entries to find out if they are directories to be descended into or if the entry satisfies the user's tests. If the execute bit `x` is missing for your UID/GID on a given entry on which `stat()` is called, the kernel returns EACCES which `find` echoes as "Permission denied".

If we want to filter these lines out of our `find` results, we can affix our previous command with `2>/dev/null`, where `2` refers to standard error file-descriptor **stderr**/**FD 2**. At run-time, a Unix process owns a table of open file-descriptors (FDs) which map tiny integers to real I/O resources. The third entry, **FD 2**, is conventionally where diagnostics are sent. For `find` in particular, this is the case.

This would be hard to figure out with having previous skimmed a shell tutorial, so now is a good time to do that. In `man bash` we can search for `REDIRECTION` and find the following:

<premarkdown>
       Bash  handles  several filenames specially when they are used in redirections, as described in the following table.  If the
       operating system on which bash is running provides these special files, bash will use them; otherwise it will emulate  them
       internally with the behavior described below.

              /dev/fd/fd
                     If fd is a valid integer, file descriptor fd is duplicated.
              /dev/stdin
                     File descriptor 0 is duplicated.
              /dev/stdout
                     File descriptor 1 is duplicated.
              /dev/stderr
                     File descriptor 2 is duplicated.
              /dev/tcp/host/port
                     If host is a valid hostname or Internet address, and port is an integer port number or service name, bash at‐
                     tempts to open the corresponding TCP socket.
              /dev/udp/host/port
                     If host is a valid hostname or Internet address, and port is an integer port number or service name, bash at‐
                     tempts to open the corresponding UDP socket.
</pre>
Then...
<premarkdown>
       Bash  handles  several filenames specially when they are used in redirections, as described in the following table.  If the
       operating system on which bash is running provides these special files, bash will use them; otherwise it will emulate  them
       internally with the behavior described below.

              /dev/fd/fd
                     If fd is a valid integer, file descriptor fd is duplicated.
              /dev/stdin
                     File descriptor 0 is duplicated.
              /dev/stdout
                     File descriptor 1 is duplicated.
              /dev/stderr
                     File descriptor 2 is duplicated.
              /dev/tcp/host/port
                     If host is a valid hostname or Internet address, and port is an integer port number or service name, bash at‐
                     tempts to open the corresponding TCP socket.
              /dev/udp/host/port
                     If host is a valid hostname or Internet address, and port is an integer port number or service name, bash at‐
                     tempts to open the corresponding UDP socket.
</pre>

`/dev/null` is, it should be noted, the **all-purpose discard targer**. Combining all that information together, we come up with `2> /dev/null` to disgard all error messages produced by `find` being unable to access an entry.


## Solutions

- find / -group bandit6 -user bandit7 -size 33c

- find / -user bandit7 -group bandit6 -size 33c 2>/dev/null


