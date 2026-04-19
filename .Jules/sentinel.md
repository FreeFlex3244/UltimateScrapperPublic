## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF via HTTP Redirects in Scraper
**Vulnerability:** The scraper handled HTTP redirects automatically via `requests.get`, which bypassed the initial URL safety checks (`is_safe_url`). An attacker could supply a safe external URL that redirects to an internal/private IP, causing SSRF.
**Learning:** Automatic redirects in HTTP clients circumvent URL-level validations made before the request. Web scrapers must explicitly handle redirects to re-validate destination URLs.
**Prevention:** Always use `allow_redirects=False` when validating endpoints in web requests. Manually handle `3xx` status codes, extract the `Location` header, normalize it, and run `is_safe_url()` on it before allowing the scraper to queue the redirect URL. Implement a maximum redirect count to prevent infinite loop DoS attacks.
