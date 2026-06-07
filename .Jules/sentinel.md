## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2024-06-07 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used requests.get to fetch URLs without disabling automatic redirects. A malicious server could return a redirect to a local or private IP, bypassing the is_safe_url check performed on the initial URL.
**Learning:** requests.get implicitly follows redirects, making pre-request URL validation insufficient for preventing SSRF.
**Prevention:** Always set allow_redirects=False when fetching user-provided URLs if redirects are not explicitly validated against the same safety criteria.
