#!/usr/bin/env python3
# dir_enum.py — Minimal directory enumerator with optional HTTP Basic Auth.
# Dependency: requests  (pip install requests)

import argparse
import sys
import time
import re
import os
from urllib.parse import urljoin

try:
    import requests
    from requests.auth import HTTPBasicAuth
except ImportError:
    sys.stderr.write("[!] This tool requires the 'requests' package: pip install requests\n")
    sys.exit(1)


BUILTIN_PATHS = [
    # super-common static/content dirs
    "files", "images", "img", "css", "js", "assets", "static", "uploads", "media",
    # admin/dev odds and ends
    "backup", "backups", "old", "tmp", "test", "dev", "staging",
    # discovery helpers
    "robots.txt", "sitemap.xml",
]

DIRLIST_PATTERNS = [
    r"Index of /",            # Apache-style
    r"Parent Directory",      # common link in listings
    r"Directory listing for", # some frameworks
    r"<title>Index of",       # Apache/NGINX variants
]


def looks_like_dir_listing(text: str) -> bool:
    for pat in DIRLIST_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def normalize_target(base: str) -> str:
    # Ensure trailing slash so urljoin treats path candidates as children
    return base if base.endswith("/") else base + "/"


def gen_candidates(common: bool, wordlist_path: str | None):
    seen = set()
    if common:
        for p in BUILTIN_PATHS:
            if p not in seen:
                seen.add(p)
                yield p
    if wordlist_path:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                p = line.strip().lstrip("/")
                if not p or p.startswith("#"):
                    continue
                if p not in seen:
                    seen.add(p)
                    yield p


def supports_color() -> bool:
    # Basic TTY check; Windows 10+ terminals usually support ANSI.
    return sys.stdout.isatty() and os.getenv("NO_COLOR") is None


def colorize(s: str, color: str, enable: bool) -> str:
    if not enable:
        return s
    COLORS = {
        "green": "\033[32m",
        "yellow": "\033[33m",
        "red": "\033[31m",
        "blue": "\033[34m",
        "bold": "\033[1m",
        "reset": "\033[0m",
    }
    return f"{COLORS.get(color,'')}{s}{COLORS['reset']}"


def classify_response(r: requests.Response) -> tuple[str, str]:
    """
    Returns (classification, body_text_if_textual_else_empty)
    classification ∈ {"DIR-LISTING", "OK", "FORBIDDEN", "NOTFOUND", "REDIR->XXX", "HTTP XXX"}
    """
    code = r.status_code
    ctype = r.headers.get("Content-Type", "")
    body = r.text if "text" in ctype else ""

    if code == 200:
        if looks_like_dir_listing(body):
            return "DIR-LISTING", body
        return "OK", body
    if code in (301, 302, 303, 307, 308):
        return f"REDIR->{code}", body
    if code == 403:
        return "FORBIDDEN", body
    if code == 404:
        return "NOTFOUND", body
    return f"HTTP {code}", body


def extract_listing_preview(body: str, max_items: int = 5) -> list[str]:
    # very naive link extraction for directory listings
    files = re.findall(r'href="([^"]+)"', body)
    files = [f for f in files if f not in ("../", "/") and not f.startswith("?")]
    # de-dup, keep order
    seen = set()
    out = []
    for f in files:
        if f not in seen:
            seen.add(f)
            out.append(f)
        if len(out) >= max_items:
            break
    return out


def main():
    ap = argparse.ArgumentParser(description="Minimal directory enumerator with Basic Auth support.")
    ap.add_argument("base_url", help="Base URL (e.g., https://target/ or http://host/)")
    ap.add_argument("-u", "--username", help="HTTP Basic Auth username")
    ap.add_argument("-p", "--password", help="HTTP Basic Auth password")
    ap.add_argument("-w", "--wordlist", help="Path to a custom wordlist (one path per line)")
    ap.add_argument("--common", action="store_true", help="Try a small built-in list of common paths")
    ap.add_argument("--timeout", type=float, default=8.0, help="Per-request timeout (seconds)")
    ap.add_argument("--delay", type=float, default=0.0, help="Delay between requests (seconds)")
    ap.add_argument("--headers", nargs="*", default=[], help='Extra headers, e.g. --headers "User-Agent: X" "Accept: text/html"')
    ap.add_argument("--max-preview", type=int, default=5, help="Max preview items to display for directory listings")
    ap.add_argument("-v", "--verbose", action="store_true", help="Verbose: print response headers for interesting hits")
    ap.add_argument("--color", choices=["auto", "always", "never"], default="auto", help="Colorized output (auto|always|never)")
    args = ap.parse_args()

    if not (args.common or args.wordlist):
        print("[i] No wordlist provided. Tip: use --common for a small built-in list, or -w wordlist.txt")

    base = normalize_target(args.base_url)
    auth = HTTPBasicAuth(args.username, args.password) if args.username and args.password else None

    # Color handling
    if args.color == "always":
        use_color = True
    elif args.color == "never":
        use_color = False
    else:
        use_color = supports_color()

    # Build header dict
    hdrs = {"User-Agent": "dir-enum/0.2"}
    for h in args.headers:
        if ":" in h:
            k, v = h.split(":", 1)
            hdrs[k.strip()] = v.strip()

    # Always consider robots.txt & sitemap.xml first (cheap wins)
    primaries = ["robots.txt", "sitemap.xml"]
    candidates = list(primaries)
    for c in gen_candidates(args.common, args.wordlist):
        if c not in candidates:
            candidates.append(c)

    print(colorize(f"[+] Target: {base}", "blue", use_color))
    if auth:
        print(colorize(f"[+] Using Basic Auth for user '{args.username}'", "blue", use_color))
    print(colorize(f"[+] Candidates: {len(candidates)}\n", "blue", use_color))

    s = requests.Session()
    s.headers.update(hdrs)

    for rel in candidates:
        # Try both as directory and as file when appropriate
        rel_clean = rel.strip("/")
        to_try = []

        if rel_clean.endswith(".txt") or "." in rel_clean:
            # Looks like a file; try exact
            to_try.append(rel_clean)
        else:
            # Try as directory (explicit slash often gives clearer server behavior)
            to_try.append(rel_clean + "/")

        for item in to_try:
            url = urljoin(base, item)
            try:
                r = s.get(url, auth=auth, timeout=args.timeout, allow_redirects=True)
            except requests.RequestException as e:
                prefix = colorize("[-]", "red", use_color)
                print(f"{prefix} {url:<70} error: {e.__class__.__name__}")
                continue

            classification, body = classify_response(r)

            # Choose prefix & color
            if classification == "DIR-LISTING":
                prefix = colorize("[+]", "green", use_color)
            elif classification in ("OK", "REDIR->301", "REDIR->302", "REDIR->303", "REDIR->307", "REDIR->308"):
                prefix = colorize("[*]", "yellow", use_color)
            elif classification in ("FORBIDDEN",):
                prefix = colorize("[-]", "red", use_color)
            elif classification in ("NOTFOUND",):
                prefix = colorize("[-]", "red", use_color)
            else:
                prefix = colorize("[?]", "yellow", use_color)

            line = f"{prefix} {r.url:<70} {classification}"

            # Add a small preview if directory listing detected
            if classification == "DIR-LISTING":
                preview = extract_listing_preview(body, max_items=args.max_preview)
                if preview:
                    line += f"  -> [{', '.join(preview)}]"

            print(line)

            # Verbose mode: print response headers for interesting hits
            if args.verbose and classification in ("DIR-LISTING", "OK", "FORBIDDEN"):
                # Minimal header dump
                print(colorize("    └─ Headers:", "bold", use_color))
                for hk, hv in r.headers.items():
                    print(f"       {hk}: {hv}")
                # Show first ~200 chars of body when it's textual and interesting
                if body and classification != "FORBIDDEN":
                    snippet = body.strip().replace("\r", "")
                    if len(snippet) > 200:
                        snippet = snippet[:200] + "…"
                    print(colorize("    └─ Body (preview):", "bold", use_color))
                    for ln in snippet.split("\n")[:6]:
                        print(f"       {ln}")

            if args.delay > 0:
                time.sleep(args.delay)


if __name__ == "__main__":
    main()
