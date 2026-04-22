## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Vulnerability via Redirects in Scraper
**Vulnerability:** The web scraper implicitly followed HTTP redirects without checking if the redirect destination resolved to a private/loopback IP address, bypassing the initial URL validation and allowing SSRF.
**Learning:** The initial URL check (`is_safe_url`) only applies to the start URL of the request. The HTTP client (e.g. `requests`) by default automatically follows redirects (status codes 30x). If a target domain redirects to `127.0.0.1`, the request will go there, bypassing the first check.
**Prevention:** Disable automatic redirects (`allow_redirects=False`). Manually handle HTTP redirect status codes (301, 302, 303, 307, 308) by extracting the `Location` header, validating the new destination URL using the security check (`is_safe_url`) before making the next request or enqueuing it, and limiting the redirect chain depth to prevent infinite loops.
