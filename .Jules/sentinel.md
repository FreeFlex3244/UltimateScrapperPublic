## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-07-04 - Prevent SSRF via HTTP Redirects
**Vulnerability:** The scraper called `requests.get(url, timeout=10)` after checking `is_safe_url(url)`, but allowed redirects, enabling an attacker to bypass the safe URL check by redirecting a safe-looking external URL to an internal IP (SSRF).
**Learning:** Validating a URL before fetching it is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Always set `allow_redirects=False` in `requests.get()` when scraping user-provided URLs that require SSRF protection, or implement a custom redirect handler that re-validates every redirect target.
