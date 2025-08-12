# Annex E – Network Hardening Incident Report

## Incident Overview
On [DATE], a major data breach occurred at a social media organization, exposing customer personal information, including names and addresses. Post-incident investigation revealed multiple network security vulnerabilities that contributed to the breach. Without remediation, these weaknesses significantly increase the likelihood of further data breaches and compromise of sensitive information.

## Identified Vulnerabilities
1. Employees share passwords.
2. Database admin password set to default.
3. Firewalls lack inbound/outbound traffic filtering rules.
4. Multifactor authentication (MFA) not implemented.

## Network Hardening Recommendations

### 1. Enforce Strong, Unique Password Policies
- **Action**: Deploy centralized authentication (e.g., Active Directory, LDAP) with enforced password complexity, expiration, and reuse prevention.
- **Frequency**: Continuous enforcement with quarterly audits.
- **Justification**: Prevents unauthorized access due to weak or shared credentials; reduces insider and credential stuffing risks.

### 2. Replace Default Passwords and Implement MFA
- **Action**: Change all default credentials immediately; implement MFA for all privileged accounts and remote logins.
- **Frequency**: Immediate change, permanent enforcement.
- **Justification**: Default passwords are a top attack vector; MFA mitigates risks from compromised passwords.

### 3. Configure Firewall Rules to Restrict Traffic
- **Action**: Define and apply inbound/outbound firewall rules based on least privilege; allow only required ports and protocols; integrate intrusion prevention systems (IPS).
- **Frequency**: Monthly rule review and real-time monitoring.
- **Justification**: Reduces attack surface and prevents unauthorized traffic from entering or leaving the network.

## Expected Outcome
By implementing the above network hardening measures, the organization will:
- Significantly reduce exposure to brute-force and credential attacks.
- Prevent exploitation via default credentials.
- Block malicious traffic before it impacts internal systems.
- Establish layered security controls aligned with best practices.

## Follow-up Actions
- Schedule penetration testing post-implementation to validate hardening effectiveness.
- Provide security awareness training to employees to discourage unsafe credential practices.
- Integrate changes into continuous monitoring and incident response workflows.

---
**Prepared by:** [YOUR NAME]  
**Date:** [DATE]  
**Related Course Module:** Google Cybersecurity Certificate – Connect and Protect: Networks and Network Security
