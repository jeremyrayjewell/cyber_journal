#!/usr/bin/env bash
# ssh_knock_connect.sh — Send knock sequence and SSH into the server

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <server-ip> <ssh-user>"
    exit 1
fi

SERVER_IP=$1
SSH_USER=$2
SEQUENCE="1111 2222 3333"

echo "__ Sending knock sequence to $SERVER_IP ..."
for PORT in $SEQUENCE; do
    nmap -Pn --host-timeout 200ms -p $PORT $SERVER_IP >/dev/null
done

echo "__ Connecting via SSH ..."
ssh "$SSH_USER@$SERVER_IP"
