## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - Werkzeug Debugger RCE
**Vulnerability:** Flask application running with debug=True exposed to 0.0.0.0.
**Learning:** Running Flask with the Werkzeug debugger enabled on a public interface allows arbitrary code execution.
**Prevention:** Always set debug=False for production or when binding to public network interfaces (0.0.0.0).
