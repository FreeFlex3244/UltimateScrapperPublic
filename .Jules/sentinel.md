## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2024-03-09 - SSRF via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` without restricting redirects (`allow_redirects=True` by default). This allows an attacker to bypass the initial `is_safe_url` check by providing a safe URL that redirects (301/302) to an internal/private IP address, causing an SSRF vulnerability.
**Learning:** URL validation at the point of entry is insufficient if the HTTP client automatically follows redirects to new, unvalidated destinations. The `requests` library automatically follows redirects for GET requests unless explicitly told not to.
**Prevention:** Always set `allow_redirects=False` in HTTP requests when fetching user-supplied URLs. Handle HTTP redirects manually by extracting the `Location` header, normalizing the URL, and validating the new destination URL with the application's safety checks (e.g., `is_safe_url`) before enqueuing or following it.
