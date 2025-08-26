SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 9: SERVER MESSAGE BLOCK (SMB)

---

- This chapter defines SMB, outlines major vulnerabilities, walks through building a basic Samba server on Linux, and ends with a short exercise. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## What is SMB

- **SMB** is a Layer-7, client-server, request/response protocol for **file, printer, port, and named-pipe sharing** across a LAN. Clients connect via TCP/IP or NetBIOS and issue commands to access shares, read/write files, and use printers; **SMB over TCP/IP uses port 445**. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}
- Originally developed by **IBM** and later adopted/adapted by **Microsoft** for Windows. :contentReference[oaicite:4]{index=4}
- **CIFS** (“Common Internet File System”) is a Microsoft dialect/implementation of SMB; now considered **obsolete** and largely replaced by **SMB 2.0** (Vista era) and **SMB 3.0** (Windows 8/Server 2012). :contentReference[oaicite:5]{index=5}

## SMB Vulnerabilities

- SMB (Windows) and **Samba** (Linux/Unix) have a long history of **critical RCE issues**. Notable Windows examples include **MS08-067** and **MS17-010 (EternalBlue)**, where specially crafted packets enabled **remote code execution with SYSTEM privileges**. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}
- Metasploit searches surface many SMB exploits (including **MS08-067** and **EternalBlue**) that were weaponized in outbreaks such as **WannaCry** and **Petya**. :contentReference[oaicite:8]{index=8}

## Building a SAMBA Server in Linux

- **Purpose**: Samba emulates a Windows SMB server on Linux/*nix so those systems can **share resources with Windows**. :contentReference[oaicite:9]{index=9}  
- **Install** (Kali/Debian family):  
  `apt-get install samba` :contentReference[oaicite:10]{index=10}  
- **Start service**:  
  `service smbd start` (the daemon is **smbd**). :contentReference[oaicite:11]{index=11}  
- **Configure** `/etc/samba/smb.conf` (open with your editor): define a share name, comment, **path**, and access properties such as `read only = no`, `browsable = yes`. :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}  
- **Create the shared directory** and permissions, then **restart** Samba:  
  `mkdir /home/OTW/HackersArise_share` → `chmod 777 /home/OTW/HackersArise_share` → `service smbd restart`. :contentReference[oaicite:15]{index=15}  
- **Access from Windows** (example): `\\192.168.1.101\HackersArise_share`. :contentReference[oaicite:16]{index=16}

## Exercises

- **Build a SAMBA server for your domain.** :contentReference[oaicite:17]{index=17}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
