## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-19 - SSRF Vulnerability in Scraper Redirects
**Vulnerability:** The scraper used `requests.get` with default `allow_redirects=True`, which bypasses the initial `is_safe_url` checks if a malicious server redirects the crawler to an internal network URL (e.g., `http://127.0.0.1/admin`).
**Learning:** Security validations on URLs must be applied recursively to all redirects in a chain, as attackers can use a public URL to proxy an attack against an internal target via HTTP redirects.
**Prevention:** Always use `allow_redirects=False` in HTTP clients used for scraping or fetching user-provided URLs. Manually handle redirects, validating the `Location` header URL against `is_safe_url` before enqueuing, and limit the maximum redirect chain length.
