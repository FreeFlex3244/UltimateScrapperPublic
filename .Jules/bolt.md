## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Repeated TCP/TLS Handshakes Bottleneck
**Learning:** The scraper was using `requests.get()` for each recursive crawl. Because we often crawl pages on the exact same domain, closing and reopening TCP and TLS connections per request creates significant latency.
**Action:** Use `requests.Session()` within the scraper's run context to enable HTTP Keep-Alive and connection pooling. This drastically speeds up sequential requests to the same origin.
