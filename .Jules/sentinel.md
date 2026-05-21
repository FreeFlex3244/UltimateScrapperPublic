## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - Werkzeug RCE in Flask Dev Server
**Vulnerability:** Running Flask with `debug=True` and `host='0.0.0.0'` exposes the interactive debugger to the entire network, leading to Remote Code Execution (RCE).
**Learning:** Development servers should never be exposed on public interfaces (0.0.0.0) with debug mode enabled.
**Prevention:** Always use `debug=False` for any application binding to '0.0.0.0'. Ensure production deployments use a WSGI server (e.g., Gunicorn).
