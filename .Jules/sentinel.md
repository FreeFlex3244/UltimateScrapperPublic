## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-03-27 - Exposed Werkzeug Debugger
**Vulnerability:** The Flask application had `debug=True` and `host='0.0.0.0'` hardcoded in `app.run()`. This exposes the interactive Werkzeug debugger to any network interface, allowing potential remote code execution (RCE).
**Learning:** Hardcoded debug flags and open network bindings in development environments pose severe security risks if accidentally deployed or exposed.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`, `FLASK_HOST`) to control application execution environments and ensure secure defaults (e.g., `debug=False`, `host='127.0.0.1'`).
