# NoFilterGPT CLI Chat

A tiny cross-platform Python script that lets you chat with the **NoFilterGPT** API from any terminal.

---

## Features

* Sends prompts to the official `v1/chat/completions` endpoint  
* Reads your API key from a local `.env` file (kept out of Git)  
* Works on Linux, macOS and Windows (Python ≥ 3.8)  
* Colorful prompt/response and graceful **Ctrl-C** exit  

---

## Quick start

```bash
# Clone
git clone https://github.com/yourname/nofiltergpt-chat.git
cd nofiltergpt-chat

# Add your key (no quotes)
echo NOFILTERGPT_API_KEY=PASTE_KEY_HERE > .env

# Install deps (pick one)
pip install -r requirements.txt              # inside a venv   ──or──
sudo pacman -S python-requests python-dotenv python-colorama   # Arch system-wide

# Run
python chat_client.py


## Script overview

chat_client.py   ← main REPL client  
.env             ← your API key (ignored by Git)  
requirements.txt ← requests, python-dotenv, colorama

## Troubleshooting

Invalid API Key:	Regenerate or re-paste the key; ensure .env is loaded.
404 Not Found:		Check the endpoint constant in the script.

## License:
MIT
::contentReference[oaicite:0]{index=00}


---

## By: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
