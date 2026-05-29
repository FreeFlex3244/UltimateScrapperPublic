## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-29 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used requests.get() with default allow_redirects=True. An attacker could provide a safe URL that redirects to an internal/private IP, bypassing the is_safe_url() check and causing SSRF.
**Learning:** Validating the initial URL is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Set allow_redirects=False on requests.get() in scrapers, or implement a custom redirect handler that re-validates the Location header against security policies before following.
