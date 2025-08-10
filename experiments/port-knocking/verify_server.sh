#!/usr/bin/env bash
# verify_server.sh — Quick server-side sanity check for the port-knocking lab.
# Prints interface, IPs, sshd + knockd status, iptables rules for SSH port,
# and the last few lines of /var/log/knockd.log.
#
# Usage:
#   sudo ./verify_server.sh [ssh-port]
#   sudo ./verify_server.sh        # defaults to 22
#
# Notes:
# - Run on the target.
# - Requires sudo to read service status and iptables.

set -euo pipefail

SSH_PORT="${1:-22}"

# Detect main interface and IPs
IFACE="$(ip route show default 2>/dev/null | awk '/default/ {print $5; exit}')"
IPV4="$(ip -4 addr show "$IFACE" 2>/dev/null | awk '/inet /{print $2}' | cut -d/ -f1 | head -n1 || true)"
IPV6="$(ip -6 addr show "$IFACE" 2>/dev/null | awk '/inet6 [^f]/{print $2}' | cut -d/ -f1 | head -n1 || true)"

echo "=== Port-Knocking Server State ==="
echo "Interface : ${IFACE:-<unknown>}"
echo "IPv4      : ${IPV4:-<none>}"
echo "IPv6      : ${IPV6:-<none>}"
echo "SSH Port  : ${SSH_PORT}"
echo

echo "== Services =="
systemctl is-active --quiet ssh    && echo "sshd     : active" || echo "sshd     : inactive"
systemctl is-active --quiet knockd && echo "knockd   : active" || echo "knockd   : inactive"
echo

echo "== iptables rules touching TCP :${SSH_PORT} (INPUT chain) =="
# Show ordered rules (table view) and raw spec (policy view)
iptables -L INPUT -n --line-numbers | awk -v p="dpt:${SSH_PORT}" '$0 ~ p {print $0}' || true
echo
echo "== iptables -S (raw) for TCP :${SSH_PORT} =="
iptables -S INPUT | grep -E -- "--dport ${SSH_PORT}(\s|$)" || echo "(no explicit INPUT rules for --dport ${SSH_PORT})"
echo

echo "== Last 20 lines of /var/log/knockd.log =="
test -r /var/log/knockd.log && tail -n 20 /var/log/knockd.log || echo "(no /var/log/knockd.log yet)"
echo

echo "== Listening sockets for sshd =="
ss -ltnp | awk -v p=":${SSH_PORT}" '$0 ~ p' || echo "(no sshd listening on :${SSH_PORT})"
echo

echo "Done."
