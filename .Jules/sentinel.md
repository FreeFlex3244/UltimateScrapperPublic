## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-01 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** Scraper was vulnerable to SSRF because `requests.get` follows redirects by default without checking if the redirect destination is a private or loopback IP.
**Learning:** Even if the initial user-provided URL is validated, subsequent requests via HTTP redirects must also be validated to prevent bypassing SSRF protections.
**Prevention:** Always use `allow_redirects=False` with `requests.get`, manually handle redirects (301-308), validate the new `Location` URL using `is_safe_url`, and limit the maximum number of redirects to prevent infinite loops.
