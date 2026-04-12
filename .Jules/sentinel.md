## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2026-04-12 - SSRF via HTTP Redirects Vulnerability in Scraper
**Vulnerability:** The scraper blindly followed HTTP redirects when fetching URLs, bypassing the initial `is_safe_url` checks.
**Learning:** Checking a URL once before fetching is insufficient if the HTTP client automatically follows redirects to new, unvalidated destinations (e.g., internal network resources).
**Prevention:** Always disable automatic redirects in HTTP clients (`allow_redirects=False`) and manually extract, validate (`is_safe_url`), and limit the depth of redirect chains before requesting the new URL.
