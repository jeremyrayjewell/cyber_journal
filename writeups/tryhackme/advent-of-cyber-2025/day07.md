# Advent of Cyber 2025 – Day 7, 2025-12-08
**Room:** Network Enumeration – Where Are the Bunnies Hiding?  
**Category:** Network Scanning / Service Enumeration  
**Skills Practiced:** Nmap scanning, TCP/UDP enumeration, banner grabbing, interacting with FTP and custom TCP services, DNS TXT lookups, identifying hidden services, and assembling multi-part keys for privileged access.

---

## Summary
This challenge focused on regaining access to a compromised QA server (tbfc-devqa01) by enumerating exposed services. Using Nmap scans, manual banner grabbing, FTP access, and DNS queries, I uncovered three hidden key fragments that together should unlock the server’s admin console. The final step was blocked by a TryHackMe UI bug: the web interface’s "Enter" button does not respond, preventing access to the console and preventing retrieval of the final flag.

This writeup documents all steps completed successfully and ends where the platform bug halted progress.

---

## Walkthrough Notes

### 1. Discovering Initial Open Ports
I started with a simple top-1000 TCP scan:

```
nmap 10.66.136.62
```

Results:

```
22/tcp   open  ssh
80/tcp   open  http
```

Port 80 showed a defaced TBFC QA web page with an "EAST-mas" takeover message.

---

### 2. Full TCP Port Scan With Banner Grabbing

```
nmap -p- --script=banner 10.66.136.62
```

Discovered additional services:

- **21212/tcp – vsFTPd 3.0.5**
- **25251/tcp – TBFC maintd v0.2**

This gave me two hidden footholds to investigate.

---

## Key Discovery

### **Key 1 – FTP (Port 21212)**
Anonymous FTP login succeeded:

```
ftp 10.66.136.62 21212
```

Listing showed:

```
tbfc_qa_key1
```

Retrieving it:

```
get tbfc_qa_key1 -
```

Output:

```
KEY1:3aster_
```

---

### **Key 2 – TBFC maintd (Port 25251)**
I used Netcat to interact with the custom service:

```
nc -v 10.66.136.62 25251
```

Typed:

```
GET KEY
```

Response:

```
KEY2:15_th3_
```

---

### **Key 3 – DNS TXT Record (UDP Scan + dig)**

I performed a UDP scan:

```
nmap -sU 10.66.136.62
```

UDP port 53 was open.

Queried for TXT records:

```
dig @10.66.136.62 TXT key3.tbfc.local +short
```

Response:

```
"KEY3:c4k3}"
```

---

## Combined Key
Concatenating the three discovered parts:

```
3aster_15_th3_c4k3}
```

The full combined admin key should be:

```
3aster_15_th3_c4k3}
```

(This matches the advertised KEYNAME:KEY pattern.)

---

## 3. Attempt to Access the Secret Admin Console (Blocked by Bug)

The instructions say to:

1. Visit the QA website at `http://10.66.136.62`
2. Enter all three key parts into the admin panel
3. Unlock the secret console
4. Run `ss -tunlp` to enumerate host-local services
5. Connect to MySQL on port 3306
6. Retrieve the final flag from the `flags` table

### **But:**  
The **“Enter” button on the admin panel is currently non-functional**.

- It does not submit the keys.
- It does not unlock the console.
- The final steps cannot be accessed on today’s deployment.

This issue has been reported by multiple users and appears to be a temporary TryHackMe UI bug.

Because access to the secret console is required, the challenge cannot currently be completed past this point.

---

## Key Takeaways
- Full-range TCP and UDP scans often reveal nonstandard services.
- Banner grabbing is invaluable for identifying misconfigured or hidden services.
- Even "anonymous-only" FTP can leak sensitive information.
- DNS TXT records can be used for covert data storage.
- Enumeration is often a multi-protocol process: TCP, UDP, FTP, custom TCP applications, DNS, and HTTP in one challenge.
- Some challenges depend on UI elements functioning correctly—today’s task ends where a TryHackMe bug prevents progression.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
