## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-07-05 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper implemented URL safety checks (`is_safe_url`) but then fetched the URLs with `requests.get()` using default behavior, which follows redirects. A malicious site could return a 302 redirect to a local IP (e.g., `127.0.0.1`), bypassing the initial pre-fetch check and achieving Server-Side Request Forgery.
**Learning:** Safety checks on URLs must be coupled with strict HTTP client configuration (like disabling redirects) to ensure the destination actually fetched is the one that was validated.
**Prevention:** Always set `allow_redirects=False` in `requests` or implement a custom redirect handler that recursively verifies the safety of `Location` header targets before following them.
