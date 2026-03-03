## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.

## 2026-03-03 - XSS Vulnerability in UI rendering
**Vulnerability:** The `renderResults` function in `src/static/script.js` constructed HTML table rows using `innerHTML` and unsanitized data (`file.filename` and `file.extension`).
**Learning:** Using `innerHTML` to render API responses directly can expose the application to Cross-Site Scripting (XSS) if the data comes from external, untrusted sources like a web scraper.
**Prevention:** Always use `document.createElement` and `textContent` to construct elements dynamically in JavaScript, bypassing any XSS execution risks.
