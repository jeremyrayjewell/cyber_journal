## Annex — Cybersecurity Incident Report (Module 3 Activity: Analyze Network Layer Communication)

**Analyst:** Jeremy Ray Jewell  
**Date of Report:** 2025-08-11  
**Incident Title:** DNS Service Disruption — Port 53 Unreachable  
**Incident ID:** M3-TCPDUMP-2025-08-11  

---

### Part 1 — Summary of Problem from tcpdump Log
**Observed Problem:**  
Users attempting to access the client’s public website **www.yummyrecipesforme.com** received the error **"destination port unreachable"**. Packet capture via `tcpdump` revealed repeated **ICMP** error responses from the DNS server IP **203.0.113.2** indicating **UDP port 53 unreachable**.  

**Protocols Observed:**  
- **UDP** — used for the DNS queries sent from the client host (192.51.100.15) to the DNS server (203.0.113.2).  
- **ICMP** — used to deliver error messages back to the client host, specifically "udp port 53 unreachable."  

**Log Details:**  
- **Timestamp:** Initial request observed at `13:24:32.192571`.  
- **Source/Destination:** Client → DNS server via UDP port 53.  
- **Error Response:** DNS server → Client via ICMP indicating destination port unreachable.  
- **Pattern:** All DNS queries in the capture produced the same ICMP error response.  

**Interpretation:**  
DNS service on the target DNS server was either down, blocked, or misconfigured, preventing resolution of the website’s IP address.

---

### Part 2 — Analysis and Recommended Actions
**Incident Timeline:**  
- **First Report:** Users reported connection failures to the website earlier in the day; confirmed by analyst at **1:24 PM local time**.  
- **Symptoms:** Inability to resolve domain name to IP; browsers displayed connection errors after DNS lookup failure; tcpdump showed immediate ICMP unreachable errors after DNS queries.  

**Current Status:**  
DNS resolution for the domain is non-functional; ICMP error confirms no active listener on UDP port 53 at the DNS server.

**Findings from Investigation:**  
- The domain name lookup process was initiated but could not complete because DNS service was inaccessible on the configured server.  
- The TCP/IP model layer implicated: **Internet Layer (IP)** — packet routing and delivery; **Application Layer** — DNS functionality failure.  
- ICMP provided diagnostic feedback revealing the exact port/protocol failure.  

**Suspected Root Cause:**  
- DNS service on 203.0.113.2 is down or misconfigured.  
- Possible firewall or ACL changes blocking inbound UDP port 53 traffic.  
- Less likely: DNS software running but bound to a different port or IP.

**Next Steps:**  
1. Verify DNS server service status (`systemctl status named` or equivalent).  
2. Check firewall rules for dropped packets on UDP port 53.  
3. Confirm DNS server configuration (`named.conf` or equivalent).  
4. Test external connectivity to alternate DNS servers to restore functionality temporarily (e.g., Google DNS 8.8.8.8).  
5. Restart DNS service and re-test using `dig` or `nslookup`.

**Proposed Immediate Mitigation:**  
- Update client systems to use a secondary/backup DNS resolver until the primary is restored.  
- Notify network engineering team to investigate and restore DNS availability on 203.0.113.2.

---

**Conclusion:**  
The incident is the result of a DNS resolution failure due to UDP port 53 being unreachable on the primary DNS server. Without functional DNS, website access via domain name fails. The most probable cause is either a DNS service outage or firewall misconfiguration. Immediate action should focus on restoring DNS service and ensuring port 53 is open to valid queries.
