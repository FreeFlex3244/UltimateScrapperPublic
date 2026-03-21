## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-03-21 - SSRF Vulnerability via HTTP Redirects in Scraper
**Vulnerability:** The scraper followed HTTP redirects automatically using `requests`, allowing malicious sites to redirect the scraper to internal services (127.0.0.1, private IPs) bypassing initial validation.
**Learning:** `is_safe_url` checks must be applied not just to initial URLs, but also to any subsequent redirected destinations. Automatic redirect handling in libraries hides this vulnerability.
**Prevention:** Disable automatic redirects (`allow_redirects=False` in `requests`). Manually handle redirects, checking the `Location` header URL with `is_safe_url` before enqueuing, and limit redirect depth.
