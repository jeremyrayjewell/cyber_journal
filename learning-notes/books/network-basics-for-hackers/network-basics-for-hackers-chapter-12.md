SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
(FIRST EDITION) BY OCCUPYTHEWEB

---

# CHAPTER 12: HTTP

---

- This chapter orients you to the core web technologies you must understand before attempting web application hacking. It introduces HTTP fundamentals, response codes, transport security, and a guided workflow for attacking web-form authentication with Burp Suite. :contentReference[oaicite:0]{index=0}

## HTTP Protocol

- **Role & model**: HTTP is the core, message-based protocol of the web. A client sends a request and the server replies with a response; HTTP itself is connection-less but rides over TCP. :contentReference[oaicite:1]{index=1}  
- **Request structure**: headers → blank line → optional body. The request line = *METHOD URL HTTP/VERSION*. :contentReference[oaicite:2]{index=2}  
- **Response structure**: *HTTP/VERSION* → numeric status code → human-readable reason phrase. :contentReference[oaicite:3]{index=3}  
- **Methods**:  
  - *GET* retrieves a resource; *POST* performs an action (typical pair when attacking apps). :contentReference[oaicite:4]{index=4}  
  - Others you may see: *HEAD* (like GET, no body), *TRACE* (diagnostics), *OPTIONS* (supported methods), *PUT* (upload a resource). :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}  
- **URLs**: canonical form `protocol://hostname[:port]/[/path/]file[?param=value]`; port is optional unless non-default (e.g., HTTP 80, HTTPS 443, FTP 21). :contentReference[oaicite:7]{index=7}  
- **Headers (examples)**:  
  - *General*: `Connection`, `Content-Encoding`, `Content-Length`, `Content-Type`, `Transfer-Encoding`. :contentReference[oaicite:8]{index=8}  
  - *Request*: `Accept`, `Accept-Encoding`, `Authorization`, `Cookie`, `Host`, `If-Modified-Since`, `If-None-Match`, `Origin`, `Referrer`, `User-Agent`. :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}  
  - *Response*: `Access-Control-Allow-Origin`, `Cache-Control`, `ETag`, `Expires`, `Location`, `Pragma`, `Server`, `Set-Cookie`, `WWW-Authenticate`, `X-Frame-Options`. :contentReference[oaicite:11]{index=11}  
- **Cookies**: server issues cookies via `Set-Cookie`; clients store and resend them on subsequent requests—commonly as name/value pairs—enabling user identification and state. :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

## Status Codes

- **Families**: `1xx` informational, `2xx` success, `3xx` redirect, `4xx` client error, `5xx` server error. :contentReference[oaicite:14]{index=14}  
- **Common codes to recognize**: `100`, `200`, `201`, `301`, `302`, `304`, `400`, `401`, `403`, `404`, `405`, `413`, `414`, `500`, `503`. :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}

## HTTPS

- **Why HTTPS**: Plain HTTP over TCP is unencrypted and vulnerable to MitM; HTTPS tunnels HTTP through SSL/TLS to protect confidentiality and integrity. :contentReference[oaicite:17]{index=17}  
- **HTTP proxies (operational context)**: A proxy sits between browser and server, forwarding requests/responses and enabling access control, caching, authentication, and filtering—useful both operationally and offensively. :contentReference[oaicite:18]{index=18}  
- **Built-in HTTP auth schemes**: Basic (Base64 in header), NTLM (challenge-response), Digest (nonce + MD5). :contentReference[oaicite:19]{index=19}

## Hacking Web App Authentication with BurpSuite

- **Setup**: Use DVWA on Metasploitable or OWASP BWA; Burp Suite Community Edition is sufficient for learning (requires JDK 11+). :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}  
- **Proxying & intercept**: Start Burp → Proxy tab → enable *Intercept*. Configure browser proxy to `127.0.0.1:8080`. Browse to DVWA login. :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}  
- **Capture credentials request**: With Intercept on, submit the login form to catch the request and view parameters (e.g., username/password) in the body. :contentReference[oaicite:24]{index=24}  
- **Send to Intruder & position markers**: Right-click → *Send to Intruder*. Verify target IP/port, then clear auto-marked fields and add the parameter(s) you want to attack (e.g., password only if username is known). :contentReference[oaicite:25]{index=25} :contentReference[oaicite:26]{index=26}  
- **Attack types**: *Sniper* (one payload set, try values in one position), *Cluster Bomb* (multiple payload sets, combinatorial), *Pitchfork* (multiple sets iterated in lockstep), *Battering Ram* (one set reused across positions). For a quick known-user attack, use *Sniper*. :contentReference[oaicite:27]{index=27} :contentReference[oaicite:28]{index=28}  
- **Payloads**: Seed with very common passwords (`admin`, `guest`, `root`, etc.) and optionally load a larger list such as `top10000_passwords.txt`. Start the attack. :contentReference[oaicite:29]{index=29} :contentReference[oaicite:30]{index=30}  
- **Reading results**: Look for anomalies—responses whose *Status* and *Length* differ from the uniform failures (e.g., repeated `302` / same length). Sort by those columns to spot likely successes. :contentReference[oaicite:31]{index=31}  
- **Unknown user & pass (Cluster Bomb)**: Add both username and password as positions; enable *Character Substitution* to “munge” passwords (e↔3, a↔4, b↔8, etc.), then load your list and run. Be aware the combinatorics can explode into billions of attempts; Community Edition throttles, while Pro is faster. :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33} :contentReference[oaicite:34]{index=34}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
