# Advent of Cyber 2025 – Day 17, 2025-12-17 
Room: CyberChef – Hoperation Save McSkidy  
Category: Encoding / Decoding, Web Analysis  
Skills Practiced: Base64 decoding, XOR, hashing, HTTP header inspection, CyberChef recipe chaining

---

## Summary
On Day 17, thechallenge consists of breaking five sequential “locks” protecting the fortress. Each lock uses a different encoding or obfuscation method that must be reversed using CyberChef and browser developer tools.

The exercise reinforces practical decoding workflows, careful inspection of client-side logic, and disciplined use of CyberChef recipes.

---

## Walkthrough Notes

## Lock 1 – Outer Gate

Guard name identified on the page. Chat messages were Base64 encoded. HTTP headers revealed the “magic question”. Encode the guard name in Base64 → used as username. Encode the magic question in Base64 and send it in chat. Guard replies with a Base64-encoded password. Login logic shows password is Base64 encoded once. Decode the guard’s reply once to obtain plaintext password.

Log in using:
   - Username: Base64-encoded guard name
   - Password: decoded plaintext password

---

## Lock 2 – Outer Wall

Same process as Lock 1. Login logic shows **double Base64 encoding**. Encode guard name (saved from earlier). Encode magic question and retrieve encoded password from guard. Decode the guard’s reply **twice** using From Base64. Log in using encoded username and decoded password.

---

## Lock 3 – Guard House

No magic question required. Page source reveals XOR key: `cyberchef`. Login logic: password is XORed with key, result is then Base64 encoded. Ask the guard for the password (simple request). Guard replies with Base64-encoded data. CyberChef reverse recipe: From Base64, XOR with key `cyberchef`. Output reveals plaintext password. Log in using saved encoded username and decoded password.

---

## Lock 4 – Inner Castle

Login logic uses **MD5 hashing**. Guard’s response decodes to a hash value. Ask the guard for the password. Decode guard’s Base64 response → MD5 hash. Submit the hash to CrackStation. CrackStation returns the plaintext password. Log in with encoded username and cracked password.

---

## Lock 5 – Prison Tower

HTTP headers reveal a **recipe ID**. Login logic changes based on recipe ID.
```
1 → From Base64 → Reverse → ROT13  
2 → From Base64 → From Hex → Reverse  
3 → ROT13 → From Base64 → XOR (key extracted)  
4 → ROT13 → From Base64 → ROT47  
```
Extract guard name and encode it. Identify recipe ID from headers. Build the correct reverse recipe in CyberChef. Apply operations in the exact order specified. Decode the guard’s response to obtain final password and log in successfully.

---

## Key Takeaways
- Encoding is not encryption; all transformations were reversible.
- CyberChef is most powerful when recipes are chained deliberately.
- Browser developer tools are essential for understanding client-side logic.
- XOR encoding can be reversed by applying the same key again.
- Hashes require external intelligence (hash databases) to recover plaintext.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
