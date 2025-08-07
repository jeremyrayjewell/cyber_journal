# Cipher Reference #

## SSH Asymmetric Encryption Types & Strengths

![Curve25519 Visualization](https://raw.githubusercontent.com/jeremyrayjewell/cyber_journal/refs/heads/main/experiments/cipher-graphs/Curve25519.png)

**SSH** (Secure Shell) network protocol enables **secure remote access** over an unsecured network. The original SSH protocol was developed in 1995 by Tatu Ylönen in response to password‑sniffing attacks over TCP (Transmission Control Protocol), the foundational protocol on top of which SSH runs. SSH‑2, introduced as a protocol revision in 1998, supersedes the original SSH‑1. **OpenSSH**, developed by the OpenBSD project, is the most widely used open‑source implementation of the SSH protocol. Its tools include `ssh`, `sshd`, `scp`, `sftp`, and `ssh-keygen`, and it comes pre‑installed on most Linux and macOS systems.

**Asymmetric encryption** is a cryptographic method that uses **two separate but mathematically linked keys**. These key pairs create **one‑way trust**, allowing a public key to be shared among multiple users with private keys held individually. This enables authentication and confidentiality with **no shared secret needed**. In SSH, asymmetric encryption is used for **authentication** and the initial **key exchange** that sets up the symmetric cipher, while symmetric encryption protects the **actual data** during the session. This makes asymmetric encryption *critical*.

Key strength is governed by the underlying math: RSA relies on large key lengths, while curve‑based keys (ECDSA, Ed25519) achieve equivalent security with much smaller parameters. Smaller keys mean faster operations and shorter signatures on the wire.

**Some common OpenSSH flags deserve some preliminary explanation:**

- `-o`: use the modern, bcrypt‑protected OpenSSH private‑key format when a passphrase is supplied  
- `-a 100`: number of key‑derivation rounds for the passphrase—crank this up on fast hardware  
- `-b`: bit‑length (RSA/ECDSA); ignored for Ed25519 because the curve is fixed  
- `-C`: comment that shows up in `authorized_keys`  

---

### RSA

Rivest–Shamir–Adleman keys rely on the hardness of factoring large integers. They are the most commonly used type of SSH asymmetric encryption. RSA uses a public‑key cryptosystem to generate a pair of keys: a public key and a private key. The public key is shared with the server, while the private key is kept secret by the user.

On connection, SSH sends the client a random challenge. The client uses its **private key to sign** that challenge, and the server verifies the signature with the client’s public key. If the signature is valid, the client is authenticated.

RSA was invented in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman at MIT. Coincidentally, Clifford Cocks developed an equivalent system in 1973 for British intelligence, but it remained classified. The RSA algorithm is based on the mathematical properties of large prime numbers and the difficulty of factoring their product.

<details>
<summary>How it works</summary>

1) **Key generation: To generate an RSA key pair, you need to follow these steps:**

- Choose two large prime numbers `p` and `q`.  
- Calculate `n = p · q`.  
- Calculate `phi(n) = (p - 1) · (q - 1)`.  
- Choose an integer `e` such that `1 < e < phi(n)` and `gcd(e, phi(n)) = 1`.  
- Calculate `d` such that `e · d ≡ 1 (mod phi(n))`.  
- The public key is `(n, e)` and the private key is `(n, d)`.

2) **Encryption: To encrypt a message using the public key, you need to:**

- Convert the message into a number `m` less than `n`.  
- Calculate `c = m^e mod n`.  
- The encrypted message is `c`.

3) **Decryption: To decrypt an encrypted message using the private key, you need to:**

- Calculate `m = c^d mod n`.  
- The decrypted message is `m`.

</details>

The security of RSA hinges on the practical infeasibility of factoring an integer `n = p · q` when `p` and `q` are large, randomly chosen primes. With current algorithms—most notably the general number field sieve—factoring a 2048‑bit modulus remains beyond even the world’s fastest classical supercomputers. In practice, most organizations now use 3072‑ or 4096‑bit moduli to maintain a comfortable security margin.

Moreover, the choice of primes matters: using “safe primes” or ensuring that `(p - 1)` and `(q - 1)` have large prime factors helps defend against specialized attacks. Finally, although RSA is secure against classical attacks today, large‑scale quantum computers running Shor’s algorithm could factor large integers in polynomial time—so long‑term security may require migration to quantum‑resistant schemes.

- **Cryptographic family**: Integer factorization  
- **Recommended modulus size**: 3072 – 4096 bits (minimum 2048 bits)  
- **Typical signature size**: ~256 – 512 bytes  
- **OpenSSH support**: Since v1.0 (released 1999)  
- **Generation command**:  
   ```bash
   ssh-keygen -t rsa -b 4096 -o -a 100 -f ~/.ssh/id_rsa -C "your@email"
   ```  
- **When to choose**: Broad compatibility with legacy clients and compliance mandates  

---

### DSA

Digital Signature Algorithm (DSA) keys rely on discrete logarithms over prime fields. DSA is the original U.S. federal digital‑signature scheme published by NIST in the 1991 Draft DSS and standardized in FIPS 186 (first issued 1994). In SSH you’ll see it identified by `ssh-dss`. DSA is primarily used for digital signatures to verify the authenticity and integrity of communications.

The DSA algorithm is based on large primes and the discrete‑log problem in a finite field. Like RSA, it uses two keys: a public key and a private key.

<details>
<summary>How it works</summary>

1) **Key generation: To generate a DSA key pair, you need to follow these steps:**

- Choose a large prime `p` and a prime divisor `q` of `(p - 1)`.  
- Select a generator `g` by picking any `h` in `[2, p - 2]` and computing  
  ```  
  g = h^((p - 1) / q) mod p  
  ```  
  ensuring `g > 1`.  
- Choose a private key `x` such that `0 < x < q`.  
- Calculate the public key  
  ```  
  y = g^x mod p  
  ```

2) **Signing: To sign a message using the private key, you need to:**

- Compute  
  ```  
  H = hash(message) mod q  
  ```  
- Choose a random per‑message value `k` such that `0 < k < q`.  
- Calculate  
  ```  
  r = (g^k mod p) mod q  
  ```  
  If `r == 0`, pick a new `k`.  
- Calculate  
  ```  
  s = (k^-1 · (H + x · r)) mod q  
  ```  
  If `s == 0`, pick a new `k`.  
- The digital signature is the pair `(r, s)`.

3) **Verification: To verify a digital signature using the public key, you need to:**

- Compute  
  ```  
  H = hash(message) mod q  
  ```  
- Calculate  
  ```  
  w = s^-1 mod q  
  ```  
- Calculate  
  ```  
  u1 = (H · w) mod q  
  u2 = (r · w) mod q  
  ```  
- Calculate  
  ```  
  v = ((g^u1 · y^u2) mod p) mod q  
  ```  
- If `v == r`, the signature is valid.

</details>

The security of DSA depends on the infeasibility of solving the discrete logarithm problem in a large prime‑order subgroup. In practice, DSA parameters typically use a 2048‑bit prime `p` with a 224‑ or 256‑bit subgroup order `q`, yielding ~112–128 bits of classical security. Unlike RSA, DSA’s strength is capped by the size of `q`, so modern deployments should use `q ≥ 256` bits and SHA‑2 hashing instead of SHA‑1. A critical requirement is a fresh, random `k` for each signature—any reuse or bias exposes the private key. Like all discrete‑log schemes, DSA would be broken by large‑scale quantum computers.

- **Cryptographic family**: Discrete‑logarithm over prime fields  
- **Recommended key size**: 1024 bits (max allowed by OpenSSH; insecure)  
- **Typical signature size**: ~40 bytes (raw) or ~70 – 80 bytes (DER)  
- **OpenSSH support**: Since v2.0 (2000); `ssh-dss` disabled by default in ≥ 7.0  
- **Generation command**:  
   ```bash
   ssh-keygen -t dsa -b 1024 -o -a 100 -f ~/.ssh/id_dsa -C "your@email"
   ```  
- **When to choose**: Only for legacy appliances requiring `ssh-dss`; otherwise use ECDSA or Ed25519  

---

### ECDSA

Elliptic curves are algebraic curves defined by an equation of the form  
```
y² = x³ + a · x + b
```  
where *a* and *b* are constants. They enable efficient point arithmetic while making the discrete‑log problem hard.

Elliptic Curve Cryptography (ECC) leverages these curves over finite fields to secure communications. ECC matches RSA/DSA security with much smaller keys.

Elliptic Curve Digital Signature Algorithm (ECDSA) uses ECC for digital signatures. Security rests on the elliptic‑curve discrete logarithm problem (ECDLP). Proposed by Koblitz (1985) and Miller (1986), ECDSA was standardized in ANSI X9.62 (1998) and NIST FIPS 186‑2 (2000).

<details>
<summary>How it works</summary>

1) **Key generation: To generate an ECDSA key pair, you need to follow these steps:**

- Select domain parameters: elliptic curve and base point `G` of order `n`.  
- Choose a random integer `d` such that `1 ≤ d < n` (your private key).  
- Calculate the public key:  
  ```  
  Q = d · G  
  ```  

2) **Signing: To sign a message, you need to:**

- Compute  
  ```  
  h = hash(message) mod n  
  ```  
- Choose a random `k` such that `1 ≤ k < n`.  
- Calculate  
  ```  
  R = k · G  
  r = R.x mod n  
  ```  
  If `r == 0`, pick a new `k`.  
- Compute  
  ```  
  k_inv = k^-1 mod n  
  ```  
- Calculate  
  ```  
  s = (k_inv · (h + d · r)) mod n  
  ```  
  If `s == 0`, pick a new `k`.  
- Signature is `(r, s)`.

3) **Verification: To verify `(r, s)`, you need to:**

- Ensure `1 ≤ r, s < n`.  
- Compute  
  ```  
  h = hash(message) mod n  
  w = s^-1 mod n  
  u1 = (h · w) mod n  
  u2 = (r · w) mod n  
  ```  
- Calculate  
  ```  
  R' = u1 · G + u2 · Q  
  ```  
- Compute  
  ```  
  v = R'.x mod n  
  ```  
- Signature valid if `v == r`.

</details>

The security of ECDSA rests on ECDLP. Standard curves—P‑256, P‑384, P‑521—offer ~128, 192, and 256 bits of security with small keys. Each signature needs a fresh, random `k`. ECDSA is faster than RSA and DSA but, like all discrete‑log schemes, is vulnerable to quantum attacks.

- **Cryptographic family**: Elliptic curve (NIST P‑256/P‑384/P‑521)  
- **Recommended curve**: P‑256, P‑384, or P‑521  
- **Typical signature size** (DER): ~70 – 142 bytes  
- **OpenSSH support**: Since v5.7 (2011)  
- **Generation command**:  
   ```bash
   ssh-keygen -t ecdsa -b 521 -o -a 100 -f ~/.ssh/id_ecdsa -C "your@email"
   ```  
- **When to choose**: Constrained environments needing strong security with small keys  

---

### Ed25519

Ed25519 is an instance of Edwards‑curve Digital Signature Algorithm (EdDSA) using Curve25519 (prime field 2^255‑19). Introduced in 2011 by Bernstein, Duif, Lange, Schwabe, and Yang, it leverages a constant‑time Montgomery ladder for fast, side‑channel‑resistant arithmetic.

Ed25519 uses SHA‑512 and deterministic nonces (RFC 8032), eliminating RNG risks. Keys are 32 bytes; signatures are 64 bytes. It is faster than ECDSA for comparable security and is the default SSH key type since v9.4 (2021).

<details>
<summary>How it works</summary>

1) **Key generation:**  
- Generate a random 256‑bit seed `sk`.  
- Compute  
  ```  
  h = SHA-512(sk)  
  ```  
- Clamp the lower 32 bytes of `h` to form scalar `d`.  
- Derive public key:  
  ```  
  A = d · B  
  ```

2) **Signing:**  
- Compute  
  ```  
  r = SHA-512(h_high || message) mod L  
  R = r · B  
  S = (r + SHA-512(R || A || message) * d) mod L  
  ```  
- Signature is `(R, S)`.

3) **Verification:**  
- Compute  
  ```  
  h = SHA-512(R || A || message) mod L  
  ```  
- Verify  
  ```  
  S · B == R + h · A  
  ```

</details>

- **Cryptographic family**: Elliptic curve (Curve25519, Edwards form)  
- **Key size**: Fixed (256 bits)  
- **Signature size**: 64 bytes  
- **OpenSSH support**: Since v6.5 (2014); default since v9.4 (2021)  
- **Generation command**:  
   ```bash
   ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "your@email"
   ```  
- **When to choose**: Modern servers, Git hosts, CI pipelines, hardware tokens, strict environments  

---

## Author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)