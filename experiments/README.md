# Experiments & Scripts

This directory contains a collection of small, self-contained experiments, utilities, and scripts related to penetration testing, cryptography, automation, and more. 

## Contents

### [blind_command_injector/](blind_command_injector/)
Python-based blind command injection tool that infers protected values by observing command execution behavior rather than direct output.

### [blind_sqli_extractor/](blind_sqli_extractor/)
Automates boolean-based blind SQL injection in Python.

### [cipher-graphs/](cipher-graphs/)
Python-based visualizations of cryptographic algorithms such as RSA, DSA, and Curve25519, using plots and animations to make complex math intuitive.

### [cmd-injector/](cmd-injector/)
A shell-based command injection tester. 

### [generate_ssh_summary/](generate_ssh_summary/)
Parses SSH debug logs from `~/ssh-logs/` and outputs a Markdown summary table (`~/ssh-summary.md`) with key connection details.

### [lfi-enumerator/](lfi-enumerator/)
A Python-based Local File Inclusion enumerator.

### [nofiltergpt-chat/](nofiltergpt-chat/)
CLI client for the **NoFilterGPT** API. Reads API key from `.env`, sends prompts, and prints formatted responses.

### [port-knocking/](port-knocking/)
Stealth SSH access using a knock sequence to temporarily open the SSH port; includes client knock scripts and a sample `knockd` configuration.

### [session_enumerator/](session_enumerator/)
A lightweight Python utility for enumerating predictable session identifiers in web applications. Designed for educational use, CTF challenges, and controlled security testing.

## [session_injector/}(session_injector/)
Targets applications that trust user-influenced session storage and illustrates how session poisoning can lead to full authentication bypass.

### [ssh-shared-tmux/](ssh-shared-tmux/)
Bash scripts to open an SSH port, start an SSH server, and create a shared `tmux` session for collaborative terminal access. Includes a disconnect script to stop SSH and close the port.

### [directory-enumerator/](directory-enumerator/)
A Python-based HTTP directory enumeration tool (`dir_enum.py`). Supports Basic Auth, built-in common paths, custom wordlists, directory listing detection, colorized output, and verbose mode for headers and body previews. Useful for quickly identifying exposed directories and files during assessments.

---

## Author
**Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
