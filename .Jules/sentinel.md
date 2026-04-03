## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Vulnerability via HTTP Redirects in Scraper
**Vulnerability:** The scraper followed HTTP redirects by default (`allow_redirects=True` implicitly), meaning malicious domains could bypass the initial `is_safe_url` validation by redirecting to internal/loopback IPs.
**Learning:** Initial URL validation is not enough if the HTTP client automatically follows redirects. The destination of each redirect must be individually verified against security policies.
**Prevention:** Always set `allow_redirects=False` in HTTP clients used for scraping. Handle 301-308 status codes manually by extracting the `Location` header and running the URL through the same validation functions (and limiting the total number of redirects) before proceeding.
