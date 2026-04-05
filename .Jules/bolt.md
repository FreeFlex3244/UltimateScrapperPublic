## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Reuse TCP connections with requests.Session()
**Learning:** Using `requests.get()` inside a loop creates a new TCP connection for every request. In a web scraper making many requests to the same domain, connection overhead is a significant bottleneck.
**Action:** Initialize `requests.Session()` within the thread and use `session.get()` to enable connection pooling and keep-alive, reducing latency.
