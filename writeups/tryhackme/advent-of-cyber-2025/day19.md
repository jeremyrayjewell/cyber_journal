# Advent of Cyber 2025 – Day 19, 2025-12-19 
**Room:** ICS / Modbus – Claus for Concer  
**Category:** Industrial Control Systems (ICS) / OT Security  
**Skills Practiced:** SCADA analysis, PLC logic inspection, Modbus TCP interaction, ICS incident response, safe remediation sequencing

---

## Summary
Day 19 focused on investigating and remediating a compromise of an **industrial control system (ICS)**. Although system dashboards reported normal operation, the warehouse was physically delivering **chocolate eggs instead of Christmas gifts**, indicating a **logic-level manipulation attack** rather than a system outage. The investigation revealed direct abuse of the **Modbus TCP protocol (port 502)** to manipulate PLC registers and coils controlling package selection, verification, logging, and protection mechanisms. A deliberately planted trap ensured that careless remediation would trigger an emergency inventory dump. Using **pymodbus**, the system was safely interrogated, the attack state reconstructed, and Christmas deliveries restored without triggering the self-destruct logic.

---

## Walkthrough Notes

### 1. Initial Reconnaissance

A targeted Nmap scan was conducted from the AttackBox:
```
nmap -sV -p 22,80,502 MACHINE_IP
```
Key findings:
- **Port 80** – HTTP service hosting a CCTV feed
- **Port 502** – Modbus TCP service (PLC communication)
- **Port 22** – SSH (not used)
The exposed Modbus service immediately indicated a classic ICS misconfiguration: **unauthenticated control-plane access.**

---

### 2. Physical Process Verification (CCTV)

Accessing the CCTV feed via the web interface confirmed:
- Conveyor belts and robotic arms operating normally
- Chocolate eggs being loaded instead of gifts
- System status marked as Compromised
This confirmed a **logic manipulation attack**, not hardware failure.

---

### 3. Modbus Connection and Register Reconnaissance

A direct Modbus TCP connection was established using pymodbus:
```
from pymodbus.client import ModbusTcpClient
client = ModbusTcpClient('MACHINE_IP', port=502)
client.connect()
```
Holding Registers Identified
- HR0 – Package type selector
  - 0 = Christmas gifts
  - 1 = Chocolate eggs
- HR1 – Delivery zone
- HR4 – System signature
Findings:
- `HR0 = 1` → eggs forced
- `HR1 = 5` → normal delivery zone
- `HR4 = 666` → Eggsploit signature present

---

### 4. Coil State Analysis (Trap Identification)

Critical coils were read next:
- C10 – Inventory verification → False
- C11 – Protection mechanism → True
- C13 – Audit logging → False
- C15 – Self-destruct armed → False
The technician’s note warning—“Never change HR0 while C11=True”—was confirmed to be accurate. Changing HR0 under protection would arm C15 and initiate a timed emergency dump.

---

### 5. Full System State Reconstruction

A consolidated reconnaissance script was created to document:
- All relevant holding registers
- All critical coils
- Threat indicators
- Required remediation steps
This established a clear attack profile:
- Direct Modbus abuse
- Disabled safety checks and logging
- Logic-level trap to punish careless responders
- Attacker signature left intentionally

---

### 6. Safe Remediation Strategy

To avoid triggering the trap, remediation steps were executed in strict order:
- Disable protection mechanism (C11 = False)
- Reset package type (HR0 = 0)
- Enable inventory verification (C10 = True)
- Enable audit logging (C13 = True)
- Confirm self-destruct never armed (C15 = False)
A Python remediation script enforced this order programmatically and verified state after each action.

---

### 7. Restoration Verification and Flag Retrieval

Upon successful restoration:
- The Christmas Restored coil (C14) was auto-set
- CCTV feed showed correct gift handling
- Emergency dump remained inactive
The final flag was extracted directly from PLC holding registers.

---

## Key Takeaways

- ICS attacks often manipulate logic, not availability
- Modbus TCP provides no authentication or authorization
- Physical processes can appear “healthy” while being maliciously controlled
- Safety and protection mechanisms can be weaponised as traps
- Order of operations matters in ICS remediation
- Incident responders must understand control logic before writing values

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
