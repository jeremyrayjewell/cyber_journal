#!/usr/bin/env bash
# ssh_knock_connect.sh — Send knock sequence and SSH into the server

set -euo pipefail

usage(){ echo "Usage: $0 <server-ip> <ssh-user> [ssh-port:22]"; exit 1; }
[ "${1:-}" ] && [ "${2:-}" ] || usage

SERVER_IP="$1"
SSH_USER="$2"
SSH_PORT="${3:-22}"
SEQUENCE=("1111" "2222" "3333")

echo "__ Sending knock sequence to $SERVER_IP ..."
if command -v knock >/dev/null 2>&1; then
  knock "$SERVER_IP" "${SEQUENCE[@]}"
else
  echo "__ 'knock' not found; using nmap to send SYNs ..."
  for PORT in "${SEQUENCE[@]}"; do
    nmap -Pn --max-retries 0 --host-timeout 200ms -p "$PORT" "$SERVER_IP" >/dev/null 2>&1 || true
  done
fi

# Give the server a moment to insert the ACCEPT rule
sleep 1

# Optional: quick availability probe (works with both nc flavors)
if command -v nc >/dev/null 2>&1; then
  echo "__ Probing TCP $SSH_PORT ..."
  nc -vz -w 2 -n "$SERVER_IP" "$SSH_PORT" || true
fi

echo "__ Connecting via SSH ..."
exec ssh -p "$SSH_PORT" "$SSH_USER@$SERVER_IP"
