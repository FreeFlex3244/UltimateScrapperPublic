## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` without restricting HTTP redirects, allowing an attacker to bypass initial `is_safe_url` validation by pointing to an external domain that redirects to a private/internal IP.
**Learning:** Initial validation of a URL does not guarantee safety if the underlying HTTP client automatically follows redirects to new, unvalidated destinations.
**Prevention:** Configure HTTP clients to disable automatic redirects (e.g., `allow_redirects=False` in `requests`) or implement a custom redirect handler that recursively applies validation logic to every hop.
