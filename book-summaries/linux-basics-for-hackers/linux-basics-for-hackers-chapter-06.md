**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 6: PROCESS MANAGEMENT

---

## Viewing Processes

* **ps** shows active processes.

  * Bare `ps` lists processes for current user and terminal.
  * `ps aux` lists all processes for all users, displaying **USER**, **PID**, **%CPU**, **%MEM**, **COMMAND**, etc.

### Filtering by Process Name

* Pipe to `grep` to isolate specific processes:

  ```bash
  ps aux | grep msfconsole
  ```

### Finding the Greediest Processes with top

* **top** displays processes sorted by resource usage, refreshing dynamically.
* Press **H** or **?** for help and **Q** to quit.

## Managing Processes

### Changing Process Priority with nice

* **nice** suggests a process priority to the kernel: range **–20** (highest) to **+19** (lowest).

  * Start a process with adjusted niceness:

    ```bash
    nice -n -10 /path/to/command   # higher priority  
    nice -n 10 /path/to/command    # lower priority
    ```
* **renice** reassigns an absolute niceness to a running process by PID:

  ```bash
  renice 19 6996   # lower priority for PID 6996
  ```
* In **top**, press **R**, then enter the PID and new nice value.

### Killing Processes

* Use **kill** with signals (default SIGTERM):

  ```bash
  kill PID           # SIGTERM (15)  
  kill -9 PID        # SIGKILL (9) – forceful termination  
  kill -1 PID        # SIGHUP (1) – restart  
  ```
* **killall** by name:

  ```bash
  killall -9 zombieprocess
  ```
* In **top**, press **K**, then enter PID.

### Running Processes in the Background

* Append **&** to run without occupying the shell:

  ```bash
  leafpad newscript &
  ```

### Moving Processes to the Foreground

* Bring background job to foreground with **fg** and its PID:

  ```bash
  fg 1234
  ```

## Scheduling Processes

* **at** schedules one-time jobs:

  ```bash
  at 7:20pm June 25    # enter commands at at> prompt, then Ctrl-D
  ```
* Common time formats: `at noon`, `at tomorrow + 2 hours`, `at HH:MM YYYY-MM-DD`, etc.
* Use **cron** (covered in Chapter 16) for recurring tasks.

---

## Summary

Process management is essential for both system administrators and hackers. You can now view (`ps`, `top`), filter, prioritize (`nice`, `renice`), terminate (`kill`, `killall`), background/foreground (`&`, `fg`), and schedule (`at`) processes—skills critical for optimizing and controlling Linux environments.

## Exercises

1. Run `ps aux` and note the first and last processes in the list.
2. Launch `top` and identify the two processes consuming the most resources.
3. Use `kill` to terminate the process using the most CPU or memory.
4. Apply `renice` to lower a running process’s priority to **+19**.
5. Create a script file `myscanning`, then schedule it with `at` to run next Wednesday at 1 AM.

**Summary author: Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
