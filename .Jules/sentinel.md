## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** Scraper followed HTTP redirects implicitly via `requests.get`, bypassing the `is_safe_url` validation and exposing the system to Server-Side Request Forgery (SSRF).
**Learning:** Redirects can be abused to point to internal IP ranges (e.g., 127.0.0.1) after the initial safe URL validation.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) and manually handle redirects, validating the new URL with `is_safe_url` before processing and limiting the redirect chain count to prevent infinite loop DoS attacks.
