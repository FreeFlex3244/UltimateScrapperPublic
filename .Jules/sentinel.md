## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper implemented an `is_safe_url` check, but `requests.get` followed HTTP redirects by default, allowing attackers to bypass the check and access internal networks (127.0.0.1, private IPs) via redirects.
**Learning:** Security checks (like `is_safe_url`) performed *before* a request can be bypassed if the HTTP client automatically follows redirects to different destinations.
**Prevention:** Disable automatic redirects (`allow_redirects=False`) when fetching URLs that were validated for safety, or implement custom redirect handling that re-validates every redirect target.
