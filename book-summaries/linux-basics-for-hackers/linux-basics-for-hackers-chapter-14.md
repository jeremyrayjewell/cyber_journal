**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 14: UNDERSTANDING AND INSPECTING WIRELESS NETWORKS

---

## Wi‑Fi Networks

### Key Terms and Concepts

* **AP (Access Point):** Wireless device providing network connectivity.
* **SSID/ESSID:** Network name (ESSID can span multiple APs).
* **BSSID:** AP’s MAC address.
* **Channels & Frequencies:** 2.4 GHz (channels 1–11 US) and 5 GHz bands.
* **Signal Strength & Quality:** Affects range (≈100 m stock; up to 20 mi with high‑gain).
* **Security Modes:** WEP (insecure), WPA/WPA2‑PSK (preshared key), WPA2‑Enterprise.
* **Interface Modes:**

  * *Managed*: Client joins AP.
  * *Master*: Interface acts as AP.
  * *Monitor*: Sniffs all wireless frames.

### Inspecting Wireless Interfaces

* **`ifconfig` / `ip a`:** Lists active interfaces; look for `wlan0`, `wlan1`, etc.
* **`iwconfig`:** Shows wireless interface details (mode, ESSID, frequency, Tx power).

### Scanning for APs

* **`iwlist wlan0 scan`:** Reports all in‑range APs with BSSID, channel, signal, encryption, ESSID.
* **`nmcli dev wifi`:** High‑level view: SSID, mode, channel, rate, signal, security.

### Connecting to Networks

* **`nmcli dev wifi connect <SSID> password <KEY>`**
* Verify with `iwconfig` (ESSID, AP MAC, link quality).

## Wi‑Fi Recon & Cracking

### aircrack‑ng Suite

1. **Enable Monitor Mode:**

   ```bash
   airmon-ng start wlan0
   ```
2. **Capture Beacons + Client Data:**

   ```bash
   airodump-ng wlan0mon
   ```
3. **Deauthenticate Clients:**

   ```bash
   aireplay-ng --deauth 100 -a <AP_BSSID> -c <CLIENT_MAC> wlan0mon
   ```
4. **Crack WPA handshake:**

   ```bash
   aircrack-ng -w wordlist.txt -b <AP_BSSID> capture.cap
   ```

## Bluetooth Devices

### Fundamentals

* Operates at 2.4 GHz with frequency‑hopping spread spectrum (1,600 hops/sec).
* Range: ≈10 m standard, up to 100 m or more with custom antenna.
* Pairing shares a link key; discoverable mode broadcasts name, class, supported services.

### BlueZ Tools

1. **`hciconfig`** – Show and enable local Bluetooth adapters.

   ```bash
   hciconfig           # list adapters
   hciconfig hci0 up   # enable adapter
   ```
2. **`hcitool scan`** – Find discoverable devices (name + MAC).

   ```bash
   hcitool scan
   ```
3. **`hcitool inq`** – Inquire nearby devices (MAC, class, clock offset).

   ```bash
   hcitool inq
   ```
4. **`sdptool browse <MAC>`** – List services offered by a device (SDP).
5. **`l2ping -c 4 <MAC>`** – Ping to test reachability and range.

## Summary Points

* Linux treats wireless adapters similarly to wired, with dedicated tools (`iwconfig`, `iwlist`, `nmcli`).
* Monitor mode and aircrack‑ng enable Wi‑Fi reconnaissance and cracking.
* BlueZ provides `hciconfig`, `hcitool`, and `sdptool` for Bluetooth discovery and service inspection.
* Mastery of these tools is essential for wireless penetration testing and network reconnaissance.

## Exercises

1. List your wireless interfaces with `ifconfig` and `iwconfig`.
2. Scan for APs using `iwlist` and `nmcli`; compare outputs.
3. Connect to a known Wi‑Fi network via `nmcli`.
4. Enable monitor mode with `airmon-ng` and capture beacon frames with `airodump-ng`.
5. Discover nearby Bluetooth devices with `hcitool scan` and probe services via `sdptool browse`.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
