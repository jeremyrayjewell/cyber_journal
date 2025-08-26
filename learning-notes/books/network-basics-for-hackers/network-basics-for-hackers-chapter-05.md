SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 5: WI-FI NETWORKS (802.11)

---

- This chapter introduces Wi-Fi fundamentals, tooling, packet anatomy, practical Wireshark filters, and a sequence of real-world attacks (WPA2 handshake/PMKID, WPS, Evil Twin, DoS), then closes with hands-on exercises. :contentReference[oaicite:0]{index=0}

## Wi-Fi Basics

- **What Wi-Fi is**: IEEE 802.11 WLAN standards maintained by the IEEE for communication over specific frequency bands. :contentReference[oaicite:1]{index=1}  
- **Channels & bands**: Channels 1–14 (U.S. uses 1–11); modern systems operate on 2.4 GHz and 5 GHz. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}  
- **Range & power**: Typical AP reach ≈ 300 ft at the .5 W U.S. limit; high-gain antennas can extend reach to miles. :contentReference[oaicite:4]{index=4}  
- **Modes**: APs use *master*; clients use *managed*; hackers generally switch adapters to *monitor* mode. :contentReference[oaicite:5]{index=5}  
- **Security evolution**: WEP→WPA→WPA2 (AES-CCMP); WPA3 is rolling out to address WPA2 issues. :contentReference[oaicite:6]{index=6}

## Wi-Fi Security Protocols

- **WEP**: Broken due to RC4 weaknesses; passwords recoverable in minutes using statistical attacks; rarely deployed today. :contentReference[oaicite:7]{index=7}  
- **WPA**: Stopgap that lengthened IVs, added TKIP (per-client keys) and a message integrity check—harder but still crackable. :contentReference[oaicite:8]{index=8}  
- **WPA2 (802.11i)**: Uses AES-based CCMP; required more capable hardware and remains widespread. :contentReference[oaicite:9]{index=9}  
- **Handshake flow**: PMK→PTK derivation during the 4-way EAPOL handshake underpins password-hash capture and offline cracking. :contentReference[oaicite:10]{index=10}

## Wi-Fi Adapters for Hacking

- **Chipset/adapter choice matters**: Select adapters that support monitor mode & injection; Alfa AWUS036NH (Ralink/Mediatek) is highlighted; consult Aircrack-ng’s compatibility list when choosing hardware. :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}

## Aircrack-ng commands

- **View wireless state**: `ifconfig` / `iwconfig` show interfaces, mode, channel, frequency, ESSID; `iwlist` can scan for APs from the CLI. :contentReference[oaicite:13]{index=13}  
- **Enable monitor mode**: `airmon-ng start wlan0` (stops conflicting processes with `airmon-ng check kill`) creates `wlan0mon`. :contentReference[oaicite:14]{index=14}  
- **Capture frames & targets**: `airodump-ng wlan0mon` lists APs/clients; focus capture with `airodump-ng --bssid <BSSID> -c <chan> --write <file> wlan0mon`. :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}

## Anatomy of Wi-Fi Frames

- **Management**: association request/response, probe request/response, beacon, authentication/deauthentication, disassociation. :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18}  
- **Control**: RTS/CTS, ACK, PS-Poll, CF-End, etc.—coordinate medium access. :contentReference[oaicite:19]{index=19}  
- **Data**: data, QoS data/null variants carry user traffic. Tools like Kismet/airodump derive visibility from these frames. :contentReference[oaicite:20]{index=20}

## Wireshark Filters for Wi-Fi Frames

- **Where to build filters**: Use *Expressions…* to search by field names/values. :contentReference[oaicite:21]{index=21}  
- **Useful display filters**: e.g., `wlan.fc.subtype == 8` (beacon), `wlan.fc.subtype == 4` (probe request), `wlan.fc.type == 0` (management), `wlan.fc.type == 1` (control), `wlan.fc.type == 2` (data). :contentReference[oaicite:22]{index=22}

## Attacking Wi-Fi APs

- **Hidden SSIDs**: De-obfuscate by capturing association frames; once a client connects, the ESSID appears in cleartext. :contentReference[oaicite:23]{index=23}  
- **Defeating MAC filtering**: Sniff a client’s MAC and spoof it; once whitelisted, you can associate. :contentReference[oaicite:24]{index=24}  
- **WPA2-PSK handshake attack**:  
  - Put adapter in monitor mode → `airmon-ng start wlan0`.  
  - Target and capture on a single AP/channel with `airodump-ng`.  
  - Force a reauth to speed up capture: `aireplay-ng --deauth 100 -a <BSSID> wlan0mon`.  
  - Crack captured handshake with `hashcat -m 16800 <cap> <wordlist>`. :contentReference[oaicite:25]{index=25} :contentReference[oaicite:26]{index=26} :contentReference[oaicite:27]{index=27}  
- **WPS (PIN) attack**: Exploit 8-digit PIN design (split verification drastically lowers keyspace to ~11k possibilities). Discover WPS-enabled APs with `wash -i wlan0mon`, then attack with tools such as *reaver*/*bully*. :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29}  
- **Evil Twin (MitM)**: Stand up a rogue AP and deauth clients from the real AP so they join yours; inspect plaintext client traffic in Wireshark (select the tunnel interface shown during setup). :contentReference[oaicite:30]{index=30} :contentReference[oaicite:31]{index=31}  
- **DoS via deauth**: Continuously send deauthentication frames with `aireplay-ng --deauth …` (scriptable to repeat). :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33}  
- **PMKID attack (no client needed)**:  
  - Idea: Grab a single RSN EAPOL frame containing PMKID; convert to hash and crack offline. :contentReference[oaicite:34]{index=34} :contentReference[oaicite:35]{index=35}  
  - Tools: Build `hcxdumptool`/`hcxtools`; enable monitor mode; run `hcxdumptool -I wlan0mon -o <outfile> --enable_status=1` (optionally filter to a target BSSID). Convert with `hcxcaptool -z hashoutput.txt <outfile>` and crack with `hashcat -m 16800 hashoutput.txt <wordlist>`. :contentReference[oaicite:36]{index=36} :contentReference[oaicite:37]{index=37} :contentReference[oaicite:38]{index=38}

## Wi-Fi Exercises

- The chapter concludes with practice exercises to reinforce scanning, capture, and cracking workflows described above. (See p. 97 for the exercise list.) :contentReference[oaicite:39]{index=39}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
