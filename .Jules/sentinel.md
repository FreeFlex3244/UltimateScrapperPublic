## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2025-02-18 - Stored XSS in Search Results
**Vulnerability:** Filenames extracted from scraped pages were rendered using `innerHTML` in the frontend search results, allowing execution of malicious scripts stored in the database.
**Learning:** Developers often focus on SQL injection but overlook stored XSS when displaying user-controlled data. Data scraped from the internet is inherently untrusted.
**Prevention:** Use `textContent` or `document.createElement()` to safely render text. Never use `innerHTML` unless absolutely necessary and sanitized with a dedicated library like DOMPurify.
