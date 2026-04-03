## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - HTTP Connection Pooling
**Learning:** Using requests.get() for sequential crawls opens a new TCP connection every time, creating unnecessary network overhead.
**Action:** Always use requests.Session() to pool and reuse connections, which significantly speeds up multiple requests to the same domains.
