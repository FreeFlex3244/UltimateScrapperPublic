## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-16 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper used requests.get() with default allow_redirects=True. An attacker could supply a safe URL that redirects to a private IP (e.g. 127.0.0.1) and bypass the initial is_safe_url check.
**Learning:** Checking is_safe_url before making a request is insufficient if the HTTP client automatically follows redirects to unchecked destinations.
**Prevention:** Always set allow_redirects=False in HTTP clients. Manually handle redirect responses (3xx), extract the Location header, and enqueue the new URL so it goes through the is_safe_url validation on the next loop iteration. Limit redirect depth to prevent loops.
