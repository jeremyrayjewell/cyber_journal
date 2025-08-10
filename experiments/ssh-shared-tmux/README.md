# SSH Shared-Tmux Scripts

Scripts for opening an SSH port, starting an `sshd` server, and creating a shared `tmux` session that multiple clients can attach to. Useful for collaborative terminal work in a lab environment.

## Features
- Opens a configurable SSH port (default: `443`).
- Starts and enables the SSH server (`sshd`).
- Creates a named `tmux` session (default: `shared`).
- Prints connection instructions both to the server shell and inside the tmux session.
- Includes a disconnect script to close SSH access and block the port.

## Dependencies
- **tmux**
- **OpenSSH server** (`sshd`)
- **iptables** (or compatible firewall package)
- **curl**
- Linux system with `systemctl` (systemd)

Install dependencies on Arch-based systems:
```bash
sudo pacman -S tmux openssh iptables curl
```

On Debian/Ubuntu:
```bash
sudo apt install tmux openssh-server iptables curl
```

## Files
- **sshconnect.sh** — Opens the port, starts SSH and tmux, prints connection instructions, and attaches the server terminal to the session.
- **sshdisconnect.sh** — Stops SSH, detaches all clients, and blocks the port.

## Usage

### On the server:
```bash
cd experiments/ssh-shared-tmux
chmod +x sshconnect.sh sshdisconnect.sh
./sshconnect.sh
```

### On a client:
```bash
ssh -t -p 443 <user>@<server-ip> tmux attach -t shared
```

## Safety Note
This setup is **intended for lab use**.  
For internet-facing deployments:
- Restrict SSH logins with `AllowUsers` in `/etc/ssh/sshd_config`.
- Use public key authentication instead of passwords.
- Consider using a firewall with IP whitelisting.

## Author
Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
