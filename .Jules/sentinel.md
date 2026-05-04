## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically via `requests.get`, bypassing the initial `is_safe_url` check and allowing SSRF to internal IPs.
**Learning:** Even if the initial URL is safe, malicious servers can redirect the client to internal network services.
**Prevention:** Always use `allow_redirects=False` and manually handle redirects, running the `is_safe_url` validation on every new location header before enqueuing.
