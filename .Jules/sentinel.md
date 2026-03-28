## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper validated initial URLs for SSRF, but automatically followed HTTP redirects (301, 302, etc.) blindly using `requests.get` defaults. This allowed an attacker to bypass initial checks by providing a safe URL that redirects to a private/loopback IP (e.g., `http://169.254.169.254`).
**Learning:** URL validation at the point of entry is insufficient if the HTTP client auto-follows redirects. An attacker can set up a public server that redirects to an internal endpoint.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`). Manually inspect the `Location` header in 3xx responses, validate the new destination URL using your SSRF checks, limit the redirect chain depth, and only then proceed to fetch it.
