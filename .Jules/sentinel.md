## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-04-07 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper manually verified `is_safe_url` for the initial request, but the underlying HTTP client (`requests.get`) automatically followed HTTP redirects. A malicious user could point the scraper to a safe external URL that immediately redirects to an internal network address, bypassing the SSRF check.
**Learning:** HTTP clients often handle redirects transparently. Security checks must be applied to *every* URL in a redirect chain, not just the initial target.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) in HTTP clients when fetching user-supplied URLs. Manually extract the `Location` header, validate the new URL, and explicitly add it to the processing queue while enforcing a maximum redirect limit.
