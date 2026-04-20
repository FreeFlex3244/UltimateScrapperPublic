## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically without verifying the safety of the new destination URL, allowing attackers to bypass initial `is_safe_url` checks.
**Learning:** Security validations must be enforced at every step of a request chain, not just the initial input.
**Prevention:** Always use `allow_redirects=False` in HTTP clients. Manually handle redirects, extract the `Location` header, and validate it using `is_safe_url` before issuing the next request.
