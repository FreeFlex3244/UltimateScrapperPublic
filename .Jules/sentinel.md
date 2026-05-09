## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-10 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically without validating the destination URL, allowing attackers to bypass initial SSRF checks and redirect the scraper to internal services.
**Learning:** Initial validation of start URLs is insufficient if the HTTP client automatically follows redirects. Attackers can provide a "safe" external URL that responds with a 302 redirect to an internal IP.
**Prevention:** Always disable automatic redirects in the HTTP client (e.g., `allow_redirects=False` in requests) and manually handle redirect loops by validating the `Location` header against SSRF filters before enqueuing the new URL.
