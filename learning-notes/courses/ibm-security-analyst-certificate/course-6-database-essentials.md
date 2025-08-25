# IBM Cybersecurity Analyst Professional Certificate  
## Course 6 – Databases and Database Vulnerabilities  

[Coursera](https://www.coursera.org/learn/database-essentials-and-vulnerabilities/home/module/1)  
---

## Overview  
Course 6 provides an in-depth study of databases, their management, and vulnerabilities. Learners gain hands-on experience with relational and non-relational databases, Structured Query Language (SQL), user roles and permissions, backup strategies, and security controls. The course emphasizes data protection techniques (encryption, hashing, masking, tokenization), auditing models, and the prevention of injection vulnerabilities (SQL injection, OS command injection). Labs include working with MySQL in Skills Network Labs, designing entity-relationship (ER) models, performing SQL queries, managing user roles, and exploring attack simulations.  

---

## Module 1: Database Fundamentals  
This module introduces databases, their types, and the fundamentals of relational models.  

**Learning Objectives:**  
- Define databases, DBMS, and their functions  
- Compare relational vs non-relational (NoSQL) databases  
- Explain entities, attributes, primary keys, and foreign keys  
- Construct ER diagrams to model relationships  
- Identify advantages and limitations of relational databases  

**Key Topics & Details:**  
- **Databases & DBMS:** Databases store, retrieve, and modify data; DBMS manages data access and querying.  
- **Relational Databases:** Structured tables with rows/columns, ACID compliance, reduced redundancy, strong backup support. Examples: MySQL, PostgreSQL, Oracle, IBM Db2, SQL Server. Cloud RDBMS: AWS RDS, Google Cloud SQL, IBM Db2 on Cloud, Azure SQL.  
- **NoSQL Databases:** Schema-less, flexible, optimized for scale and speed. Types include key-value (Redis, DynamoDB), document (MongoDB, CouchDB), column-based (Cassandra, HBase), and graph (Neo4j, CosmosDB). Useful for IoT, big data, social media.  
- **ER Diagrams:** Entities = tables, attributes = columns, PK uniquely identifies rows, FK links tables. Example: Library DB with Books, Authors, Borrowers.  
- **Lab:** Car Dealership schema — identify tables, PKs, FKs, and relationships.  

---

## Module 2: SQL Basics and Database Management  
This module covers SQL operations and database administration practices.  

**Learning Objectives:**  
- Retrieve and manipulate data using SQL (SELECT, INSERT, UPDATE, DELETE)  
- Apply WHERE clauses, predicates, and comparison operators  
- Use COUNT, DISTINCT, and LIMIT functions  
- Configure roles, permissions, and backups  
- Differentiate DDL, DML, and DCL categories  

**Key Topics & Details:**  
- **DML Commands:**  
  - SELECT: retrieve columns/rows with WHERE, operators (`=`, `!=`, `<`, `>`, `<=`, `>=`).  
  - INSERT: add rows to a table (single or multiple).  
  - UPDATE: modify data values with conditions.  
  - DELETE: remove rows; without WHERE, all rows are deleted.  
- **Expressions:** COUNT (# of rows), DISTINCT (remove duplicates), LIMIT (restrict results).  
- **Permissions:** Database, system, and object privileges. GRANT, REVOKE, DENY manage user rights. Roles group permissions for efficiency. Public role = default.  
- **SQL Categories:**  
  - DDL (schema definition: CREATE, DROP, ALTER, TRUNCATE).  
  - DML (data operations: INSERT, UPDATE, DELETE, SELECT).  
  - DCL (security: GRANT, REVOKE).  
- **Database Management:** Import/export data via SQL Server Import Wizard, SSIS, or OPENROWSET. Reporting tools: Crystal Reports, Jaspersoft, ClearPoint.  
- **Backups:**  
  - Physical (copy of directories, data, logs)  
  - Logical (tables, schemas, procedures)  
  - Methods: Full, Differential, Incremental, Virtual  
  - Tools: ScaleGrid, Cyber Shield, Backup Ninja, SQL Safe Backup  
- **Lab:** Perform basic SQL queries and database backups in MySQL via phpMyAdmin.  

---

## Module 3: Database Security and Data Protection  
This module introduces data classification, types, and protection measures.  

**Learning Objectives:**  
- Identify data types (trade secrets, IP, legal, financial, human-readable, non-human-readable)  
- Classify data as sensitive, confidential, restricted, private, public, or critical  
- Apply encryption, hashing, masking, tokenization, and obfuscation  
- Enforce least privilege and RBAC in user management  
- Implement auditing and monitoring practices  

**Key Topics & Details:**  
- **Data Types:**  
  - Trade secrets (business strategies, processes)  
  - Intellectual property (patents, copyrights, trademarks)  
  - Legal data (contracts, case files)  
  - Financial data (bank records, payroll, taxes)  
  - Human-readable (emails, spreadsheets) vs Non-human-readable (logs, binaries)  
- **Data Classification:** Sensitive, confidential, restricted, private, critical, public. Guides prioritization of protections.  
- **Protection Techniques:**  
  - Encryption (AES, RSA) for data at rest/in transit  
  - Hashing (SHA-256) for integrity  
  - Masking/tokenization for PII (personally identifiable information)  
  - Obfuscation for source code protection  
- **User Management:** Configure accounts, enforce password policies, assign roles, monitor logs.  
- **Auditing Models:** Continuous monitoring, separation of duties, access reviews.  
- **Lab:** Configure MySQL user access, enforce policies, test encryption and permissions.  

---

## Module 4: Injection Vulnerabilities  
This module focuses on database exploitation techniques and defenses.  

**Learning Objectives:**  
- Describe injection vulnerabilities and their risks  
- Differentiate OS command injection and SQL injection  
- Apply best practices for preventing injection attacks  
- Explore secure coding, parameterized queries, and input validation  

**Key Topics & Details:**  
- **OS Command Injection:** Attackers execute unauthorized system commands via unsanitized inputs.  
- **SQL Injection:**  
  - Examples: `' OR '1'='1' --` bypasses authentication; UNION queries extract data.  
  - Impacts: data theft, modification, privilege escalation, denial of service.  
  - Prevention: Prepared statements, parameterized queries, least privilege, web application firewalls (WAF).  
- **Other Injections:** XML injection, LDAP injection.  
- **Lab:** Exploit SQL injection in a controlled environment, then apply fixes with input sanitization and parameterization.  

---

## Final Project: Secure Online Retail Database System  
The capstone project integrates skills across modules. Learners secure an online retail database by designing schemas, applying SQL queries, enforcing permissions, configuring backups, and protecting against injection vulnerabilities.  

**Project Tasks:**  
- Design schema with ER diagrams  
- Populate and query database with SQL  
- Configure roles and permissions with GRANT/REVOKE  
- Apply encryption, hashing, and auditing  
- Simulate injection attacks and implement defenses  

---

## Supplementary Projects  
- **ER Diagram Design** – Car Dealership schema lab (Module 1)  
- **SQL Query Practice** – SELECT, COUNT, DISTINCT, LIMIT, INSERT, UPDATE, DELETE (Module 2)  
- **Database Backup Lab** – Full, differential, incremental, and virtual backups in MySQL (Module 2)  
- **User Access Lab** – Manage roles and permissions, enforce RBAC (Module 3)  
- **Injection Exploitation & Mitigation** – SQL injection attack and defense lab (Module 4)  
- **Final Project** – Secure Online Retail Database System design and hardening  

---

## Completion Status  
- All modules completed  
- All videos, readings, and labs completed  
- All graded assignments and final project submitted with perfect scores (100%)  

---

**Author:** Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
