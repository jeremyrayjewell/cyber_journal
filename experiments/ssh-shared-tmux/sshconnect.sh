#!/usr/bin/env bash
# sshconnect.sh _ open SSH and land you in a server-side shared tmux session

# ─── CONFIG ───────────────────────────────────────────────────────────────────
SSH_PORT=443
TMUX_SESSION="shared"
# ──────────────────────────────────────────────────────────────────────────────

echo "__ Opening SSH server on port $SSH_PORT_"

# 1) Firewall: unblock & accept
sudo iptables -D INPUT -p tcp --dport $SSH_PORT -j DROP 2>/dev/null
sudo iptables -I INPUT -p tcp --dport $SSH_PORT -j ACCEPT

# 2) Start (and enable) sshd
sudo systemctl enable --now sshd

# 3) Ensure tmux session exists (detached)
if command -v tmux &>/dev/null; then
  if ! tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
    tmux new-session -d -s "$TMUX_SESSION"
    echo "__ Created tmux session '$TMUX_SESSION' (detached)."
  else
    echo "__ tmux session '$TMUX_SESSION' already exists."
  fi
else
  echo "__  tmux not installed_please install it to use shared sessions."
fi

# 4) Grab IPs
IFACE=$(ip route show default | awk '/default/ {print $5}')
LOCAL_IP=$(ip -4 addr show "$IFACE" \
           | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
PUBLIC_IP=$(curl -s ifconfig.me)

# 5) Print client_side one-liners
echo
echo "__ SSH is up on port $SSH_PORT."
echo
echo "__ From any client, attach to the shared tmux with:"
echo
echo "   ssh -t -p $SSH_PORT $USER@$PUBLIC_IP tmux attach -t $TMUX_SESSION"
echo
echo "__ Or on your LAN:"
echo
echo "   ssh -t -p $SSH_PORT $USER@$LOCAL_IP  tmux attach -t $TMUX_SESSION"
echo

# 6) Finally: attach *this* terminal into the tmux session on the server
if [[ -t 1 ]]; then
  echo "__ Attaching to tmux session '$TMUX_SESSION' on SERVER now_"
  exec tmux attach -t "$TMUX_SESSION"
fi
