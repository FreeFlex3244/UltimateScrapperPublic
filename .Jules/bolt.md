## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Connection Pooling with Requests Session
**Learning:** The recursive crawler was establishing a new TCP connection for every request to the same domain, incurring repeated handshake overhead.
**Action:** Replaced `requests.get` with `requests.Session()` to leverage Keep-Alive connection pooling for faster sequential requests.
