# Write-up: Natas 16 → 17  
**Date:** 2025-12-29  

## Obfuscated password (ROT13)  
`RdwUWob7YSAo8ijuUo9f75ubxu5GS0BP`

---

## OBJECTIVE

> Extract the password for the user `natas17` by exploiting a command injection vulnerability in the Natas 16 challenge, despite character filtering intended to block shell execution.

---

## PURPOSE

This challenge demonstrates how blacklist-based input filtering is insufficient for preventing command injection. Even when common shell metacharacters are blocked, alternative execution mechanisms can still be abused. The goal is to identify and exploit such a weakness to retrieve sensitive data.

---

## SOLUTION

The application passes user input directly into a shell command using `passthru()`:

```php
passthru("grep -i "$key" dictionary.txt");
```

Although certain characters are filtered, command substitution using $() remains possible. This allows user-controlled input to be evaluated by the shell before the grep command is executed. By injecting payloads such as `$(grep ^a /etc/natas_webpass/natas17)`, the shell evaluates the inner command first. If the guessed prefix matches the beginning of the target password, the inner grep produces output; otherwise, it produces none. That output (or lack of it) is then substituted into the surrounding grep command.

This difference in behavior becomes observable, allowing the attacker to determine whether a given prefix is correct. By repeating this process character by character, the password can be reconstructed incrementally.

The attack is automated using a [custom script (blind_command_injector.py)](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/blind_command_injector) that iterates through candidate characters and detects changes in command output to infer correctness.

Command:
```
python blind_command_injector.py \
  --url "http://natas16.natas.labs.overthewire.org/" \
  --param "needle" \
  --payload-template '$(grep ^{guess} /etc/natas_webpass/natas17)' \
  --charset "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" \
  --max-length 32 \
  --auth "natas16:<PASSWORD>"
```

---

## TAKEAWAYS

- Blacklist-based filtering is insufficient for preventing command injection
- Shell command substitution can be abused even when direct command execution appears restricted
- Behavioral side effects can leak sensitive information without direct output
- Proper input handling and avoiding shell invocation are critical for secure design 

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
