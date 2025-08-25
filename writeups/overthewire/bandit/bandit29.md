# Write-up: Bandit 29 → 30
**Date:** 2025-08-25

## Obfuscated password (ROT13) 
`dc30rk3IYm5ZQT1a91LbjGi4D8y7PQMY`

## OBJECTIVE
> "There is a git repository at `ssh://bandit29-git@localhost/home/bandit29-git/repo` via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.
>
> Clone the repository and find the password for the next level."

## PURPOSE

Clone a Git repository over **SSH on port 2220** using the **bandit29** password (for user `bandit29-git`). In this level the password is **not** in the current working tree on the default branch; it’s stored on a **different branch**. Key notes and tactics:

- **Custom SSH port:** include it in the URL: `ssh://user@host:PORT/path`.
- **Auth:** when prompted for `bandit29-git`, use the **bandit29** password.
- After cloning, list **all branches** (local + remote) with `git branch -a`.
- Remote branches appear under `remotes/origin/...`. To read their files you can:
  - **Switch/track that branch** (classic):  
    `git checkout -b <name> origin/<name>` then `cat` the file.
  - **Or** inspect a file **without switching**:  
    `git show origin/<name>:README` (or whichever file holds the password).
- Helpful views:
  - `git log --oneline --decorate --graph --all` to see all branch tips.
- The password is typically in a small text file (often `README` / `README.md`) on the non-default branch.

## SOLUTIONS
- Clone the repo over SSH on port 2220:
  ```bash
  git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
  ```
- Enter the **bandit29** password when asked.
- Explore and locate the right branch:
  ```bash
  cd repo
  ls -la
  git branch -a
  ```
- Option A — **Switch** to the remote branch and read the file:
  ```bash
  git checkout -b <branch> origin/<branch>
  ls -la
  cat README
  ```
- Option B — **Show** the file directly from the remote branch (no switch):
  ```bash
  git show origin/<branch>:README
  ```
- Copy the revealed **bandit30** password and (optionally) ROT13 it into the header of this write-up.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
