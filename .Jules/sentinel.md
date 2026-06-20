## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-20 - SSRF bypass via HTTP redirects
**Vulnerability:** The scraper validates URLs using `is_safe_url` but `requests.get` defaults to following redirects. A safe external URL could redirect to an unsafe internal IP (e.g., localhost), bypassing the security check and causing SSRF.
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects without validating the target URL.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) or implement custom redirect validation when fetching user-provided URLs in a scraper.
