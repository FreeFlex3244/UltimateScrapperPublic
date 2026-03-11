## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-11 - HTTP Connection Pooling with requests.Session
**Learning:** The scraper was establishing a new TCP connection and performing a new TLS handshake for every single request by calling `requests.get()`. This creates significant network overhead when making multiple requests to the same domain during a crawl.
**Action:** Use `requests.Session()` to enable HTTP connection pooling. This reuses existing TCP connections for subsequent requests to the same host, drastically reducing latency and connection overhead. Always instantiate the session within the thread to ensure thread safety and ensure `session.close()` is called for proper socket cleanup.
