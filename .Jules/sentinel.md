## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-18 - SSRF Vulnerability via Redirects
**Vulnerability:** The scraper followed redirects automatically, allowing SSRF bypass.
**Learning:** Web scrapers following redirects blindly can bypass initial URL validation.
**Prevention:** Set allow_redirects=False and manually handle redirects, validating the Location header against is_safe_url.
