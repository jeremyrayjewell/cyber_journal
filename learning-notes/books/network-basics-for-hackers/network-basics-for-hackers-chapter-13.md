SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 13: AUTOMOBILE NETWORKS

---

- This chapter introduces automobile networks and hands-on CAN bus hacking using Linux can-utils, a virtual CAN interface, the ICSim simulator, and a key-fob relay attack.

## The CAN Protocol

- **Origins & purpose**: Controller Area Network (CAN) was developed by Bosch, standardized as ISO 11898-1/-2, to enable robust, host-less communication among microcontrollers, sensors, and actuators in vehicles. It is a broadcast bus: all nodes “see” all frames, with local filtering deciding what to act on. Physical signaling uses a two-wire differential pair (CAN-H/CAN-L). :contentReference[oaicite:0]{index=0}

- **Message types**: CAN defines four frame types—Data, Remote, Error, and Overload—of which **Data frames** carry application data. :contentReference[oaicite:1]{index=1}

- **OBD-II access**: Modern vehicles expose a 16-pin OBD-II port under the dash; connecting here allows reading and sending messages on the in-vehicle network. :contentReference[oaicite:2]{index=2}

- **Packet layout** (standard vs. extended): Core fields include **Arbitration ID** (sender identity), **IDE** (identifier extension; 0 in standard frames), **DLC** (0–8 bytes), and **Data** (payload). Extended frames chain additional ID bits yet remain backward-compatible. Because frames are broadcast and lack a return address, spoofing is trivial on CAN. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

- **Security**: CAN provides **no built-in encryption or authentication**, enabling MitM and spoofing; some OEMs add authentication around critical functions, but these are inconsistent and often weak. :contentReference[oaicite:5]{index=5}

## CAN-UTILS or SocketCAN

- **What they are**: *can-utils* is a Linux toolkit (built atop the kernel’s SocketCAN stack) for sniffing, generating, and replaying CAN traffic. :contentReference[oaicite:6]{index=6}

- **Install**: On Kali/Debian, `sudo apt install can-utils`; otherwise clone from GitHub. :contentReference[oaicite:7]{index=7}

- **Tooling overview**: Functional groups include traffic display/record/generation, IP-socket access, in-kernel gateway config, measurement, ISO-TP tools, log converters, and slcan helpers. Key basics:  
  - `candump` (log/display), `canplayer` (replay), `cansend` (send a frame), `cangen` (generate traffic), `cansniffer` (highlight changing data). :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}

## Setting up a Virtual CAN network

- **Virtual interface**: Load the vcan module and create/bring up a virtual interface (vcan0), then verify it like any Linux NIC.  
  `modprobe vcan`  
  `ip link add dev can0 type vcan`  
  `ip link set up vcan0`  
  `ifconfig vcan0` :contentReference[oaicite:10]{index=10}

## CAN Simulation

- **Dependencies**: Install SDL2 libraries on Kali. :contentReference[oaicite:11]{index=11}

- **ICSim**: Clone Craig Smith’s ICSim, run `setup_vcan.sh` (loads CAN/vcan modules and creates vcan0), then start the instrument panel and controller.  
  `git clone https://github.com/zombieCraig/ICSim` → `cd ICSim` → `./setup_vcan.sh` → `./icsim vcan0` → `./controls vcan0` :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

- **Sniffing in the sim**: With the sim running, use `cansniffer -c vcan0` to view live traffic (changing bytes turn red). Filter by Arbitration ID from within cansniffer (mask then `+ID`). :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15}

## Reverse Engineer a CAN Packet

- **Find the control packet**: Drive the ICSim car to 100 mph, observe changing frames, and focus on Arbitration ID **244** using cansniffer filter entries (`-000000` then `+244`). :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17}

- **Capture/replay/send**:  
  - Log traffic: `candump -c -l vcan0` (or `-c -l -s 0 -a` to colorize, log, and ASCII-decode simultaneously).  
  - Replay logs: `canplayer -I candump-...log`  
  - Send a single frame: `cansend vcan0 161#...` / `cansend vcan0 244#0000003812` :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20}

- **Force the effect**: A single accelerate frame may be overridden by normal traffic; continuously sending the frame (e.g., `while true; do cansend vcan0 244#0000003812; done`) overwhelms the idle signals—taking control of the simulated car’s speed. :contentReference[oaicite:21]{index=21} :contentReference[oaicite:22]{index=22}

## Key Fob Hacking

- **PKES & threat**: Passive Keyless Entry and Start (introduced 1999) unlocks/starts when the fob is near. The **Signal Amplification Relay Attack (SARA)** relays the LF fob exchange over distance using two radios—no decryption needed—tricking the car into believing the fob is nearby. Effective against many pre-2014 vehicles and some models later (e.g., Honda up to 2021). :contentReference[oaicite:23]{index=23} :contentReference[oaicite:24]{index=24} :contentReference[oaicite:25]{index=25}

- **Mechanics of the relay**: Capture the vehicle’s LF challenge, up-convert to ~2.5 GHz and transmit up to ~100 m to a receiver near the car, down-convert back to LF, amplify, and re-radiate via a loop LF antenna to open doors/start engine. :contentReference[oaicite:26]{index=26} :contentReference[oaicite:27]{index=27}

## Exercises

- Download **can-utils** and **ICSim**, create a virtual CAN network, and replicate the CAN replay steps from this chapter. :contentReference[oaicite:28]{index=28}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
