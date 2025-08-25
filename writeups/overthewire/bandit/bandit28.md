# Write-up: Bandit 28 → 29
**Date:** 2025-08-20

## Obfuscated password (ROT13) 
`4cG1g5QRAnLhdadinqLf1bR4DYPqwzW7`

## OBJECTIVE
> "There is a git repository at `ssh://bandit28-git@localhost/home/bandit28-git/repo` via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.
>
> Clone the repository and find the password for the next level."

## PURPOSE

We need to clone a Git repository over **SSH on port 2220** using the **bandit28** password (for user `bandit28-git`). The trick for this level is that the current files don’t show the password; it’s hidden in the **commit history**. Practical notes:

- **Custom SSH port** in Git URLs: include it explicitly → `ssh://user@host:PORT/path`.
- You’ll authenticate as `bandit28-git` with the **same password** as `bandit28`.
- After cloning, check the **history** with `git log` and view prior content with:
  - `git log -p` (shows diffs including removed lines),
  - or `git show <commit>` (see a specific commit’s diff),
  - or `git show <commit>:<path>` (print a file’s full contents at that commit),
  - or `git checkout <commit>` then `cat` the file.
- Typical pattern: a commit message like “fix leak” or “remove password from README” — the previous commit still contains it.
- Git uses a pager (usually `less`); `/password` searches inside `git log` output.

## SOLUTIONS
- Clone the repo over SSH on port 2220 (accept host key if prompted):
  ```bash
  git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
  ```
- Enter the **bandit28** password when asked (it’s also the password for `bandit28-git`).
- Inspect the repo:
  ```bash
  cd repo
  ls -la
  ```
- Look through history and find the commit that removed the password:
  ```bash
  git log -p
  ```
  *(Scroll; look for a line revealing the password in a prior version of the file, e.g., README.)*

  **Or** list concise history, then open a specific commit:
  ```bash
  git log --oneline
  git show <commit-hash>
  ```
  **Or** print the older file contents directly:
  ```bash
  git show <commit-hash>:README
  ```
- Copy the revealed **bandit29** password, and (optionally) ROT13 it into the header of this write-up.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
