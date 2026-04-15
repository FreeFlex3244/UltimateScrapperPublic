## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The web scraper automatically followed HTTP redirects using requests.get, which could allow a malicious public URL to redirect the scraper to a private IP/internal network (SSRF) bypassing the initial is_safe_url validation.
**Learning:** The initial URL validation is not enough if the HTTP client blindly follows redirects to unchecked locations.
**Prevention:** Always set allow_redirects=False for HTTP clients in scrapers. Manually handle 301-308 status codes, extract the Location header, and validate the new destination URL with is_safe_url before continuing the request or enqueuing it. Also limit redirect depth to prevent infinite loops.
