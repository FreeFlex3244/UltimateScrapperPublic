## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF via Open Redirects
**Vulnerability:** The scraper used `requests.get` with default settings (`allow_redirects=True`), which blindly follows HTTP redirects (e.g., 301, 302). An attacker could bypass the initial `is_safe_url` check by providing a safe URL that redirects to a private/loopback IP.
**Learning:** Security validations on URLs must be enforced at every step of a request chain. Automatic redirects bypass pre-request validations and inherently trust the `Location` header provided by the external server.
**Prevention:** Always set `allow_redirects=False` when making HTTP requests where the destination is user-controlled or untrusted. Manually inspect redirect status codes, extract the `Location` header, and recursively validate the new destination URL against the security rules (like `is_safe_url`) before explicitly following it. Also implement a `redirect_count` to prevent infinite redirect loop DoS attacks.
