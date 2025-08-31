SUMMARY OF 
**LINUX BASICS FOR HACKERS** 
(FIRST EDITION) BY OCCUPYTHEWEB

---

# CHAPTER 3: ANALYZING AND MANAGING NETWORKS

---

## Analyzing Networks with ifconfig

The `ifconfig` (*interface configuration*) tool shows interface status and configures interfaces. 

- lists each network device (`eth0`, `wlan0`, `lo`, etc.) with its MAC address, IPv4/IPv6 addresses, MTU, link state, packet statistics, and errors. 

- brings an interface up/down: `ifconfig eth0 up`

- sets an IP/netmask: `ifconfig eth0 192.168.1.10 netmask 255.255.255.0`

- assigns an alias (secondary address): `ifconfig eth0:1 10.0.0.5`

- changes MAC to MTU, enables promiscuous mode, etc.

It is part of the old Berkeley `net-tools` suite; largely replaced by the more modern `ip` command (`ip addr show`, `ip link set ...`) on most current Linux distros. In general, it is still handy for a fast glance.

The following is a description of what `ifconfig` shows with some expanded examples for contemporary Arch, the distro I am using, that differs from the author's Kali from 2019 or so:

- `eth0`: the first wired *Ethernet* network interface on the system

- `HWaddr` or `ether` : hardware class label followed by the MAC; showing that it is an Ethernet-format MAC

- `inet addr` or `inet`: the *IPv4 address* currently assigned to the interface which it describes (above it)

- `inet6` : *IPv6* info

- `netmask` : *network mask* is used to determine which part of the address is the network and which part is the host

- `Bcast` or `broadcast` : *broadcast address* for the subnet; packets sent here reach every host on the local network
 
- `lo` or `loop` : the *loopback* or *localhost* interface (address 127.0.0.1); lets programs talk to the same machine internally

- `wlan0`, `wifi0`, etc. : *wireless (Wi-Fi)* network interface

## Checking Wireless Network Devices with iwconfig

While `ifconfig` is part of the *net-tools* suite (1980s), `iwconfig` is part of the *wireless-tools* suite (late 1990s). `iwconfig` was conceived as a companion program to `ifconfig` when Wi-Fi first appeared and wireless radio control was needed. Just like `ifconfig` has a newer counterpart in `ip`, iwconfig has a new counterpart in `iw`.

When we run `iwconfig` we will see our interface names followed by their radio specifications, usually `IEEE 802.11` possibly followed by some additional letters.

We can also see the `Access Point`, if any, to which the interface is currently connected.

## Changing Your Network Information

### Changing Your IP Address

Changing your **IP address** helps hide your identity for example during a DoS (Denial of Service) attack, etc.

- `ifconfig eth0 192.168.181.115` changes the `eth0` interface to IP address `192.168.181.115`

### Changing Your Network Mask and Broadcast Address

**Network masks** and **broadcast addresses** tell every host *how the IP address should be interpreted inside the local LAN*. The **Netmask** says which bits of the address identify the network and which bits identify the host. The **broadcast address** is an "all-hosts" destination derived from that netmask (every host in the subnet must agree on it).

Changing these has nothing to do with hiding your location the way changing your IP address does. Instead, it's about **shaping the layer-2/3 boundaries of a network**.

- `ifconfig eth0 192.168.181.115 netmask 255.255.0.0 broadcast 192.168.255.255`

Realistic use cases: you might want to shrink a broadcast domain so fewer devices hear every broadcast, allowing ARP storms and chatty protocols to stay local. Alternatively, you may want to grow a LAN without renumbering everything, make point-to-point links/tunnels, create greater segmentation or utilize special protocols which depend on directed broadcast.

### Spoofing Your MAC Address

A **MAC** (*Media Access Control*) address lets devices on the same local network tell one another apart. It is burned into the network-interface card (NIC) by the manufacturer, and its first 24 bits form the **OUI** (*Organizationally Unique Identifier*) of your device's vendor. Spoofing it, therefore, allows for greater anonymity on a local network. The MAC described by `ifconfig` in the book's Kali as `HWaddr` and in my Arch as `ether`

An interface has to be "down" before the driver will accept a new MAC address because the NIC, its driver, and the kernel all cache  that address in places that are actively used while frames are moving.

- `ifconfig eth0 down`

- `ifconfig eth0 hw ether 00:11:22:33:44:55`

- `ifconfig eth0 up`

Also we can use the `ip link set` command (not mentioned in the book) instead of `ifconfig`:

- `ip link set dev eth0 address 00:11:22:33:44:55`

### Assigning New IP Addresses from the DHCP Server

**DHCP** (*DynamicHost Configuration Protocol*) is the system that automatically hands out an IP address and the rest of a host's basic network settings every time a device joins a TCP/IP network. An attacker would want to "pull a fresh IP" from the DHCP server for a number of reasons:

- **Evade IP-based blocks** : Blue-team IDS/Firewall blocks *192.168.1.57*, so attacker just asks DHCP for the next free address and is back in business within seconds.

- **Match a spoofed MAC** : After cloning a victim's MAC to dodge a MAC filter, the attacker must obtain a matching IP/netmask/gateway so traffic looks normal.

- **Impersonate a specific host** : Send a DHCP DISCOVER with "*requested IP=192.168.10.254*" IP pf a specific host and some mis-configured server oblige, allowing you to steal traffic or perform MITM (*man in the middle*) attacks.

- **Bypass VLAN/ACL tied to IP ranges** : Some internal apps trust anything from 10.10.0.0/24. By renewing until the server hands out an address in that subnet, the attacker jumps the fence.

- **Blend into log files ("IP churn")** : Rotate leases every few minutes so SOC analysts see dozens of short-lived IPs instead of a single smoking gun.

- **DHCP-Starvation DoS / Rogue DHCP** : Hammer the server with thousands of DISCOVERs, exhausting the pool. Then when legitimate hosts can't get an IP, attacker launches a **rogue DHCP** that answers instead, funneling victims' traffic through a malicious gateway/DNS.

We can request a new IP address from DHCP by running `dhclient` plus the interface we want the IP assigned to. I.e.:

- `dhclient eth0`

You can confirm the success of the request by running `ifconfig`. We can also give an interface a new IP using `ip addr add`:

- `ip addr add 192.0.2.10/24 dev eth0` 

The `ifconfig`/`ip` commands for changing IPs let *you* jam any address onto an interface right now, while the `dhclient` (or NetworkManager, systemd-networkd, etc.) asks a DHCP server to *lease* an address. While both result in a new IP, they solve different problems:

- Static `ifconfig`/`ip` IP changes are enough in labs, tunnels, and boot-strapping a headless server

- DHCP requested IP changes allow you to blend in silently, learn about hidden infrastructure via options fields, steal an identity by spoofing a MAC before requesting, and stage a rouge DHCP attack

Note that the static changes do not effectively hide your **public IP**, so this also doesn't help for discreet remote server connections the way a VPN, proxychain, Tor, or tunnel would.

## Manipulating the Domain Name System

### Examining DNS with dig

`dig` (*Domain Information Groper*, where "groper" was once a Unix naming habit for diagnostic tools) is a multi-purpose DNS (*Domain Name System*) utility.  tool

- `dig hackers-arise.com ns` gives information about the domain server

- `dig hackers-arise.com mx` gives information about a domain mail exchange server

Linux user nomenclature sometimes refers to DNS as BIND, after the Berkley Internet Naming Domain. Although BIND is the most common Linux server, BIND and DNS are not the same thing.

### Changing Your DNS Server

One of my first personal experiences with DNS server changing was discovering that DNS hijacking on the part of my ISP was slowing my video calls to a severe degree. You can point to a public DNS resolver like 1.1.1.1 or 8.8.8.8 to bypass the ISP's DNS resolver. DNS hijacking is done to both collect your navigation history to sell on to others, and also to manage traffic to the ISP's benefit (even if to your detriment.

Other reasons to change your DNS Server include: evade local controls, hide reconnaissance queries, use ECS-free resolver which does not leak partial client IP, and victim resolver changes for certain attacks.

- `leafpad /etc/resolv.conf` to edit your DNS resolver configuration with a line `nameserver 1.1.1.1` or the like

- `echo "nameserver 1.1.1.1"> /etc/resolv.conf` to **overwrite** your existin DNS resolver settings entirely

!!! NOTE: if you run `dhclient` or a related command to request an IP from a DHCP server with its own DNS server settings then your `resolv.conf` file will be overwritten with that DHCP server's settings.

### Mapping Your Own IP Addresses

`/etc/hosts` is a table that maps host-names to IP addresses --  alocal, static mini-DNS that every TCP/IP stack consults before (or instead of) querying the network.

In this file you can essentially **override** downstream DNS resolvers for the machine where the file lives, redirecting traffic from a public DNS's IP to an IP of your choosing, allowing *DNS spoofing*. 

- `leafpad /etc/hosts` to edit the file

`dnsspoof` is a DNS-forgery utility that ships in Dug Song's *dsniff* suite. It can sit on a LAN segment, watch for DNS queries, and forge replies of your choosing, allowing victims to be redirected to any IP address. Once a machine's `/etc/hosts` file is altered to misdirect traffic its hosts-formatted mapping can be fed to `dnsspoof` once you have MITM control.

- `dnsspoof -i eth0 -f /etc/hosts`

Technically, however, `dnsspoof` could use any hosts-formatted file, and because `/etc/hosts` - though syntactically valid - applies to ones local machine, it is unlikely to serve as well as the base for malicious misdirection itself outside of prototyping.

## Summary

Networking skills are vital for reconnaissance, spoofing, and connecting to other systems.

## Exercises

- investigate your active network interface using the commands `iwconfig`, `ifconfig`, `ip, and `iw`

- practice changing your IP with `ifconfig`, `ip addr add` and `dhclient` and your hardware addresses with `ifconfig` and `ip link set`

- use `dig` with `ns` (nameserver) and `mx` (email exchange) on a website of your choosing.

- add Google's DNS server to your `/etc/resolv.conf`. If you are worried about DNS hijacking, you can totally replace your local DNS server. Quad and Cloudflare's DNSes are also pretty good.

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
