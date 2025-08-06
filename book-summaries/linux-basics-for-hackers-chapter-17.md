**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 15: MANAGING THE LINUX KERNEL AND LOADABLE KERNEL MODULES (LKMs)

---

## What Is a Kernel Module?

* The **kernel** is the core of the OS, managing hardware, processes, memory, and I/O.
* Linux’s **monolithic kernel** allows for **Loadable Kernel Modules (LKMs)**, which can be inserted or removed at runtime without rebuilding the entire kernel.
* LKMs enable drivers (e.g., for new USB or filesystem support) to be added dynamically—but also open a route for rootkits.

## Checking the Kernel Version

* `uname -a` shows the running kernel version, architecture, and build info:

  ```bash
  uname -a
  ```
* `/proc/version` yields similar details via `cat /proc/version`.

## Kernel Tuning with `sysctl`

* **`sysctl`** reads and sets kernel parameters at runtime.
* View all tunable parameters:

  ```bash
  sysctl -a | less
  ```
* Example: **IP forwarding** for MITM attacks

  ```bash
  sysctl -w net.ipv4.ip_forward=1
  ```
* To persist changes, edit `/etc/sysctl.conf` and uncomment or add lines such as

  ```text
  net.ipv4.ip_forward=1
  ```

## Managing Kernel Modules

### Listing Loaded Modules

* `lsmod` displays all currently loaded modules, their sizes, and dependencies:

  ```bash
  lsmod
  ```

### Inspecting Module Info

* `modinfo <module>` reveals metadata, dependencies, author, license, parameters, and compatible kernel versions:

  ```bash
  modinfo bluetooth
  ```

### Inserting and Removing Modules

* **`modprobe -a <module>`** loads a module and its dependencies safely.
* **`modprobe -r <module>`** removes a module (if not in use).
* Older tools: `insmod` and `rmmod` (manual and riskier, no dependency handling).

### Verifying Module Actions

* After loading, check kernel logs for module messages:

  ```bash
  dmesg | grep <module-name>
  ```

## Summary

* LKMs allow dynamic extension of the Linux kernel but pose security risks if malicious modules are loaded.
* Knowing how to view (`lsmod`), inspect (`modinfo`), tune parameters (`sysctl`), and safely add/remove modules (`modprobe`) is crucial for both system administration and stealthy hacking.

## Exercises

1. Check your current kernel version with `uname -a` and `cat /proc/version`.
2. List all loaded modules using `lsmod`.
3. Enable IP forwarding at runtime:

   ```bash
   sysctl -w net.ipv4.ip_forward=1
   ```
4. Make IP forwarding permanent by editing `/etc/sysctl.conf`, then disable it again.
5. Select a loaded module and display its details using `modinfo <module>`.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
