#!/usr/bin/env python3
import argparse, os, pathlib, re, sys
from collections import defaultdict

# Regexes tolerant of minor OpenSSH output variations
RX_KEX       = re.compile(r"\bkex:\s+algorithm:\s+([^\s]+)", re.IGNORECASE)
RX_HOSTKEY   = re.compile(r"\bkex:\s+host key algorithm:\s+([^\s]+)", re.IGNORECASE)
RX_CIPHERDIR = re.compile(r"\bkex:\s+(client->server|server->client)\s+cipher:\s+([^\s]+).*?(?:MAC:\s*([^\s]+))?", re.IGNORECASE)
RX_ELAPSED   = re.compile(r"\belapsed=([0-9:.]+)")
RX_EXIT      = re.compile(r"\bexit=(\d+)")

def parse_args():
    p = argparse.ArgumentParser(description="Summarize SSH algorithm negotiation from verbose logs.")
    p.add_argument("--log-dir", default=os.path.expanduser("~/ssh-logs/2025-08-18"),
                   help="Directory containing *.log files (default: %(default)s)")
    p.add_argument("--pattern", default="*.log", help="Glob pattern for log files (default: %(default)s)")
    p.add_argument("--out", default="-", help="Output file (Markdown). '-' = stdout (default).")
    p.add_argument("--latest-per-profile", action="store_true",
                   help="If multiple logs per profile exist, only keep the newest by timestamp in filename.")
    p.add_argument("--profile-from-name", action="store_true",
                   help="Derive profile from the start of filename before the first '-' (e.g., 'baseline-2025-...').")
    return p.parse_args()

def profile_from_filename(name: str) -> str:
    # Example: baseline-2025-08-18T12:34:56.log -> baseline
    if "-" in name:
        return name.split("-", 1)[0]
    return pathlib.Path(name).stem

def load_files(log_dir, pattern, latest_per_profile, derive_profile):
    files = sorted(pathlib.Path(log_dir).glob(pattern))
    if not files:
        return []

    if not latest_per_profile:
        return files

    # Keep only the newest file per profile (by filename lexical order, which works for ISO timestamps)
    buckets = defaultdict(list)
    for f in files:
        prof = profile_from_filename(f.name) if derive_profile else pathlib.Path(f).stem
        buckets[prof].append(f)

    latest = []
    for prof, flist in buckets.items():
        flist.sort(key=lambda p: p.name)  # ISO timestamps in names will sort correctly
        latest.append(flist[-1])
    return sorted(latest, key=lambda p: p.name)

def parse_log(path: pathlib.Path):
    kex = hostkey = None
    c2s_cipher = c2s_mac = None
    s2c_cipher = s2c_mac = None
    elapsed = exit_code = None

    try:
        with path.open("r", errors="ignore") as f:
            for line in f:
                if kex is None:
                    m = RX_KEX.search(line);       kex = m.group(1) if m else kex
                if hostkey is None:
                    m = RX_HOSTKEY.search(line);   hostkey = m.group(1) if m else hostkey
                m = RX_CIPHERDIR.search(line)
                if m:
                    direction, cipher, mac = m.groups()
                    if direction.lower().startswith("client"):
                        c2s_cipher, c2s_mac = cipher, (mac or "")
                    else:
                        s2c_cipher, s2c_mac = cipher, (mac or "")
                # Optional timing if present anywhere in file
                if elapsed is None:
                    me = RX_ELAPSED.search(line);  elapsed = me.group(1) if me else elapsed
                if exit_code is None:
                    mx = RX_EXIT.search(line);     exit_code = mx.group(1) if mx else exit_code
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)

    return {
        "kex": kex or "",
        "hostkey": hostkey or "",
        "c2s": (c2s_cipher or "") + (f"/{c2s_mac}" if c2s_mac else ""),
        "s2c": (s2c_cipher or "") + (f"/{s2c_mac}" if s2c_mac else ""),
        "elapsed": elapsed or "",
        "exit": exit_code or ""
    }

def main():
    args = parse_args()
    files = load_files(args.log_dir, args.pattern, args.latest_per_profile, args.profile_from_name)
    if not files:
        print(f"No logs found in {args.log_dir} matching {args.pattern}", file=sys.stderr)
        sys.exit(2)

    rows = []
    for f in files:
        prof = profile_from_filename(f.name) if args.profile_from_name else f.stem
        data = parse_log(f)
        rows.append((prof, f.name, data))

    # Emit Markdown
    headers = ["Profile", "Logfile", "KEX", "HostKey", "C2S cipher/MAC", "S2C cipher/MAC", "Elapsed?*", "Exit?*"]
    out_lines = []
    out_lines.append("| " + " | ".join(headers) + " |")
    out_lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for prof, fname, d in sorted(rows):
        out_lines.append(
            f"| {prof} | {fname} | `{d['kex']}` | `{d['hostkey']}` | {d['c2s']} | {d['s2c']} | {d['elapsed']} | {d['exit']} |"
        )
    out_lines.append("")
    out_lines.append("_* Elapsed/Exit only appear if those fields exist in the log (e.g., if you included time output)._")

    md = "\n".join(out_lines)
    if args.out == "-" or not args.out:
        print(md)
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)

if __name__ == "__main__":
    main()
