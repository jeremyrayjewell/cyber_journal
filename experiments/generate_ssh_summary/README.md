# SSH Summary Generator

A Python utility that turns raw SSH debug logs into a Markdown table for quick review and analysis.

## Features
- Reads `~/ssh-logs/` for SSH debug log files.
- Extracts key session details (host, command, outcome, notes).
- Outputs a `~/ssh-summary.md` file formatted as a Markdown table.

## Requirements
- Python 3.6+
- SSH debug logs located in `~/ssh-logs/`
- `chmod +x` permission on the script

## Usage
From the `generate_ssh_summary` directory:

cd experiments/generate_ssh_summary  
chmod +x generate_ssh_summary.py  
./generate_ssh_summary.py  
cat ~/ssh-summary.md  

## Example Output
| Host      | Command/Flags        | Outcome           | Notes                   |
|-----------|----------------------|-------------------|-------------------------|
| bandit0   | ssh -v bandit0 ...   | Auth succeeded    | Used password auth ...  |
| kali-lab  | ssh -vvv kali@...    | Auth succeeded    | Verified host keys ...  |

## Notes
- Works best with SSH logs generated using `ssh -v`, `ssh -vv`, or `ssh -vvv`.
- Script overwrites `~/ssh-summary.md` each run.

## Author
Jeremy Ray Jewell  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
