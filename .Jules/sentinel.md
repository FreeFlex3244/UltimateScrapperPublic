## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** The scraper initially followed HTTP redirects automatically via `requests.get()`, bypassing the custom `is_safe_url()` check which was only applied to the initial URL. This allowed an attacker to supply a seemingly safe initial URL that simply redirected to an internal, private IP address, enabling Server-Side Request Forgery.
**Learning:** Web scrapers must validate not only the initial seed URLs but also the destination URLs of all HTTP redirects to prevent them from acting as open proxies.
**Prevention:** Disable automatic redirects in the HTTP client (`allow_redirects=False` in `requests`), extract the `Location` header manually, and pass the new destination URL through the `is_safe_url` validation check before enqueuing or requesting it. Limit redirect chains to prevent infinite loops.
