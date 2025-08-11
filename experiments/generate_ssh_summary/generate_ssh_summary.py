#!/usr/bin/env python3
"""
generate_ssh_summary.py — summarize SSH logs into ~/ssh-summary.md

Conventions this script expects:
  ~/ssh-logs/
    <host>-<scenario>-ssh-YYYY-MM-DD[_HH-MM].log

Examples:
  kali-preknock-ssh-2025-08-10.log
  kali-postknock-ssh-2025-08-10_16-02.log
  bandit0-session-ssh-2025-08-07.log

It will ignore non-SSH logs (e.g., *-nc-*.log, *-knock-*.log) automatically.
"""

import os, re, sys, glob, time
from datetime import datetime

LOG_DIR = os.path.expanduser("~/ssh-logs")
OUT_MD  = os.path.expanduser("~/ssh-summary.md")

# Accept only SSH logs that follow the naming convention above.
SSH_NAME_RE = re.compile(
    r'^(?P<host>[^-]+)-(?P<scenario>[^-]+)-ssh-(?P<date>\d{4}-\d{2}-\d{2})(?:_(?P<hm>\d{2}-\d{2}))?\.log$'
)

# Simple classifiers
def classify(text: str):
    t = text
    # Transport-level failures
    if ("No route to host" in t or
        "Connection timed out" in t or
        "Operation timed out" in t or
        "Connection timedout" in t or  # some nc typos
        "Connection refused" in t or
        "kex_exchange_identification: banner line contains" in t):
        return "Network/transport failure"
    # Auth failures
    if "Permission denied" in t:
        return "Authentication failed"
    if "Auth cancelled" in t or "Too many authentication failures" in t:
        return "Authentication failed"
    # Success signals
    if "Authenticated to " in t or "Last login:" in t or "Welcome to" in t:
        return "Authentication succeeded (entered session)"
    # Host key issues
    if "REMOTE HOST IDENTIFICATION HAS CHANGED" in t:
        return "Host key changed (blocked)"
    if "WARNING: POSSIBLE DNS SPOOFING" in t:
        return "Host key mismatch (warning)"
    # Fallback
    return "No clear auth result"

def extract_kex(text: str):
    # Try a few patterns commonly seen in OpenSSH -vvv output
    m = re.search(r'kex: algorithm: ([^\s]+)', text)
    if m: return m.group(1)
    m = re.search(r'KEX algorithms?:\s*(.*)', text)
    if m: return m.group(1).strip()
    m = re.search(r'kex_exchange_identification', text)
    if m: return "kex_exchange_identification"
    return None

def parse_timestamp_from_name(date_str, hm_str):
    try:
        if hm_str:
            ts = datetime.strptime(f"{date_str} {hm_str}", "%Y-%m-%d %H-%M")
        else:
            ts = datetime.strptime(date_str, "%Y-%m-%d")
        return ts
    except Exception:
        return None

def main():
    if not os.path.isdir(LOG_DIR):
        print(f"No log dir: {LOG_DIR}", file=sys.stderr)
        open(OUT_MD, "w").write("| Host | Scenario | Time | Outcome | Notes |\n|------|----------|------|---------|-------|\n")
        print(f"SSH summary written to {OUT_MD}")
        return

    rows = []
    for path in glob.glob(os.path.join(LOG_DIR, "*.log")):
        name = os.path.basename(path)
        m = SSH_NAME_RE.match(name)
        if not m:
            # ignore non-SSH logs like *-nc-*.log or *-knock-*.log
            continue

        host = m.group("host")
        scenario = m.group("scenario")
        date_str = m.group("date")
        hm_str   = m.group("hm")

        # Read file (cap size in case of huge logs)
        try:
            with open(path, "r", errors="ignore") as f:
                text = f.read()
        except Exception:
            continue

        outcome = classify(text)
        kex = extract_kex(text)
        notes = f"KEX {kex}" if kex else ""

        # Timestamp: from filename if present, else file mtime
        ts_from_name = parse_timestamp_from_name(date_str, hm_str)
        if ts_from_name is None:
            ts = datetime.fromtimestamp(os.path.getmtime(path))
        else:
            ts = ts_from_name
        timestr = ts.strftime("%Y-%m-%d %H:%M")

        rows.append((ts, host, scenario, timestr, outcome, notes))

    # Sort by timestamp
    rows.sort(key=lambda r: r[0])

    # Emit Markdown
    lines = []
    lines.append("| Host | Scenario | Time | Outcome | Notes |")
    lines.append("|------|----------|------|---------|-------|")
    for _, host, scenario, timestr, outcome, notes in rows:
        # keep Notes short
        notes_disp = notes if notes else ""
        lines.append(f"| {host} | {scenario} | {timestr} | {outcome} | {notes_disp} |")

    with open(OUT_MD, "w") as out:
        out.write("\n".join(lines) + "\n")

    print(f"SSH summary written to {OUT_MD}")

if __name__ == "__main__":
    main()
