# Advent of Cyber 2025 – Day 1  
**Room:** Linux CLI – Shells Bells  
**Category:** Linux Fundamentals  
**Skills Practiced:** Basic Linux commands, navigation, reading files, SSH, terminal usage

---

## Summary
This day introduces the Linux command-line interface (CLI) and uses a fictional scenario involving McSkidy and the TBFC team. The goal is to learn to navigate the filesystem, understand simple Linux utilities, and begin uncovering what happened before McSkidy disappeared.

The room provides a Linux virtual machine where you use common shell tools to explore tbfc-web01, a server that processes Christmas wishlists. The focus is on foundational skills: using `ls`, `cd`, `cat`, understanding file paths, and examining system structure.

---

## Walkthrough Notes

### **Connecting to the Machine**
You can connect in two ways:
1. Using the THM split-view terminal (automatic when starting the machine)
2. Using SSH from your own machine:
```bash
ssh mcskidy@MACHINE_IP
# password: AoC2025!
```

### **Key navigation and inspection commands used**
Typical commands for this room include:

```bash
ls -la
pwd
cd /path
cat filename
grep -r "keyword" .
```

These allow you to:
- Inspect directories
- View hidden files
- Search recursively
- Read logs or configuration files

### **Goal**
Explore directories related to wishlist processing to find early clues about McSkidy’s last interactions and King Malhare’s involvement.

Because this is Day 1, the tasks focus on getting comfortable with:
- filesystem layout
- recognizing important directories (`/home`, `/etc`, `/var`)
- using the CLI to reveal information

---

## Key Takeaways
- Linux navigation is essential for both attackers and defenders.
- The CLI gives deeper visibility and control than any GUI.
- Knowing how to explore files, read configs, and move through the system is foundational for future challenges.
- SSH allows remote access to Linux machines exactly like this — a common real-world workflow.

---

## Answers
No answer needed for Task 1 (environment setup).

Other answers (non-proprietary summaries only) will go here after completing the CLI exercises.

___

Writeup author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
