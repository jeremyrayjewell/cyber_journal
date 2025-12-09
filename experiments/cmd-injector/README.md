# cmd_injector.sh — Command Injection Testing Tool

This is a minimal Bash script for testing command injection vulnerabilities via HTTP GET parameters.  
It automates sending payloads to a user‑supplied target with optional HTTP Basic Authentication.

## Usage

```bash
./cmd_injector.sh \
  --target "http://target.url" \
  --auth "username:password" \
  --payload ";sh -c 'cat /etc/passwd'"
```
## Options
| Flag                   | Description                                    |
|------------------------|------------------------------------------------|
| `--target`             | Full URL to test (including query string)      |
| `--auth`               | Basic auth in the form username:password       |
| `--payload`            | Command injection payload to test              |

## Notes
- The script currently tests a single payload per execution.
- Injection is performed through a `needle= GET` parameter.
- Responses are printed directly to `stdout`.

## License

MIT License

## Author

Jeremy Ray Jewell  
[Github](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyyrayjewell
