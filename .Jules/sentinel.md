## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-18 - XSS in client-side search results rendering
**Vulnerability:** A SyntaxError orphaned safe `textContent` DOM node creation, falling back to a dangerous `innerHTML` rendering of `file.filename` in `src/static/script.js`.
**Learning:** Orphaned code outside `forEach` loops can mask intended secure implementations and leave dangerous `innerHTML` implementations active.
**Prevention:** Always verify DOM nodes are constructed with `textContent` for untrusted user inputs instead of `innerHTML`, and use `node -c` for immediate client-side JS syntax checking.
