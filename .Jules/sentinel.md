## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-06-15 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper's HTTP client followed redirects by default, allowing SSRF validation to be bypassed.
**Learning:** `requests.get` follows redirects automatically. An attacker could provide a safe URL that redirects to an internal IP (like `http://127.0.0.1`), bypassing initial `is_safe_url` checks.
**Prevention:** Always configure HTTP clients in security-sensitive contexts (like scrapers) with `allow_redirects=False`, or manually validate the Location header on redirect.
