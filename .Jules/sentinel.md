## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** HTTP clients automatically following redirects can bypass initial URL validation and lead to Server-Side Request Forgery.
**Learning:** Validating the initial URL is not enough if the HTTP client automatically follows redirects. Redirects must be handled manually, and each new URL in the redirect chain must be validated.
**Prevention:** Use `allow_redirects=False` in HTTP requests. Manually handle redirects, validating each destination URL and enforcing a maximum redirect chain length.
