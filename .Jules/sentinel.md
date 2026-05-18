## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-23 - SSRF Vulnerability in Scraper Redirects
**Vulnerability:** Scraper was following HTTP redirects automatically, which could bypass initial `is_safe_url` checks and crawl restricted internal IP addresses (e.g., via 301/302 redirects to localhost).
**Learning:** Even if the start URL is safe, redirects can point to unsafe internal networks.
**Prevention:** Always use `allow_redirects=False` in HTTP clients and manually validate the `Location` header against safety checks before enqueuing the new URL.
