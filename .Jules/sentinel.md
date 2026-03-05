## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2026-03-05 - SSRF via HTTP Redirects
**Vulnerability:** The scraper followed HTTP redirects automatically via requests.get(allow_redirects=True), bypassing the URL safety check (is_safe_url) for the redirected destination, leading to potential SSRF on internal networks.
**Learning:** URL validation must be performed on every hop of an HTTP redirect chain, not just the initial URL provided by the user. Requests automatically handles redirects unless configured otherwise.
**Prevention:** Use allow_redirects=False for HTTP requests and handle redirects manually by extracting the Location header and applying the safety check to the new destination before requesting it.
