# Write-up: Bandit 30 → 31
**Date:** 2025-08-22

## Obfuscated password (ROT13) 
`so5F2ko7oElSzNiDLDTRdfouIlWduaQl`

## OBJECTIVE
> "There is a git repository at `ssh://bandit30-git@localhost/home/bandit30-git/repo` via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.
>
> Clone the repository and find the password for the next level."

## PURPOSE

Clone a Git repository over **SSH on port 2220** using the **bandit30** password (for user `bandit30-git`). In this level, the password is **not** in the working tree or the main branch; it’s stored in a **Git tag** (metadata attached to a commit). Notes:

- **Custom port in Git SSH URLs:** include it explicitly → `ssh://user@host:PORT/path`.
- **Auth:** when prompted for `bandit30-git`, use the **bandit30** password.
- **Tags vs branches:**  
  - *Branches* move; they point to the “current line” of development.  
  - *Tags* are static references, often used for releases or markers, and can carry **messages**.
- **Annotated vs lightweight tags:**  
  - *Annotated* tags store an object with **author, date, and message**.  
  - *Lightweight* tags are just pointers with no message.  
  - The password is typically in an **annotated tag’s message**.
- **How to find/read tags:**  
  - List tags: `git tag` or `git tag -n` (shows first line of messages).  
  - Show full contents of a tag: `git show <tag>` (prints the tag message and referenced commit).  
  - Low-level view: `git cat-file -p <tag>`.

## SOLUTIONS
- Clone the repo (accept host key if asked) and enter the **bandit30** password when prompted:
  ```bash
  git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
  ```
- Inspect the repository and list tags:
  ```bash
  cd repo
  ls -la
  git tag -n99
  ```
- Show each tag until you find the password in the tag message (common tag names include things like `secret` or similar):
  ```bash
  git show <tagname>
  # or low-level:
  git cat-file -p <tagname>
  ```
- Copy the revealed **bandit31** password, and (optionally) ROT13 it into the header of this write-up.

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) • [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
