## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically, allowing an attacker to bypass initial URL validation by providing a safe URL that redirects to a restricted internal IP.
**Learning:** Initial validation is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Always use `allow_redirects=False` in HTTP clients, manually extract the `Location` header, and validate the new URL against SSRF checks before following.
