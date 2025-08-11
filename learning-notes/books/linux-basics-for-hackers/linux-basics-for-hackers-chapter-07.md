**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 7: MANAGING USER ENVIRONMENT VARIABLES

---

## Viewing and Modifying Environment Variables

### Viewing All Environment Variables

* `env` shows only environment variables (uppercase).
* `set` lists environment, shell variables, and functions; pipe to `more` for paged view:

  ```bash
  set | more
  ```

### Filtering for Particular Variables

* Use `grep` to find a specific variable:

  ```bash
  set | grep HISTSIZE
  ```

### Changing Variable Values for a Session

* Assign new value directly:

  ```bash
  HISTSIZE=0
  ```

  (Change lasts only for current shell.)

### Making Variable Value Changes Permanent

* After setting, export to child processes and future sessions:

  ```bash
  export HISTSIZE
  ```
* To restore, reset value and `export` again.

## Changing Your Shell Prompt

* `PS1` controls prompt format using placeholders:

  * `\u` = user name
  * `\h` = hostname
  * `\w` = current working directory
* Example:

  ```bash
  PS1="World's Best Hacker: # "
  export PS1
  ```
* Windows-style:

  ```bash
  export PS1='C:\\w> '
  ```

## Changing Your PATH

* `PATH` lists colon-separated directories searched for commands.

  ```bash
  echo $PATH
  ```

### Adding to the PATH Variable

* Append a directory without removing existing entries:

  ```bash
  PATH=$PATH:/root/newhackingtool
  export PATH
  ```

### How Not to Add to the PATH Variable

* **Don’t** overwrite PATH or you lose access to system binaries:

  ```bash
  PATH=/root/newhackingtool   # Incorrect—removes other paths
  ```

## Creating a User-Defined Variable

* Define custom variable and view it:

  ```bash
  MYNEWVARIABLE="Your value here"
  echo $MYNEWVARIABLE
  ```
* Persist across sessions with `export`, remove with `unset`:

  ```bash
  export MYNEWVARIABLE
  unset MYNEWVARIABLE
  ```

---

## Summary

Environment variables shape your shell’s behavior and user experience. You can view (`env`, `set`), filter, change, and export them—plus create your own—to tailor your Linux environment for efficiency, convenience, and stealth.

## Exercises

1. View environment variables with `set | more`.
2. Use `echo` to display the `HOSTNAME` variable.
3. Modify the prompt to show backslashes instead of slashes in the Windows-style PS1 example.
4. Create `MYNEWVARIABLE` with your name, `echo` it, and `export` it.
5. View `PATH` with `echo $PATH`.
6. Add your home directory to `PATH`.
7. Change `PS1` to “world’s Greatest Hacker:”.

**Summary author: Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
