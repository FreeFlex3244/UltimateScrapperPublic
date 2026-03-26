## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-03-25 - SSRF Vulnerability via Unhandled HTTP Redirects
**Vulnerability:** The scraper used `requests.get` with default settings (`allow_redirects=True`), automatically following redirects to internal/private IPs and bypassing the initial URL validation.
**Learning:** Even if the initial URL is safe, a malicious server can redirect the scraper to an unsafe, internal IP to achieve SSRF.
**Prevention:** Always set `allow_redirects=False` on HTTP client requests. Manually inspect the `Location` header, validate the redirected URL/IP, and track redirect count to prevent infinite loop DoS.
