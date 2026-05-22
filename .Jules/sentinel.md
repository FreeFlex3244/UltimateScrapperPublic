## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-05-24 - Werkzeug Debugger RCE
**Vulnerability:** The Flask application was running with `debug=True` while bound to the public interface (`0.0.0.0`), exposing the Werkzeug interactive debugger and enabling remote code execution (RCE).
**Learning:** Enabling the interactive debugger on a public interface allows any attacker to execute arbitrary Python code on the server.
**Prevention:** Never use `debug=True` in production or when binding to public IP addresses like `0.0.0.0`. Always set `debug=False` for public interfaces.
