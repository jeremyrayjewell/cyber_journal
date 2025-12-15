# Advent of Cyber 2025 – Day 14, 2025-12-14 
**Room:** Container Security – DoorDasher / Hopperoo \
**Category:** Container Security / Docker Exploitation \
**Skills Practiced:** Docker fundamentals, container vs VM architecture, Docker socket abuse, container escape, privilege escalation, incident recovery.

---

## Summary

Day 14 focused on **container security and Docker runtime abuse** through a realistic incident response scenario. A food delivery platform, DoorDasher, had been defaced and rebranded as Hopperoo after attackers gained control. Although the primary engineer was locked out, the SOC team still had access via an **uptime-checker container**.

The objective was to investigate running Docker services, identify misconfigurations, escape a restricted container via the Docker socket, escalate privileges, and execute a recovery script to restore the service. This challenge demonstrated how **container isolation is not equivalent to security** when runtime controls are misconfigured.

---

## Walkthrough Notes

### Environment Setup

Both the **Target Machine** and **AttackBox** were started. The target system dropped me into a shell as the `mrbombastic` user. Initial reconnaissance confirmed Docker was installed and actively running multiple containers.

### 1. Enumerating Running Containers

I began by listing active Docker containers to understand the environment: `docker ps`. This revealed several services, including:
- the defaced web application running on port 5001
- an uptime-checker container
- a deployer container
Visiting the web app confirmed the Hopperoo defacement.

---

### 2. Accessing the Monitoring Container & Confirming Docker Escape Capability

The uptime-checker container appeared non-critical but had shell access: `docker exec -it uptime-checker sh`. Inside the container, I inspected Docker socket access: `ls -la /var/run/docker.sock`. The socket was **mounted and accessible**, meaning the container could communicate directly with the Docker daemon. This is a major security flaw. Access to the Docker socket is effectively equivalent to root access on the host.

To validate the impact, I attempted Docker commands from inside the container: `docker ps`.  The command succeeded, confirming full Docker API access from within the container. At this point, a container escape was possible.

---

### 3. Escalating to a Privileged Container & Restoring the Service

Rather than creating a new container, I pivoted directly into the privileged deployer container: `docker exec -it deployer bash`. Running `whoami` confirmed elevated privileges inside the container. Exploring the filesystem revealed the recovery script intended to restore DoorDasher.

With privileged access, I executed the recovery script: `sudo /recovery_script.sh`. Refreshing the site on port 5001 confirmed the DoorDasher service was restored successfully. A completion flag was located in the same directory as the script and retrieved with cat.

---

### Bonus Discovery
A secondary service running on port 5002 contained a hidden message. The message doubled as the password for the deployer user, highlighting poor credential hygiene and the risk of embedding secrets directly in application content.

---

## Key Takeaways
- Containers provide isolation, not security, by default.
- Mounting `/var/run/docker.sock` inside a container grants full control over the Docker host.
- Docker socket access is effectively root-level access.
- Monitoring or utility containers are common escalation paths.
- Principle of least privilege applies strongly to container environments.
- Secrets should never be embedded in application content or images.
- Container misconfigurations can completely bypass host security controls.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
