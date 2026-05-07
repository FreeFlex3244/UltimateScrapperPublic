## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically (`allow_redirects=True` by default in `requests.get`), allowing an attacker to bypass the initial `is_safe_url` check by providing a safe URL that redirects to an internal/private IP.
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Always use `allow_redirects=False` in HTTP clients used for web scraping/fetching. Manually handle redirects by extracting the `Location` header, validating the new URL, and enforcing a maximum redirect depth to prevent infinite loops.
