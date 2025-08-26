SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 8: DOMAIN NAME SYSTEM (DNS)

---

- Focus: what domain names are, how DNS resolution works, core DNS components and records, packet-level behavior in Wireshark, common weaknesses and DNSSEC, plus a walk-through to build a local BIND server and exercises. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## Domain Names

- Domain names are registered via **ICANN** (often through registrars like VeriSign/GoDaddy). DNS is hierarchical: **TLDs** (e.g., *.com, .edu, .org*) → **second-level domains (SLD)** → **subdomains**; the leftmost label is most specific. An **FQDN** specifies the name from the DNS root. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}  
- Records you’ll see in zones: **SOA** (required; authority/timers), **NS** (delegation), **A/AAAA** (host→IP, with AAAA for IPv6), **CNAME** (alias), **PTR** (reverse), **MX** (mail). :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

## How DNS Works

- Historically, name→IP mappings lived in local **hosts** files, which still override DNS on a system. The book shows editing `/etc/hosts` and demonstrates that `localhost` and any entries (e.g., a bank domain) resolve from this file first. :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}  
- Modern DNS (Mockapetris, 1983) is **distributed** and **hierarchical**. A resolver queries its local DNS; if unknown, it follows referrals: **root** → **TLD** → **authoritative** server for the domain/subdomain, which returns the resource (IP) if present. :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

## DNS Components

- Four components: **DNS cache** (host/server caches; also servers doing recursive caching only), **resolvers** (clients that need lookups), **name servers** (hold zone data and answer queries), **name space** (the database of names↔addresses). :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}  
- **Zone files & records:** each zone has a zone file with **resource records** using the form `Owner TTL Class Type RDATA`; records must be updated, and **zone transfers** propagate changes. **SOA** is mandatory and includes primary NS, admin email, serial, and refresh timers. :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19}

## Packet Level Analysis of DNS

- In Wireshark, a client sends a **standard query** and receives a **standard query response**; normal queries use **UDP/53** (while **TCP/53** is used for zone transfers or when messages are too large). :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}

## DNS Security and Vulnerabilities

- DNS once had more fragility; information can be harvested via **DNS recon/scans**. On LANs, **DNS spoofing** (e.g., `dnsspoof`) can redirect users (e.g., to fake banking sites). Today the dominant successful attacks are **DoS** on resolvers/authoritatives; compromising **zone data** (e.g., malicious changes) is particularly harmful. :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23} :contentReference[oaicite:24]{index=24}  
- The chapter cites a **U.S.-CERT**-warned campaign in which attackers changed DNS settings/records (A/NS) and used infrastructure (certs/load balancers) to harvest credentials, including split behavior for inside vs. outside requests. :contentReference[oaicite:25]{index=25} :contentReference[oaicite:26]{index=26}

## DNSSec

- DNS is not inherently authenticated (UDP, connectionless). **DNSSEC** adds authenticity/integrity via **public-key signatures**: zones sign data; resolvers validate with the zone’s public key, preventing tampering/poisoning (e.g., illicit zone transfers corrupting data). :contentReference[oaicite:27]{index=27}

## Building a DNS Server (BIND)

- Install BIND9, or clone from ISC if needed. Edit **`/etc/bind/named.conf.options`** to listen on **53** for `localhost` and the LAN (e.g., `192.168.1.0/24`), allow queries from those ranges, set a **forwarder** (e.g., `75.75.75.75`), and enable **recursion**. Define zones in **`named.conf.local`**. :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29} :contentReference[oaicite:30]{index=30}  
- Create **forward** and **reverse** zone files from templates (`/etc/bind/db.local` → `forward.hackers-arise.local`; `/etc/bind/db.127` → `reverse.hackers-arise.local`) and edit records for domain, NS, mail, and host IPs (example server **192.168.1.27**). Restart the service (`service bind9 restart` or `systemctl restart bind9`). :contentReference[oaicite:31]{index=31} :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33}

## Exercises

- Open and review your **hosts** file.  
- Build a **BIND** DNS server for your own test domain.  
- Search the **CVE** database for recent DNS issues. :contentReference[oaicite:34]{index=34}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
