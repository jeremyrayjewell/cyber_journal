# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 8 – Cryptographic Solutions  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 8 introduces cryptographic solutions that ensure confidentiality, integrity, authenticity, and non-repudiation of data. Learners compare symmetric and asymmetric encryption, study hashing techniques, explore PKI and digital certificates, and review emerging concepts like blockchain and obfuscation.  

---

## Module 8.1: Cryptographic Solutions Overview  
**Learning Objectives:**  
- Define cryptography and its functions in security  
- Recognize the four core goals of cryptography  

**Key Topics:**  
- Confidentiality, integrity, authenticity, non-repudiation  
- Applications: secure communication, digital signatures, certificates 
- **Cryptography:** practice and study of writing and solving codes to hide the true meaning of the information
- **Encryption:** process of converting ordinary information (plaintext) into an unintelligible form (ciphertext)
- data at rest: inactive data that is being archived
- data in transit: data that moves across the network, resides inside RAM, or moves to and from the processor
- data in use: data undergoing a current constant state of change
- ROT13
- A cipher is an algorithm that performs the cnryption or decryption
- Algorithms: mathematical function
- Encryption strength comesf rom the key, not the algorithm
- Key: essential piece of information that determines the output of a cipher; the 'key' to security inside encryption is the actual key itself
	- use larger key lengths and rotate keys frequently
	- the length of a key is proportional to the level of security it provides
	- regularly changing cryptographic keys is a best practice
	- most encryption algorithms are open-source and publicly accessible
	- store in secure hardware modules, encrypt keys when at rest, transmit keys securely when used
	- limit key access to regular audits and monitoring
- asymmetric algorithms: use a pair of keys, a public key for encryption and a private key for decryption
- symmetric algorithms: use the same key for both encryption and decryption

---

## Module 8.2: Symmetric vs. Asymmetric  
**Learning Objectives:**  
- Compare symmetric and asymmetric encryption  
- Identify advantages and limitations of each  

**Key Topics:**  
- **Symmetric:** single shared key; fast, but requires secure key distribution  
- **Asymmetric:** public/private key pairs (different than one another); enables key exchange, slower performance  
- Use together in hybrid solutions (e.g., SSL/TLS) 
- **Symmetric Algorithm (Private Key):** encryption algorithm in which both the sender and the receiver must know the same shared secret using a privately held key
- **Asymmetric Algorithm (Public Key):** encryption algorithm where different keys are used to encrypt and decrypt the data	
	- Diffie-Hellman
	- RSA (Ron Rivest, Adi Shamir, and Leonard Adleman)
	- Elliptic Curve Cryptography (ECC)
- **Hybrid Implementation:** utilizes asymmetric encryption to securely transfer a private key that can then be used with symmetric encryption
- algorithms can also be classified as **stream cipher** or **block cipher**:
	- stream cipher: utilizes a keystream generator to encrypt data bit by bit using a mathematical XOR function to create the ciphertext
	- block cipher: breaks the input into fixed-length blocks of data and performs the encryption on each block; typically of 64, 128, or 256 bits, rather than one bit at a time

---

## Module 8.3: Symmetric Algorithms  
**Learning Objectives:**  
- Identify common symmetric algorithms  
- Recognize their use cases  

**Key Topics:**  
- Examples: AES, DES, 3DES, RC4  
- Applications: disk encryption, VPNs, bulk data encryption 
- **Symmetric Algorithm:** method of encryption where the same key is used for both encryption and decryption of data
	- **Data Encryption Standard (DES):** breaks the input into 64-bit blocks and uses transposition and substitution to create ciphertext using an effective key strength of only 56-bits
	- **Triple DES (3DES):** uses three se[arate symmetric keys to encrypt, decrypt, then encrypt the plaintext into ciphertext in order to increase the strength of DES
	- **International Data Encryption Algorithm (IDEA):** symmetric block cipher which uses 64-bit blocks to encrypt plaintext into ciphertext
	- **Advanced Encryption Standard (AES):** symmetric block cipher that uses 128-bit, 192-bit, or 356-bit blocks and a matching encryption key size to encrypt plaintext into ciphertext 
	- **Blowfish:** symmetric block cipher that uses 64-bit blocks and a variable length encryption key to encrypt plaintext into ciphertext
	- **Twofish:** provides the ability to use 128-bit blocks in its encryption algorithm and uses 128-bit, 192-bit, or 256-bit encryption keys
	- **Rivest Ciphers (RC4, RC5, RC6):** RC Cipher Suite created by Ron Rivest, a cryptographer who's created six algorithms under the name RC which stands for the Rivest Cipher
		- **RC4:** symmetric stream cipher using a variable key size from 40-bits to 2048-bits that is used in SSL and WEP
		- **RC5:** symmetric block cipher that uses key sizes up to 2048-bits
		- **RC6:** symmetric block cipher that was introduced as a replacement for DESs but AES was chosen instead

---

## Module 8.4: Asymmetric Algorithms  
**Learning Objectives:**  
- Identify asymmetric algorithms  
- Explain how they provide secure communication  

**Key Topics:**  
- Examples: RSA, ECC, Diffie-Hellman, ElGamal  
- Use in key exchange, digital signatures, email encryption 
- **Asymmetric Algorithm:** does not require a shared secret key, often referred to as public ket cryptography since their key is considered to be freely and openly available to the public
	- Confidentiality, Integrity, Authentication, Non-repudiation
	- **Digital Signature:** a hash digest of a message encrypted with the sender's private key to let the recipient know the document was created and sent by the person claiming to have sent it
- **Specific asymmetric algorithms:**
	- **Diffie-Hellman (DH):** used to conduct key exchanges and secure key distribution over an unsecure network; used for the key exchange inside of creating a VPN tunnel establishment as part of IPSec
	- **Rivest-Shamir-Adleman (RSA):** asymmetric algorithm that relies on the mathematical difficulty of factoring large prime numbers; can support key sizes between 1024-bits and 4096-bits
	- **Elliptic Curve Cryptography (ECC):** heavily used in mobile devices and it's based on the algebraic structure of elliptical curves over finite fields to define its keys; ECC with a 256-bit key is just as secure as RSA with a 2048-bit key; ECC is most commonly used for mobile devices and low-power computing devices
	- **Elliptic Curve Diffie-Hellman Ephemeral (ECDHE):** uses a different key for each portion of the key establishment process inside the Diffie-Hellman key exchange

---

## Module 8.5: Hashing  
**Learning Objectives:**  
- Explain hashing and its purpose  
- Identify common hashing algorithms  

**Key Topics:**  
- Produces fixed-length digest from input data  
- Ensures data integrity  
- Algorithms: MD5, SHA-1, SHA-2, SHA-3 
- **Hashing:** one-way cryptographic function that takes an input and produces a unique message digest as its output; another unique thing about a hash digest is that they are always the same length
	- **MD5:** creates a 128-bit hash value that is unique to the input file
		- **collision:** two files having the exact same resulting hash digest becaue the MD5 output is only 128 bits long
	- **Secure Hash Algorithm (SHA) families:** each version of SHA performs a different number of rounds of mathematical computations to create the hash digest (~64-80 rounds in SHA-1 and SHA-2)
		- **SHA-1:** creates a 160-bit hash digest, which significantly reduces the number of collisions that occur
		- **SHA-2:** functions that contain longer hash digests
			- **SHA-224, SHA-256, SHA-348, SHA-512**
		- **SHA-3:** newer (fundamentally different!) family of hash functions, and its hash digest can go between 224 bits and 512 bits (like SHA-2), but it uses 120 rounds of computations to provide more security
	- **RACE Integrity Primitive Evaluation Message Digest (RIPEMD):** comes in 160-bit (most common: *RIPEMD-160*), 256-bit, nd 320-bit versions	
		- **RIPEMD-160:** open-source hashing algorithm that was created as a competitor to the SHA family, but not as poopulat
	- **Hash-based Message Authentication Code (HMAC):** used to check the integrity of a message and provide some level of assurance that its authenticity is real; *paired with other algorithms*
		- **HMAC-MD5, HMAC-SHA1, HMAC-SHA256**
- **Digital Signature:** created by hashing a file and then taking that resulting hash digest and encrypting it with a private key; *creates non-repudiation*
	- to practically use digital signatures, we will use either DSA, RSA, or an elliptic curve cryptogtaphy version of either DSA or SHA
- **Digital Security Standard (DSS):** used by the US federal government; relies upon a 160-bit message digest created by the Digital Security Algorithm
	- most commerical entities will rely in RSA instead because it tends to be faster and multi-use
- **Code Signing:** the process of digitally signing software or code using a cryptographic certificate to verify two things: authenticity and integrity

---

## Module 8.6: Increasing Hash Security  
**Learning Objectives:**  
- Recognize methods to strengthen hashes  
- Explain salting and key stretching  

**Key Topics:**  
- **Salting:** adding random values to inputs  
- **Key stretching:** PBKDF2, bcrypt, scrypt, Argon2  
- Prevents rainbow table and brute force attacks 
- Hashing is a common method of storing passwords inside systems
- **Pass the Hash Attack:** hacking technique that allows the attacker to authenticate to a remote server or service by using the underlying hash of a user's password instead of requiring the associated plaintext password
-

---

## Module 8.7: Public Key Infrastructure (PKI)  
**Learning Objectives:**  
- Define PKI and its components  
- Explain trust models in PKI  

**Key Topics:**  
- Certificate Authorities (CAs), Registration Authorities (RAs), certificate revocation  
- Hierarchical vs. web-of-trust models  
- Used in SSL/TLS, VPNs, secure email 

---

## Module 8.8: Digital Certificates  
**Learning Objectives:**  
- Define digital certificates and their role  
- Recognize certificate contents  

**Key Topics:**  
- Certificates bind identities to public keys  
- Contain subject, issuer, validity dates, public key, signature  
- Used in authentication, encryption, integrity checks 

---

## Module 8.9: Exploring Digital Certificates  
**Learning Objectives:**  
- Examine details inside certificates  
- Recognize key fields and their purposes  

**Key Topics:**  
- Fields: subject, issuer, serial number, validity, extensions  
- Role in verifying identity and trust chains 

---

## Module 8.10: Blockchain  
**Learning Objectives:**  
- Define blockchain technology  
- Explain its relation to cryptography  

**Key Topics:**  
- Distributed ledger with chained blocks  
- Provides integrity, transparency, tamper resistance  
- Applications: cryptocurrency, smart contracts, supply chain tracking 

---

## Module 8.11: Encrption Tools  

---

## Module 8.12: Obfuscation  
**Learning Objectives:**  
- Define obfuscation as a security method  
- Recognize use cases  

**Key Topics:**  
- Hiding data or making code harder to interpret  
- Examples: code obfuscation, data masking, steganography  
- Adds complexity to delay attackers

---

## Module 8.13: Crpyotgraphic Attacks  

---

## Completion Status  
- All Section 8 materials reviewed  
- Flashcards created for algorithms, PKI components, certificate fields, and hash hardening techniques  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
