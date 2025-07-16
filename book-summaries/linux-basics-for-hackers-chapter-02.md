SUMMARY OF 
**LINUX BASICS FOR HACKERS** 
(FIRST EDITION) BY OCCUPYTHEWEB

---

# CHAPTER 2: TEXT MANIPULATION

---

## Viewing Files

While `cat` is described as probably "the most basic text display command", there are more optimal methods to limit the amount of content output to the CLI.

### Finding the Head 

The `head` utility takes a filename (or reads from STDIN) as its argument and outputs the first 10 lines by default (or the first *N* lines if you specify `-N`)

- `head /etc/snort/snort.conf`

- `head -20 /etc/snort/snort.conf`

### Finding the Tail

The `tail` utility takes a filename (or STDIN) and outputs the last 10 lines by default (or the last *N* lines with `-N`).

- `tail /etc/snort/snort.conf`

- `tail -20 /etc/snort/snort.conf`

### Numbering the Lines

The `nl` utility numbers each line of a text file (or standard input), prefixing lines with their line numbers to make referencing and navigation easier.

- `nl /etc/snort/snort.conf`

## Filtering Text with grep

The `grep` utility scans one or more input files (or STDIN) for lines matching a given pattern (regular expression or fixed string) and outputs only those matching lines.

`| grep output` takes whatever the previous command writes to STDOUT and "pipes" it with `|` into `grep`, which then scans those lines and **only** prints the ones that contain the literal string `output`. In other words, it filters the stream down to lines matching `output`.

### Hacker Challenge: Using grep, nl, tail, and head

The `nl command` is used to number lines in a file. The `-n+` option on the `tail` and `head` utilities is used to display a specific number of lines from the end or beginning of a file, respectively. The `+` sign indicates that the count should start from the specified line number, rather than counting from the beginning or end of the file.

Piping (`|`) the results of line numbers 507 through the end of the file (`tail -n+507`) to `head -n 6` returns the first 6 lines of that input, therefore resulting in the printing of lines 507-512. The opposite can be achieved by reversing the `tail` and `head` commands' positions.

- `cat /etc/snort/snort.conf | grep output`

- `nl /etc/snort/snort.conf | grep output`

- 'tail -n+507 /etc/snort/snort.conf | head -n 6'

- 'head -n+507 /etc/snort/snort.conf | tail -n 6`


## Using sed to Find and Replace

The `sed` or *stream editor* tet processing utility is used to perform basic text transformations on an input stream. The author compares it to the Windows "find and replace" function.

If we wanted to replace every instance in our snort config file of *mysql* with *MySQL*, we could enter the command `sed s/mysql/MySQL/g /etc/snort/snort.conf > snort2.conf` to create a *snort2.conf* file with those changes running `cat` on the two files and piping results to `grep` can help us confirm the results.

- `cat /etc/snort/snort.conf | grep mysql` to see what we want to change

- `sed s/mysql/MySQL/g /etc/snort/snort.conf > snort2.conf` to make the change everywhere

- `sed s/mysql/MySQL/ snort.conf > snort2.conf` to replace the first occurence of the term **per line** (the book fails to mention this)

- `sed s/mysql/MySQL/2 snort.conf > snort2.conf` to replace only the second occurence **per line**`

- `cat /etc/anort/snort2.conf | grep MySQL` to confirm changes


Notice that here we are using `sed` with forward slashes (`/`) between *operands*. The use of a hyphen (`-`) id conventionally to denote flags or options. Any options should go before the operands. Remember that options are related to *how* a program runs, and operands relate to the *thing* it should act on.

## Viewing Files with more and less
	
### Controlling the Display with more

The `more` pager allows us to view the content of a file one screenful at a time in a uni-directional, forward-only way.

- `more /etc/snort/snort.conf`

### Displaying and Filtering with less

The `less` pager allows us to view the contents of a file one screenful at a time in a bi-directional, backward-and-froward way.

-`less /etc/snort/snort.conf`

The **"less is more"** expression refers to the better overall efficiency of using `less` instead of `more`, both in terms of the greater navigational fluidity with the former and in terms of its taking up less memory and processing power. But `less` also allows for searches.

The bottom left of the `less` screen shows the path to the file. If we press `/`, `less` will let us search for a term in that field. This will take us to the first occurance of the search input, from where we can navigate to the next by pressing `n`.

## Summary

User preferences may vary, but text manipulation is an indispensable skill for Linux users.

## Exercises

- Navigate to Kali's default wordlists location, and use the `cat`, `more`, `less`, `nl`, `tail, and `head` command to explore the long files there. Specifically, the auhthor recommends `password.lst`.

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
