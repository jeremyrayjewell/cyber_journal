# Advent of Cyber 2025 – Day 20, 2025-12-20 
**Room:** Race Conditions – Toy to The World \
**Category:** Web Application Security  \
**Skills Practiced:** Race condition exploitation, Burp Suite Repeater, concurrent request analysis, transaction logic abuse

---

## Summary
Day 20 focused on identifying and exploiting a race condition vulnerability in a web-based checkout system. TBFC’s limited-edition SleighToy was oversold despite a fixed stock limit, indicating a failure to correctly handle concurrent transactions. By capturing a legitimate checkout request and replaying it simultaneously using Burp Suite’s parallel Repeater execution, the application’s lack of atomic transaction handling was exploited. This allowed multiple purchases to succeed before inventory values were updated, pushing stock counts into negative values and revealing embedded flags. This exercise demonstrated how even millisecond-level timing flaws can lead to serious business logic vulnerabilities in real-world systems.
  
---

## Walkthrough Notes

### 1. Environment Setup

Both the AttackBox and Target Machine were started. Firefox was configured to proxy traffic through **Burp Suite** using **FoxyProxy**, and Burp was launched as a **temporary in-memory project**. Intercept was explicitly turned off to allow normal browsing while still recording traffic for later replay.

---

### 2. Legitimate Checkout Request

The web application was accessed at `http://MACHINE_IP`. Login credentials:
- Username: attacker
- Password: attacker@123
On the dashboard, the SleighToy Limited Edition item was shown with a stock of 10 units. A normal purchase flow was completed:
- Add to cart
- Checkout
- Confirm & Pay
The application returned a successful order confirmation, establishing a valid baseline request.

---

### 3. Capturing the Checkout Request

In Burp Suite:
- The POST request to /process_checkout was located under **Proxy → HTTP history**
- This request was sent to **Repeater**
This request represented a single valid checkout transaction, including session cookies and CSRF tokens.

---

### 4. Parallel Request Execution (Race Condition Exploit)

Inside Burp Repeater:
- The request tab was grouped into a **Repeater tab group**
- The request was duplicated **15 times**, exceeding available stock
- The **Send group in parallel (last-byte sync)** option was used
This forced the server to process multiple identical checkout requests **at the same time**, exploiting a timing window between:
- stock availability check
- stock deduction and order confirmation
Because these steps were not atomic, multiple purchases succeeded before inventory was updated.

---

### 5. Exploit Verification

After sending the requests in parallel:
- The web interface showed multiple confirmed orders
- The SleighToy stock value dropped below zero
- A flag appeared once the stock became negative
This confirmed a successful race condition exploitation.

---

### 6. Repeating the Attack on a Second Product

The same process was repeated for **Bunny Plush (Blue)**:
- Legitimate purchase captured
- Checkout request duplicated in Repeater
- Parallel execution triggered overselling
Again, the stock value went negative, revealing a second flag.

---

## Key Takeaways

- Race conditions arise when shared resources are modified without proper synchronization
- Stock checks and stock updates must occur within atomic transactions
- Parallel request execution can bypass business logic constraints
- Burp Suite Repeater is effective for simulating high-speed concurrent attacks
- Business logic flaws can be as damaging as traditional exploits
- Simple mitigations (atomic DB operations, idempotency keys, rate limiting) can prevent entire attack classes

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
