# BANDIT 12 -> 13

## Obfuscated password (ROT13): 

SB5qjSfp0ponVvU0u8W2rHxf2iqGQjNa

## OBJECTIVE

"The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)"

## PURPOSE

The primary challenge here is decompression and knowing how to do it with different formats with different requirements. As the objective states, we want to take advantage of the word-writable `/tmp` directory to do all the necessary operations on `data.txt`. We can make a subdirectory there with `mkdir` and then copy the file into our new directory with `cp`:

<pre markdown>
bandit12@bandit:~$ mkdir /tmp/foo
bandit12@bandit:~$ cp data.txt /tmp/foo
bandit12@bandit:~$ cd /tmp/foo
bandit12@bandit:/tmp/foo$ ls
 data.txt
</pre>

Alternatively, as the objective suggests, we can use `mktemp -d` to automatically create a uniquely named temporary files directory: 

<pre markdown>
bandit12@bandit:~$ mktemp -d
/tmp/tmp.jC2VKve0U8
bandit12@bandit:~$ cp data.txt /tmp/tmp.jC2VKve0U8
bandit12@bandit:~$ cd /tmp/tmp.jC2VKve0U8
bandit12@bandit:/tmp/tmp.jC2VKve0U8$ ls
data.txt
</pre>

The next thing we need to do is use the `xxd` utility to revert the hexdump to binary with the `-r` option plus an output file name.

<pre markdown>
bandit12@bandit:/tmp/tmp.jC2VKve0U8$ xxd -r data.txt foo
bandit12@bandit:/tmp/tmp.jC2VKve0U8$ file foo
dump: gzip compressed data, was "data2.bin", last modified: Mon Jul 28 19:03:32 2025, max compression, from Unix, original size modulo 2^32 578
</pre>

We now see by running `file` that the binary contiains gzip compressed data. We can decompress it, but gzip requires that we first add a recognized suffix like `.gz`. We can rename it to `foo.gz` with `mv`, then we can run `gzip -d foo.gz`.

Repeating the `file` command on the decompressed results shows us that it contains bzip2 compressed data. The `bzip2` `-d` option requires no specific suffix, so we can run `bzip2 -d foo` and receive the output `foo.out`.

`file foo.out` reveals gzip compression again, which we can reverse in the same way we did before after using `mv` to change our `out` extension to `gz`.

`file foo` now reveals our output as a POSIX tar archive. `tar -xf foo` (the *extract* and *file* flags) gives us `data5.bin`, which `file` reveals once again as a POSIX tar archive. `tar -xf data5.bin`.

The output of that is `data6.bin`, another bzip2 compression. Its output, `data6.bin.out`, is another POSIX tar archive. `tar -xf` on that produces `data8.bin`, a gzip compression. We must rename this one once again to satisfy gzip's suffix requirements. The output of that, `data8`, is ASCII text containing the password for the next level. 

## SOLUTIONS

Copy to a temporary directory, then:

	- `file` to identify data type

	- `mv` to change to `.gz` suffix for gzip decompression

	- `gzip -d`, `bzip2 -d`, and `tar -xf` depending on compression type

	- change default bzip2 `.out` suffix where necessary.

