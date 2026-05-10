## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` with default settings (`allow_redirects=True`), which automatically followed redirects to internal IP addresses even if the initial URL was validated as safe by `is_safe_url`.
**Learning:** Automatic HTTP redirects in libraries like `requests` can bypass initial input validation checks, allowing SSRF attacks against internal network resources.
**Prevention:** Always set `allow_redirects=False` in HTTP clients used for scraping. Manually process redirects by extracting the `Location` header and validating the new destination URL before fetching it.
