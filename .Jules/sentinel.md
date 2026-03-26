## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-23 - Fix SSRF via Automatic Redirects
**Vulnerability:** The scraper was automatically following HTTP redirects, bypassing initial URL validation. This allowed an attacker to provide a safe URL that redirects to an unsafe internal IP (e.g., localhost), leading to Server-Side Request Forgery (SSRF).
**Learning:** Initial validation of a URL (`is_safe_url`) is insufficient if the HTTP client automatically follows redirects. The target of the redirect must also be validated against the same safety checks.
**Prevention:** Disable automatic redirects in HTTP clients (e.g., `allow_redirects=False` in `requests.get`). Manually handle redirect status codes (301-308), extract the `Location` header, and validate the new URL before adding it to the processing queue. Limit the number of redirects to prevent infinite loop DoS attacks.
