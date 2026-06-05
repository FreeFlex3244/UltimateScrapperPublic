## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2026-06-05 - SSRF via HTTP Redirects
**Vulnerability:** Scraper was susceptible to Server-Side Request Forgery (SSRF) bypass through HTTP redirects because the `is_safe_url` check was only performed on the initial URL, while `requests.get` automatically follows redirects by default.
**Learning:** Even if an initial URL is validated, an attacker can provide a safe-looking URL that redirects to internal or restricted IP addresses, bypassing the security check.
**Prevention:** Always set `allow_redirects=False` in `requests.get` when scraping or implement custom redirect handling to validate each subsequent URL in the redirect chain.
