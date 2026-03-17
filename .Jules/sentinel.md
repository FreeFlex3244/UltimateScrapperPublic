## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Vulnerability in Scraper via HTTP Redirects
**Vulnerability:** The scraper was vulnerable to Server-Side Request Forgery (SSRF) because it automatically followed HTTP redirects (using the default `requests.get` behavior) without validating the redirection targets, potentially allowing access to private or loopback IP addresses.
**Learning:** Even if the initial user-provided URL is validated, subsequent HTTP redirects can point to unsafe local or internal resources, bypassing the initial validation and leading to an open redirect/SSRF vulnerability.
**Prevention:** Always use `allow_redirects=False` in HTTP requests when fetching external resources. Manually handle HTTP redirects (status codes 301-308) by extracting the `Location` header and validating the new destination URL using `is_safe_url` before processing or following it.
