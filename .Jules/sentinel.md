## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-10-24 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper disabled scraping of private/loopback IPs using `is_safe_url`, but `requests.get` implicitly followed HTTP redirects to those same blocked IPs.
**Learning:** Validation applied only to the initial URL is insufficient if the HTTP client automatically follows redirects to new, unvalidated destinations.
**Prevention:** Always configure HTTP clients to disable automatic redirects (`allow_redirects=False`) or implement custom redirect handlers that enforce the same security validations on every hop.
