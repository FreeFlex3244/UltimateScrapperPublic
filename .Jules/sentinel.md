## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-19 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically (`allow_redirects=True` by default in `requests.get`). A safe starting URL could redirect to an unsafe internal IP, bypassing the initial `is_safe_url` check.
**Learning:** URL validation must occur not just on the initial request, but on every redirect target in the chain. Default HTTP client behaviors (like automatic redirects) can silently bypass security checks.
**Prevention:** Disable automatic redirects (`allow_redirects=False`). Manually handle redirect status codes, extract the `Location` header, validate the new URL, and enforce a redirect limit to prevent infinite loops.
