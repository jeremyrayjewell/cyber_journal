# NoFilterGPT CLI Chat

A tiny cross-platform Python script that lets you chat with the **NoFilterGPT** API from any terminal.

## Features
- Sends prompts to the official `v1/chat/completions` endpoint.  
- Reads your API key from a local `.env` file (kept out of Git).  
- Works on Linux, macOS, and Windows (Python ≥ 3.8).  
- Colorful prompt/response display and graceful **Ctrl-C** exit.

## Dependencies
- Python 3.8+
- requests
- python-dotenv
- colorama

Install dependencies with:
```bash
pip install -r requirements.txt
# ── or ──
pip install requests python-dotenv colorama
```

## Quick Start
```bash
# Clone repository
git clone https://github.com/yourname/nofiltergpt-chat.git
cd nofiltergpt-chat

# Add your API key (no quotes)
echo NOFILTERGPT_API_KEY=PASTE_KEY_HERE > .env

# Install dependencies (choose one method)
pip install -r requirements.txt              # Inside a virtualenv
# ── or ──
sudo pacman -S python-requests python-dotenv python-colorama   # Arch system-wide

# Run the client
python chat_client.py
```

## Script Overview
- **chat_client.py** — Main REPL client.  
- **.env** — Stores your API key (ignored by Git).  
- **requirements.txt** — Python dependencies (`requests`, `python-dotenv`, `colorama`).

## Troubleshooting
- **Invalid API Key:** Regenerate or re-paste the key; ensure `.env` is loaded.  
- **404 Not Found:** Check the endpoint constant in the script.

## License
MIT

## Author
**Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
