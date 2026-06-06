## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-19 - Prevent SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper validates URLs using `is_safe_url` but then fetches them using `requests.get` with default redirect following behavior.
**Learning:** Even if the initial URL is safe, the target server can respond with a 301/302 redirect to a local or private IP (e.g., `http://169.254.169.254`), bypassing the initial security check.
**Prevention:** Always set `allow_redirects=False` in HTTP clients used by scrapers or implement a custom redirect handler that re-validates the Location header against `is_safe_url` before following.
