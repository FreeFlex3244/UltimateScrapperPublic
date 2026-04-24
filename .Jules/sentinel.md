## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** The scraper used `requests.get()` with default settings (which automatically follow redirects) after initial URL validation, allowing malicious servers to redirect requests to internal/private IPs.
**Learning:** Security checks performed only on the initial URL are insufficient if the HTTP client automatically follows redirects.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) and manually validate the `Location` header against a safe URL checker before proceeding with the redirect chain.
