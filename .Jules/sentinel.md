## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Redirect Bypass
**Vulnerability:** The scraper validates the start URL against private IPs, but follows redirects by default via `requests.get`, allowing it to fetch private IPs via redirect payloads.
**Learning:** When performing URL validation for SSRF protection, HTTP clients must explicitly disable automatic redirects or re-validate redirect destinations to prevent bypass.
**Prevention:** Configure HTTP clients in scrapers with `allow_redirects=False` or implement a custom redirect handler that re-runs security checks on the `Location` header.
