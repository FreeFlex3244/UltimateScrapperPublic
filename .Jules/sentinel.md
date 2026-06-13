## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-18 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper was susceptible to SSRF bypass because `requests.get` followed HTTP redirects by default.
**Learning:** Even if a URL is validated with `is_safe_url` before making the request, an attacker can provide a safe URL that redirects to a malicious/internal IP, bypassing the initial check.
**Prevention:** Always set `allow_redirects=False` when making HTTP requests in a scraper, or implement custom redirect validation to re-run security checks on the `Location` header.
