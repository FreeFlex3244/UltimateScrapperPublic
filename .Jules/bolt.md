## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-04-06 - Connection Pooling with requests.Session
**Learning:** Opening a new connection for every HTTP request is a significant performance bottleneck when scraping. Using `requests.Session` enables TCP connection pooling, reducing overhead.
**Action:** Always use `requests.Session()` for repetitive network requests instead of standalone `requests.get()` to improve throughput.
