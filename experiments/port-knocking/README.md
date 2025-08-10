# Port Knocking — Stealth SSH Access

**Port knocking** hides your SSH port from scanners by requiring a secret sequence of connection attempts to specific ports before the real SSH port opens.  
Until the correct sequence is received, the SSH port remains closed.

## Features
- Requires a predefined **knock sequence** (example: `1111,2222,3333`).
- Automatically opens the SSH port after a successful knock.
- Closes the port after a timeout or when a reverse sequence is sent.
- Uses **knockd** for sequence listening and **iptables** for access control.

## Files
- **knockd.conf** — Example knock sequence configuration for the server.
- **ssh_knock_connect.sh** — Sends the knock sequence from a client and connects to SSH.
- **ssh_knock_disconnect.sh** — Sends the reverse knock to close the SSH port.
- **verify_server.sh** — Server-side quick checker: interface/IPs, sshd/knockd status, iptables rules, and recent knockd logs.

## Dependencies
**Server:** knockd, iptables, systemd  
**Client:** knock (from the knockd package) or nmap, ssh, nc (netcat)

---

## Step-by-Step Lab Setup

### 1️⃣ Install dependencies
On **server (Kali)**:
```bash
sudo apt update
sudo apt install -y knockd iptables
```
On **client (BlackArch)**:
```bash
sudo pacman -S knockd
# (provides the 'knock' client)
```

### 2️⃣ Configure the knock sequence (server)
Edit `/etc/knockd.conf`:
```ini
[options]
    logfile = /var/log/knockd.log

[openSSH]
    sequence      = 1111,2222,3333
    seq_timeout   = 15
    command       = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags      = syn

[closeSSH]
    sequence      = 3333,2222,1111
    seq_timeout   = 15
    command       = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags      = syn
```

### 3️⃣ Ensure knockd uses the right interface (server)
```bash
IFACE=$(ip route show default | awk '/default/ {print $5; exit}')
echo "START_KNOCKD=1" | sudo tee /etc/default/knockd
echo "KNOCKD_OPTS=\"-i $IFACE\"" | sudo tee -a /etc/default/knockd
sudo systemctl enable --now knockd
```

### 4️⃣ Close SSH by default (server)
> Make sure this port matches the one in `/etc/knockd.conf` (22 or 443).
```bash
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
```

### 5️⃣ Make client scripts executable (client)
```bash
chmod +x ssh_knock_connect.sh ssh_knock_disconnect.sh
```

### 6️⃣ Open SSH with the knock sequence (client)
```bash
./ssh_knock_connect.sh <server-ip> <ssh-user> [ssh-port]
```

### 7️⃣ Close SSH with the reverse knock (client)
> Run this from the **same client IP** that opened the port.
```bash
./ssh_knock_disconnect.sh <server-ip> [ssh-port]
```

---

## Server Quick Check
From the **server (Kali)**, run:
```bash
sudo ./verify_server.sh [ssh-port]
```
You’ll see:
- Interface and current IPs
- `sshd` and `knockd` active/inactive
- Current **iptables** rules for the SSH port
- Recent `/var/log/knockd.log` entries
- Listening sockets for sshd

---

## Troubleshooting
- **“No route to host”**: fix network reachability (same subnet/bridge, gateway). Confirm from client:
  - `ping <server-ip>`
  - `ip route get <server-ip>`
- **Knock works but SSH still closed**: on Kali, watch logs and ensure an `ACCEPT ... --dport <port>` rule appears *above* the DROP:
  ```bash
  sudo tail -f /var/log/knockd.log
  sudo iptables -L INPUT -n --line-numbers | grep ":<port>"
  ```
- **Reverse knock didn’t close**: ensure `closeSSH` uses `-s %IP%`, and send the reverse knock from the **same client IP** that opened it.
- **Netcat options differ**: use `nc -vz -w 2 -n <ip> <port>` (avoid `-4` if unsupported).
- **Existing sessions**: closing the port only blocks **new** SSH connections; established sessions remain active.

---

## Author
**Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
