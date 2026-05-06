## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-06 - SSRF Vulnerability via HTTP Redirects in Scraper
**Vulnerability:** The scraper used `requests.get` with default settings, which automatically follows HTTP redirects. A safe URL could redirect to an unsafe internal IP (e.g., 127.0.0.1), bypassing the initial `is_safe_url` check and leading to SSRF.
**Learning:** Initial validation of URLs is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Disable automatic redirects (`allow_redirects=False`) and manually validate the `Location` header of redirect responses against the `is_safe_url` function before following them. Limit redirect chains to prevent loops.
