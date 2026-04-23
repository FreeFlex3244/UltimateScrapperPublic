## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects blindly, allowing an attacker to bypass initial `is_safe_url` checks by providing a safe URL that redirects to an internal IP (SSRF).
**Learning:** Validation checks on URLs are useless if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) in HTTP clients. Manually handle 3xx responses, extract the `Location` header, and validate the new URL before requesting it. Limit redirect chains to prevent infinite loop DoS.
