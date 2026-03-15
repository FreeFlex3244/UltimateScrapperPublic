## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-03-15 - SSRF via Blind HTTP Redirects
**Vulnerability:** The web scraper blindly followed HTTP redirects when fetching pages with `requests.get()`. This allowed an attacker to supply a safe initial URL that returns a 3xx redirect to an internal or restricted IP (e.g., `http://169.254.169.254/latest/meta-data/`), completely bypassing the application's `is_safe_url()` check.
**Learning:** Checking a URL before making a request is insufficient if the HTTP client is configured to automatically follow redirects. Security checks must be applied at every step of the redirect chain.
**Prevention:** Always set `allow_redirects=False` in HTTP requests. Manually handle redirects by extracting the `Location` header, validating the new URL against safety constraints, and tracking the redirect chain length to prevent infinite loop DoS attacks.
