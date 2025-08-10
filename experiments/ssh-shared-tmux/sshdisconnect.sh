#!/bin/bash

SSH_PORT=443        # your SSH port
TMUX_SESSION="shared"

echo "🛑 Closing SSH server..."

# 1) Stop the SSH service
sudo systemctl stop sshd

# 2) Detach all clients from the tmux session (but leave it running)
if command -v tmux &>/dev/null; then
  tmux detach-client -a -t "$TMUX_SESSION" 2>/dev/null || true
  echo "🛑 Detached all clients from tmux session '$TMUX_SESSION' (still running)."
fi

# 3) Clean up firewall rules:
#    Remove the ACCEPT rule we added in sshconnect.sh, if present
sudo iptables -D INPUT -p tcp --dport "$SSH_PORT" -j ACCEPT 2>/dev/null

#    Now add a DROP rule to block new SSH attempts
sudo iptables -I INPUT -p tcp --dport "$SSH_PORT" -j DROP

echo "🔒 Port $SSH_PORT is now blocked and the SSH server is offline."
