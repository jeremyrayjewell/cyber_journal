# Advent of Cyber 2025 – Day 24, 2025-12-24
**Room:** Exploitation with cURL – Hoperation Eggsploit \
**Category:** Web Exploitation / HTTP Fundamentals  \
**Skills Practiced:** Raw HTTP interaction, cURL usage, POST requests, session handling, cookie replay, User-Agent manipulation, basic brute forcing

---

## Summary
Day 24 focused on **interacting with web applications using only the command line**, specifically through **cURL**. Without access to a browser or interception tools, the task demonstrated how attackers and defenders alike can manually craft HTTP requests, inspect server responses, manage sessions via cookies, and automate interactions. The exercise reinforced that HTTP is a simple, text-based protocol and that many common web attacks are fundamentally just scripted request/response exchanges.

---

## Walkthrough Notes

### 1. Speaking HTTP Without a Browser

The first step was to interact with the target web server using a basic HTTP GET request: `curl http://MACHINE_IP/`. This sent a raw GET request and returned the server’s HTML response directly in the terminal. Without rendering, the response still exposed application structure and hints about available endpoints. This established that browsers are not required to understand or exploit web applications.

---

### 2. Submitting Data with POST Requests

Next, POST requests were sent to backend endpoints to simulate form submissions: `curl -X POST -d "username=admin&password=admin" http://MACHINE_IP/post.php`. This demonstrated how form data is transmitted as URL-encoded key-value pairs in the request body. The server response revealed whether authentication succeeded and returned the first flag. Adding the `-i` flag showed full HTTP responses, including headers, which is critical when identifying redirects, cookies, or server behavior changes.

---

### 3. Session Handling with Cookies

Authentication was followed by session handling using cookies. Because cURL does not automatically store cookies, they were explicitly saved and reused:
```
curl -c cookies.txt -d "username=admin&password=admin" http://MACHINE_IP/cookie.php
curl -b cookies.txt http://MACHINE_IP/cookie.php
```
This mimicked how browsers maintain session state and demonstrated how session replay works at a protocol level. Reusing the saved cookie allowed access to protected functionality and returned the second flag.

---

### 4. Automating Login Attempts (Brute Force)

A simple brute-force attack was implemented using a Bash loop and cURL:
```
for pass in $(cat passwords.txt); do
  response=$(curl -s -X POST -d "username=admin&password=$pass" http://MACHINE_IP/bruteforce.php)
  if echo "$response" | grep -q "Welcome"; then
    echo "[+] Password found: $pass"
    break
  fi
done
```
This demonstrated how automated credential attacks are simply repeated HTTP POST requests with variable input and response comparison. The successful password was identified by a difference in the response body rather than status codes.

---

### 5. Bypassing User-Agent Restrictions

Some endpoints enforced access controls based on the User-Agent header. A default cURL request failed, while a spoofed User-Agent succeeded: `curl -A "TBFC" http://MACHINE_IP/agent.php`. This highlighted how weak client-side assumptions can be abused and how easily HTTP headers can be manipulated. The response returned the next flag.

---

### 6. Bonus Mission (Optional)

The optional final mission required chaining all learned techniques:
- Endpoint discovery
- Authentication
- Cookie handling
- Brute forcing credentials
- Submitting authorized requests to close the wormhole
This simulated a realistic control-panel takeover using nothing more than command-line HTTP interaction.

---

## Key Takeaways
- HTTP is a simple, text-based protocol that can be fully controlled from the command line
- cURL provides precise control over request methods, headers, body data, and cookies
- Web authentication and sessions rely heavily on cookies that can be replayed
- Brute-force attacks are fundamentally repeated HTTP requests with response analysis
- User-Agent and header-based access controls are trivial to bypass
- Many “advanced” web attacks reduce to basic request automation

---

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell) | [LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
