## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-03-12 - SSRF via HTTP Redirects
**Vulnerability:** The scraper used `requests.get` with default settings (which automatically follows redirects), allowing a malicious site to redirect requests to internal network IPs, bypassing initial URL validation.
**Learning:** Automated HTTP clients must have redirects disabled (`allow_redirects=False`) or employ a custom redirect handler that re-validates the destination IP at every hop to prevent SSRF.
**Prevention:** Manually handle 3xx status codes, extract the `Location` header, and enforce strict URL/IP validation on the new destination before making subsequent requests.
