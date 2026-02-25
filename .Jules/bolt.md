## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-24 - Network I/O Connection Pooling
**Learning:** The scraper was establishing a new TCP connection (and SSL handshake) for every single request using `requests.get()`. This is highly inefficient when scraping the same domain, as it ignores the Keep-Alive optimization provided by HTTP/1.1.
**Action:** Always use `requests.Session()` for scraping tasks, especially when hitting the same domain repeatedly, to reuse connections and reduce latency.
