## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - HTTP Connection Pooling in Scraper loops
**Learning:** Re-establishing a new TCP/SSL connection for every single HTTP request in a scraper loop introduces significant overhead, causing poor network latency. Making repeated requests sequentially without a pool is a performance bottleneck.
**Action:** Always use connection pooling (e.g. `requests.Session()`) in iterative HTTP request loops to reuse connections and decrease latency.
