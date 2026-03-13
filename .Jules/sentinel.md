## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-03-13 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` with default settings, which automatically followed HTTP redirects. This allowed an attacker to bypass the initial `is_safe_url` checks by providing a safe URL that redirected to an internal, malicious IP (e.g. 127.0.0.1).
**Learning:** Initial URL validation is not enough if the HTTP client automatically follows redirects. The destination of each redirect must also be validated against security policies before being followed.
**Prevention:** Always use `allow_redirects=False` in HTTP requests when dealing with user-supplied URLs. Manually extract the `Location` header, validate the redirect URL, and enforce a maximum redirect depth to prevent infinite loops and SSRF.
