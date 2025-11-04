# CompTIA Security+ (SY0-701) Complete Course & Practice Exam  
## Section 17 – Identity and Access Management (IAM) Solutions  

[Udemy](https://www.udemy.com/course/securityplus/)  
---

## Overview  
Section 17 focuses on Identity and Access Management (IAM), which governs how users are identified, authenticated, and authorized. Learners review IAM frameworks, multifactor authentication, password security, and common password attacks, along with defenses against them.  

---

## Module 17.1: IAM Solutions Overview  
**Learning Objectives:**  
- Define IAM and its importance  
- Recognize goals of IAM solutions  

**Key Topics:**  
- IAM ensures the right individuals access the right resources at the right times  
- Components: identification, authentication, authorization, and accounting (AAA)  
- Supports compliance, security, and operational efficiency  
- **Identity and Access Management (IAM):** ensures the right access for the right people at the right times
	- IAM technologies manage digital identities and access securely
	- IAM secures resource access for authorized users
- **Identification:** claims a username or email as an identity
- **Authorization:** establishes the user's access permissions or levels
- **Accounting/Auditing:** involves monitoring and recording user actions for compliance and security records

---

## Module 17.2: Identity and Access Management (IAM)  
**Learning Objectives:**  
- Explain IAM principles  
- Recognize common IAM technologies  

**Key Topics:**  
- **Identification:** claiming an identity (e.g., username)  
- **Authentication:** verifying identity (passwords, MFA, biometrics)  
- **Authorization:** granting appropriate permissions  
- **Accounting:** auditing access and usage  
- Tools: SSO, federation, directory services (LDAP, Active Directory)  
- **Identity and Access Management (IAM):** systems and processes used to  manage access to information in an organization to ensure that the right individuals have access to the right resources at the right times for the right reasons
	- **Identification:** process where a user claims an identity to a system, typically using a unique identifier like a username or an email address
	- **Authentication:** process of verifying the identity of a user, device, or system and this involves validating the credentials provided by the user against a database of authorized users
	- **Authorization:** process that determines what permissions or levels of access the user has
	- **Accounting:** process of tracking and recording user activities
	 	- detect security incidents
		- find vulnerabilities
		- provide evidence
- **Provisioning and Deprovisioning:** process of creating new user accounts, assigning them appropriate permissions, and providing users with access to systems
- **Identity Proofing:** process of verifying the identity of a user before the account is created
- **Interoperability:** the ability of different systems, devices, and applications to work together and share information
- **Attestation:** process of validating that user accounts and access rights are correct and up-to-date

---

## Module 17.3: Multifactor Authentication (MFA)  
**Learning Objectives:**  
- Define MFA and its categories  
- Recognize the strength of layered authentication  

**Key Topics:**  
- MFA requires two or more factors:  
  - Something you know (password, PIN)  
  - Something you have (token, smart card, phone)  
  - Something you are (biometrics)  
- Increases resilience against credential theft  
- Common in VPNs, cloud logins, and banking systems
- **Multi-Factor Authentication (MFA):** security system that requires more than one method of authentication from independent categories of credentials to verify the user's identity
	- **Knowledge-based Factor:** knowledge-based information the user must provide to authenticate their identity
	- **Possession-based Factor:** something the user phsyically possesses like a smart card, a hardware token like a key fob, or a software token used with a smartphone
		- a software token does the same job as a hard token without needing specific hardware
		- when logging in, the software token produces a one-time passcode for user authentication
		- apps like Google Authenticator or Microsoft Authenticator generate time-based, one-time passcodes
		- the smartphone receives a one-time passcode sent to the user's registered phone or email
	- **Inherence-based Factor:** involves biometric characteristics that are unique to individuals, including fingerprints, facial recognition, or iris scans
		- recently, biometric factors have become more common in MFA systems
	- **Location-based Factor:** involves determining a user's location to help authenticate them
	- **Behavior-based Factor:** recognizing patterns that are typically associated with a user, such as their keystroke patterns, mouse movement, or even the way a user walks down the hallway
- **Single-factor Authentication:** using a single authentication factor to access a user account
- **Two-factor Authentication (2FA):** using two different authentication factors to gain access to a system
- generally, using more authentication types makes a system safer
- most companies will use a multifactor authentication system using 2 or 3 factors
- knowledge-based factors like passwords and PINs are the most common authentication methods
- these password managers can generate different long, strong, and complex passwords for each website or application
- **Passkeys:** users can create and access online accounts without needing to input a password
- when logging in, users unlock their device using their chosen authentication, such as a facial scan or fingerprint  
- MFA methods provide a high level of security than single-factor authentication methods
- each factor adds a comprehensive security approach, making authentication systems robust and multi-layered

---

## Module 17.4: Password Security  
**Learning Objectives:**  
- Explain best practices for password security  
- Recognize policies that strengthen authentication  

**Key Topics:**  
- Enforce strong password complexity and length  
- Encourage passphrases over short, complex strings  
- Regular password changes balanced with usability  
- Storage: hash + salt to protect credentials in databases  
- **Password Security:** measures the password's ability to resist guessing and brute-force attacks
	- **Password Length:** use 12-16 characters for better security
		- more characters exponentially increase password security
			- 4-digit PIN = 10,000 possible combinations (10^4)
			- 5-digit PIN = 100,000 possible combinations (10^5)
			- 8-digit PIN = 100,000,000 possible combinations (10^8)
	- **Password Complexity:** mix uppercase, lowercase, numbers, and symbols
		- more *kinds of* characters exponentially increase password security
			- 4-digit PIN = 10,000 possible combinations (10^4)
			- lowercase, four characters: 26^4 = 456,976 combinations
			- upper & lowercase, four characters: 52^4 = 7,311,616
		- lowercase, uppercase, numbers, special characters
		- **aW3+:** lowercase, uppercae, number, special symbol
 	- **Password Reuse:** using the same password for multiple accounts increases risk
		- password reuse includes using old passwords within one site
	- **Password Expiration:** mandates regular password changes
	- **Password Age:** refers to the length of time a password has been in use
- **Password Managers:** store, generate, and autofill passwords to enhance security
	- **Password Generation:** password managers create unique strong passwords for accounts to prevent reuse and enhance security
	- **Autofill:** password managers autofill login details, sparing users the need to recall or input information manually
	- **Cross-Platform Access:** password managers offer cross-device compatibility, allowing access to passwords from any location or device
	- **Passwordless Authentication:** provides improved security and more user-friendly experience
		- **Biometric Authentication:** verifies uudentity using distinct biological features like fingerprints, facial recognition, or iris scans
		- **One-Time Passwrod (OTP):** code sent to email or phone used to log in or authenticate access
		- **Magic Link:** email that automatically logs a user into a website
		- **Passkey:** serves as an authentication tool that integrates with the browser or operating system	
---

## Module 17.5: Password Attacks  
**Learning Objectives:**  
- Identify common password attack types  
- Explain defenses against them  

**Key Topics:**  
- Attacks: brute force, dictionary, rainbow table, credential stuffing, spraying  
- Defenses: account lockouts, MFA, password complexity, salting and hashing  
- Monitoring for compromised credentials in breaches  
- **Brute Force Attack:** involves trying every possible combination of characters until the correct password is found
	- increasing password complexity
	- increasing password length
	- limiting the number of logn attempts
	- using multifactor authentication
	- using CAPTCHAS
- **Dictionary Attack:** using a list (or 'dictionary') of commonly used passwords and trying them all
	- dictionary attacks can be effective against users who use common, easy-to-guess passwords
- **Password Spraying:** a form of brute force attack that involves trying a small number of commonly used passwords against a large number of usernames or accounts
	- password spraying attacks avoid triggering account lockouts from too many failed login attempts on one account
	- password spraying attacks can be mitigated by using unique passwords and by implementing multifactor authentication
- **Hybrid Attack:** blends brute force and dictionary techniques by using common passwords with variations, such as adding numbers or special characters
	- password must contain an 8-character dictionary word and then append a 6-digit random number at the end

---

## Module 17.6: Single Sign-On (SSO)
- **Single Sign-On (SSO):** authentication process that allows a user to access multiple applications or websites by logging in only once with a single set of credentials
	- SSO works based on a trusted relationship that is established between an application and an Identity Provider
- **Identity Provider (IdP):** system that creates, maintains, and manages identity information for principals while providing authentication services to relying applications within a federation or distributed network
- **Benefits to SSO:** improved user experience, increased productivity, reduced information technology support costs, enhanced security
- **SSO protocols:** LDAP, OAut, SAML
- **Lightweight Directory Access Protocol (LDAP):** used to access and maintain distributed directory information services over an Internet protocol network
	- an organization might use LDAP to form a directory of its employees
	- the LDAP is also used in authentication and serves as a central repository for user information
	- LDAP stores user data for authorization, like group membership and roles
	- **LDAPS:** can support LDAP over SSL or StartTLS, both of which encrypt the data to provide secure transmission
- **Open Authorization (OAuth):** open standard for token-based authentication and authorization that allows an individuals's account information to be used by third-party services without exposing the user's password
	- the OAuth protocol is commonly used for authentication and authorization in RESTful APIs
	- the client app or service registers with the authorization server, provides a redirect URL, and gets an ID and secret
- **Security Assertion Markup Language (SAML):** a standard for logging users into applications based on their sessions in another context
	- SAML allows services to separate from identity providers and removes the need for direct user authentication

---

## Module 17.7: Federation  
- **Federation:** process that allows for the linking of electronic identities and attributes to store information across multiple distinct identity management systems
	- federation works by using the trust relationsips that exist between different systems
	- it acknowledges the need for networks to be open to a wider audience, including partners, suppliers, and customers
	- a supplier or customer can authenticate using their own network credentials
	- **Login initiation:** the user accesses a service or application and chooses to login
	- **Redirection to an identity provider:** the service provider redirects the user to the Identity Provider (IdP) for authentication
	- **Authenticating the user:** after a user submits credentials to the Identity Provider (IdP), it validates the user's identity
	- **Generation of an assertion:** the IdP creates an assertion that includes information about the user's identity
	- **Returning to a service provider:** the user is redirected back to the service provider with the authentication assertion from the Identity Provider (IdP)
	- **Verification and access:** the service provider checks the assertion from a trusted IdP and grants access based on its information
- federation config relies on: SAML, OAuth, OpenID Connect
- federation benefits: simplified user experience, reduced administrative overhead, increased security

---

## Module 17.8: Privileged Access Management (PAM)  
- **Privileged Access Management (PAM):** solutions that helps organizations restrict and monitor privileged access within an IT environment
	- PAM refers to the policies, procedures, and tchnical controls that are used to prevent malicious abuse of privileged accounts
	- components:
		- **Just-In-Time Permissions:** security model where administrative access is granted only when needed for a specific period
		- **Password Vaulting:** technique used to store and manage passwords in a secure environment, such as in a digital vault
		- **Temporal Accounts:** used to provide time-limited access to resources, and they are automatically disabled or deleted after a certain period of time

---

## Module 17.9: Access Control Models
- **Mandatory Access Control (MAC):** employs security labels to authorize user access to specific resources
	- in MAC, if not explicitly allowed, it's considered forbidden for users
- **Discretionary Access Control (DAC):** resource's owner determines which users can access each resource
- **Role-Based Access Control (RBAC):** assigns users to roles and uses these roles to grant permissions to resources
	- role-based access control enforces minimum privileges
- **Rule-based Access Control (RBAC):** access is determined by rules set by the system administrator
	- enables administrators to apply security policies to all users
- **Attribute-based Access Control (ABAC):** uses object characteristics for access control decisions
	- **User Attributes:** user's name, role, organization, ID, or security clearance level
	- **Environment Attributes:** times of access, data location, and current organization's threat level
	- **Resource Attributes:** file creation date, resource owner, file name, and data sensitivity
- **Time-of-day restrictions:** controls restrict resource access based on request times
- **Implementation/Principle of least privilege:** granting users the minimum access required for their tasks, without extra privileges
	- least privilege reduces the risk of an account being misused if compromised by a threat actor
	- the least privilege requires continually reviewing user permissions to prevent permission creep
	- **Permission or Authorization Creep:** occurs when a user gains excessive rights during their career progressino in the company

---
## Module 17.10: Assigning Permissions  
- **Usernames, Passwords, Biometrics**
- **Privileges**
- **Principle of Least Privilege:** a user should only have the minimum access rights needed to perform their job functions and tasks, and nothing additional or extra
- **Microsoft Account:** free online account that you can use to sign in to a variety of Microsoft services
- **User Account Control (UAC):** a mechanism designed to ensure that actions requiring adminstrative rights are explicitly authorized by the user
- access control and permissions can also apply to groups of users
- setting permissions at the foler level applies those permissions to all files within that folder
	- right click on a file/folder, select 'properties', navigate to the 'security' tab
- always ensure to only give out the necessary permissions

___

## Completion Status  
- All Section 17 materials reviewed  
- [Flashcards created for IAM concepts, MFA categories, password best practices, and attack defenses](https://jeremyrayjewell-flashcards.netlify.app/security-plus-dion.html#deck=17)     

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)  
