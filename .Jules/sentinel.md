## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Vulnerability via HTTP Redirect Bypass
**Vulnerability:** The scraper handled HTTP redirects automatically, allowing an attacker to bypass initial `is_safe_url` checks by providing a safe URL that redirects to a private IP (e.g., 127.0.0.1).
**Learning:** Automated HTTP redirect following in scrapers nullifies pre-request security checks.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`). Manually inspect the `Location` header of redirects and validate the new destination URL with `is_safe_url` before processing.
