## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-23 - Prevent SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper checked URLs for safety using `is_safe_url` but then fetched them using `requests.get` which follows HTTP redirects by default. This allowed attackers to bypass the IP restriction by providing a safe URL that redirects to a malicious/internal IP.
**Learning:** Always disable automatic redirects (`allow_redirects=False`) or re-validate redirect targets when implementing SSRF protections.
**Prevention:** Explicitly configure HTTP clients to not follow redirects when fetching user-provided URLs in security-sensitive contexts, and add comments explaining why.
