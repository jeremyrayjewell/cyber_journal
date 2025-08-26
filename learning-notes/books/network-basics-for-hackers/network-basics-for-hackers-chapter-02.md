SUMMARY OF 
**NETWORK BASICS FOR HACKERS** 
BY OCCUPYTHEWEB

---

# CHAPTER 2: SUBNETTING AND CIDR NOTATION

---

- This chapter introduces why subnetting matters, how subnet masks work, how to read CIDR notation, and walks through a practical subnetting scenario. :contentReference[oaicite:0]{index=0}

## Why Sub-netting?

- Subnetting lets administrators use IPv4’s 32-bit space more efficiently by creating sub-networks within Class A, B, or C ranges, yielding host counts that match real needs. It also separates large environments into multiple physical networks and broadcast domains to avoid slowdowns. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

## Sub-nets

- A subnet is a “network within a network” (Class A/B/C) created by borrowing host bits to extend the network ID. Class A has an 8-bit network ID, Class B a 16-bit network ID, and Class C a 24-bit network ID; subnetting enables network IDs of arbitrary size. :contentReference[oaicite:3]{index=3}

## Sub-Net Masks

- A **network mask (netmask)** is applied to an IP address to determine whether two addresses are in the same subnet; it uses a bitwise **AND** of the IP and mask. In a 32-bit mask, **1-bits** mark the **network** portion; **0-bits** mark the **host** portion. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

## CIDR Notation

- **CIDR** expresses an address and its mask with a slash and bit count (e.g., `192.168.1.0/24`, where **/24** is the number of mask bits). The bit count varies with how many subnets you create. :contentReference[oaicite:6]{index=6}

## Our Scenario

- Given a Class C network `192.168.1.0` (254 host addresses available), suppose we need **five** networks with **≤30 hosts** each. Borrowing **3 bits** from the host portion yields **2³ = 8** subnets, **6 usable** (subtracting network and broadcast), with **5 host bits** left: **2⁵ = 32** addresses per subnet, **30 usable** hosts—meeting the requirement. :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}

## Summary

- Subnetting is an essential skill for network engineers and forensics/analysis practitioners; this chapter equips you to be conversant with the core ideas. :contentReference[oaicite:9]{index=9}

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
