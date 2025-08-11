**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 10: FILESYSTEM AND STORAGE DEVICE MANAGEMENT

---

## The Device Directory `/dev`

Linux represents every hardware device as a file under `/dev`:

* Character devices (c): handle data one character at a time (e.g., keyboards).
* Block devices (b): handle data in blocks (e.g., HDDs, flash drives).

### How Linux Represents Storage Devices

* Legacy IDE: `hda`, `hdb`…
* Modern SATA/SCSI: `sda`, `sdb`, `sdc`…
* Multiple disks increment letter: first disk `sda`, second `sdb`, etc.

### Drive Partitions

* Partitions append numbers: `sda1`, `sda2`, …
* View partitions with:

  ```bash
  fdisk -l
  ```

  Lists each device’s size, partition table, and types (e.g., Linux, swap, NTFS).

### Character and Block Devices

* Prefix in `ls -l /dev`: `c` for character, `b` for block.
* Use `lsblk` to display block devices and mount points hierarchically:

  ```bash
  lsblk
  ```

## Mounting and Unmounting

Linux mounts storage into the unified filesystem tree—no drive letters.

### Mounting Storage Devices Yourself

* Ensure an empty mount point (e.g., `/mnt` or `/media`).

  ```bash
  mount /dev/sdb1 /mnt
  ```
* Mounted devices persist if listed in `/etc/fstab`.

### Unmounting with `umount`

* Always unmount before removal:

  ```bash
  umount /dev/sdb1
  ```
* Busy devices will not unmount until no process is using them.

## Monitoring Filesystems

### Getting Information on Mounted Disks

* Use `df` to view disk usage in human-readable form:

  ```bash
  df -h
  ```

  Shows filesystem, size, used, available, use%, and mount point.

### Checking for Errors

* `fsck` checks and optionally repairs filesystems (must unmount first):

  ```bash
  umount /dev/sdb1
  fsck -p /dev/sdb1
  ```

  `-p` auto-repairs; for ext2/3/4 uses `e2fsck`, for exFAT uses `exfatfsck`.

---

## Summary

Linux abstracts hardware as files under `/dev`, with block and character device types. You learned to identify disks and partitions (`fdisk`, `lsblk`), mount/unmount devices, monitor disk usage (`df`), and fix filesystem errors (`fsck`). These are essential for system administration and forensic analysis.

## Exercises

1. Mount and unmount a USB flash drive using `mount` and `umount`.
2. Use `df -h` to check free space on your primary hard drive.
3. Unmount and run `fsck` on your flash drive to check for errors.
4. Use `dd` to copy one flash drive’s raw contents to another.
5. Display block device info with `lsblk`.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
