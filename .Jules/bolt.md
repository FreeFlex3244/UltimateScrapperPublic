## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - HTTP Connection Pooling in Scraping
**Learning:** Web scrapers executing sequential requests to the same domain suffer significant overhead from repeated TCP and TLS handshakes when using `requests.get()` individually.
**Action:** Use `requests.Session()` within the scraper's execution context to leverage HTTP Keep-Alive and connection pooling. Ensure thread-safety by scoping the session to the worker thread.