## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-29 - SSRF Redirect Bypass
**Vulnerability:** The scraper's `requests.get` followed redirects by default, allowing a safe URL to redirect to an unsafe internal IP (SSRF), bypassing `is_safe_url` checks.
**Learning:** Always consider redirect behavior when performing network requests, especially after verifying the initial URL is safe. A redirect can point anywhere.
**Prevention:** Set `allow_redirects=False` in HTTP clients used for web scraping/fetching, or manually resolve redirects and re-validate each hop against the safety checks.
