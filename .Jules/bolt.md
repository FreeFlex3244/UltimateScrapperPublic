## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-23 - Connection Pooling for Repeated Requests
**Learning:** Making repeated HTTP requests to the same domain (e.g., recursive web scraping) using `requests.get` incurs a significant performance penalty due to TCP handshake and socket setup for every request.
**Action:** Always use `requests.Session()` within the thread execution to reuse underlying TCP connections for a measurable speed boost. Ensure `.close()` is called in a `finally` block to prevent resource leaks.
