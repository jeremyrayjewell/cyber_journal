**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 9: COMPRESSING AND ARCHIVING

---

## What is Compression?

* **Compression** reduces file size for storage and transfer.
* **Lossy** (e.g., JPG, MP3) sacrifices exact fidelity; **lossless** (e.g., TAR, ZIP) preserves data integrity—essential for scripts and binaries.

## Tarring Files Together

* **tar** (tape archive) bundles files into a single archive (tarball).

  * Create: `tar -cvf archive.tar file1 file2 file3`
  * List contents: `tar -tvf archive.tar`
  * Extract: `tar -xvf archive.tar`
* Note: Initial tar adds overhead; compression follows.

## Compressing Files

Linux offers three common lossless compressors, each with different speed/compression trade‑offs.

### Compressing with gzip

* Compress: `gzip archive.tar` → produces `archive.tar.gz`
* Decompress: `gunzip archive.tar.gz`
* Typical result: moderate speed, good compression.

### Compressing with bzip2

* Compress: `bzip2 archive.tar` → produces `archive.tar.bz2`
* Decompress: `bunzip2 archive.tar.bz2`
* Typical result: slower, highest compression ratio.

### Compressing with compress

* Compress: `compress archive.tar` → produces `archive.tar.Z`
* Decompress: `uncompress archive.tar.Z`
* Typical result: fastest, least compression.

## Creating Bit-by-Bit or Physical Copies of Storage Devices

* **dd** clones devices/files byte-for-byte, capturing deleted data—useful for forensics and full-disk backups.

  * Basic: `dd if=/dev/sdX of=/path/to/image bs=4096 conv=noerror`
  * `if=` is input file/device; `of=` is output file; `bs=` sets block size; `conv=noerror` continues on errors.
* **Warning**: dd is slow; use logical copy tools (cp, rsync) for everyday file copying.

## Summary

Tar archives bundle files; gzip, bzip2, and compress apply lossless compression with different performance/compression characteristics. The dd command performs raw device cloning, preserving all data for forensic analysis or full backups.

## Exercises

1. Create three scripts named `Linux4Hackers1`, `Linux4Hackers2`, and `Linux4Hackers3`.
2. Bundle them into `L4H.tar` using tar; compare size before/after.
3. Compress `L4H.tar` with gzip; note size change and experiment with overwrite flags.
4. Repeat step 3 using bzip2 and compress.
5. Use dd to make a bit-by-bit copy of a flash drive.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
