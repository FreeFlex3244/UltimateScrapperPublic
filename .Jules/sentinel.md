## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF Vulnerability via Unhandled Redirects
**Vulnerability:** The recursive web scraper disabled unsafe initial URLs, but the `requests.get` call automatically followed HTTP redirects by default. An attacker could supply a safe external URL that redirects to a sensitive internal IP (e.g., `127.0.0.1` or AWS Metadata), bypassing the initial validation.
**Learning:** Default HTTP client configurations often automatically follow redirects. To safely crawl unknown URLs, redirects must be handled manually, and each new destination must be validated against SSRF protections before execution.
**Prevention:** Always use `allow_redirects=False` when making requests to unverified domains. Manually handle 301-308 status codes, extract the `Location` header, and strictly validate the resolved URL using `is_safe_url` before adding it to the crawl queue.
