## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically, allowing an attacker to bypass `is_safe_url` checks by providing a safe URL that redirects to a private IP.
**Learning:** Always use `allow_redirects=False` when making HTTP requests where the destination is user-controlled, and manually validate the redirect `Location` header before following it.
**Prevention:** Handle redirects manually, validate the new URL with the safety check function, and implement a redirect limit (e.g., max 5) to prevent infinite loops.
