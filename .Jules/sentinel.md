## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-07-06 - Prevent SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` which follows redirects by default, allowing attackers to bypass `is_safe_url` checks by providing a safe URL that redirects to a malicious or internal IP.
**Learning:** Checking a URL before fetching is insufficient if the HTTP client automatically follows redirects to unchecked locations.
**Prevention:** Always set `allow_redirects=False` when fetching user-provided URLs in a scraper, or validate every redirect URL.
