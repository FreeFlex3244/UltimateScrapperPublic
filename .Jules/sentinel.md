## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-04-02 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` with default settings which automatically follows HTTP redirects. A malicious server could return a 301/302 redirect pointing to an internal IP (e.g., `127.0.0.1`), bypassing the initial `is_safe_url` check on the start URL.
**Learning:** Initial validation of a URL is insufficient if the HTTP client automatically follows redirects to new, unvalidated destinations.
**Prevention:** Always set `allow_redirects=False` when fetching URLs. Manually handle redirect status codes (301-308), extract the `Location` header, validate the new URL, and enforce a maximum redirect depth to prevent infinite loops.
