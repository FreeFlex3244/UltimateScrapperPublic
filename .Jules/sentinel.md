## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-23 - Stored XSS in Search Results
**Vulnerability:** Filenames scraped from external websites were rendered using `innerHTML` without sanitization, allowing Stored XSS.
**Learning:** Scraped data stored in the database is untrusted user input and must be treated as such.
**Prevention:** Use `textContent` or DOM creation methods (e.g., `document.createElement`) when rendering dynamic content from the database.
