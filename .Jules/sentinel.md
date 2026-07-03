## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-07-04 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper evaluated `is_safe_url` only on the initial URL. A safe initial URL could return an HTTP redirect to an internal IP (like localhost), which `requests.get` followed by default, leading to SSRF.
**Learning:** Checking the safety of a URL before sending a request is insufficient if the HTTP client automatically follows redirects to new, unverified destinations.
**Prevention:** Set `allow_redirects=False` on HTTP clients when interacting with user-supplied URLs, or implement a custom redirect handler that validates every redirect target against security constraints.
