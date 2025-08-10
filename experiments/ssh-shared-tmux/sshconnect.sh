#!/usr/bin/env bash
# sshconnect.sh — open SSH and land you in a server-side shared tmux session

# ─── CONFIG ───────────────────────────────────────────────────────────────────
SSH_PORT=443
TMUX_SESSION="shared"
# ──────────────────────────────────────────────────────────────────────────────

echo "__ Opening SSH server on port $SSH_PORT_"

# 1) Firewall: unblock & accept
sudo iptables -D INPUT -p tcp --dport "$SSH_PORT" -j DROP 2>/dev/null
sudo iptables -I INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT

# 2) Start (and enable) sshd
sudo systemctl enable --now sshd

# 3) Grab IPs for instructions (prefer IPv4; best-effort fallbacks)
IFACE=$(ip route show default | awk '/default/ {print $5}')
LOCAL_IP=$(ip -4 addr show "$IFACE" 2>/dev/null | awk '/inet / {print $2}' | cut -d/ -f1 | head -n1)
PUBLIC_IP=$(curl -4 -s ifconfig.me || curl -s ifconfig.me)

# Use the invoking user if script runs via sudo; otherwise $USER
INVOKER="${SUDO_USER:-$USER}"

# 4) Always start with a fresh tmux session and inject info into it
if command -v tmux &>/dev/null; then
  tmux kill-session -t "$TMUX_SESSION" 2>/dev/null || true
  tmux new-session -d -s "$TMUX_SESSION"

  # Build and show instructions in tmux session (values embedded now)
  tmux send-keys -t "$TMUX_SESSION":0 \
"clear && echo && echo '__ SSH is up on port $SSH_PORT.' && \
echo && echo '__ From any client, attach to the shared tmux with:' && \
echo '   ssh -t -p $SSH_PORT $INVOKER@${PUBLIC_IP:-<public_ip>} tmux attach -t $TMUX_SESSION' && \
echo && echo '__ Or on your LAN:' && \
echo '   ssh -t -p $SSH_PORT $INVOKER@${LOCAL_IP:-<local_ip>} tmux attach -t $TMUX_SESSION' && \
echo && echo '__ Tip: detach with Ctrl-b then d, reattach with: tmux attach -t $TMUX_SESSION' && echo" C-m

  echo "__ Created tmux session '$TMUX_SESSION' (detached)."
else
  echo "__ tmux not installed — please install it to use shared sessions."
  exit 1
fi

# 5) Print client-side one-liners to this shell too
echo
echo "__ SSH is up on port $SSH_PORT."
echo
echo "__ From any client, attach to the shared tmux with:"
echo "   ssh -t -p $SSH_PORT $INVOKER@${PUBLIC_IP:-<public_ip>} tmux attach -t $TMUX_SESSION"
echo
echo "__ Or on your LAN:"
echo "   ssh -t -p $SSH_PORT $INVOKER@${LOCAL_IP:-<local_ip>} tmux attach -t $TMUX_SESSION"
echo

# 6) Attach *this* terminal into the tmux session
if [[ -t 1 ]]; then
  echo "__ Attaching to tmux session '$TMUX_SESSION' on SERVER now_"
  exec tmux attach -t "$TMUX_SESSION"
fi
