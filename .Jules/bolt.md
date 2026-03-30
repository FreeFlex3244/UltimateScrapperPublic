## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-30 - Connection Pooling for Recursive Web Scraper
**Learning:** Initializing `requests.Session()` instead of using `requests.get()` inside the recursive web scraping thread `run()` method enables connection pooling. This significantly reduces network overhead by eliminating repetitive TCP handshakes when continuously connecting to the same target domain while remaining thread-safe, making scraping measurably faster.
**Action:** Always use `requests.Session()` within the execution context of a thread when making multiple requests to the same host/domain to optimize performance via connection pooling.
