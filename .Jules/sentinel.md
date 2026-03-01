## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-03-01 - SSRF via HTTP Redirect Chains
**Vulnerability:** The scraper blindly followed HTTP redirects when fetching pages. An attacker could provide a safe-looking external URL that responds with a 301/302 redirect pointing to an internal, restricted IP address, bypassing the initial `is_safe_url` check.
**Learning:** Checking a URL before requesting it is insufficient if the HTTP client automatically follows redirects to unchecked locations. Every link in a redirect chain must be independently validated.
**Prevention:** Disable automatic redirects in the HTTP client (e.g., `requests.get(..., allow_redirects=False)`). Manually capture the `Location` header from 3xx responses, normalize the URL, and enqueue it so it passes through the same validation logic as any other discovered link.
