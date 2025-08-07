#!/usr/bin/env python3
import re
from pathlib import Path

LOG_DIR = Path.home() / "ssh-logs"
SUMMARY_FILE = Path.home() / "ssh-summary.md"

def parse_log(path):
    raw = path.read_text()
    # Host alias: filename before the last date suffix
    host = path.stem.rsplit("-", 3)[0]

    # Build SSH command
    cmd = f"ssh -v {host}"
    m_port = re.search(r"Connecting to [^ ]+ .* port (\d+)", raw)
    if m_port and m_port.group(1) != "22":
        cmd += f" -p {m_port.group(1)}"

    # Determine outcome
    kex_match = re.search(r"debug1: kex: algorithm: ([^ ]+)", raw)
    auth_match = re.search(r"debug1: Authentication succeeded", raw)
    enter_match = "Entering interactive session" in raw
    exit_match = re.search(r"debug1: Exit status 0", raw)

    if auth_match:
        kex = kex_match.group(1) if kex_match else None
        outcome = f"Authentication succeeded; {kex} used" if kex else "Authentication succeeded"
    elif enter_match:
        outcome = "Authentication succeeded (entered session)"
    elif exit_match:
        outcome = "Authentication succeeded (exit status 0)"
    elif "Permission denied" in raw:
        outcome = "Permission denied"
    else:
        outcome = "No clear auth result"

    return host, cmd, outcome


def generate_summary():
    rows = []
    for log in sorted(LOG_DIR.glob("*.log")):
        h, c, o = parse_log(log)
        rows.append((h, c, o))

    content = ["| Host | Command/Flags | Outcome |", "|------|---------------|---------|"]
    content += [f"| {h} | `{c}` | {o} |" for h, c, o in rows]
    SUMMARY_FILE.write_text("\n".join(content))


def main():
    if not LOG_DIR.exists():
        print(f"Log directory {LOG_DIR} does not exist.")
        return
    generate_summary()
    print(f"SSH summary written to {SUMMARY_FILE}")

if __name__ == "__main__":
    main()
