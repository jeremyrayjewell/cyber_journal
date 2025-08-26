SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 14: SCADA/ICS NETWORKS

---

- Focus: how SCADA/ICS environments differ from traditional IT (notably, many non-standardized industrial protocols), major vendors you’ll encounter, the most common control-system protocols with a close look at **Modbus**/**Modbus TCP**, and core security weaknesses and attack surfaces in these systems. :contentReference[oaicite:0]{index=0}

## SCADA Manufacturers

- The chapter highlights leading industrial vendors you’ll see in the field—**Siemens**, **Honeywell**, **Toshiba**, **Rockwell Automation/Allen-Bradley**, **Mitsubishi**, **GE**, **Schneider Electric**, among others. Different product lines often speak different (sometimes proprietary) protocols, which complicates uniform defense and has historically benefited from “security through obscurity.” :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

## SCADA/ICS Communication Protocols

- Common protocols you’ll encounter include **Modbus**, **DNP3**, **ICCP**, **CIP**/**EtherNet/IP**, **CompoNet**, **ControlNet**, **DeviceNet**, **OPC**, **PROFIBUS**, and **Foundation Fieldbus H1**. A tester needs at least a working grasp of how these speak to PLCs/RTUs. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

- **Modbus (overview)**: Originally **Modbus RTU** (serial, 1979; Modicon/Schneider), public-domain, lightweight, OSI **Layer 7**, request/response, **master/slave** model; historically on **RS-232/RS-485** multi-drop with up to ~32 devices, each with a unique ID. Payloads are small (≤ **253 bytes**). :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}

- **Function codes**: Operations are expressed via Modbus **function codes** (e.g., reads, writes; diagnostics are **Function 8** with sub-functions). Notably, **Function 8 / sub-function 04 “Force Listen Only Mode”** can induce a **DoS** on some devices. :contentReference[oaicite:8]{index=8}

- **Modbus TCP**: Encapsulates Modbus for IP networks; same request/response and size limits, adds an **MBAP header**; runs on **TCP/502**. Link-layer checksums replace the RTU checksum. :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

## SCADA Security and Vulnerabilities

- **Why this matters**: Compromising a single plant (power, water, petroleum, manufacturing) can cost billions and threaten lives; everyone in security should be conversant with SCADA/ICS risks. :contentReference[oaicite:11]{index=11}

- **Modbus weaknesses** (representative of many legacy ICS protocols):  
  - **No authentication**—anyone crafting a valid address/function/data can issue commands. :contentReference[oaicite:12]{index=12}  
  - **No encryption**—cleartext traffic leaks configuration and operations to eavesdroppers. :contentReference[oaicite:13]{index=13}  
  - **Checksum handled at lower layers in TCP/IP**, enabling **spoofing** at the application layer. :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15}  
  - **No broadcast suppression**—attackers can DoS with broadcast floods. :contentReference[oaicite:16]{index=16}

- **Real-world targets & discovery**: PLCs (e.g., **Schneider TM221**) control a wide range of industrial processes and are often reachable over the Internet; the text demonstrates finding exposed units with **Shodan** (searching “TM221”) and notes many are vulnerable. :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
