## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-12 - Prevent SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper's `requests.get` call implicitly followed HTTP redirects, allowing an attacker to bypass the `is_safe_url` check by providing an external URL that redirects to a restricted local IP (e.g., `127.0.0.1`), leading to Server-Side Request Forgery (SSRF).
**Learning:** URL validation checks (like `is_safe_url`) performed *before* an HTTP request are insufficient if the HTTP client automatically follows redirects. The target server can redirect the client to a private IP after the initial validation.
**Prevention:** Always configure HTTP clients to disable automatic redirects (`allow_redirects=False`) when fetching user-supplied URLs, or implement a custom redirect handler that recursively validates each redirect target against the security policy.
