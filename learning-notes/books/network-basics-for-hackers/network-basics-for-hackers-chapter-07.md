SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 7: ADDRESS RESOLUTION PROTOCOL (ARP)

---

- ARP maps **IP addresses** to **MAC addresses** on Ethernet LANs so switches/routers can deliver frames to the correct physical host; understanding it enables discovery and Man-in-the-Middle (MiTM) abuse. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## How ARP Works

- ARP uses simple **request/response** messages spanning OSI **Layers 2–3**. A sender that knows the target’s IP but not its MAC first consults its **ARP table** (IP⇔MAC cache). If missing, it **broadcasts** “Who has 192.168.1.101?”, and the owner **unicasts** “I have it; my MAC is 11:22:33:44:55:66,” allowing delivery to that MAC. :contentReference[oaicite:2]{index=2}

## ARP Command

- Windows: `arp -a` shows the ARP table (IP, **Physical/MAC**, and **type**: static vs. dynamic). :contentReference[oaicite:3]{index=3}  
- Linux: `arp -a` lists entries; `arp -v` presents a cleaner table and includes a **flags mask** indicating the IP class. Use `sudo` on Kali. :contentReference[oaicite:4]{index=4}

## ARP Packets in Wireshark

- Filter with `arp` to see ARP traffic; selecting a packet and expanding **Address Resolution Protocol** reveals **Sender/Target IPs** and **MACs** for inspection. :contentReference[oaicite:5]{index=5}

## How Hackers Use ARP

- Because ARP has **no authentication**, attackers can enumerate hosts on a LAN or pivot after an initial foothold. Tools send **gratuitous ARP** and record replies. :contentReference[oaicite:6]{index=6}  
- Example reconnaissance workflow with **netdiscover**: view help (`sudo netdiscover -h`) and scan a CIDR range (e.g., `netdiscover -r 192.168.100.0/24`) to list IP, MAC, and NIC vendor for each system. :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}  
- Post-exploitation: **Meterpreter** can broadcast gratuitous ARP to find additional internal targets to pivot to after compromising one host. :contentReference[oaicite:9]{index=9}

## ARP Vulnerabilities

- **ARP spoofing/poisoning** enables MiTM: attackers announce themselves as the destination for a victim’s IP, intercepting (and possibly altering) traffic. Tools include **Ettercap**, **arpspoof**, and **driftnet**. :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}

## Exercises

- Use the **arp** command to view your ARP cache.  
- Use **netdiscover** to enumerate systems on your LAN.  
- Create a **Wireshark** display filter to show only ARP packets. :contentReference[oaicite:12]{index=12}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
