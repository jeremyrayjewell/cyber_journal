#!/usr/bin/env python3
"""
Minimal terminal chat for NoFilterGPT.

Prereqs (Arch Linux):
    sudo pacman -S --needed python-requests python-dotenv python-colorama
or (inside a venv):
    pip install requests python-dotenv colorama
"""

import os
import sys
import signal
import requests
from pathlib import Path
from colorama import Fore, Style, init
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# 0. Load API key from .env or environment variable
# ---------------------------------------------------------------------------

# If there's a .env file alongside this script, load it
env_path = Path(__file__).with_name(".env")
if env_path.exists():
    load_dotenv(env_path)

API_KEY = os.getenv("NOFILTERGPT_API_KEY")
if not API_KEY:
    sys.exit("❌  Set NOFILTERGPT_API_KEY in .env or export it before running.")

# ---------------------------------------------------------------------------
# 1. Constants
# ---------------------------------------------------------------------------

API_ENDPOINT = "https://api.nofiltergpt.com/v1/chat/completions"

# Nice terminal colours
init(autoreset=True)
USER_COLOR = Fore.CYAN + Style.BRIGHT
BOT_COLOR  = Fore.GREEN

# ---------------------------------------------------------------------------
# 2. Helper: send prompt to API and return assistant message
# ---------------------------------------------------------------------------

def send_to_api(prompt: str) -> str:
    """
    POST `prompt` to NoFilterGPT and return the assistant's reply text.

    Raises RuntimeError on any network or API error.
    """
    url = f"{API_ENDPOINT}?api_key={API_KEY}"

    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",   "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 150,
        "top_p": 1
    }

    try:
        resp = requests.post(url, json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except (requests.RequestException, ValueError, KeyError) as exc:
        raise RuntimeError(f"API request failed: {exc}") from exc

# ---------------------------------------------------------------------------
# 3. Graceful Ctrl-C exit
# ---------------------------------------------------------------------------

def graceful_exit(_sig=None, _frame=None):
    print("\n👋  Bye!")
    sys.exit(0)

signal.signal(signal.SIGINT, graceful_exit)

# ---------------------------------------------------------------------------
# 4. Main REPL loop
# ---------------------------------------------------------------------------

def main() -> None:
    print("🔌  Connected to NoFilterGPT. Type your message (Ctrl-C to quit).")
    while True:
        try:
            user_in = input(f"{USER_COLOR}> {Style.RESET_ALL}")
            if not user_in.strip():
                continue
            bot_out = send_to_api(user_in.strip())
            print(f"{BOT_COLOR}{bot_out}{Style.RESET_ALL}")
        except RuntimeError as err:
            print(Fore.RED + str(err))

if __name__ == "__main__":
    main()
