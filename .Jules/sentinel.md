## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects in Scraper
**Vulnerability:** The scraper followed HTTP redirects automatically (`allow_redirects=True`), allowing attackers to bypass initial `is_safe_url` validation by hosting an external server that redirects to a protected internal IP (e.g., 127.0.0.1).
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects. Attackers can use 301/302 redirects to pivot into internal networks after the initial payload passes the whitelist.
**Prevention:** Always set `allow_redirects=False` in HTTP clients used for fetching external content. Manually process redirects, validating the `Location` header against security policies (like `is_safe_url`) before enqueuing the new destination.
