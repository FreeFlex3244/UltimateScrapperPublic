## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via Unhandled HTTP Redirects
**Vulnerability:** Scraper was vulnerable to SSRF via HTTP Redirects. Attackers could bypass URL validation by supplying a safe URL that redirects to an internal/private IP.
**Learning:** Validation via `is_safe_url` must apply to redirect targets too.
**Prevention:** Use `allow_redirects=False` and manually handle redirects to validate targets.
