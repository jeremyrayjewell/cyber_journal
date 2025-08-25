# Write-up: Bandit 27 → 28
**Date:** 2025-08-19

## Obfuscated password (ROT13) 
`Lm9VcY0fOpPrhT7z9hDSg8MAcF4UMEpA`

## OBJECTIVE
> "There is a git repository at `ssh://bandit27-git@localhost/home/bandit27-git/repo` via the port 2220. The password for the user `bandit27-git` is the same as for the user `bandit27`.
>
> Clone the repository and find the password for the next level."

## PURPOSE

We must clone a Git repository over **SSH on nonstandard port 2220**, using **bandit27’s password** when prompted for `bandit27-git`. After cloning, inspect the repo (usually a `README`) to retrieve the **bandit28** password.

Notes:
- For Git over SSH with a custom port, include the port in the URL:  
  `ssh://user@host:PORT/path`
- If prompted to add the host to `known_hosts`, answer **yes**.

## SOLUTIONS
- Clone the repo over SSH on port 2220:  
  `git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo`
- Enter the **bandit27** password when asked (same password for `bandit27-git`).
- Change into the repo and list files:  
  `cd repo`  
  `ls -la`
- Read the contents (typically a README with the password):  
  `cat README`

*(If there’s no obvious file, also try: `git log -p`, `git show`, or look for other tracked files.)*

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)

