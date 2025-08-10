#!/usr/bin/env bash
# sshconnect.sh — open SSH and land in a server-side shared tmux session
# Zero-spam version: no send-keys, no popups/hooks on attach.
# Writes instructions to /tmp and adds a tmux keybinding (Ctrl-b i) to view them on demand.

set -euo pipefail

# Remember who invoked us (pre-sudo) so we print correct username in hints
INVOKER="${SUDO_USER:-${USER:-unknown}}"

# Self-elevate for iptables/systemctl
if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  exec sudo -E bash "$0" "$@"
fi

# ─── CONFIG ────────────────────────────────────────────────────────────────────
SSH_PORT="${SSH_PORT:-443}"
TMUX_SESSION="${TMUX_SESSION:-shared}"
INFO_FILE="/tmp/ssh_shared_instructions.txt"
# ───────────────────────────────────────────────────────────────────────────────

log(){ printf '%s\n' "$*"; }

log "__ Opening SSH server on port $SSH_PORT"

# 1) Firewall: allow SSH port (best-effort)
if command -v iptables &>/dev/null; then
  iptables -w 5 -D INPUT -p tcp --dport "$SSH_PORT" -j DROP 2>/dev/null || true
  iptables -w 5 -C INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT 2>/dev/null || \
  iptables -w 5 -I INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT
else
  log "__ iptables not found; skipping firewall changes."
fi

# 2) Start sshd
if command -v systemctl &>/dev/null; then
  systemctl enable --now sshd 2>/dev/null || systemctl enable --now ssh 2>/dev/null || {
    log "__ Could not start ssh/sshd via systemd"; exit 1; }
else
  service sshd start 2>/dev/null || service ssh start 2>/dev/null || true
fi

# 3) Ensure tmux session exists (detached)
if ! command -v tmux &>/dev/null; then
  log "__ tmux not installed — please install it."; exit 1
fi
if ! tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
  tmux new-session -d -s "$TMUX_SESSION"
  log "__ Created tmux session '$TMUX_SESSION' (detached)."
else
  log "__ tmux session '$TMUX_SESSION' already exists."
fi

# 4) Gather IPs (best-effort)
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

# 5) Write connection instructions to /tmp
cat > "$INFO_FILE" <<EOF
__ SSH is up on port $SSH_PORT.

__ From any client, attach to the shared tmux with:
   ssh -t -p $SSH_PORT $INVOKER@${PUBLIC_IP:-<public_ip>} tmux attach -t $TMUX_SESSION

__ Or on your LAN:
   ssh -t -p $SSH_PORT $INVOKER@${LOCAL_IP:-<local_ip>}  tmux attach -t $TMUX_SESSION

__ Tips:
   • Detach with Ctrl-b then d.
   • Reattach later with:  tmux attach -t $TMUX_SESSION
   • View these instructions inside tmux:  cat $INFO_FILE
   • Press Ctrl-b i to open a popup (or a viewer) with these instructions.
EOF
chmod 0644 "$INFO_FILE"

# 6) Install a safe, on-demand keybinding (Ctrl-b i) inside the session
#    - If popups are supported, show a popup that you close with any key.
#    - Otherwise, open a dedicated INFO window running less.
TMUX_VER_RAW="$(tmux -V | awk '{print $2}')"
TMUX_MAJ="${TMUX_VER_RAW%%.*}"
TMUX_MIN="${TMUX_VER_RAW#*.}"; TMUX_MIN="${TMUX_MIN%%.*}"

supports_popup=0
if [[ "$TMUX_MAJ" -ge 3 && "$TMUX_MIN" -ge 2 ]] || [[ "$TMUX_MAJ" -ge 4 ]]; then
  supports_popup=1
fi

if [[ "$supports_popup" -eq 1 ]]; then
  tmux set-option -t "$TMUX_SESSION" -gq @show_info_binding "display-popup -E 'clear; cat $INFO_FILE; echo; echo \"Close with any key\"; stty -echo; dd bs=1 count=1 of=/dev/null 2>/dev/null; stty echo'"
  tmux bind-key -t "$TMUX_SESSION" i run-shell "#{@show_info_binding}"
else
  # Fallback: open INFO window with less (quit with 'q')
  tmux set-option -t "$TMUX_SESSION" -gq @show_info_binding "run-shell 'tmux kill-window -t $TMUX_SESSION:INFO 2>/dev/null || true; tmux new-window -t $TMUX_SESSION -n INFO \"exec less -S $INFO_FILE\"; tmux select-window -t $TMUX_SESSION:INFO'"
  tmux bind-key -t "$TMUX_SESSION" i run-shell "#{@show_info_binding}"
fi

# 7) Tell the invoking terminal how to view info (before attaching)
log ""
log "__ How to connect from a client:"
log "   ssh -t -p $SSH_PORT $INVOKER@${PUBLIC_IP:-<public_ip>} tmux attach -t $TMUX_SESSION"
log "   (LAN) ssh -t -p $SSH_PORT $INVOKER@${LOCAL_IP:-<local_ip>} tmux attach -t $TMUX_SESSION"
log ""
log "__ Inside tmux: press Ctrl-b i to view instructions (popup/less)."
log "   Or: cat $INFO_FILE"
log ""

# 8) Attach this terminal to the session (no output injected into panes)
if [[ -t 1 ]]; then
  log "__ Attaching to tmux session '$TMUX_SESSION' now"
  exec tmux attach -t "$TMUX_SESSION"
fi
