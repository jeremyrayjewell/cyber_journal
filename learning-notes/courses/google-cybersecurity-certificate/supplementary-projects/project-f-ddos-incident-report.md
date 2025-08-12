.# Annex F – Incident Report Analysis (NIST Cybersecurity Framework)

## 1. Identify

**Summary of Incident:**  
On [date], the organization experienced a Distributed Denial of Service (DDoS) attack targeting its internal network. The attack consisted of a high-volume flood of ICMP packets entering through an unconfigured firewall. This vulnerability allowed the attacker to overwhelm the network, making critical services inaccessible for approximately two hours.

**Cause:**  
An unconfigured firewall allowed unrestricted ICMP traffic from untrusted sources.

**Impact:**
- Complete outage of internal network access for two hours.
- Disruption of critical services, affecting all business operations.
- Potential reputational damage to the organization.

**Type of Attack:**  
ICMP flood DDoS attack (network layer).

**Systems Impacted:**
- Internal LAN and WAN infrastructure
- Core routing and switching equipment
- Application servers dependent on network connectivity

---

## 2. Protect

**Protection Plan:**
- Fully configure firewall rules to restrict ICMP traffic and apply rate-limiting.
- Enable IP source verification to prevent spoofed traffic from entering the network.
- Segment the network to isolate critical services from public-facing endpoints.
- Conduct quarterly firewall configuration reviews and penetration testing.
- Implement employee training to ensure awareness of network security policies.

---

## 3. Detect

**Detection Methods:**
- Deploy Intrusion Detection and Prevention Systems (IDS/IPS) to monitor ICMP packet patterns and flag anomalies.
- Implement continuous network traffic monitoring with baselines for normal activity.
- Configure SIEM (Security Information and Event Management) to alert on unusual ICMP or high packet rates.
- Use flow analysis tools (NetFlow/sFlow) to detect volumetric anomalies.
- Conduct regular audits of firewall and IDS logs to identify suspicious patterns early.

---

## 4. Respond

**Response Plan:**
- Immediately contain attack traffic using updated firewall rules and packet filtering.
- Temporarily disable non-critical network services to free up resources.
- Use incident playbooks for ICMP floods to guide response team actions.
- Document all events, timelines, and actions for post-incident analysis.
- Notify stakeholders and provide updates during the incident resolution process.

---

## 5. Recover

**Recovery Steps:**
- Restore all critical network services and verify operational status.
- Reconfigure and test firewall policies to ensure no similar vulnerability remains.
- Conduct a full post-incident review to identify root causes and lessons learned.
- Update disaster recovery and business continuity plans to include DDoS-specific mitigation strategies.
- Schedule follow-up penetration tests to validate fixes.
