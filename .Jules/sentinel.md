## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-07-01 - SSRF bypass via redirects
**Vulnerability:** The scraper follows HTTP redirects by default when making requests, which could allow bypassing the initial URL validation check and SSRF protections if an attacker provides a safe URL that redirects to an internal/private address.
**Learning:** Using `requests.get` with default settings allows HTTP redirects, rendering simple URL checks insufficient to prevent SSRF.
**Prevention:** Always set `allow_redirects=False` in `requests.get` when performing URL safety checks, or perform the safety check on every redirect step if following is required.
