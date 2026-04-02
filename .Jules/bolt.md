## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Connection Pooling with requests.Session()
**Learning:** Initializing `requests.Session()` instead of using `requests.get()` across repeated network requests in the web scraper yields significant performance improvements. It leverages connection pooling, allowing underlying TCP/TLS connections to the same host to be reused, avoiding the overhead of creating new connections on every scrape attempt.
**Action:** Always use a `Session` object when writing crawlers or scripts making many requests, ensuring it is instantiated locally to the thread and closed out properly in a `finally` block to prevent resource leaks.
