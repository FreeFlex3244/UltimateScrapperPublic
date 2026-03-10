## 2024-05-20 - Connection Pooling for Web Scraper
**Learning:** The previous implementation opened a new TCP connection for every single HTTP request via `requests.get()`. This creates massive overhead (DNS resolution, TCP handshake, TLS negotiation) for scrapers making hundreds of requests, severely bottlenecking throughput.
**Action:** Use `requests.Session()` to enable HTTP Keep-Alive. Ensure it's initialized within the thread (`run()`) to avoid thread-safety issues, and explicitly call `session.close()` in the `finally` block to prevent socket leaks.
