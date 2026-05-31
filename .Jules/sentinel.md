## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Redirect Bypass in Scraper
**Vulnerability:** The scraper used `requests.get` which automatically followed HTTP redirects, bypassing the initial `is_safe_url` checks.
**Learning:** Even if the initial URL is safe, the target server can redirect to a malicious internal IP (e.g., 127.0.0.1) which the HTTP client will blindly follow, re-introducing the SSRF vulnerability.
**Prevention:** Always set `allow_redirects=False` in HTTP clients used for scraping and manually validate redirect `Location` headers against the security checks before following them.
