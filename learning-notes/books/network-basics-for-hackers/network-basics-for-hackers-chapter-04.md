SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 4: LINUX FIREWALLS

---

- This chapter introduces Linux host and network firewalls through **iptables**: what a firewall is, the iptables architecture (tables, chains, matches, targets), installing and inspecting iptables, setting default policy, creating practical rules (IP/port/domain examples), rule ordering, listing tables, and flushing/resetting rules. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## Iptables Basics

- **Firewall concept**: software/hardware control that blocks or allows traffic into/out of a system; hardware firewalls typically protect entire networks, software firewalls protect the local host. :contentReference[oaicite:2]{index=2}

- **What iptables is**: command-line firewall utility for Linux/*nix that checks packets against rules; if no rule matches, the default action (policy) applies. Developed by the Netfilter project and included in the kernel since 2001. :contentReference[oaicite:3]{index=3}

- **Tables** (functional groupings):  
  - `FILTER` (default), `NAT` (rewrite src/dst), `MANGLE` (packet alteration, e.g., TCP header fields), `RAW` (connection-tracking exemptions). :contentReference[oaicite:4]{index=4}

- **Chains** (ordered lists of rules in a table):  
  - `INPUT` (packets to local system), `OUTPUT` (packets leaving local system), `FORWARD` (packets routed *through* the system). :contentReference[oaicite:5]{index=5}

- **MATCH**: a packet meets a rule’s condition; **TARGETS**: action when matched—`ACCEPT`, `DROP`, `LOG`, `REJECT`, `RETURN`. :contentReference[oaicite:6]{index=6}

## Installing Iptables

- Generally preinstalled; if missing on Kali/*nix:  
  `kali > sudo apt install iptables`. :contentReference[oaicite:7]{index=7}

## Configuring the Default Policy

- Decide the default chain policy (what to do when no rule matches). View policies and rules:  
  `kali > sudo iptables -L`. On most systems the default is `ACCEPT`; highly locked-down hosts may set default `DROP` and then explicitly allow needed traffic (secure but maintenance-heavy). :contentReference[oaicite:8]{index=8}

## iptables help

- `kali > sudo iptables -h`  
  Key options include **uppercase** `-A` (append), `-D` (delete), `-L` (list); and **lowercase** `-s` (source), `-d` (destination), `-j` (jump/target). :contentReference[oaicite:9]{index=9}

## Create Some rules

- **Block a specific source IP** (e.g., 192.168.1.102):  
  Append to the `INPUT` chain, match by `-s`, drop with `-j DROP`. (Same pattern works for a whole subnet via CIDR, e.g., `192.168.1.0/24`.) :contentReference[oaicite:10]{index=10}

- **Block a destination port** (e.g., SSH):  
  Use protocol and dport match: `-p tcp --dport ssh` with target `DROP`. :contentReference[oaicite:11]{index=11}

- **Allow only one site (example)**:  
  Permit outbound TCP to a specific domain:  
  `kali > sudo iptables -A OUTPUT -p tcp -d amazon.com -j ACCEPT`  
  Note: DNS is resolved **once** at rule creation—IP changes can break the rule; prefer pinning to IP where possible. :contentReference[oaicite:12]{index=12}

- **Deny everything else (web)**:  
  Drop outbound HTTP/HTTPS:  
  `kali > sudo iptables -A OUTPUT -p tcp --dport 80 -j DROP`  
  `kali > sudo iptables -A OUTPUT -p tcp --dport 443 -j DROP`  
  **Order matters**: evaluation stops at first match; place your `ACCEPT` for the allowed site **before** the general `DROP`s. :contentReference[oaicite:13]{index=13}

- **List and reset**:  
  View rules: `-L`; flush all rules to start fresh:  
  `kali > sudo iptables -F`. After flushing, listing shows an empty rule set. :contentReference[oaicite:14]{index=14}

## Summary

- With a modest command set and careful rule ordering, **iptables** gives Linux practitioners a powerful, flexible firewall comparable to expensive commercial products. :contentReference[oaicite:15]{index=15}

## Exercises

- Build a firewall that allows access to **Hackers-Arise** only on ports **80** and **443**.  
- Add a rule that **blocks port 445**.  
- **Flush** the rules to reset your table. :contentReference[oaicite:16]{index=16}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
