## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-28 - Werkzeug RCE via debug=True
**Vulnerability:** Flask application bound to 0.0.0.0 with debug=True enabled.
**Learning:** Running Flask with debug=True on a public interface (0.0.0.0) exposes the Werkzeug interactive debugger, leading to Remote Code Execution (RCE).
**Prevention:** Always set debug=False for public interfaces or production environments.
