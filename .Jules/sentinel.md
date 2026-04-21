## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-19 - SSRF Bypass via HTTP Redirects
**Vulnerability:** Scraper was vulnerable to SSRF bypass through HTTP redirects because requests followed redirects automatically without re-validating the target URL using `is_safe_url()`.
**Learning:** Even if the initial URL is safe, a server can respond with a 3xx redirect to an internal IP (like `127.0.0.1` or `169.254.169.254`), which `requests` follows by default, bypassing validation.
**Prevention:** Always use `allow_redirects=False` in HTTP requests. Manually handle redirects by extracting the `Location` header, validating the new destination URL with your security function, and maintaining a redirect limit to prevent infinite loops.
