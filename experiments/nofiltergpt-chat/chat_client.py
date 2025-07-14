#!/usr/bin/env python3
"""
chat_client.py – Terminal chat client for NoFilterGPT
- Keeps full conversation history (basic “memory”)
- Works on Linux, macOS, Windows (Python ≥ 3.8)

Deps: requests, python-dotenv, colorama
"""

import os
import sys
import signal
import requests
from pathlib import Path
from colorama import Fore, Style, init
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# 0. Load API key from .env or environment
# ---------------------------------------------------------------------------
env_path = Path(__file__).with_name(".env")
if env_path.exists():
    load_dotenv(env_path)

API_KEY = os.getenv("NOFILTERGPT_API_KEY")
if not API_KEY:
    sys.exit("❌  Set NOFILTERGPT_API_KEY in .env or export it before running.")

# ---------------------------------------------------------------------------
# 1. Constants & colour setup
# ---------------------------------------------------------------------------
API_ENDPOINT = "https://api.nofiltergpt.com/v1/chat/completions"
SYSTEM_MSG   = {"role": "system", "content": "You are a helpful assistant."}

init(autoreset=True)
USER_COLOR = Fore.CYAN + Style.BRIGHT
BOT_COLOR  = Fore.GREEN
ERR_COLOR  = Fore.RED + Style.BRIGHT

# ---------------------------------------------------------------------------
# 2. Conversation history (starts with system prompt)
# ---------------------------------------------------------------------------
history = [SYSTEM_MSG]          # list of dicts, grows each turn

def send_to_api(user_text: str) -> str:
    """Add user_text to history, send to API, append assistant reply, return reply."""
    history.append({"role": "user", "content": user_text})

    url = f"{API_ENDPOINT}?api_key={API_KEY}"
    payload = {
        "messages": history,
        "temperature": 0.7,
        "max_tokens": 150,
        "top_p": 1
    }

    try:
        resp = requests.post(url, json=payload, timeout=20)
        resp.raise_for_status()
        assistant_text = resp.json()["choices"][0]["message"]["content"].strip()
    except (requests.RequestException, ValueError, KeyError) as exc:
        raise RuntimeError(f"API request failed: {exc}") from exc

    history.append({"role": "assistant", "content": assistant_text})
    return assistant_text

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
    print("🔌  Connected to NoFilterGPT (conversation memory enabled). Ctrl-C to quit.")
    while True:
        try:
            user_in = input(f"{USER_COLOR}> {Style.RESET_ALL}")
            if not user_in.strip():
                continue
            bot_out = send_to_api(user_in.strip())
            print(f"{BOT_COLOR}{bot_out}{Style.RESET_ALL}")
        except RuntimeError as err:
            print(ERR_COLOR + str(err))

if __name__ == "__main__":
    main()

