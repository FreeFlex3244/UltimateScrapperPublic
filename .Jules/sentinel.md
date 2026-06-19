## 2025-02-18 - SSRF Vulnerability in Scraper
**Vulnerability:** The recursive web scraper accepted user-supplied URLs without validation and crawled internal networks (127.0.0.1, private IPs).
**Learning:** Web scrapers inherently trust user input as "start URLs". Without strict validation, they become open proxies to internal services.
**Prevention:** Always validate destination IPs against private/loopback ranges before initiating requests. Use `ipaddress` module for robust checks.
## 2024-05-23 - XSS via innerHTML duplication
**Vulnerability:** Found a duplicated rendering block in `src/static/script.js` that used unescaped `innerHTML` to render `file.filename` and `file.url`, leading to a potential Cross-Site Scripting (XSS) vulnerability.
**Learning:** Even if a secure textContent-based DOM construction method is present, leftover or duplicated legacy innerHTML code blocks can reintroduce critical XSS risks.
**Prevention:** Always ensure legacy innerHTML blocks are fully removed when implementing secure DOM creation methods, and regularly scan for `.innerHTML` usage in frontend code.
