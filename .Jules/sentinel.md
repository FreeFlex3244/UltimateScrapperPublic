## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-05 - SSRF via HTTP Redirect in Scraper
**Vulnerability:** The web scraper allowed HTTP requests to follow redirects automatically (`requests.get` defaults to `allow_redirects=True`). This allowed attackers to bypass the initial `is_safe_url` check by providing a safe URL that redirects to an internal/private IP.
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Always set `allow_redirects=False` in HTTP clients. Manually handle HTTP redirects (status codes 301-308), extract the `Location` header, and validate the new destination URL using `is_safe_url` before enqueuing it. Limit the redirect chain count to prevent infinite loops.
