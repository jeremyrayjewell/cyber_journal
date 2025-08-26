SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 6: BLUETOOTH NETWORKS

---

- Overview: what Bluetooth is, how it pairs and forms piconets, essential Linux tooling (BlueZ utilities), the protocol stack and security modes, reconnaissance/attack tooling, and a hands-on BlueBourne exploitation walkthrough, plus exercises. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## Bluetooth Basics

- Bluetooth: low-power, near-field wireless at **2.4–2.485 GHz** using **spread-spectrum frequency hopping (1,600 hops/s)**; originated at Ericsson (1994); named for King Harald Bluetooth. Minimum spec range **10 m**; many devices reach **~100 m** (more with special antennas). :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}  
- **Pairing** exchanges a pre-shared “link key”; discoverable devices advertise **name**, **class**, **services**, and **technical info**. Each device has a unique **48-bit identifier** (MAC-like). :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}  
- **Piconet**: one master with up to **7** active slaves; hopping minimizes mutual interference. :contentReference[oaicite:8]{index=8}

## Basic Linux Bluetooth Tools

- **BlueZ** stack (installed by default on Kali or available via repo). Utilities:  
  - `hciconfig` — bring up/query Bluetooth interfaces (e.g., **hci0**).  
  - `hcitool` — inquiry (device name/ID/class/clock).  
  - `hcidump` — sniff Bluetooth comms. :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

## Bluetooth Protocol Stack

- Applications use vertical slices of the stack; protocols include **LMP/L2CAP/SDP**, **RFCOMM**, **TCS Binary/AT-commands**, and adopted protocols (**PPP**, **UDP/TCP/IP**, **OBEX**, **WAP**, **vCard/vCal**, **IrMC**, **WAE**). **HCI** exposes commands/status to baseband/link manager (hence `hciconfig`, `hcidump`, `hcitool`). :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}

## Bluetooth Security

- Security features: **frequency hopping** plus **128-bit** auth/encryption from the pairing key. Modes:  
  **Mode 1** (no active security), **Mode 2** (service-level security via a manager), **Mode 3** (device-level security; auth+encryption always on). :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

## Bluetooth Hacking Tools in Kali

- Menu: **Applications → Kali Linux → Wireless Attacks → Bluetooth Tools**. Tools include **Bluelog** (site survey/logging), **Bluemaho** (GUI test suite), **Blueranger** (i2cap pings for distance), **Btscanner** (discoverable scan), **Redfang** (find hidden devices), **Spooftooph** (Bluetooth spoofing). :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}

## Some Bluetooth Attacks

- **Blueprinting** (footprinting), **Bluesnarfing** (steal SMS/calendar/images/phonebook/chats), **Bluebugging** (phone takeover; e.g., Bloover PoC), **Bluejacking** (contact “business card” messages), **Bluesmack** (DoS). :contentReference[oaicite:17]{index=17}  
- Despite improvements, the author argues Bluetooth remains widely vulnerable across device classes. :contentReference[oaicite:18]{index=18}

## The BlueBourne Attack

- Armis-disclosed exploits (affecting **Android**, **Windows**, and **iOS < 10**) target **SDP**; the victim device **need not be discoverable—only powered on**. :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20}  
- Lab workflow (unpatched device required):  
  1) Dependencies: `apt-get install bluetooth libbluetooth-dev`; `pip install pybluez pwntools`. :contentReference[oaicite:21]{index=21}  
  2) Clone PoC: `git clone https://github.com/ojasookert/CVE-2017-0785`; `chmod 755 CVE-2017-0785.py`. :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}  
  3) Recon MAC: `hcitool scan`. :contentReference[oaicite:24]{index=24}  
  4) Exploit: `python CVE-2017-0785.py TARGET=<MAC>`; example PoC dumps the **first 30 bytes** of memory (editable to retrieve more). :contentReference[oaicite:25]{index=25}  
- References and context: author links to **Hackers-Arise** Bluetooth page and Armis **BlueBorne** write-up. :contentReference[oaicite:26]{index=26}

## Exercises

- Install **BlueZ** (if needed); find your adapter MAC with **`hciconfig`**; scan nearby devices with **`hcitool scan`**. :contentReference[oaicite:27]{index=27}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
