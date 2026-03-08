## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-08 - Connection Pooling with requests.Session()
**Learning:** When repeatedly crawling the same domain, initializing a new `requests.get()` call for each URL opens a new TCP connection and negotiates a new TLS handshake. This introduces significant network overhead.
**Action:** Always use `requests.Session()` to enable HTTP Keep-Alive. This allows connection pooling and reuses the same underlying TCP connection across multiple requests to the same host, yielding a measurable speedup (often 2-3x faster for the network request portion).
