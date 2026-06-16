## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-16 - Prevent SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used requests.get without restricting HTTP redirects, allowing attackers to bypass initial is_safe_url checks by providing a safe URL that redirects to internal endpoints (SSRF).
**Learning:** Security validation performed prior to a network request is easily bypassed if the HTTP client automatically follows redirects to unvalidated locations.
**Prevention:** Always configure HTTP clients in scraping/fetching contexts with allow_redirects=False or implement a custom redirect handler that re-runs security checks on every new Location header.
