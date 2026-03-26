## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-24 - HTTP Connection Pooling
**Learning:** The scraper was establishing a new TCP connection for every URL scraped using `requests.get()`, creating unnecessary latency overhead.
**Action:** Use `requests.Session()` to reuse underlying TCP connections and improve scraping speed.
