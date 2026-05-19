## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2024-05-24 - SSRF via HTTP Redirects
**Vulnerability:** The scraper explicitly validated URLs against `is_safe_url` before fetching, but allowed the underlying HTTP client (`requests.get`) to follow redirects automatically. An attacker could bypass SSRF protections by providing a safe URL that redirects to an internal/loopback IP address.
**Learning:** Automated HTTP redirect following in client libraries (like `requests`) completely bypasses pre-fetch URL validation routines because the intermediate redirect destinations are never passed back to the validation logic.
**Prevention:** Always disable automatic redirect following (`allow_redirects=False`) in HTTP clients when scraping user-provided URLs. Manually intercept 3xx status codes, extract the `Location` header, and subject the new destination to the identical `is_safe_url` validation checks before explicitly enqueueing it.
