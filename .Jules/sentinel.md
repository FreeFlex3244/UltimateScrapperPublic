## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - Werkzeug Debugger Remote Code Execution (RCE) Risk
**Vulnerability:** The Flask application had `debug=True` hardcoded in `app.run()`, which exposed the Werkzeug interactive debugger on all network interfaces (`host='0.0.0.0'`). This allows unauthenticated Remote Code Execution (RCE) by anyone who can reach the port.
**Learning:** Hardcoding `debug=True` combined with binding to `0.0.0.0` is a critical misconfiguration that inadvertently exposes development tooling and sensitive application internals to the public network.
**Prevention:** Never hardcode `debug=True`. Always control debug mode via environment variables (e.g., `os.environ.get('FLASK_DEBUG')`) and default it to `False` to ensure secure production deployments.
