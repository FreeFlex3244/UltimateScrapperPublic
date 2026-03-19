## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-12 - Prevent SSRF via HTTP Redirect Loops
**Vulnerability:** Scraper used `requests.get` with default settings, automatically following HTTP redirects, which could bypass `is_safe_url` checks leading to SSRF.
**Learning:** Automatic redirects in an HTTP client bypass application-level validation logic (like SSRF checks on initial enqueue) and can lead to infinite loops if not constrained.
**Prevention:** Use `allow_redirects=False`, manually handle 3xx status codes, extract the `Location` header, validate the destination URL with `is_safe_url` before queueing, and track/limit `redirect_count` in the queue format `(url, depth, redirect_count)`.
