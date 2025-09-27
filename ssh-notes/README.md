# SSH Weekly Notes

A lightweight, automated lab notebook capturing hands-on SSH sessions, key takeaways, and next steps.

Every week, I aim to generate concise, reproducible notes of my SSH work, focusing on:

* **Sessions**: Hosts connected, commands/flags used, outcomes, and relevant notes (e.g., negotiated ciphers, log filenames).
* **Takeaways**: What you learned, patterns spotted, and insights for future sessions.
* **Next Steps**: Planned experiments, automation improvements, or new targets to explore.

---


## Directory Structure

```
│  cyber_journal/
│  ├── ssh-notes/             # Weekly Markdown notes
│  │   ├── ssh-week-2025-08-07.md
│  │   └── cipher-reference.md
│  └── experiments/           # Automation scripts and experiments
│       └── generate_ssh_summary/
│             └── generate_ssh_summary.py
└── ssh-logs/              # Raw SSH debug logs (outside the repo)
```

## Automation

Use the `generate_ssh_summary.py` script to compile all `~/ssh-logs/*.log` into a Markdown table (`~/ssh-summary.md`) with host, command, and outcome.

```bash
./experiments/generate_ssh_summary/generate_ssh_summary.py
cat ~/ssh-summary.md
```

No private paths or usernames are hard-coded—logs are read from `~/ssh-logs`, and the summary is saved to `~/ssh-summary.md`.

## Author

**Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
