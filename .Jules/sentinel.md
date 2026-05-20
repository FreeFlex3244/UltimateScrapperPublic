## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF via HTTP Redirects
**Vulnerability:** Scrapers with `requests.get` natively follow HTTP redirects unless disabled. Attackers can provide a benign "start URL" that responds with a 301/302 pointing to `http://127.0.0.1`, bypassing initial safe-URL validations.
**Learning:** Initial validation is insufficient if the client automatically follows unvalidated subsequent requests.
**Prevention:** Always use `allow_redirects=False` in libraries like `requests`. Extract the `Location` header and manually re-validate the new destination using `is_safe_url` before fetching.
