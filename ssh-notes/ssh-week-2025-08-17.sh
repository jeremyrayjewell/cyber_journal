#!/usr/bin/env bash
set -euo pipefail

SERVER="kali@192.168.1.12"
LOGDIR=~/ssh-logs/2025-08-18
mkdir -p "$LOGDIR"

PROFILES=(baseline classical hybridpq legacy)

for p in "${PROFILES[@]}"; do
  ts=$(date -Iseconds)
  log="${LOGDIR}/${p}-${ts}.log"
  echo "== Testing $p at $ts =="
  ssh -vvv -o ConnectTimeout=7 -o PreferredAuthentications=publickey \
    $SERVER 'echo READY; exit' 2>&1 | tee "$log"
done
