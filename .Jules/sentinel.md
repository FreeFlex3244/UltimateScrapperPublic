## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-10 - Flask Debug Mode on 0.0.0.0
**Vulnerability:** Running Flask with debug=True on host 0.0.0.0
**Learning:** The Werkzeug debugger allows arbitrary code execution and should never be exposed to external network interfaces.
**Prevention:** Always use debug=False when binding to 0.0.0.0 or public interfaces.
