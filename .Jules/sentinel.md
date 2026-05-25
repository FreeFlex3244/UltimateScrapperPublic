## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-25 - Werkzeug RCE in Debug Mode
**Vulnerability:** Running Flask with debug=True on host='0.0.0.0'.
**Learning:** Running Flask apps in debug mode exposed to 0.0.0.0 allows unauthenticated remote code execution via the Werkzeug debugger.
**Prevention:** Never use debug=True for production or publicly exposed interfaces. Ensure debug=False when host is set to 0.0.0.0.
