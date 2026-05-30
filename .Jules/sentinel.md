## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-23 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper was vulnerable to an SSRF bypass because `requests.get` followed HTTP redirects by default. This allowed a malicious server (passing the initial `is_safe_url` check) to respond with a 3xx redirect to a private IP (e.g., 127.0.0.1 or 169.254.169.254), which `requests` would blindly follow, circumventing the application's URL validation.
**Learning:** Checking a URL once before fetching it is insufficient if the HTTP client automatically follows redirects to unchecked URLs. This is a classic SSRF bypass pattern (CWE-918).
**Prevention:** Always disable automatic redirects (`allow_redirects=False` in `requests`) when fetching URLs in a scraping context, or implement a custom redirect handler that recursively runs the destination URL through the `is_safe_url` validator before following it.
