## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-24 - SSRF Bypass via HTTP Redirects
**Vulnerability:** Scraper was vulnerable to SSRF bypass because `requests.get` followed HTTP redirects by default. A malicious server could pass the initial `is_safe_url` check and then redirect to a local or private IP address (e.g. `127.0.0.1`).
**Learning:** Checking URL safety before making a request is insufficient if the HTTP client automatically follows redirects to new, unverified destinations.
**Prevention:** Always set `allow_redirects=False` when making HTTP requests to user-supplied URLs, or implement a custom redirect handler that recursively validates each redirect destination.
