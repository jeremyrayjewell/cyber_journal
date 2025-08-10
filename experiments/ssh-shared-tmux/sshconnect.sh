#!/usr/bin/env bash
# sshconnect.sh — open SSH and land in a server-side shared tmux session
# - Starts/ensures sshd is up
# - Opens firewall port
# - Ensures a shared tmux session exists
# - Writes connection instructions to /tmp and shows them *once* in tmux
# - Attaches you to the session

set -euo pipefail

# ─── REMEMBER WHO INVOKED US (before sudo) ─────────────────────────────────────
INVOKER="${SUDO_USER:-${USER:-unknown}}"

# ─── SELF-ELEVATE (needed for iptables/systemctl) ──────────────────────────────
if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  exec sudo -E bash "$0" "$@"
fi

# ─── CONFIG ────────────────────────────────────────────────────────────────────
SSH_PORT="${SSH_PORT:-443}"
TMUX_SESSION="${TMUX_SESSION:-shared}"
INFO_FILE="/tmp/ssh_shared_instructions.txt"
# ───────────────────────────────────────────────────────────────────────────────

log() { printf '%s\n' "$*"; }

log "__ Opening SSH server on port $SSH_PORT"

# 1) Firewall: unblock & accept (best-effort; wait for xtables lock)
if command -v iptables &>/dev/null; then
  iptables -w 5 -D INPUT -p tcp --dport "$SSH_PORT" -j DROP 2>/dev/null || true
  iptables -w 5 -C INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT 2>/dev/null || \
  iptables -w 5 -I INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT
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
if ! command -v tmux &>/dev/null; then
  log "__ tmux not installed — please install it to use shared sessions."
  exit 1
fi
if ! tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
  tmux new-session -d -s "$TMUX_SESSION"
  log "__ Created tmux session '$TMUX_SESSION' (detached)."
else
  log "__ tmux session '$TMUX_SESSION' already exists."
fi

# 4) Grab IPs (best-effort)
IFACE="$(ip route show default 2>/dev/null | awk '/default/ {print $5; exit}' || true)"
LOCAL_IP=""
if [[ -n "${IFACE:-}" ]]; then
  LOCAL_IP="$(ip -4 addr show "$IFACE" 2>/dev/null | awk '/inet / {print $2}' | cut -d/ -f1 | head -n1 || true)"
fi
if command -v curl &>/dev/null; then
  PUBLIC_IP="$(curl -fsS ifconfig.me || true)"
else
  PUBLIC_IP=""
fi

# 5) Build connection instructions and write to /tmp (readable by all)
cat > "$INFO_FILE" <<EOF
__ SSH is up on port $SSH_PORT.

__ From any client, attach to the shared tmux with:
   ssh -t -p $SSH_PORT $INVOKER@${PUBLIC_IP:-<public_ip>} tmux attach -t $TMUX_SESSION

__ Or on your LAN:
   ssh -t -p $SSH_PORT $INVOKER@${LOCAL_IP:-<local_ip>}  tmux attach -t $TMUX_SESSION

__ Tip:
   Detach with Ctrl-b then d. Reattach later with:
   tmux attach -t $TMUX_SESSION
EOF
chmod 0644 "$INFO_FILE"

# 6) One-shot "show instructions when a client attaches" using a helper script

HELPER="/tmp/tmux_show_info_once.sh"
cat > "$HELPER" <<'EOSH'
#!/usr/bin/env bash
SESSION="$1"
INFO_FILE="$2"

# Try popup (tmux >= 3.2); if not available, open an INFO window with less
tmux display-popup -t "$SESSION" -E \
  "clear; cat \"$INFO_FILE\"; echo; echo 'Close this with q or ESC.'; sh -c 'read -r -n1 _ 2>/dev/null || true'" 2>/dev/null \
|| {
  tmux kill-window -t "$SESSION":INFO 2>/dev/null || true
  tmux new-window -t "$SESSION" -n INFO "exec less -S \"$INFO_FILE\""
  tmux select-window -t "$SESSION":INFO
}

# Unset the hook so it only runs once
tmux set-hook -t "$SESSION" -u client-attached 2>/dev/null || true
EOSH
chmod +x "$HELPER"

# Register the hook (no -Q, compatible with older tmux)
tmux set-hook -t "$TMUX_SESSION" client-attached "run-shell '$HELPER $TMUX_SESSION $INFO_FILE'"



# 7) Attach *this* terminal into the tmux session
if [[ -t 1 ]]; then
  log "__ Attaching to tmux session '$TMUX_SESSION' on SERVER now"
  exec tmux attach -t "$TMUX_SESSION"
fi
