## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-13 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically (`allow_redirects=True`), which bypassed the initial `is_safe_url` validation, allowing attackers to redirect the scraper to internal services.
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects to new, unvalidated destinations.
**Prevention:** Always use `allow_redirects=False` and manually handle HTTP redirects by extracting the `Location` header, validating the new URL against SSRF checks, and enqueuing it.
