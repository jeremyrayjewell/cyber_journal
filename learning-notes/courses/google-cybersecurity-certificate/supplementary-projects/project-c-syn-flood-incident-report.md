# Annex C – SYN Flood Incident Report

## Incident Overview

**Date/Time of Detection:** [Insert date/time]  
**Detected by:** Automated network monitoring system  
**Analyst:** Jeremy Ray Jewell  
**Organization:** [Insert company name] – Travel Agency

---

## Incident Summary

A web server hosting the company’s sales webpage experienced a **network service outage** due to a large volume of **TCP SYN requests** originating from an unfamiliar IP address.  
The packet capture analysis indicates a **SYN flood attack** — a type of **Denial of Service (DoS)** attack targeting the TCP handshake process.

---

## Attack Description

- **Type of Attack:** SYN Flood (DoS)
- **Method:** The attacker sends a high number of SYN packets to the target server without completing the handshake.
- **Impact on Network:**
  - Server resources allocated to half-open TCP connections are exhausted.
  - Legitimate requests are dropped or delayed.
  - Service becomes inaccessible to internal staff and customers.
- **Observed Symptoms:**
  - Website connection timeouts.
  - Elevated SYN request rate in Wireshark logs.
  - Unresponsive web server under heavy network load.

---

## Immediate Response Actions

1. **Took web server offline temporarily** to allow recovery of resources.
2. **Blocked attacking IP address** at the firewall level.
3. **Alerted management** regarding incident details and next steps.
4. **Documented network traffic patterns** from Wireshark for forensic reference.

---

## Business Impact

- **Customer Experience:** Customers unable to access promotions and vacation packages.
- **Internal Operations:** Staff unable to retrieve sales information for clients.
- **Revenue Risk:** Potential loss of sales during outage period.
- **Reputation Risk:** Negative impact on trust if outages persist.

---

## Recommended Mitigation & Prevention

- **Deploy SYN cookies** to manage TCP handshake resource allocation.
- **Implement rate limiting** for inbound SYN requests.
- **Enable intrusion prevention system (IPS)** to detect and block abnormal connection attempts.
- **Consider load balancing and redundancy** to reduce single-point vulnerability.
- **Monitor for IP spoofing** and distributed attack patterns (DDoS).

---

## Conclusion

The attack was a **SYN flood DoS** that temporarily took down the company’s public-facing web service.  
While initial IP blocking was effective short-term, the attacker could easily evade this via IP spoofing.  
A combination of **proactive monitoring**, **traffic shaping**, and **protocol-level defenses** is recommended to mitigate similar attacks in the future.
