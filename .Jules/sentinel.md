## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2026-03-18 - Prevent SSRF in Web Scraper
 **Vulnerability:** Server-Side Request Forgery (SSRF) could occur via HTTP redirects, allowing requests to internal or restricted IP addresses.
 **Learning:** Using `requests.get` with default settings automatically follows redirects without re-validating the target URL, circumventing initial URL safety checks.
 **Prevention:** Disable automatic redirects with `allow_redirects=False`, handle redirects manually, and explicitly re-validate the `Location` header URL using `is_safe_url` before enqueueing.
