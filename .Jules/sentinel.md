## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-24 - SSRF Bypass via HTTP Redirects
**Vulnerability:** Scraper was vulnerable to Server-Side Request Forgery (SSRF) bypass because `requests.get` followed HTTP redirects automatically, bypassing initial `is_safe_url` checks.
**Learning:** Checking a URL against security policies before fetching is insufficient if the HTTP client automatically follows redirects to restricted addresses.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) or implement custom redirect handling that validates the `Location` header against security policies before following.
