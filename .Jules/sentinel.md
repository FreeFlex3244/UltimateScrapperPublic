## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The web scraper validated the initial URL but used `requests.get()` which automatically follows HTTP redirects. An attacker could provide a URL that passes validation, but returns a 301/302 redirect to a local or internal IP address (e.g., `http://127.0.0.1/`), bypassing the SSRF protection entirely.
**Learning:** Security controls on URLs (like SSRF IP filtering) must be enforced at every step of a request lifecycle, especially when following redirects. HTTP clients that follow redirects by default inherently bypass these checks if not configured properly.
**Prevention:** Disable automatic redirects in HTTP clients (`allow_redirects=False` in `requests`). Intercept 3xx status codes, extract the `Location` header, and process it as a new URL through the same validation pipeline (e.g., adding it back to the crawl queue to be validated by `is_safe_url()`).
