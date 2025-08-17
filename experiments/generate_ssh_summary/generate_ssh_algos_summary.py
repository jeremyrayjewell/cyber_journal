#!/usr/bin/env python3
import argparse, os, pathlib, re, sys

# What we want to extract from ssh -vvv logs
RX_KEX         = re.compile(r"\bkex:\s+algorithm:\s+([^\s]+)", re.IGNORECASE)
RX_HOSTKEY     = re.compile(r"\bkex:\s+host key algorithm:\s+([^\s]+)", re.IGNORECASE)
RX_C2S_CIPHER  = re.compile(r"\bkex:\s+client->server\s+cipher:\s+([^\s]+)", re.IGNORECASE)
RX_S2C_CIPHER  = re.compile(r"\bkex:\s+server->client\s+cipher:\s+([^\s]+)", re.IGNORECASE)

# Signals of a good session
RX_READY       = re.compile(r"\bREADY\b")
RX_AUTH_OK     = re.compile(r"Authentication succeeded", re.IGNORECASE)

# Common failure signatures
FAIL_PATTERNS = [
    r"no matching key exchange method found",
    r"no matching kex.*found",
    r"Connection timed out",
    r"Operation timed out",
    r"Connection refused",
    r"Network is unreachable",
    r"kex_exchange_identification: .*",
    r"ssh_exchange_identification: .*",
    r"handshake.*failed",
    r"Unable to negotiate",
    r"All configured authentication methods failed",
    r"Permission denied",
    r"protocol error",
    r"fatal: .+",
]
RX_FAIL = re.compile("|".join(FAIL_PATTERNS), re.IGNORECASE)

def profile_from_name(name: str) -> str:
    return pathlib.Path(name).stem  # e.g. forced-curve25519.log -> forced-curve25519

def parse_log(path: pathlib.Path):
    data = ""
    try:
        data = path.read_text(errors="ignore")
    except Exception as e:
        return dict(success=False, reason=f"parse error: {e}", kex="", host="", c2s="", s2c="")

    # Extract fields
    kex   = (RX_KEX.search(data).group(1) if RX_KEX.search(data) else "")
    host  = (RX_HOSTKEY.search(data).group(1) if RX_HOSTKEY.search(data) else "")
    c2s   = (RX_C2S_CIPHER.search(data).group(1) if RX_C2S_CIPHER.search(data) else "")
    s2c   = (RX_S2C_CIPHER.search(data).group(1) if RX_S2C_CIPHER.search(data) else "")

    # Determine outcome
    success = bool(RX_READY.search(data) or RX_AUTH_OK.search(data) or (kex and c2s and s2c))
    reason  = ""
    if not success:
        m = RX_FAIL.search(data)
        reason = m.group(0) if m else "no negotiation (likely disabled/blocked/timeout)"

    return dict(success=success, reason=reason, kex=kex, host=host, c2s=c2s, s2c=s2c)

def main():
    ap = argparse.ArgumentParser(description="Summarize SSH algorithm negotiation from verbose logs.")
    ap.add_argument("--log-dir", default=os.path.expanduser("~/ssh-logs/2025-08-18"))
    ap.add_argument("--pattern", default="*.log")
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    files = sorted(pathlib.Path(args.log_dir).glob(args.pattern))
    if not files:
        print(f"No logs in {args.log_dir} matching {args.pattern}", file=sys.stderr)
        sys.exit(2)

    def dash(s): return s if s else "—"

    lines = []
    headers = ["Profile","Logfile","Outcome","Reason","KEX","HostKey","C2S cipher","S2C cipher"]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"]*len(headers)) + "|")

    for f in files:
        prof = profile_from_name(f.name)
        d = parse_log(f)
        outcome = "Success" if d["success"] else "**Failed**"
        reason  = dash(d["reason"])
        lines.append(
            f"| {prof} | {f.name} | {outcome} | {reason} | "
            f"`{dash(d['kex'])}` | `{dash(d['host'])}` | {dash(d['c2s'])} | {dash(d['s2c'])} |"
        )

    md = "\n".join(lines)
    if args.out == "-" or not args.out:
        print(md)
    else:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(md)

if __name__ == "__main__":
    main()
