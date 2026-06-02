## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-23 - Prevent SSRF via HTTP Redirects
**Vulnerability:** The scraper was vulnerable to an SSRF bypass because HTTP redirects were automatically followed by requests.get without being validated against the is_safe_url check.
**Learning:** requests.get follows redirects by default, meaning an attacker could provide a safe URL that redirects to a malicious internal IP, bypassing pre-request validation.
**Prevention:** Set allow_redirects=False in HTTP client calls and manually validate redirect targets, or disable redirects if they are not necessary.
