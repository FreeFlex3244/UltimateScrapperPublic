## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Redirect Bypass
**Vulnerability:** The scraper followed HTTP redirects by default, allowing attackers to bypass `is_safe_url` checks by providing a safe URL that redirects to an internal IP (e.g., `127.0.0.1`).
**Learning:** Security validations on URLs are useless if the HTTP client transparently follows redirects to unvalidated destinations.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) when fetching user-supplied URLs, or manually validate the redirect `Location` header before following.
