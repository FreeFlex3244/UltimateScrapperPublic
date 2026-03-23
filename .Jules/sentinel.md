## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Bypass via HTTP Redirects in Scraper
**Vulnerability:** Even if the initial URL is validated against private IPs, a malicious server can return a 301/302 redirect to a private IP (e.g., `http://127.0.0.1`). If the HTTP client (e.g., `requests.get`) automatically follows redirects (`allow_redirects=True`), it bypasses the initial `is_safe_url` validation, leading to SSRF.
**Learning:** Security validations must be applied to every step of a URL chain, not just the initial request. Built-in HTTP clients often handle redirects automatically, making them a common vector for SSRF bypass.
**Prevention:** Disable automatic redirects (`allow_redirects=False` in `requests`). Manually handle HTTP redirects by extracting the `Location` header, validating the new destination URL with `is_safe_url` before enqueuing, and enforcing a maximum redirect limit to prevent infinite loops.
