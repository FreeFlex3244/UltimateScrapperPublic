## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-06-27 - Fix Werkzeug RCE in Flask Application
**Vulnerability:** Flask application running with `debug=True` while binding to `host='0.0.0.0'`, leading to Werkzeug Remote Code Execution (RCE).
**Learning:** Exposing the Werkzeug debugger on all network interfaces allows unauthenticated attackers to execute arbitrary Python code.
**Prevention:** Never use `debug=True` in production or when binding to public interfaces (`0.0.0.0`). Set `debug=False` for public-facing deployments.
