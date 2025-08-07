**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 13: BECOMING SECURE AND ANONYMOUS

---

## How the Internet Gives Us Away

* Every IP packet carries source and destination addresses.
* Tools like `traceroute` show each hop between you and a destination:

  ```bash
  traceroute example.com
  ```

  Reveals routers and latency; exposes your network path.

## The Onion Router System

Tor provides layered anonymity by routing encrypted traffic through volunteer nodes.

### How Tor Works

* Builds a circuit of three relays: entry, middle, exit.
* Each relay knows only its predecessor and successor IP, encrypting other layers.
* Exit node sees destination but not origin; entry sees origin but not destination.

### Security Concerns

* Tor can be slow due to limited bandwidth.
* Powerful adversaries (e.g., NSA) may run relays or correlate traffic to deanonymize users.

## Proxy Servers

Proxies mask your IP by forwarding requests on your behalf.

### Setting Proxies in the Config File

* Kali’s `proxychains` uses `/etc/proxychains.conf`:

  ```text
  [ProxyList]
  socks4 114.134.186.12 22020
  socks4 188.187.190.59 8888
  ```
* Default last line is `socks4 127.0.0.1 9050` (Tor).
* Run:

  ```bash
  proxychains firefox www.example.com
  ```

### Some More Interesting Options

* **dynamic\_chain**: skip dead proxies in list.
* **strict\_chain**: require all proxies online.
* **random\_chain** + `chain_len = N`: pick N random proxies per request.

### Security Concerns

* Free proxies often log/sell your data.
* Proxy operator can reveal your IP under legal pressure.

## Virtual Private Networks

VPNs encrypt your traffic and tunnel it through a gateway, hiding your IP from sites and local observers.

* Simple setup via commercial services (e.g., NordVPN, ExpressVPN).
* Must trust provider’s no-log policy to prevent later deanonymization.

## Encrypted Email

End-to-end encrypted email (e.g., ProtonMail) ensures only sender and recipient can read messages.

* Servers store encrypted content; even administrators cannot decrypt.
* Watch for limitations when emailing non-encrypted addresses.

---

## Summary

Tracking online comes from IP headers, DNS, cookies, and unencrypted services. Use Tor, proxy chains, VPNs, and encrypted email to raise the bar for surveillance and protect your privacy and hacking activities.

## Exercises

1. Run `traceroute` to any website and note hop count.
2. Install and test the Tor Browser; compare browsing speed.
3. Use `proxychains` with Firefox to visit a site anonymously.
4. Research a VPN provider from the list; test a trial.
5. Create a ProtonMail account and send a secure message to `occupytheweb@protonmail.com`.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
