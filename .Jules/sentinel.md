## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2026-06-22 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper's requests.get() implicitly followed HTTP redirects, potentially bypassing is_safe_url() to reach internal IPs.
**Learning:** URL validation must be strictly applied to every request, including redirect destinations, or redirects must be disabled.
**Prevention:** Configure HTTP clients with allow_redirects=False or implement custom redirect handlers to re-validate URLs.
