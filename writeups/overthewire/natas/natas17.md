# Write-up: Natas 17 → 18  
**Date:** 2025-12-30  

## Obfuscated password (ROT13)  
`6BT1CoXqIwlOycktQ4QQoET6MYyPTtPW`

---

## OBJECTIVE

> The objective of this level was to extract the password for natas18 from a vulnerable web application that does not display query results directly. Instead, the application only reveals whether a SQL condition evaluates to true or false, requiring a blind SQL injection approach.
> 
---

## PURPOSE

The purpose of this challenge was to demonstrate how blind SQL injection vulnerabilities can be exploited using timing-based inference, even when no output is returned to the user. This level specifically tests the ability to:
- Identify a timing side channel
- Construct conditional SQL payloads
- Automate extraction reliably under latency
- Avoid false positives through proper calibration
To solve it cleanly, I reworked my existing blind SQL extraction tool to support time-based inference, adaptive thresholds, and consistent output formatting.

---

## SOLUTION

The target endpoint accepts a `username` parameter that is interpolated directly into a SQL query. While the application never reveals query results, it does execute conditional logic. By injecting a payload of the form `' AND IF(SUBSTRING(password, N, 1) = 'a', SLEEP(2), 0) --` it becomes possible to infer the correctness of a guess based on the response time.

### Tool Improvements

To solve this level reliably, I extended my existing [blind SQL extractor](https://github.com/jeremyrayjewell/cyber_journal/tree/main/experiments/blind_sqli_extractor) with:
- A dedicated time-based attack mode
- Median-based timing analysis to reduce noise
- Configurable sleep intervals and thresholds
- Unified output formatting for both boolean and timing attacks
The tool now performs the following steps:
- Measures baseline response time.
- Iterates over each character position.
- Tests candidate characters using conditional delays.
- Records the character when the delay exceeds the threshold.
- Repeats until the full password is recovered.

---

## TAKEAWAYS

- Blind SQL injection remains viable even when applications suppress output.
- Time-based attacks require careful threshold calibration to avoid false positives.
- Automating inference logic is essential for reliability and repeatability.
- Building reusable tooling significantly improves efficiency across similar challenges.

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
