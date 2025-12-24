# Advent of Cyber 2025 – Day 23, 2025-12-23
**Room:** AWS Security – S3cret Santa \
**Category:** Cloud Security / IAM Enumeration  \
**Skills Practiced:** AWS CLI usage, IAM permission enumeration, role assumption, S3 enumeration, cloud privilege escalation fundamentals

---

## Summary
Day 23 introduced **basic AWS security enumeration** from an attacker’s perspective using exposed credentials. The lab focused on understanding how **IAM users, roles, and policies** interact, and how limited permissions can still be chained together to access sensitive cloud resources. By enumerating IAM permissions, identifying an assumable role, and leveraging temporary credentials via AWS STS, access was escalated from a low-privilege user to an S3-enabled role, ultimately allowing sensitive data to be retrieved from an S3 bucket.

---

## Walkthrough Notes

### 1. Credential Validation and Identity Enumeration

The provided AWS credentials were already configured in the environment under ~/.aws/credentials. To validate that the credentials were functional and identify the associated account and user, the following command was executed: `aws sts get-caller-identity`. This confirmed:
- The credentials were valid
- The AWS account ID
- The IAM user `sir.carrotbane`
This step established a confirmed foothold into the target AWS account.

---

### 2. IAM Fundamentals Review

The lab reviewed the four core IAM components:
- Users – long-lived identities with credentials
- Groups – collections of users with shared permissions
- Roles – assumable, temporary identities
- Policies – JSON documents defining permissions
Understanding the distinction between users and roles was critical for the later privilege escalation.

---

### 3. Enumerating User Permissions

User enumeration was performed with: `aws iam list-users`. Next, permissions assigned directly to sir.carrotbane were examined. Inline policies were identified using: `aws iam list-user-policies --user-name sir.carrotbane`. The inline policy was retrieved and reviewed: `aws iam get-user-policy --user-name sir.carrotbane --policy-name <POLICY_NAME>`. The policy allowed extensive IAM read-only enumeration and, critically, the action: `sts:AssumeRole`. This revealed a potential path to privilege escalation.

---

### 4. Enumerating and Assuming Roles

Available roles in the account were listed: `aws iam list-roles`. A role named bucketmaster stood out, as its trust policy allowed it to be assumed by `sir.carrotbane`. The role’s inline policy was inspected: `aws iam get-role-policy --role-name bucketmaster --policy-name BucketMasterPolicy`. This policy granted permissions related to **Amazon S3**, including:
- Listing all buckets
- Listing specific bucket contents
- Retrieving objects from a specific bucket
To gain these permissions, the role was assumed using AWS STS: `aws sts assume-role --role-arn arn:aws:iam::<ACCOUNT_ID>:role/bucketmaster --role-session-name TBFC`. Temporary credentials were exported as environment variables, and identity verification confirmed the role assumption.

---

### 5. Enumerating S3 Buckets and Exfiltrating Data

With the bucketmaster role active, S3 buckets were enumerated: `aws s3api list-buckets`. An interesting bucket, easter-secrets-123145, was identified. Its contents were listed: `aws s3api list-objects --bucket easter-secrets-123145`. A file named cloud_password.txt was discovered and retrieved: `aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt`. The file contained the final secret, demonstrating successful access to sensitive cloud data.

---

## Key Takeaways

- Cloud breaches often begin with exposed credentials, not exploits
- IAM read-only permissions can still be dangerous
- `sts:AssumeRole` is a common and powerful escalation vector
- Temporary credentials enable lateral movement without permanent changes
-  Misconfigured IAM roles can expose critical cloud resources
- S3 buckets frequently contain sensitive data and are common targets

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
