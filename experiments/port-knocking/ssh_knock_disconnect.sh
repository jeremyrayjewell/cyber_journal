#!/usr/bin/env bash
# ssh_knock_disconnect.sh — Close SSH access with reverse knock
# NOTE: Run this from the SAME CLIENT IP that opened the port.

set -euo pipefail

usage(){ echo "Usage: $0 <server-ip> [ssh-port:22]"; exit 1; }
[ "${1:-}" ] || usage

SERVER_IP="$1"
SSH_PORT="${2:-22}"
REVERSE=("3333" "2222" "1111")

echo "__ Sending reverse knock sequence to $SERVER_IP ..."
if command -v knock >/dev/null 2>&1; then
  knock "$SERVER_IP" "${REVERSE[@]}"
else
  echo "__ 'knock' not found; using nmap to send reverse SYNs ..."
  for PORT in "${REVERSE[@]}"; do
    nmap -Pn --max-retries 0 --host-timeout 200ms -p "$PORT" "$SERVER_IP" >/dev/null 2>&1 || true
  done
fi

# Optional: quick closed-check
if command -v nc >/dev/null 2>&1; then
  echo "__ Verifying TCP $SSH_PORT is closed to this client ..."
  nc -vz -w 2 -n "$SERVER_IP" "$SSH_PORT" || true
fi

echo "__ SSH access closed (new connections from this IP should now fail)."

