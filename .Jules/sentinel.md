## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2026-06-25 - Fix SSRF bypass via HTTP redirects
**Vulnerability:** The scraper explicitly checks `is_safe_url` to prevent scraping local/private networks, but it allows `requests.get` to automatically follow HTTP redirects. A malicious external server could redirect the scraper to a local IP address (e.g. `http://127.0.0.1`), bypassing the initial check.
**Learning:** `requests.get` follows redirects by default. Security checks on initial URLs can be easily bypassed if the HTTP client blindly follows redirects to unverified targets.
**Prevention:** Always disable automatic redirects when fetching user-supplied URLs (`allow_redirects=False`) or implement a custom redirect handler that recursively validates each redirect target against the security policy.
