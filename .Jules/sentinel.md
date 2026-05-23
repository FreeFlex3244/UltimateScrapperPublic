## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2025-02-18 - XSS Vulnerability in Frontend Rendering
**Vulnerability:** The `renderResults` function in `script.js` directly injected unescaped `file.filename` into `innerHTML`, creating a Cross-Site Scripting (XSS) vulnerability.
**Learning:** Never trust data from external sources, including a local database, when rendering HTML. Direct assignment to `innerHTML` with unsanitized data is a severe security risk.
**Prevention:** Always use `textContent` to safely assign text values to DOM elements, or securely escape HTML entities before injection.
