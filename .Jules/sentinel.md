## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-02 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically (`requests.get` defaults), which could allow an attacker to bypass the initial `is_safe_url` check by pointing to an external domain that redirects to an internal/private IP.
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`). Manually handle 3xx status codes by extracting the `Location` header, and enqueuing the new URL so it goes through the `is_safe_url` validation. Limit redirect chains to prevent infinite loops.
