## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-03-09 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` with default settings, which automatically follows HTTP redirects. An attacker could provide a safe initial URL that redirects to an unsafe internal URL, bypassing `is_safe_url` validation and causing SSRF.
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects to unvalidated destinations. Security checks must be applied to every step of a redirect chain.
**Prevention:** Always use `allow_redirects=False` in `requests.get` when building scrapers or webhooks. Manually handle redirects, extracting the `Location` header and validating the new destination before initiating the next request.
