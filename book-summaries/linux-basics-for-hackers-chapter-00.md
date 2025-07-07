SUMMARY OF 
**LINUX BASICS FOR HACKERS** 
(FIRST EDITION) BY OCCUPYTHEWEB

---

# CHAPTER 0: INTRODUCTION

---

## Introduction

- The 21st-centrury world is shaped by hacking

- Most professional hacking toold are Linux-based

- The book is for newcomers, and covers essentials with real-world examples

- It uses Kali as its OS of choice (I used Arch while reading the book and will note distinctions where applicable)

## What's in This Book?

- This section lays out the roadmap for the book, showing how each chapter builds your Linux and hacking skill set.

## What is Ethical Hacking?

- Ethical/white-hat hacking: the authorized practice of probing and exploiting systems to uncover vulnerabilities and improve security.

### Penetration Testing

- Penetration testing: a legally authorized, commissioned attack on an organization's network and systems, conducted after an intitial vulnerability scan, to validate which identified weaknesses are real and help the organization decide where to invest in remediation.

### Military and Espionage

- Military and intelligence agencies now depend on hackers to conduct cyber espionage and warfare. Breaching adversaries' networks to steal strategic information and disable critical infrastructure, hacking has become a pivotal element of modern national defense.

## Why Hackers Use Linux

- A higher level of control.

### Linux is Open Source

- Source code is open and available to all to adapt to new uses.

### Linux is Transparent

- Its openness means you and others are constantly observing code, making it harder for unwanted things to be hidden inside.

### Linux Offers Granular Control

- "Granular" here just means a non-monolithic, "one-size-fits-all" structure. Linux allows us control of all levels.

### Most Hacking Tools Are Written for Linux

- Even those which have been ported elsewhere often lack the full functionality which they have in Linux.

### The Future Belongs to Linux/Unix

- It dominates: servers, routers, switches, virtualization, and mobile devices.

## Downloading Kali Linux

- From https://www.kali.org/

- Breifly discusses Kali's history, versions differences for different architectures. Book assumes amd64.

- Lacks a discussion of download verification using hash and GPG signature, a very worthwhile topic when downloading Linux.

## Virtual Machines

- VMware, Oracle, and Microsoft options are mentioned. Author prefers Oracle's VirtualBox. 
	
### Installing VirtualBox

- https://www.virtualbox.org/ 

### Setting Up Your Virtual Machine

- Open installer, click `New` to open the Create Virtual Machine dialog

- Name your machine, select Linux from the `Type` menu, select Debian from the third drop-down. Click `Next`.

- Author recommends 25 or less of available RAM.

- On Hard Disk screen, choose `Create Virtual Hard Disk` and click `Create`. Author recommends `Dynamically Allocated`.

### Installing Kali on the VM

- Click `Start` in VirtualBox Manager to power on the Kali VM.

- Select the *iso* and click `Start`.

## Setting Up Kali

- Any error likely caused by virtualization not being enabled within your system BIOS.

- Choose your install method from boot menu, language if applicable, hostname, password, timezone.

- Partitioning: Choose `Guided - use entire disk`. Be conscious of erasure if not installing on a virtual disk. Choose `All files in one partition` and `Finish partitioning and write changes to disk`.

- Accept the GRUB boot loader installation.

- Log in to Kali using the name *root* and the password you set earlier.

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
