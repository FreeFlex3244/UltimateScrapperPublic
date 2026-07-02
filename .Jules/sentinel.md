## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-07-02 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper validates URLs using `is_safe_url` but then uses `requests.get` with default redirect behavior.
**Learning:** Even if the initial URL is safe, the server can return a 30x redirect to an internal IP (like localhost), which `requests.get` will follow, bypassing the `is_safe_url` check.
**Prevention:** Always set `allow_redirects=False` or implement a custom redirect handler that validates every redirect target against security policies.
