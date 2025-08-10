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

## Dependencies
**Server:**
- `knockd`
- `iptables`
- `systemd` (for service management)

**Client:**
- `knock` command (part of `knockd` package)
- `ssh`

---

## Step-by-Step Lab Setup

### 1️⃣ Install dependencies
On **server**:
```bash
sudo apt update && sudo apt install knockd iptables -y        # Debian/Ubuntu
# or
sudo pacman -S knockd iptables                                 # Arch/Manjaro
```

On **client**:
```bash
sudo apt update && sudo apt install knock -y                   # Debian/Ubuntu
# or
sudo pacman -S knockd                                          # Arch/Manjaro
```

---

### 2️⃣ Configure the knock sequence (server)
Edit `/etc/knockd.conf`:
```ini
[options]
    logfile = /var/log/knockd.log

[openSSH]
    sequence      = 1111,2222,3333
    seq_timeout   = 15
    command       = /sbin/iptables -I INPUT -p tcp --dport 443 -j ACCEPT
    tcpflags      = syn

[closeSSH]
    sequence      = 3333,2222,1111
    seq_timeout   = 15
    command       = /sbin/iptables -D INPUT -p tcp --dport 443 -j ACCEPT
    tcpflags      = syn
```

---

### 3️⃣ Enable knockd on the server
```bash
sudo systemctl enable --now knockd
```

For **Debian/Ubuntu**, also edit `/etc/default/knockd`:
```
START_KNOCKD=1
KNOCKD_OPTS="-i eth0"
```
Replace `eth0` with your real interface (`ip route show default` to check).

---

### 4️⃣ Close SSH port by default (server)
```bash
sudo iptables -A INPUT -p tcp --dport 443 -j DROP
```

---

### 5️⃣ Make scripts executable (client)
```bash
chmod +x ssh_knock_connect.sh ssh_knock_disconnect.sh
```

---

### 6️⃣ Open SSH with the knock sequence (client)
```bash
./ssh_knock_connect.sh <server-ip> <ssh-user>
```
Example:
```bash
./ssh_knock_connect.sh 192.168.1.50 jeremy
```

---

### 7️⃣ Close SSH with the reverse knock (client)
```bash
./ssh_knock_disconnect.sh <server-ip>
```

---

## Safety Notes
- Port knocking is **security by obscurity** — use it alongside **public key authentication** and other hardening.
- Keep your knock sequence secret to prevent unauthorized access.
- Test in **lab environments** before deploying publicly.

---

## Author
**Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
