## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - Stored XSS in Search Results
**Vulnerability:** The search results table was constructed using `innerHTML` with unsanitized data (filenames) scraped from external websites.
**Learning:** Data scraped from the web and stored in a database is untrusted input. Malicious sites can use filenames containing XSS payloads (e.g., `<img onerror>`) to execute code on the scraper's dashboard.
**Prevention:** Always use `textContent` (or equivalent safe methods) when rendering dynamic data in the DOM. Never use `innerHTML` for displaying user-controlled content.
