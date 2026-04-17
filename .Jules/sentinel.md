## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF via HTTP Redirects in Scraper
**Vulnerability:** The scraper followed HTTP redirects automatically (`allow_redirects=True` by default in `requests.get`), allowing attackers to bypass initial `is_safe_url` checks by providing an external URL that redirects to an internal/private IP (e.g., `http://169.254.169.254` or `http://localhost`).
**Learning:** Initial validation is insufficient if the underlying HTTP client automatically follows redirects to unvalidated destinations. This is a classic SSRF bypass technique.
**Prevention:** Always disable automatic redirects (`allow_redirects=False`) in HTTP clients used for scraping or fetching user-provided URLs. Manually handle 3xx redirect status codes, extract the `Location` header, and explicitly re-validate the new destination URL using `is_safe_url` before fetching it. Implement a strict redirect chain limit (e.g., 5) to prevent infinite loop Denial of Service.
