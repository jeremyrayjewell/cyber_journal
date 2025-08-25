# Write-up: Bandit 31 → 32
**Date:** 2025-08-23

## Obfuscated password (ROT13) 
`3B9EsudlNyIORMcIo6YLFgfuMbdbFk5X`

## OBJECTIVE
> "There is a git repository at `ssh://bandit31-git@localhost/home/bandit31-git/repo` via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.
>
> Clone the repository and find the password for the next level."

## PURPOSE

This level teaches **Git over SSH (custom port)** and interacting with a repo that contains **instructions to push a file**. The trick is that the repo’s **`.gitignore` ignores `*.txt`**, so you must **force-add** the required file before you can commit/push. When you push, the remote runs a **pre-receive hook** that validates your submission: it **prints the password** for the next level and then **rejects** the push (that rejection is *expected*). :contentReference[oaicite:0]{index=0}

Key notes:
- Use the SSH URL with a **port**: `ssh://user@host:PORT/path`.
- Authenticate as `bandit31-git` using the **same password** as `bandit31`.
- Read `README.md` in the repo; it tells you to create **`key.txt`** with content **`May I come in?`** on **branch `master`**. :contentReference[oaicite:1]{index=1}
- `.gitignore` contains `*.txt`, so normal `git add key.txt` is ignored; use **`git add -f key.txt`** (or delete `.gitignore`, but force-adding is cleaner). :contentReference[oaicite:2]{index=2}
- On push, a server hook prints a “Well done!” banner and the **bandit32 password**, then declines the push via **pre-receive hook**; you still have the password in the push output. :contentReference[oaicite:3]{index=3}

## SOLUTIONS
- **Clone the repo (accept host key if prompted):**
  ```bash
  git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
  cd repo
  ls -la
  cat README.md
  ```
  *(README instructs: create `key.txt` with `May I come in?` on branch `master`.)* :contentReference[oaicite:4]{index=4}

- **Create the required file and handle `.gitignore`:**
  ```bash
  printf 'May I come in?\n' > key.txt
  cat .gitignore            # shows: *.txt
  git add -f key.txt        # force-add despite .gitignore
  ```
  *(Alternative: `rm .gitignore` then `git add key.txt`, but force-add is preferred.)* :contentReference[oaicite:5]{index=5}

- **Commit (set identity if Git asks) and push:**
  ```bash
  git config user.email 'bandit31@bandit'
  git config user.name  'bandit31'

  git commit -m "Add key.txt as instructed"
  git push origin master
  ```
  During `git push`, the remote prints a banner with the **bandit32 password** and then rejects the push via a **pre-receive hook** — this is expected; copy the password from that output. :contentReference[oaicite:6]{index=6}

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
