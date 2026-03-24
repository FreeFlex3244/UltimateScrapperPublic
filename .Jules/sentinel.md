## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - SSRF through HTTP Redirects in Scraper
**Vulnerability:** Even if the initial URL is validated, the scraper was blindly following HTTP redirects via `requests.get`'s default behavior, allowing it to be redirected to internal, private, or loopback IPs (e.g., SSRF).
**Learning:** Security controls on the initial input are easily bypassed if network libraries automatically follow redirects. Every hop in a redirect chain must be independently validated.
**Prevention:** Disable automatic redirects (`allow_redirects=False`) and manually handle 3xx status codes, extracting the `Location` header and running the same URL validation (`is_safe_url`) on each redirect before following it. Also implement a max redirect count to prevent infinite loops.
