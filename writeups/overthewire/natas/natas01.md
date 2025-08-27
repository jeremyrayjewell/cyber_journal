# Write-up: Natas 01 → 02  
**Date:** 2025-08-27  

## Obfuscated password (ROT13)

GthZAkXb1QFn1ghwOYhMWaQHyPpHNCyV

## OBJECTIVE

> "You can find the password for the next level on this page, but right-clicking has been blocked!"

## PURPOSE ##

This level introduces a common anti-inspection “defense”: disabling right-click to discourage **View Source**. It’s purely cosmetic. Client-side restrictions (JavaScript handlers, context-menu blockers) don’t prevent access to HTML, CSS, or JS that the browser has already downloaded. You can always inspect with:
- **Developer Tools** (Ctrl+Shift+I / F12), **Elements** tab to read the live DOM.  
- **View Source via keyboard** (Ctrl+U / ⌘+Option+U).  
- **curl** / **wget** to fetch and read the HTML directly.

## SOLUTIONS ##

### Method 1: Browser DevTools
- Open the level and authenticate as **natas1**.  
  URL: `http://natas1.natas.labs.overthewire.org`  
  Username: `natas1`  

- Right-click is disabled, but DevTools still works: press **Ctrl+Shift+I** (or **F12**), then select the **Elements** (Inspector) panel.  

- Scan the HTML. A developer **HTML comment** contains the next password:  
  `<!--The password for natas2 is [REDACTED] -->`  

- Use that password to authenticate as **natas2**.  

---

### Method 2: curl / wget
- Instead of using the browser, you can fetch the page source directly:  
    `curl -u natas1:<password-for-natas1> http://natas1.natas.labs.overthewire.org/` 
    `wget --http-user=natas1 --http-password=<password-for-natas1> -O natas1.html http://natas1.natas.labs.overthewire.org/`   

- The output contains the same HTML as the browser. Searching through it reveals the comment with the next level’s password.  

- This proves that **blocking right-click doesn’t protect anything**—if the browser can see it, so can you.  

___

Writeup author: **Jeremy Ray Jewell**  
[GitHub](https://github.com/jeremyrayjewell)  
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
