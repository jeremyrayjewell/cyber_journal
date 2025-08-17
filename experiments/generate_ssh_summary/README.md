# SSH Summary Generators

Python utilities that turn raw SSH debug logs into Markdown tables for quick review and analysis.  
They help track experiments on port-knocking, authentication scenarios, and algorithm negotiation.

---

## Features

### `generate_ssh_summary.py`
- Parses logs from **scenario-based experiments** (e.g., preknock, postknock, postclose).
- Extracts key session details:
  - Host
  - Scenario
  - Timestamp
  - Outcome
  - Notes
  - Optional timing fields (`elapsed`, `exit code`).
- Outputs a Markdown table (`~/ssh-summary.md`) for your weekly notes.

### `generate_ssh_algos_summary.py`
- Parses logs from **algorithm negotiation experiments** (created with `ssh -vvv`).
- Extracts negotiated algorithms:
  - KEX (Key Exchange)
  - HostKey type
  - Client→Server cipher/MAC
  - Server→Client cipher/MAC
  - (Optional) elapsed/exit if present in logs.
- Outputs a Markdown table you can paste under **Results** in weekly SSH notes.

---

## Dependencies

- Python 3.6+
- Standard library (`pathlib`, `re`, `argparse`, `os`)
- No third-party packages required

*(Earlier versions of this project used `pandas`, but the current scripts no longer require it.)*

---

## Requirements

- SSH debug logs located under `~/ssh-logs/` by default
- Filenames that identify the profile/scenario, e.g.:
  - `kali-preknock-ssh-2025-08-10.log`
  - `baseline-2025-08-18T12:34:56.log`
- `chmod +x` permission on the scripts if run directly

---

## Usage

From the `experiments/generate_ssh_summary` directory:

### Scenario / Port-Knocking Experiments
```bash
chmod +x generate_ssh_summary.py
./generate_ssh_summary.py
cat ~/ssh-summary.md

---

## Author
Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
