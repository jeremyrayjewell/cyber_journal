SUMMARY OF 
**PRACTICAL PACKET ANALYSIS** 
(THIRD EDITION) BY CHRIS SANDERS

---

# CHAPTER 9: COMMON UPPER-LAYER PROTOCOLS

---

## Overview

- Upper-layer (application) protocols sit atop TCP/UDP and carry the “human-meaningful” exchanges we troubleshoot daily.
- This chapter focuses on **DHCP**, **DNS**, **HTTP**, and **SMTP** (with quick notes on **FTP** and **SMB**). For each: message flow, key fields, Wireshark display filters, and failure patterns you’ll actually see.

---

## DHCP (Dynamic Host Configuration Protocol)

**Purpose:** Automatically assigns IP addressing parameters to clients joining a network.

**Ports:** UDP/67 (server) and UDP/68 (client).

**DHCPv4 four-way flow (DORA)**
1. **Discover** (broadcast from client, `0.0.0.0 → 255.255.255.255`): “Anyone out there?”
2. **Offer** (unicast/broadcast from server): “Use this IP + options.”
3. **Request** (broadcast from client): “I’d like the offered IP (X).”
4. **ACK** (unicast/broadcast from server): “Granted. Lease parameters attached.”

**Renewals/Transitions**
- **T1** (50% of lease): client unicasts **Request** to the original server.
- **T2** (87.5%): client broadcasts if the original server didn’t respond.
- **Decline/NAK:** client can **Decline** a bad address (e.g., ARP conflict); server can **NAK** (e.g., policy change).

**Key options you’ll see**
- **Option 53**: Message Type  
- **Option 50**: Requested IP  
- **Option 54**: Server Identifier  
- **Option 1/3/6**: Subnet Mask / Router (gateway) / DNS Servers  
- **Option 51**: Lease Time; **58/59**: T1/T2

**Wireshark filters**
- `bootp` (historical name; matches DHCPv4)  
- `dhcp` (recent builds)  
- `udp.port == 67 or udp.port == 68`  
- `dhcp.option.dhcp == 5` (ACK), `dhcp.option.dhcp == 6` (NAK)

**Failure patterns**
- **No Offer**: rogue VLAN, DHCP helper misconfig, or server down.
- **ACK never arrives**: ACLs, relay (ip helper) path blocked, asymmetric routing.
- **Address conflicts**: ARP probe reveals another MAC using the offered IP → client sends **Decline**.
- **Relay issues**: check **giaddr** and that IP helpers are set on the L3 SVI.

**DHCPv6 (quick contrast)**
- Uses **Solicit/Advertise/Request/Reply** (SARR) and relies on **ICMPv6 ND**; may coexist with SLAAC.
- Ports: UDP/546 (client), UDP/547 (server).
- Avoid blocking essential ICMPv6 (needed for basic operation).

---

## DNS (Domain Name System)

**Purpose:** Translates names ↔ addresses and provides other metadata (MX, NS, TXT, etc.).

**Ports:** UDP/53 for most queries; TCP/53 for large responses/zone transfers (AXFR/IXFR).

**Message structure**
- **Header**: ID, flags (QR, AA, TC, RD, RA), RCODE (e.g., **0** NoError, **2** ServFail, **3** NXDomain).  
- **Sections**: Question, Answer, Authority, Additional.

**Common record types**
- **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias), **NS**, **MX**, **TXT**, **SRV**, **SOA**.

**Recursion & caching**
- Resolver sets **RD**; server replies with **RA** if it performed recursion.  
- Responses carry **TTL**; caches should honor TTL (but middleboxes sometimes don’t).

**Zone transfers**
- **AXFR/IXFR** over TCP; only between authorized secondaries/primaries. Unexpected AXFR attempts can indicate reconnaissance.

**Wireshark filters**
- `dns`  
- `dns.flags.response == 0` (queries) / `== 1` (responses)  
- `dns.qry.name contains "example.com"`  
- `dns.flags.rcode > 0` (errors)  
- `tcp.port == 53` (zone transfers)

**Failure patterns**
- **NXDOMAIN vs SERVFAIL**: NXDOMAIN = name truly doesn’t exist; SERVFAIL = upstream problem or DNSSEC validation error.  
- **Truncation (TC=1)**: response didn’t fit UDP; client retries over TCP—if TCP/53 blocked, name resolution fails intermittently.  
- **Split-horizon surprises**: different answers inside vs outside; ensure you’re hitting the intended resolver.  
- **EDNS/size issues**: middleboxes dropping large UDP DNS; watch for retry to TCP and MTU/fragmentation problems.

**Triage tips**
- Add columns for `dns.qry.name`, `dns.qry.type`, and RCODE; spot spikes of `ServFail` or timeouts in I/O Graphs.
- Check whether client talks to a local resolver (correct) or directly to the Internet due to misconfigured DHCP.

---

## HTTP (Hypertext Transfer Protocol)

**Purpose:** Web protocol transporting requests/responses; in practice you’ll see **HTTP/1.1** in the clear (lab) and **HTTPS (HTTP over TLS)** in production.

**Ports:** TCP/80 (HTTP), TCP/443 (HTTPS by convention).

**HTTP/1.1 basics**
- **Request line**: `GET /path HTTP/1.1`  
- **Headers**: `Host`, `User-Agent`, `Accept`, `Cookie`, etc.  
- **Response**: `HTTP/1.1 200 OK` + headers + body.  
- **Keep-Alive**: multiple requests per TCP connection; watch **pipelining** (rare now).

**Useful fields/columns**
- `http.request.method`, `http.host`, `http.request.uri`, `http.response.code`, `http.content_type`, `http.user_agent`.

**TLS considerations (HTTPS)**
- You won’t see HTTP headers/payloads unless you decrypt.  
- You can still use **SNI** (`tls.handshake.extensions_server_name`) and **JA3/JA3S** (fingerprints, with plugins) to infer app/SaaS.  
- With permission, use **SSLKEYLOGFILE** to decrypt client-side browser sessions.

**Wireshark filters**
- `http`  
- `http.response.code >= 400` (client/server errors)  
- `tls.handshake.type == 1` (ClientHello)  
- `tls.handshake.extensions_server_name contains "example.com"`

**Failure patterns**
- **High TTFB**: slow server or upstream dependency (DB, microservice). Set **Time Reference** on request; measure delta to first response byte.  
- **Resets**: middlebox policy or idle timeout; filter `tcp.flags.reset==1` and check who sent it.  
- **MTU/PMTUD**: large responses stall under black-holed ICMP; correlate with missing `Fragmentation Needed/Packet Too Big`.

**Workflow**
1. Follow TCP Stream (or SSL stream if decrypted).  
2. Check handshake options (MSS/WS/SACK) and zero-window/retrans indicators for transport issues.  
3. For HTTPS, pivot with SNI/Server Cert details to identify the backend.

---

## SMTP (Simple Mail Transfer Protocol)

**Purpose:** Transports email between mail servers and from clients to submission servers.

**Ports:** Historically **25** (server-to-server), **587** (submission with AUTH/STARTTLS), **465** (smtps, legacy but widely used). POP3/IMAP are separate retrieval protocols.

**Flow (simplified)**
1. **Connect** → server banner (`220 ...`).  
2. **EHLO** (or `HELO` legacy) → server lists capabilities (e.g., **SIZE**, **STARTTLS**, **AUTH** mechanisms).  
3. **MAIL FROM:** sender envelope.  
4. **RCPT TO:** recipient(s).  
5. **DATA** → message headers/body; terminates with `\r\n.\r\n`.  
6. **QUIT**.

**Security & auth**
- **STARTTLS** upgrades plaintext to TLS on the same port (25/587).  
- **AUTH PLAIN/LOGIN** (after STARTTLS on submission); don’t send credentials in clear.  
- **SPF/DKIM/DMARC** are DNS/crypto policies seen indirectly (look for results in headers, not on the wire unless you decrypt).

**Wireshark filters**
- `smtp`  
- `smtp.req.command == "EHLO"`  
- `smtp.req.parameter contains "STARTTLS"`  
- `tcp.port == 25 or tcp.port == 587 or tcp.port == 465`

**Failure patterns**
- **Relay denied**: server returns `550`/`554`; check AUTH / permitted senders.  
- **TLS negotiation failure**: `STARTTLS` accepted, then TLS alert/abort (cipher mismatch, cert problems).  
- **Greylisting/retries**: delays visible as server 4xx responses; client retries later.

---

## Quick Notes: FTP & SMB (you’ll still meet these)

**FTP (control on TCP/21)**
- **Active mode**: server connects back to client’s data port (firewall pain).  
- **Passive mode**: client opens data connection to server-chosen port (easier through NAT).  
- Filters: `ftp` (control), `ftp-data` (heuristic), or track by negotiated data port in control channel.

**SMB (file sharing)**
- Modern stacks use **SMB2/SMB3** over TCP/445.  
- Look at **Session Setup**, **Tree Connect**, **Create**, **Read/Write** exchanges; latency often shows in server think-time or auth delays.  
- Filters: `smb2` (or `smb` for legacy), plus `ntlmssp` if NTLM auth is in play.

---

## Cross-Protocol Troubleshooting Patterns

- **It’s not DNS… it was DNS.** Check resolver used, RCODEs, truncation (TC), and UDP→TCP fallback.  
- **Auth works, app still fails.** For HTTP/SMTP, confirm post-auth exchanges and look for 4xx/5xx server responses.  
- **Everything breaks for large payloads.** Suspect **PMTUD black holes**; confirm with ICMP evidence or MSS clamping differences.  
- **Intermittent failures at the top but transport is clean.** Look for server-side rate limits, load balancer health checks, sticky-session issues.

---

## Display Filters (copy/paste)

- **DHCP**: `bootp` • ACK only: `dhcp.option.dhcp == 5`
- **DNS**: `dns` • Errors: `dns.flags.rcode > 0` • Queries only: `dns.flags.response == 0`
- **HTTP**: `http` • Errors: `http.response.code >= 400`
- **TLS/SNI**: `tls.handshake.type == 1` • `tls.handshake.extensions_server_name`
- **SMTP**: `smtp` • `smtp.req.parameter contains "STARTTLS"`
- **FTP**: `ftp or ftp-data`
- **SMB2**: `smb2`

---

## Mini-Labs

1) **DHCP lease lifecycle**
   - Reconnect a client to trigger **Discover/Offer/Request/ACK**.
   - Observe **Option 53** transitions and lease **T1/T2** renewals.

2) **DNS recursion & errors**
   - Query a known-bad name (expect **NXDOMAIN**) and a temporarily broken domain (expect **SERVFAIL**).
   - Capture UDP→TCP fallback for a large DNS response (set EDNS/large TXT in a lab).

3) **HTTP TTFB measurement**
   - Set **Time Reference** on `GET` and measure delta to first server byte.
   - Compare same URL from LAN vs across WAN.

4) **SMTP STARTTLS path**
   - Connect to a submission server; watch `EHLO` capabilities and `STARTTLS` upgrade.
   - If allowed, attempt AUTH after TLS; confirm no credentials on the wire pre-TLS.

---

## What You Should Be Able to Do After Chapter 9

- Read DHCP/DNS/HTTP/SMTP exchanges, field-by-field, and identify where a transaction breaks.  
- Use targeted display filters and columns (e.g., `dns.qry.name`, `http.response.code`) to surface meaning quickly.  
- Distinguish name-resolution failures from transport issues and server/application errors.  
- Anticipate middlebox behaviors (DNS truncation, FTP active/passive constraints, SMTP STARTTLS) and test around them.

---

## Summary author: **Jeremy Ray Jewell**
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
