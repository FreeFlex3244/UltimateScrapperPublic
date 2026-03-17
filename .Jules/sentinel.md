## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-03-17 - SSRF via HTTP Redirects in Scraper
**Vulnerability:** The scraper automatically followed HTTP redirects using `requests.get`. A malicious external server could return a 301/302 redirect pointing to an internal service (e.g., `http://127.0.0.1:8080/admin`), bypassing the initial `is_safe_url` validation and causing SSRF.
**Learning:** Initial URL validation is insufficient if the HTTP client automatically follows redirects to unvalidated destinations.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) in security-sensitive contexts. Manually handle redirects by extracting the `Location` header, validating the new URL against security policies, and preventing infinite redirect loops.
