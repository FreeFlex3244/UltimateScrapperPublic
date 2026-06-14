## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-14 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper explicitly validated URLs using `is_safe_url` but allowed `requests.get` to follow redirects transparently.
**Learning:** `requests.get` follows HTTP redirects by default, meaning a safe-looking URL could return a 301/302 redirect to an internal IP (like 169.254.169.254 or localhost), bypassing initial domain validation and causing an SSRF.
**Prevention:** Always configure `allow_redirects=False` on HTTP clients used for scraping or implement a custom redirect handler that recursively validates each redirect location against `is_safe_url`.
