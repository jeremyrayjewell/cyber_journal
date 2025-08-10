# Pen-Testing Experiments & Scripts

This directory contains a collection of small, self-contained experiments, utilities, and scripts related to penetration testing, cryptography, and automation.

## Contents

### [cipher-graphs/](cipher-graphs/README.md)
Python-based visualizations of cryptographic algorithms such as RSA, DSA, and Curve25519, using plots and animations to make complex math intuitive.  
**Dependencies:** Python 3.8+, matplotlib, numpy, sympy, pycryptodome, (optional) plotly, mayavi.

### [generate_ssh_summary/](generate_ssh_summary/README.md)
Parses SSH debug logs from `~/ssh-logs/` and outputs a Markdown summary table (`~/ssh-summary.md`) with key connection details.  
**Dependencies:** Python 3.6+.

### [nofiltergpt-chat/](nofiltergpt-chat/README.md)
CLI client for the **NoFilterGPT** API. Reads API key from `.env`, sends prompts, and prints formatted responses.  
**Dependencies:** Python 3.8+, requests, python-dotenv, colorama.

### [ssh-shared-tmux/](ssh-shared-tmux/README.md)
Bash scripts to open an SSH port, start an SSH server, and create a shared `tmux` session for collaborative terminal access. Includes a disconnect script to stop SSH and close the port.  
**Dependencies:** tmux, OpenSSH server (`sshd`), iptables, curl.

---

## Author
**Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
