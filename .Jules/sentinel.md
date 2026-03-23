## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Vulnerability via Open Redirects in Scraper
**Vulnerability:** The recursive web scraper handled URLs gracefully but allowed the `requests` library to automatically follow redirects. This meant that a seemingly safe URL could redirect the scraper to an unsafe, internal IP address, bypassing the initial validation and leading to an SSRF vulnerability.
**Learning:** Even if initial user input is validated, subsequent actions resulting from that input (like HTTP redirects) must also be validated. Web scrapers must track and validate redirect locations to prevent being weaponized as open proxies.
**Prevention:** Always use `allow_redirects=False` in HTTP clients used for scraping. Manually intercept redirect status codes (301-308), extract the `Location` header, validate it against internal IP ranges (e.g., `is_safe_url`), and limit the redirect depth to prevent infinite loops.
