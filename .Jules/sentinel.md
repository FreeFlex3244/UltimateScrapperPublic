## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** The scraper validates initial URLs but allows the HTTP client to transparently follow redirects, which can bypass the initial validation and lead to SSRF.
**Learning:** Security validations must be enforced at every step of a process, not just at the entry point. HTTP clients following redirects automatically can easily bypass domain/IP restrictions.
**Prevention:** Disable automatic redirects (`allow_redirects=False`) and handle them manually, validating each new destination URL before enqueuing.
