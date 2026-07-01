## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-07-01 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper validates URLs using `is_safe_url` but then calls `requests.get` with default settings, which automatically follows HTTP redirects. An attacker could bypass the safety check by providing a safe URL that redirects to a private IP.
**Learning:** Checking a URL's safety is insufficient if the HTTP client can be instructed by the server to fetch a different, unverified URL via a 30x redirect.
**Prevention:** Always explicitly disable automatic redirects (`allow_redirects=False`) when fetching user-supplied URLs, or implement a custom redirect handler that recursively validates each redirect target against the safety policy.
