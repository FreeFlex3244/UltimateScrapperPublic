## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-03-12 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper manually validated user-supplied starting URLs but failed to apply the same `is_safe_url` validation to subsequent HTTP redirects. An attacker could provide a safe URL that automatically redirects to an internal, private IP (e.g. `127.0.0.1`), bypassing the initial SSRF check.
**Learning:** HTTP clients like `requests` will transparently follow redirects by default. Validation of a URL must occur for every hop in a redirect chain, not just the initial request, to prevent SSRF and infinite redirect loops.
**Prevention:** Disable automatic redirects (`allow_redirects=False`). Manually capture redirect status codes (301-308), extract the `Location` header, and validate it using the security check before adding the new destination to the scraping queue. Introduce a limit on the number of redirects to prevent DoS via infinite loops.
