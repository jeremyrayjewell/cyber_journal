**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 15: MANAGING THE LINUX KERNEL AND LOADABLE KERNEL MODULES (LKMs)

---

## What is a Kernel Module?

* The **kernel** is the core of the OS, managing hardware, memory, and processes.
* **Loadable Kernel Modules (LKMs)** let you insert or remove functionality (e.g., drivers) at runtime without rebuilding the entire kernel.
* **Risks:** Malicious LKMs (rootkits) can grant full control and hide from system tools.

## Checking the Kernel Version

* `uname -a` shows distro, kernel version, build info, and architecture.

  ```bash
  uname -a
  ```
* Alternatively, inspect `/proc/version`:

  ```bash
  cat /proc/version
  ```

## Kernel Tuning with `sysctl`

* **`sysctl`** reads and writes kernel parameters at runtime.
* View all settings:

  ```bash
  sysctl -a | less
  ```
* **Example:** Enable IP forwarding for MITM attacks:

  ```bash
  sysctl -w net.ipv4.ip_forward=1
  ```
* Persistent changes go in `/etc/sysctl.conf`; add or uncomment lines like:

  ```text
  net.ipv4.ip_forward=1
  net.ipv4.icmp_echo_ignore_all=1  # ignore pings
  ```

  Then reload:

  ```bash
  sysctl -p
  ```

## Managing Kernel Modules

### Listing Modules

* `lsmod` lists loaded modules, sizes, and dependencies.

  ```bash
  lsmod
  ```

### Finding More Info with `modinfo`

* Show details about a module (path, version, dependencies, params):

  ```bash
  modinfo <module_name>
  ```

### Adding and Removing with `modprobe`

* **Load** a module (auto-handles dependencies):

  ```bash
  modprobe <module_name>
  ```
* **Remove** a module:

  ```bash
  modprobe -r <module_name>
  ```
* After loading, check `dmesg` for related kernel messages:

  ```bash
  dmesg | grep <module_name>
  ```

### Inserting/Removing a Test Module

* **Insert** (example):

  ```bash
  modprobe HackersAriseNewVideo
  ```
* **Remove** it:

  ```bash
  modprobe -r HackersAriseNewVideo
  ```
* **Verify** load/unload with `lsmod` or `dmesg`.

---

## Summary

* The Linux kernel is a protected core; LKMs enable flexible extension but pose security risks.
* `uname`, `/proc/version`, and `sysctl` allow inspection and tuning of kernel behavior.
* `lsmod`, `modinfo`, and `modprobe` are essential for safe module management.
* Vigilance against malicious LKMs (rootkits) is critical for system integrity.

## Exercises

1. Check your kernel version with `uname -a` and `/proc/version`.
2. List all loaded modules with `lsmod`.
3. Enable IP forwarding at runtime using `sysctl`, then disable it.
4. Edit `/etc/sysctl.conf` to permanently enable IP forwarding; apply changes.
5. Pick a module, use `modinfo` to examine it, then safely load and unload it with `modprobe`.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
