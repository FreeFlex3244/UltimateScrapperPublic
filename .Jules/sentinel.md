## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-21 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The web scraper checked URLs against `is_safe_url` but then fetched them using `requests.get` with default settings.
**Learning:** By default, `requests.get` follows HTTP redirects. An attacker could provide a URL pointing to a malicious server that passes `is_safe_url` checks but then redirects the client to a restricted internal IP (e.g., localhost), bypassing the security controls.
**Prevention:** Set `allow_redirects=False` on outbound HTTP requests when scanning external resources or manually implement a strict redirect-following loop that re-validates each new `Location` header against `is_safe_url`.
