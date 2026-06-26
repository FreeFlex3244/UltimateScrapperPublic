## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-24 - SSRF via HTTP Redirects
**Vulnerability:** The scraper was vulnerable to SSRF bypass because `requests.get` followed HTTP redirects by default, circumventing the `is_safe_url` validation.
**Learning:** Checking a URL's safety before a request is insufficient if the HTTP client automatically follows redirects to potentially unsafe internal endpoints.
**Prevention:** Always configure HTTP clients to disable automatic redirects (`allow_redirects=False`) or implement a secure redirect handler that re-validates each location against the safety criteria.
