## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper's `requests.get` call followed HTTP redirects by default, allowing bypass of the `is_safe_url` check if a malicious external URL redirected to a private IP or localhost.
**Learning:** Validation checks applied only to the initial URL are insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Disable automatic redirects (`allow_redirects=False`) or implement custom redirect handlers that validate every subsequent `Location` header against SSRF protections before following.
