SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 15: RADIO FREQUENCY NETWORKS WITH SDR

---

- This chapter introduces radio fundamentals, RF attack patterns, SDR hardware and setup, and three hands-on projects: intercepting aircraft voice, decoding ADS-B flight data, and spoofing GPS. :contentReference[oaicite:0]{index=0}

## Basic Radio Terminology

- **Amplitude**: strength of a radio signal. **Frequency**: cycles per second (Hz). **Sample rate**: digital sampling rate (Hz). **Filter**: cleans received/transmitted signals to reduce noise/interference. **Digital Signal Processing (DSP)**: numerically analyzing/modifying/synthesizing sampled signals over time/space/frequency domains. :contentReference[oaicite:1]{index=1}

## Radio Attack Methods

- **Sniffing**: tune an SDR to the target frequency to study protocols, extract instructions, and eavesdrop when unencrypted. :contentReference[oaicite:2]{index=2}  
- **Replay**: many RF systems lack anti-replay; capture then retransmit (e.g., car/garage doors, home switches). :contentReference[oaicite:3]{index=3}  
- **Signal deception (spoofing)**: craft packets/keys/verifiers to send fake but valid signals to the target. :contentReference[oaicite:4]{index=4}  
- **Hijacking / DoS**: jam or downgrade (e.g., force 4G→3G/2G) to intercept; can involve femtocells/Stingray-type devices. :contentReference[oaicite:5]{index=5}  
- **Threat surface**: many RF applications (remotes, sensors, alarms, microphones, etc.) have little/no security; captures can be decrypted or replayed. :contentReference[oaicite:6]{index=6}

## SDR for Hackers Hardware Comparison

- **USRP**: open-source stack; multiple series (X: 10G Ethernet, N: 1G, B: USB 3.0 incl. B200mini; E: onboard ARM—no host PC). Developer-oriented, high performance. :contentReference[oaicite:7]{index=7}  
- **RTL-SDR**: <$40 receive-only DVB-T dongle (RTL2832U); broad software support (librtlsdr). Low-cost entry point; cannot transmit (limits replay). :contentReference[oaicite:8]{index=8}  
- **HackRF One**: ~$; open-source, 1 MHz–6 GHz; **half-duplex** TX/RX (good for many projects incl. replay). :contentReference[oaicite:9]{index=9}  
- **bladeRF**: **full-duplex**, strong for projects like OpenBTS; main drawback: upper freq ≈3.8 GHz. :contentReference[oaicite:10]{index=10}  
- **LimeSDR**: open-source, “apps-enabled”; supports UMTS/LTE/GSM, LoRa, Bluetooth, Zigbee, RFID, etc.; packaged for Snappy Ubuntu Core with app ecosystem. :contentReference[oaicite:11]{index=11}

## What is SDR?

- SDR moves radio functions (modulation/demodulation, tuning, filtering, etc.) into software running on general-purpose processors/DSPs; with a PC, you can capture, decode, replay, and hack a wide range of signals (AM/FM, TV, aircraft, LEO satellites, public safety, car unlocking, etc.). :contentReference[oaicite:12]{index=12}

## Setting Up our First SDR

- **Hardware**: start with an inexpensive RTL-SDR USB dongle kit (antenna + cabling). :contentReference[oaicite:13]{index=13}  
- **Software**: HDSDR (Windows; runs under Wine on Linux) or SDR#. :contentReference[oaicite:14]{index=14}  
- **Driver (Windows)**: use **Zadig** to install WinUSB for the RTL device (often “Bulk-In, Interface 0”); use “List All Devices” if empty, then “Replace Driver.” :contentReference[oaicite:15]{index=15}  
- **FM demo**: set sampling rate (≥48 kHz suffices for audio), choose FM mode, tune to a local station, align on the spectral peak; you should hear audio. :contentReference[oaicite:16]{index=16}:contentReference[oaicite:17]{index=17}

## Intercepting Aircraft Communication

- **Bands/Mode**: ITU allocates aircraft **HF** voice (3–30 MHz) and **VHF** voice **118–137 MHz**; use **AM** mode. VHF is line-of-sight but higher audio quality. :contentReference[oaicite:18]{index=18}  
- **HDSDR setup**: Mode = **AM**; Frequency Manager = **Air**. Sample ≥2× voice bandwidth (≥40 kHz) for quality. :contentReference[oaicite:19]{index=19}  
- **Find local tower frequencies** (airport website). Example shown: Farmington Ground **121.7** and Tower **118.9**—tune until the red spike indicates activity. :contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}

## Air Traffic Position and Speed Monitoring

- **ADS-B basics**: aircraft broadcast GPS location, altitude, ground speed, etc., once per second (“ADS-B Out”); “ADS-B In” provides cockpit traffic/weather. :contentReference[oaicite:22]{index=22}  
- **Tools**: clone and build **dump1090**, or use **DragonOS** (Linux distro focused on SDR). :contentReference[oaicite:23]{index=23}  
- **Run**:  
  - `cd dump1090 && ./dump1090` (start decoder) :contentReference[oaicite:24]{index=24}  
  - `./dump1090 --raw` (raw frames) :contentReference[oaicite:25]{index=25}  
  - `./dump1090 --interactive` (live table) :contentReference[oaicite:26]{index=26}  
  - `./dump1090 --interactive --net` then browse **`localhost:8080`** for a live map. :contentReference[oaicite:27]{index=27}

## Spoofing Your GPS

- **Build GPS signal simulator**: compile `gps-sdr-sim`  
  `sudo gcc gpssim.c -lm -O3 -o gps-sdr-sim -DUSER_MOTION_SIZE=4000` (build flags explained in text). :contentReference[oaicite:28]{index=28}  
- **Ephemerides**: download latest daily GPS broadcast ephemeris from NASA CDDIS archives. :contentReference[oaicite:29]{index=29}  
- **Choose target coordinates** (e.g., via Google Maps). :contentReference[oaicite:30]{index=30}  
- **Generate I/Q**:  
  `sudo ./gps-sdr-sim -b 8 -e brdc0010.22n -l <lat>,<lon>,100` → produces `gpssim.bin`. :contentReference[oaicite:31]{index=31}  
- **Transmit with HackRF**:  
  `sudo hackrf_transfer -t gpssim.bin -f 1575420000 -s 2600000 -a 1 -x 0` (spoofs position at L1 frequency). :contentReference[oaicite:32]{index=32}

## Exercises

- Install **HDSDR**.  
- Intercept your local airport’s **AM voice** traffic.  
- Use **RTL-SDR + dump1090** to capture ADS-B location/speed data and visualize it. :contentReference[oaicite:33]{index=33}

---

## Summary author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
