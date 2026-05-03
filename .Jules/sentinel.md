## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** The scraper utilized the default `requests` library configuration, which automatically follows HTTP 301/302 redirects. This allowed attackers to bypass the initial `is_safe_url` validation by supplying a safe external URL that redirects to a protected internal IP (e.g., `127.0.0.1`).
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects. The destination of every hop in a redirect chain must be independently verified against security constraints.
**Prevention:** Always set `allow_redirects=False` in HTTP clients used for scraping or generic outbound requests. Manually handle 301-308 status codes, extract the `Location` header, validate it via `is_safe_url()`, and track a `redirect_count` to prevent infinite loops.
