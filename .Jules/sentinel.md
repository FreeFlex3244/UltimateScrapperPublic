## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - SSRF Vulnerability via HTTP Redirects in Scraper
**Vulnerability:** The scraper used requests.get() which automatically follows redirects, bypassing initial is_safe_url() validation and allowing SSRF to internal networks.
**Learning:** Automatic HTTP redirects can bypass URL validation. We must disable automatic redirects and manually validate each hop.
**Prevention:** Use allow_redirects=False in requests.get(), manually handle 3xx status codes, and run is_safe_url() on the new Location header before enqueuing.

## 2025-02-18 - Werkzeug RCE via Debug Mode
**Vulnerability:** The Flask app hardcoded debug=True and host='0.0.0.0', exposing the Werkzeug debugger console to all network interfaces, allowing Remote Code Execution.
**Learning:** Debugger pins can be bypassed or guessed, and exposing the interactive debugger on 0.0.0.0 in any environment is a critical RCE risk.
**Prevention:** Control debug mode via environment variables (FLASK_DEBUG) and never bind the development server to 0.0.0.0 unless required and secured.
