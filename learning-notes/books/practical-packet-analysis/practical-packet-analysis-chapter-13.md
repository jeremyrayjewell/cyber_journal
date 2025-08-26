SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 13: WIRELESS PACKET ANALYSIS

---

## Overview

- Wired rules don’t directly apply in the air. You must reason about **RF**, **channels**, and **802.11 frame types** (management, control, data) to make sense of Wi-Fi behavior.
- In Wireshark, wireless captures hinge on **monitor mode**, **channel selection**, and **radiotap metadata** (RSSI, data rate, channel width, MCS). Most problems reduce to **association/auth**, **interference/airtime**, **roaming**, or **security (EAPOL/WPA[2|3])**.

---

## RF & Channel Fundamentals (what shapes what you see)

- **Bands & channels**
  - 2.4 GHz: only three non-overlapping 20 MHz channels in most regions (**1/6/11**); lots of interference (Bluetooth, microwaves).
  - 5 GHz: many non-overlapping channels; some are **DFS** (radar sharing) and may **vacate** on detection.
  - 6 GHz (Wi-Fi 6E): clean spectrum, more 80/160 MHz options; management frames use **multicast mandatory rates**.
- **Widths & modulation**
  - 20/40/80/160 MHz; wider = faster PHY, but consumes more spectrum and is more interference-sensitive.
  - **MCS index** captures modulation + coding + spatial streams; higher MCS needs better SNR.
- **Airtime** is the currency. A few slow clients can dominate airtime and crush aggregate throughput even if RSSI looks okay.

---

## Capturing Wi-Fi Correctly

- **Monitor mode** is required to see other stations’ traffic and management/control frames.
  - Linux: best support; set channel/width explicitly (e.g., `iw`/`airmon-ng`).
  - macOS: limited but workable on supported chipsets.
  - Windows: requires special adapters/drivers; many stock drivers cannot do monitor mode.
- **One channel at a time per adapter.** Roaming across channels or multi-AP sites often need multiple adapters (or repeated captures per channel).
- **Lock the channel & width** to the BSS you care about; hopping adapters miss transient events (auths, EAPOL handshakes).
- **Prefer pcapng + radiotap** so you retain: RSSI (dBm), channel, data rate, MCS, NSS, channel width, and antenna index.
- **Ambient noise** matters: record noise floor if your adapter exposes it; SNR = signal − noise.

---

## Radiotap/Metadata Columns to Add (make the RF visible)

- `radiotap.dbm_antsignal` (RSSI, dBm)
- `radiotap.channel.freq` and `radiotap.channel.type` (or `wlan_radio.channel`)
- `wlan_radio.data_rate` or `radiotap.mcs` fields (MCS/NSS/gi)
- `wlan.fc.retry` (retries), `wlan.ta` (transmitter), `wlan.ra` (receiver)
- `wlan.bssid`, `wlan.sa`, `wlan.da`
- `wlan.qos.tid` (priority), if QoS troubleshooting
- For security work: `eapol`, `wlan.fc.protected`, `wlan.rsna.ie.akms`, `wlan.tag.ssid`

---

## 802.11 Addressing & Flags (decode who’s who)

- **Infrastructure BSS** uses **To-DS/From-DS** flags to interpret four address fields:
  - To-DS=0, From-DS=0: STA↔STA (ad-hoc or mgmt/control).
  - To-DS=1, From-DS=0: STA→AP; DA=BSSID, SA=STA.
  - To-DS=0, From-DS=1: AP→STA; SA=BSSID, DA=STA.
  - To-DS=1, From-DS=1: WDS/mesh; Address 4 used.
- **BSSID** identifies the AP interface for an SSID (per band/channel). Multiple SSIDs can share one radio via multiple BSSIDs.

---

## Frame Types You’ll Read Daily

- **Management (type=0)**
  - **Beacon**: SSID, supported rates, channel, security IEs (RSN/WPA), HT/VHT/HE capabilities, TIM.
  - **Probe Req/Resp**: active discovery.
  - **Auth / Assoc / Reassoc**: join process; failures reveal wrong passphrase, policy blocks, or mismatched capabilities.
  - **Deauth / Disassoc**: session teardown; spikes can indicate attacks, sticky-client steering, or PMF absence.
  - **Action**: 802.11k/v/r, Block Ack setup (ADDBA), channel switch announcements, etc.
- **Control (type=1)**
  - **RTS/CTS**, **ACK**, **Block Ack**; high RTS/CTS and retries → contention/interference.
- **Data (type=2)**
  - **QoS Data**, A-MPDU/A-MSDU aggregation; look for `wlan.fc.retry==1` and Block-Ack exchanges to judge link quality.

---

## Association, Authentication & Roaming (the join dance)

- **Open auth** → **Association** → (if secured) **EAPOL 4-way handshake** (WPA/WPA2/WPA3).
- **WPA2-PSK**: you can decrypt (for your own lab) by supplying SSID + PSK in Wireshark; capture must include 4-way handshake.
- **WPA2-Enterprise (802.1X/EAP)**: requires key material from the authenticator/supplicant; typically not decryptable without logs/keys.
- **WPA3**: uses **SAE** (Dragonfly) for PSK-like flows; **OWE** for open encryption (no auth).
- **PMF (802.11w)**: protects deauth/disassoc; if absent, look for spoofed management frames.
- **Roaming**: client issues **Reassociation** to new AP, often with 802.11r fast BSS transition. Long gaps or repeated attempts = sticky client, weak coverage, or key caching problems.

---

## Security & EAPOL Essentials

- **EAPOL handshake (4 messages)**
  - M1: ANonce from AP → STA
  - M2: SNonce + RSN IE from STA → AP
  - M3: GTK + MIC from AP → STA
  - M4: ACK from STA → AP
- **Failures**
  - Missing M3/M4 → retries; wrong key/PSK; MIC failures.
  - Frequent deauths after M4 → key install issues or policy kicks (e.g., MFP requirement).
- **Filters**
  - `eapol`
  - `wlan.fc.protected == 1` (encrypted data frames)
  - `wlan_mgt.tag.number == 48` (RSN IE) or `wlan.rsn.version`
  - `wlan.sa == <STA MAC>` and `wlan.bssid == <AP MAC>` to focus a client/AP pair

---

## Interference, Contention & Airtime (why “Wi-Fi is slow”)

- **Retries & low data rates** signal poor SNR or interference; watch `wlan.fc.retry==1` and dropping `data_rate`.
- **Co-channel interference (CCI)** vs **adjacent-channel interference (ACI)**:
  - 2.4 GHz: use only 1/6/11; overlapping channels yield ACI and brutal retries.
  - 5/6 GHz: prefer wider channels only where SNR and client mix justify it.
- **RTS/CTS spikes**: hidden-node mitigation active; expect lower throughput.
- **Legacy protection** (802.11g protection, CTS-to-Self) eats airtime when legacy clients are present.
- **DFS events**: look for Channel Switch Announcements (CSA action frames) and AP move; clients may drop/reassoc.

---

## Practical Workflows

- **Basic site survey (passive)**
  - Filter `wlan.fc.type == 0 and wlan.fc.subtype == 8` (beacons).
  - Build columns: SSID, BSSID, channel, security (RSN), signal (dBm).
  - Identify overlapping BSS on same channel; check mandatory rates and HT/VHT/HE capabilities.
- **“Can’t connect / wrong password”**
  - Follow `Auth → Assoc → EAPOL`. No EAPOL after Assoc → captive portal/VLAN issues or policy block.
  - Repeated EAPOL M1/M2 without M3 → PSK mismatch or RSN parameter mismatch.
- **Roaming sticky client**
  - Track a STA’s RSSI vs time; look for reassoc only when RSSI is already very low and retries spiking; vendor steering may deauth to force roam.
- **Throughput poor**
  - High `wlan.fc.retry`, many RTS/CTS, low data rates for far clients.
  - Correct channel plan, reduce cell size, trim legacy rates, ensure minimum mandatory rates are sensible.
- **Deauth storm / attack suspicion**
  - Bursts of `Deauthentication` frames from spoofed BSSID; if `PMF` absent, clients drop; with `PMF`, deauths should be protected or ignored.

---

## Display Filters You’ll Reuse

- Management types:
  - `wlan.fc.type == 0` (all mgmt)
  - `wlan.fc.type_subtype == 0x08` (beacon)
  - `wlan.fc.type_subtype == 0x04` (probe request), `0x05` (probe response)
  - `wlan.fc.type_subtype == 0x0b` (auth), `0x00` (assoc req), `0x01` (assoc resp), `0x02/0x03` (reassoc)
  - `wlan.fc.type_subtype == 0x0c` (deauth), `0x0a` (disassoc)
- Control/data health:
  - `wlan.fc.retry == 1`
  - `wlan.qos` (QoS data)
  - `wlan.fc.moredata == 1` (buffered to PS stations)
- Targeting a conversation:
  - `wlan.sa == aa:bb:cc:dd:ee:ff` or `wlan.addr == aa:bb:cc:dd:ee:ff`
  - `wlan.bssid == aa:bb:cc:dd:ee:ff` (per-cell focus)
- Security:
  - `eapol`
  - `wlan.fc.protected == 1`
  - `wlan.rsn.akms.type` (AKM suites, if parsed)

---

## Mini-Labs

- **A) Beacon census**
  - Capture on channel 1 (then 6, then 11). List SSIDs, BSSIDs, security, and RSSI. Identify overlapping cells and mismatched mandatory rates.
- **B) EAPOL handshake**
  - In a lab WPA2-PSK WLAN, capture a client join. Verify M1→M4; intentionally use a wrong PSK to see MIC failure/retries. Decrypt in Wireshark with SSID+PSK.
- **C) Retry/airtime stress**
  - Introduce a noise source (or distance the client). Track `wlan.fc.retry` rate, data rate downshift, and Block-Ack gaps.
- **D) Roam test**
  - Walk between APs while streaming; observe reassociation frames and any 802.11r FT action frames; correlate short-drop with buffer/DTIM behavior.

---

## Common Pitfalls → Remedies

- **Capturing while channel-hopping and missing the event**
  - Remedy: lock monitor to the target channel/width; use multiple adapters for multi-channel studies.
- **Reading RSSI without context**
  - Remedy: consider SNR and retries; high RSSI with high retries implies interference or congestion, not weak signal.
- **Assuming SSID == security**
  - Remedy: read RSN IEs; hidden SSIDs and multi-BSSID deployments can differ in security per BSSID.
- **Ignoring mandatory/basic rates**
  - Remedy: beacons reveal them; too-low basics keep slow clients and waste airtime.
- **Deauth floods fooling you when PMF is enabled**
  - Remedy: check `wlan.fc.protected` on mgmt frames; with PMF, spoofed deauths should not affect clients.

---

## What You Should Be Able to Do After Chapter 13

- Capture correctly in **monitor mode**, on the **right channel/width**, with **radiotap** metadata preserved.
- Read **management/control/data** frames, the **join/roam** sequences, and **EAPOL** handshakes.
- Diagnose **slow/unstable Wi-Fi** using retries, rates, RTS/CTS, and beacon parameters (mandatory rates, channel plan, DFS moves).
- Validate or decrypt (your own lab) **WPA2-PSK** sessions and recognize WPA3/PMF implications.
- Build filters/columns that surface **RSSI/MCS/airtime** signals quickly and tell a concise RF story.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
