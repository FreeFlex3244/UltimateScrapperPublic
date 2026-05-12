## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-13 - SSRF via HTTP Redirects
**Vulnerability:** The scraper disabled automatic redirects but didn't safely handle manual ones, potentially allowing malicious servers to redirect requests to internal network IPs.
**Learning:** Always validate the destination URL of HTTP redirects against SSRF protections (e.g., `is_safe_url`) and set a maximum redirect limit to prevent infinite loops.
**Prevention:** Use `allow_redirects=False`, extract the `Location` header, validate the URL with `is_safe_url`, and track redirect counts in the processing queue.
