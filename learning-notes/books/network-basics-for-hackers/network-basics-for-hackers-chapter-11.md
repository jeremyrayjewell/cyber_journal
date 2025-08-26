SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 11: SIMPLE NETWORK MANAGEMENT PROTOCOL (SNMP)

---

- SNMP is widely deployed yet often poorly understood; if breached, an attacker can inventory and even reconfigure network gear—and, as shown in public disclosures, potentially unmask encrypted VPN traffic. SNMP primarily uses **UDP/161** (queries) and **UDP/162** (traps). :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## Background on SNMP

- **Role & model**: Application-layer protocol for managing networked devices. A **manager** polls/controls multiple **agents** on managed hosts. Agents expose management data via the **Management Information Base (MIB)**—a hierarchical database of objects (e.g., users, OS/version, open ports, installed software) invaluable for recon and planning exploitation. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}  
- **PDUs**: Seven types—**GetRequest, SetRequest, GetNextRequest, GetBulkRequest, Response, Trap, InformRequest**. :contentReference[oaicite:4]{index=4}

## SNMP Versions

- **SNMPv1**: weak security; **community strings** (“public” for read, “private” for write) in **cleartext** and shared across nodes by default. :contentReference[oaicite:5]{index=5}  
- **SNMPv2**: performance/security improvements but not broadly adopted due to backward-compatibility issues. :contentReference[oaicite:6]{index=6}  
- **SNMPv3**: adds **authentication, integrity, and encryption**; still not universal in the field. :contentReference[oaicite:7]{index=7}  
- Despite v1’s risks, it remains in use—even in large enterprises—so sniffed traffic can reveal credentials. :contentReference[oaicite:8]{index=8}

## Wireshark Analysis of SNMP

- A capture of **SNMPv1** on a LAN shows **Get-Request**, **Get-Response**, and **Get-Next-Request** PDUs; critically, the **community string** appears in cleartext in the packet details. :contentReference[oaicite:9]{index=9}

## Abusing SNMP for Information Gathering

- **snmpcheck** (Kali → Information Gathering → SNMP Analysis → *snmpcheck*) queries the MIB of a target (defaults: community `public`, version `1`):  
  `kali > snmpcheck -t <target IP>`  
  Output enumerates **hardware**, **OS & uptime**, **device info**, **storage**, **user accounts**, and **installed software**—all high-value recon. :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

## Cracking SNMP Community Strings

- **onesixtyone** (Kali → Information Gathering → SNMP Analysis → *onesixtyone*) performs dictionary attacks against SNMP to recover community strings:  
  `kali > onesixtyone [options] <host IP> <community string private or public>`  
  It ships with a small default dictionary; augment with org-specific variants (e.g., `<company>-public`). After discovery, reuse the string in **snmpcheck** to dump the MIB. :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17}

## NSA Exploits against SNMP

- Public reporting links **NSA “ExtraBacon”** to abusing SNMP to help **decloak VPN** traffic on certain Cisco ASA versions; although patched, the text cautions that similar capabilities may persist. :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
