SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 1: PACKET ANALYSIS AND NETWORK BASICS	

---

## Packet Analysis and Packet Sniffers

- **Packet analysis**: the systematic process of capturing, inspecting, and interpreting individual network *packets* as they traverse a network link. Packet analysis lets you **understand protocols**, **troubleshoot connectivity**, **detect anomalies**, and **manage bandwidth usage**.

- **Packet sniffer**: software or hardware tool that **intercepts** ("sniffs) network traffic, capturing raw packet data for later analysis. This book focuses on **Wireshark**.

### Evaluating a Packet Sniffer

- Criteria: Supported protocols, user-friendliness, cost, program support, source code access (i.e. open source or not), operating system support

- In terms of supported protocols, most support common netowkr protocols such as IPv4 and ICMP, TDP and UDP transport protocols, and DNS and HTTP application protocols. Fewer may support newer and more complex protocls such as IPv6, SMBv2, and SIP.

### How Packet Sniffers Work

- **Collection** of raw binary data by using your network interface's *promiscuous mode*, **conversion** of captured binaries into readable form, and **analysis**.

## How Computers Communicate

### Protocols

*Protocols* are common languages used to communicate between systems. A *protocol stack* is a group of protocols that work together. Common protocols (followed by descriptions not found in the book yet) include:

- **TCP** *Transmission Control Protocol*: `transport-layer`, provides connection-oriented, reliable, ordered, byte-stream service between two endpoints.

- **IP** *Internet Protocol*: `network-layer`, addresses and routes packets between hosts across one or more networks.

- **ARP** *Address Resolution Protocol*: `link-layer`, maps IP addresses to MAC (hardware) addresses on a local network.

- **DHCP** *Dynamic Host Configuration Protocol*: `application-layer`, automates IP address and related configuration for hosts joining a network

Protocols can be simple or complex but they mostly address the same issues: Connection initiation, negotiation of connection characteristics, data formatting, error detection and correction, connection termination.

### The Seven-Layer OSI Model

The OSI Model is an industry-recommended standard for mapping protocols based on their function which was first published in 1983. It has seven layers:
<pre markdown>                                                               
+-------+--------------+--------------+-------------------------------------+
| LEVEL |    LAYER     |     UNIT     |              PROTOCOLS              |
+-------+--------------+--------------+-------------------------------------+
|   7   |  application |data (message)|HTTP, SMTP, FTP, Telnet              |
+-------+--------------+--------------+-------------------------------------+
|   6   | presentation |  data (PPDU) |ASCII. MPEG, JPEG, MIDI              |
+-------+--------------+--------------+-------------------------------------+
|   5   |    session   |  data (SPDU) |NetBIOS, SAP, SDP, NWLink            |
+-------+--------------+--------------+-------------------------------------+
|   4   |   transport  |    segment*  |TCP, UDP, SPX                        |
+-------+--------------+--------------+-------------------------------------+
|   3   |    network   |    packet    |IP, IPX                              |
+-------+--------------+--------------+-------------------------------------+
|   2   |   data link  |    frame     |Ethernet, token ring, FDDI, AppleTalk|
+-------+--------------+--------------+-------------------------------------+
|   1   |   physical   |     bits     |wired, wireless                      |
+-------+--------------+--------------+-------------------------------------+
* segment (TCP) or datagram (UDP)
</pre>
We can say that each layer "sits on" or "rides on" the one below it (i.e. HTTP sits on TCP, TCP sits on IP, etc.)

Another networking model is the Department of Defense (DoD) model, a.k.a. the DARPA or TCP/IP model (elaborated here but not in the book).
<pre markdown>
+-----------------+---------+
|4. application   | OSI 5-7 |
+-----------------+---------+
|3. transport     | OSI 4   |
+-----------------+---------+
|2. internet      | OSI 3   |
+-----------------+---------+
|1. network access| OSI 1   |
+-----------------+---------+
</pre>

- *Data Flow Through the OSI Model*: Data goes down the chain from the sender, up the chain to the receiver.
<pre markdown>
+---+  +---+  +---+  +---+  +---+  +---+  +---+
| 7 |=>| 6 |=>| 5 |=>| 4 |=>| 3 |=>| 2 |=>| 1 |
+---+  +---+  +---+  +---+  +---+  +---+  +---+
                                            ⇓
+---+  +---+  +---+  +---+  +---+  +---+  +---+
| 7 |=>| 6 |=>| 5 |=>| 4 |=>| 3 |=>| 2 |=>| 1 |
+---+  +---+  +---+  +---+  +---+  +---+  +---+
</pre>

- *Data Encapsulation*: protocols add headers or footers to the data being transferred, creating in the process a **PDU** (protocol data unit) which will then be decrypted by removing the headers and footers as the data climbs back up the chain on the receiving end.

- Note that there are "housekeeping" and control protocols that generate traffic by themselves, so not all data transfers begin and end at layer 7.

### Network Hardware

- **Hub** - *Physical (Layer 1)*: Pure repeater - takes every packet on one port and broadcasts it (*half-duplex*) to all other ports. Every device "sees" every transmission - others discard un-addressed packets.

- **Switch** - *Data Link (Layer 2)*: Uses CAM table of MAC addresses to send each frame only to the port of its intended recipient (*full-duplex*). Managed switches can also enable/disable ports, show stats, change config, and reboot remorely. Traffic goes only where it's meant to go, greatly cutting unnecessary load.

- **Router** - *Network (Layer 3)*: Examines IP addresses and uses routing protocols to forward packets between separate networks. Moves packets across network segments (like turning from one street onto another).

### Traffic Classifications

- **Broadcast Traffic** - *all hosts on a single network segment (broadcast domain)*: L2 `ff:ff:ff:ff:ff:ff`l L3 highest IP in subnet (e.g. `192.168.0.255`): one-to-all; every device sees then drops non-target traffic

- **Multicast Traffic** - *only hosts that join a specific group*: IP `224.0.0.0`-`239.255.255.255`: one-to-many; packets replicated only along paths to group members

- **Unicast Traffic** - *a single destination host*: that host's unique MAC or IP: one-to-one; direct point-to-point delivery with minimal overhead

### Final Thoughts

- You *must* understand everything in this chapter in order to be able to troubleshoot network issues.

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)