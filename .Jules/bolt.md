## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Network Connection Pooling for Scrapers
**Learning:** Establishing a new TCP connection (and TLS handshake for HTTPS) for every single network request adds significant overhead. Because web scrapers generally loop over pages on the same domain repeatedly, failing to utilize connection pooling is a major performance bottleneck.
**Action:** Always use `requests.Session()` instead of `requests.get()` directly in web crawlers and scrapers to persist network connections. Initialize it inside the execution thread to avoid thread safety issues and explicitly call `.close()` in `finally` blocks for socket cleanup.
