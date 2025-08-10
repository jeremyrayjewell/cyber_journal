# Pen-Testing Experiments & Scripts

This directory contains a collection of small, self-contained experiments, utilities, and scripts related to penetration testing, cryptography, and automation.

## Contents

### [cipher-graphs/](cipher-graphs/README.md)
Python-based visualizations of cryptographic algorithms such as RSA, DSA, and Curve25519, using plots and animations to make complex math intuitive.

### [generate_ssh_summary/](generate_ssh_summary/README.md)
Parses SSH debug logs from `~/ssh-logs/` and outputs a Markdown summary table (`~/ssh-summary.md`) with key connection details.

### [nofiltergpt-chat/](nofiltergpt-chat/README.md)
CLI client for the **NoFilterGPT** API. Reads API key from `.env`, sends prompts, and prints formatted responses.

### [ssh-shared-tmux/](ssh-shared-tmux/README.md)
Bash scripts to open an SSH port, start an SSH server, and create a shared `tmux` session for collaborative terminal access. Includes a disconnect script to stop SSH and close the port.

### [port-knocking/](port-knocking/README.md)
Stealth SSH access using a knock sequence to temporarily open the SSH port; includes client knock scripts and a sample `knockd` configuration.

---

## Author
**Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
