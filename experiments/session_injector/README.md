# session_injector

A generic session poisoning and cross-application session exploitation framework.

This tool targets applications that trust user-influenced session storage and demonstrates how insecure session design can lead to full authentication bypass, including privilege escalation across application boundaries.

![Session Injector Screenshot](session_injector.png)

---

## Overview

`session_injector` is a configurable security testing utility designed to exploit insecure server-side session handling.  
It demonstrates how improperly validated session data can be manipulated to escalate privileges without authentication.

Unlike single-purpose CTF scripts, this tool models two real-world vulnerability classes:

1. **Single-host session poisoning**  
   One application writes unsafe user input into its own session storage and later trusts that data.

2. **Cross-host session poisoning**  
   One application writes arbitrary session data that another colocated application blindly trusts.

Both cases represent critical architectural failures in session design and appear frequently in poorly isolated PHP deployments, monolithic applications, and shared-session microservice environments.

The tool is intended for:

- Educational use  
- CTF challenges  
- Authorized security research  
- Demonstrating session integrity failures  

---

## How It Works

The framework exploits applications that store session data without validating ownership, origin, or integrity.

Two attack models are supported:

### 1. Single-Host Mode
Used when the same application:
- Writes attacker-controlled input into session storage
- Later reads and trusts that data

Attack flow:
1. Establish a valid session
2. Inject crafted session content via a parameter
3. Revisit the same application
4. Detect privilege escalation

This models classic session poisoning vulnerabilities such as newline-based session file injection.

---

### 2. Cross-Host Mode
Used when:
- One application writes to a shared session backend
- Another application trusts the same session data

Attack flow:
1. Establish a session on the injection endpoint
2. Capture the session identifier
3. Inject attacker-controlled key/value pairs into the session
4. Reuse the same session cookie on a different application
5. Detect privilege escalation

This models real-world failures in shared-session architectures, SSO misconfigurations, and poorly isolated auxiliary tools.

---

## Usage

The tool is fully configuration-driven. No target-specific logic is embedded.

### Single-host mode

```bash
python3 session_injector.py \
  --mode single-host \
  --inject-url http://target.example.com/index.php \
  --read-url   http://target.example.com/index.php \
  --user username \
  --password password \
  --param name \
  --payload $'anyone\nadmin 1'
```

What this does:

- Creates a session on the target
- Injects a crafted value into the `name` parameter
- Revisits the same application
- Detects privileged access

---

### Cross-host mode

```bash
python3 session_injector.py \
  --mode cross-host \
  --inject-url http://inject.example.com/index.php \
  --read-url   http://target.example.com/index.php \
  --user username \
  --password password \
  --require-submit \
  --submit-key submit \
  --submit-value 1 \
  --kv admin=1
```

What this does:

- Creates a session on one application
- Injects arbitrary session variables
- Forces reuse of the same session identifier on a second application
- Detects privilege escalation across applications

---

## Command-Line Options

| Option | Description |
|------|------------|
| `--mode` | Attack model: `single-host` or `cross-host` |
| `--inject-url` | URL where the session is created and poisoned |
| `--read-url` | URL where the poisoned session is evaluated |
| `--user` | HTTP Basic Auth username |
| `--password` | HTTP Basic Auth password |
| `--cookie-name` | Session cookie name (default: `PHPSESSID`) |
| `--timeout` | Request timeout in seconds |
| `--verbose` | Print full server responses |

### Single-host mode options

| Option | Description |
|------|------------|
| `--param` | Parameter name that writes to the session |
| `--payload` | Value injected into that parameter |

### Cross-host mode options

| Option | Description |
|------|------------|
| `--kv` | Key=value pair injected into session storage (repeatable) |
| `--require-submit` | Include a form-trigger parameter |
| `--submit-key` | Name of the trigger parameter |
| `--submit-value` | Value of the trigger parameter |

---

## Why This Tool Exists

Most session attacks are taught as isolated tricks.  
This framework models session compromise as a **system-level failure**, where:

- Trust boundaries are broken
- Session ownership is not enforced
- Applications implicitly become authentication authorities for each other

This is the same class of vulnerability responsible for:

- Cross-service authentication bypass
- Shared session store privilege escalation
- Broken SSO implementations
- Compromised internal tooling becoming external attack surfaces

---

## Ethical Notice

This tool is intended solely for:

- Education  
- CTF challenges  
- Authorized security testing  

Do not use it against systems you do not own or do not have explicit permission to test.

---

## Author

Jeremy Ray Jewell  
GitHub: https://github.com/jeremyrayjewell  
LinkedIn: https://www.linkedin.com/in/jeremyrayjewell
