## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Bypass via HTTP Redirects
**Vulnerability:** The scraper used requests.get() with default allow_redirects=True, which automatically follows HTTP 3xx redirects to any destination, bypassing the initial is_safe_url() check and allowing an attacker to force the scraper to request internal network resources.
**Learning:** Always disable automatic redirects (allow_redirects=False) when fetching user-supplied URLs, and manually validate the Location header of redirect responses against the security policy before following them.
**Prevention:** Manually handle 301, 302, 303, 307, 308 status codes, extract the Location header, pass it through is_safe_url(), and limit the redirect depth to prevent infinite loops.
