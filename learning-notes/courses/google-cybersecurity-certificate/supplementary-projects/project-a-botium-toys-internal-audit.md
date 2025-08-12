# Annex A: Botium Toys Internal Security Audit

**Date:** 2025-08-11  
**Auditor:** Jeremy Ray Jewell  
**Scope:** Entire security program at Botium Toys — including assets, internal network, systems, policies, and procedures.

---

## 1. Scope and Goals

**Scope:**  
Covers all assets, systems, and processes managed by the Botium Toys IT Department, including:

- On-premises equipment for in-office business needs
- Employee equipment (desktops, laptops, smartphones, headsets, etc.)
- Storefront inventory (retail and warehouse)
- IT-managed systems: accounting, telecommunications, databases, security, e-commerce, inventory
- Internet access and internal networking
- Data retention/storage systems
- Legacy system maintenance

**Goals:**  
1. Assess existing assets.  
2. Complete the controls and compliance checklist.  
3. Identify missing controls and compliance gaps.  
4. Recommend actions to improve Botium Toys’ security posture.

---

## 2. Risk Assessment Summary

**Risk Score:** 8/10 (High)  
**Potential Impact:** Medium for asset loss; High for compliance-related fines.  

**Key Risks Identified:**
- All employees have access to sensitive data, including PII and cardholder data.
- No encryption of credit card data in storage or transmission.
- No enforcement of least privilege or separation of duties.
- No IDS implemented.
- No disaster recovery plan or backups.
- Password policy is minimal; no centralized password management.
- Legacy systems have no regular maintenance schedule.
- Compliance gaps with PCI DSS and GDPR requirements.

---

## 3. Controls Assessment

| Control | In Place? | Notes |
|---------|-----------|-------|
| Least Privilege | **No** | All employees have broad data access. |
| Disaster Recovery Plans | **No** | No documented plan or backups exist. |
| Password Policies | **Partial** | Minimal requirements; not aligned with best practices. |
| Separation of Duties | **No** | No role-based segregation of access. |
| Firewall | **Yes** | Rules configured appropriately. |
| Intrusion Detection System (IDS) | **No** | Not implemented. |
| Backups | **No** | No backup procedures in place. |
| Antivirus Software | **Yes** | Installed and monitored. |
| Manual Monitoring (Legacy Systems) | **Partial** | Maintained but without a schedule. |
| Encryption | **No** | Sensitive data unencrypted. |
| Password Management System | **No** | No central enforcement of password policy. |
| Physical Locks (Office, Storefront, Warehouse) | **Yes** | Secure locks in place. |
| CCTV Surveillance | **Yes** | Functional and up to date. |
| Fire Detection/Prevention | **Yes** | Fire alarms and sprinklers operational. |

---

## 4. Compliance Assessment

### PCI DSS

| Best Practice | In Place? | Notes |
|---------------|-----------|-------|
| Only authorized users access credit card info | **No** | Access not restricted by role. |
| Secure environment for storing/processing card data | **No** | Stored unencrypted locally. |
| Data encryption procedures | **No** | No encryption implemented. |
| Secure password management policies | **Partial** | Weak policy, no enforcement tools. |

### GDPR

| Best Practice | In Place? | Notes |
|---------------|-----------|-------|
| E.U. customer data kept private/secure | **Partial** | Policies exist but no encryption or role restrictions. |
| Breach notification within 72 hours | **Yes** | Plan in place. |
| Data classification/inventory | **No** | Assets not classified or inventoried. |
| Privacy policies enforced | **Yes** | Documented and enforced among IT staff. |

### SOC 1 / SOC 2

| Best Practice | In Place? | Notes |
|---------------|-----------|-------|
| User access policies established | **No** | No formal role-based access control. |
| Sensitive data remains confidential | **Partial** | Policies exist but no technical enforcement. |
| Data integrity maintained | **Yes** | Integrity controls exist. |
| Data available to authorized personnel | **Yes** | Availability ensured. |

---

## 5. Recommendations

1. **Implement role-based access control (RBAC)** to enforce least privilege and separation of duties.
2. **Deploy an IDS** to monitor for suspicious activity.
3. **Encrypt sensitive data** in storage and transmission, especially cardholder and PII/SPII.
4. **Develop and test a disaster recovery plan** including offsite backups.
5. **Upgrade password policy** to meet modern standards (length, complexity, expiration).
6. **Adopt a centralized password management system** to enforce policies and reduce helpdesk tickets.
7. **Classify and inventory all assets** in line with NIST CSF "Identify" function.
8. **Schedule regular maintenance for legacy systems** to reduce vulnerabilities.
9. **Achieve PCI DSS and GDPR compliance** to reduce risk of fines and legal action.

---

**End of Annex A**
