#!/usr/bin/env bash
# ssh_knock_disconnect.sh — Close SSH access with reverse knock

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <server-ip>"
    exit 1
fi

SERVER_IP=$1
REVERSE_SEQUENCE="3333 2222 1111"

echo "__ Sending reverse knock sequence to $SERVER_IP ..."
for PORT in $REVERSE_SEQUENCE; do
    nmap -Pn --host-timeout 200ms -p $PORT $SERVER_IP >/dev/null
done

echo "__ SSH access closed."
