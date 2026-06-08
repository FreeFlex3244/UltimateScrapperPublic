## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-08 - Flask RCE via debug=True
**Vulnerability:** The Flask app binds to `host='0.0.0.0'` while running with `debug=True`, exposing the Werkzeug debugger to the network and potentially allowing unauthenticated remote code execution.
**Learning:** Development settings should never be used on a public interface.
**Prevention:** Hardcode `debug=False` for public interfaces or rely on environment variables to handle debug modes safely.
## 2024-06-08 - SSRF Redirect Bypass
**Vulnerability:** The scraper checks `is_safe_url` initially but then `requests.get()` allows redirects by default, meaning an attacker could host a safe site that redirects to a local/internal address (SSRF bypass).
**Learning:** Redirects bypass initial target validation if not disabled or validated per-redirect.
**Prevention:** Always use `allow_redirects=False` when scraping unvalidated user input or implement custom redirect validation.
