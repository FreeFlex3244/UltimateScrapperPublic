## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-04 - SSRF Bypass via HTTP Redirects
**Vulnerability:** Scraper application allowed requests to redirect without re-validating the URL against the `is_safe_url` check.
**Learning:** Using `requests.get()` follows redirects by default, meaning a safe URL can redirect to a malicious, restricted internal IP, completely bypassing the initial `is_safe_url` safety checks.
**Prevention:** Always use `allow_redirects=False` when fetching user-supplied URLs if subsequent requests are not re-validated, or implement a custom redirect handler that re-verifies every hop.
