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

---

## Module 8.5: Hashing  
**Learning Objectives:**  
- Explain hashing and its purpose  
- Identify common hashing algorithms  

**Key Topics:**  
- Produces fixed-length digest from input data  
- Ensures data integrity  
- Algorithms: MD5, SHA-1, SHA-2, SHA-3 

---

## Module 8.6: Increasing Hash Security  
**Learning Objectives:**  
- Recognize methods to strengthen hashes  
- Explain salting and key stretching  

**Key Topics:**  
- **Salting:** adding random values to inputs  
- **Key stretching:** PBKDF2, bcrypt, scrypt, Argon2  
- Prevents rainbow table and brute force attacks 

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
