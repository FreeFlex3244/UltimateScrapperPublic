## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-23 - Implicit SSRF via HTTP Redirects
**Vulnerability:** The requests library automatically follows HTTP redirects (3xx status codes) by default. Even if the initial URL is validated as safe using is_safe_url, the server could redirect the request to an internal or private IP address (e.g., http://127.0.0.1:5000), bypassing the initial SSRF protection.
**Learning:** URL validation must occur not just on the initial URL, but on every subsequent URL in a redirect chain. Relying on default HTTP client behavior for redirects in web scrapers is a significant SSRF vector.
**Prevention:** Always use `allow_redirects=False` in HTTP clients used for scraping or fetching user-provided URLs. Manually handle 3xx responses by extracting the `Location` header, passing the new URL through the same validation logic (`is_safe_url`), and enforcing a maximum redirect limit to prevent infinite loops.
