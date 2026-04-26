## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-04-26 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The recursive web scraper followed HTTP redirects automatically (`allow_redirects=True`), which bypassed the pre-request `is_safe_url` checks. An attacker could host a server that returns a 301 redirect pointing to an internal IP (e.g. 127.0.0.1) and force the scraper to request internal network resources.
**Learning:** HTTP libraries like `requests` follow redirects by default, making pre-request SSRF validation easily bypassable via 301/302 chains.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) for user-supplied URLs. Manually handle redirects by extracting the `Location` header and running the URL through validation functions (`is_safe_url`) before appending them to the request queue.
