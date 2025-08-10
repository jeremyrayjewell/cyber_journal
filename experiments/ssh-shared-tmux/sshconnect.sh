#!/usr/bin/env bash
# sshconnect.sh — open SSH and land in a server-side shared tmux session
set -euo pipefail

# ─── SELF-ELEVATE (needed for iptables/systemctl) ──────────────────────────────
if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  exec sudo -E bash "$0" "$@"
fi

# ─── CONFIG ────────────────────────────────────────────────────────────────────
SSH_PORT=${SSH_PORT:-443}
TMUX_SESSION=${TMUX_SESSION:-shared}
# ───────────────────────────────────────────────────────────────────────────────

log() { printf '%s\n' "$*"; }

log "__ Opening SSH server on port $SSH_PORT"

# 1) Firewall: unblock & accept (best-effort; wait for xtables lock)
if command -v iptables &>/dev/null; then
  iptables -w 5 -D INPUT -p tcp --dport "$SSH_PORT" -j DROP 2>/dev/null || true
  iptables -w 5 -C INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT 2>/dev/null || iptables -w 5 -I INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT
else
  log "__ iptables not found; skipping firewall rule changes."
fi

# 2) Start (and enable) sshd (support both service names)
if command -v systemctl &>/dev/null; then
  systemctl enable --now sshd 2>/dev/null || systemctl enable --now ssh 2>/dev/null || {
    log "__ Could not start ssh/sshd via systemd"; exit 1;
  }
else
  service sshd start 2>/dev/null || service ssh start 2>/dev/null || true
fi

# 3) Ensure tmux session exists (detached)
if command -v tmux &>/dev/null; then
  if ! tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
    tmux new-session -d -s "$TMUX_SESSION"
    log "__ Created tmux session '$TMUX_SESSION' (detached)."
  else
    log "__ tmux session '$TMUX_SESSION' already exists."
  fi
else
  log "__ tmux not installed — please install it to use shared sessions."
  exit 1
fi

# 4) Grab IPs (best-effort)
IFACE=$(ip route show default 2>/dev/null | awk '/default/ {print $5; exit}' || true)
LOCAL_IP=""
if [[ -n "${IFACE:-}" ]]; then
  LOCAL_IP=$(ip -4 addr show "$IFACE" 2>/dev/null | awk '/inet / {print $2}' | cut -d/ -f1 | head -n1 || true)
fi
if command -v curl &>/dev/null; then
  PUBLIC_IP=$(curl -fsS ifconfig.me || true)
else
  PUBLIC_IP=""
fi

# 5) Inject connection instructions *into* tmux
INFO_HEADER="__ SSH is up on port $SSH_PORT."
INFO_REMOTE="   ssh -t -p $SSH_PORT $USER@${PUBLIC_IP:-<public_ip>} tmux attach -t $TMUX_SESSION"
INFO_LAN="   ssh -t -p $SSH_PORT $USER@${LOCAL_IP:-<local_ip>}  tmux attach -t $TMUX_SESSION"

read -r -d '' INFO <<EOF || true
$INFO_HEADER

__ From any client, attach to the shared tmux with:
$INFO_REMOTE

__ Or on your LAN:
$INFO_LAN

__ Tip: detach with Ctrl-b then d. Reattach with:
   tmux attach -t $TMUX_SESSION
EOF

tmux set-buffer -- "$INFO"
tmux paste-buffer -t "$TMUX_SESSION":0.0
tmux send-keys  -t "$TMUX_SESSION":0.0 C-m

# 6) Attach *this* terminal into the tmux session
if [[ -t 1 ]]; then
  log "__ Attaching to tmux session '$TMUX_SESSION' on SERVER now"
  exec tmux attach -t "$TMUX_SESSION"
fi
