## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-17 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper was vulnerable to SSRF bypass where a safe URL could redirect to an unsafe, internal IP address.
**Learning:** `requests.get` follows redirects by default, allowing attackers to bypass `is_safe_url` checks on the initial URL.
**Prevention:** Always set `allow_redirects=False` when making requests to URLs that have been checked for SSRF, or implement custom redirect validation that re-checks each redirect location.
