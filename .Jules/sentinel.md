## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2026-03-07 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper explicitly validated the initial user-provided URL against internal/loopback IPs, but failed to validate the `Location` header URLs of HTTP redirects (301, 302, etc.) followed automatically by `requests.get()`. This allowed SSRF attacks bypassing initial checks.
**Learning:** Security validation must be applied continuously across state transitions, such as HTTP redirects. Web clients like `requests` silently follow redirects by default, silently bridging external interactions to internal networks.
**Prevention:** Disable automatic redirect following (`allow_redirects=False`) when fetching external resources. Manually inspect redirect URLs, fully validate them (e.g., `is_safe_url`), and manage the redirect chain securely within the application layer.
