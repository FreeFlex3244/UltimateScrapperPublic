## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` with default settings, which automatically follows HTTP redirects. An initially validated safe URL could redirect to an internal IP or localhost, bypassing the `is_safe_url` checks.
**Learning:** HTTP redirect chains are a common mechanism for bypassing initial SSRF protections because the redirect target is not evaluated by the application before it is followed.
**Prevention:** Always disable automatic redirects when fetching URLs with `allow_redirects=False`. Catch redirect status codes (3xx), extract the `Location` header, and recursively validate the new URL against your safety rules before following it.
