## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Connection Pooling in Scraper
**Learning:** Initializing `requests.Session()` significantly reduces network latency when scraping multiple pages from the same server by enabling HTTP connection pooling and keep-alive. This prevents the overhead of repeated TCP handshakes and TLS negotiations.
**Action:** Always use `requests.Session()` for repeated HTTP requests instead of isolated `requests.get()`, ensuring it is initialized per-thread to avoid thread-safety issues, and cleanly closed in the `finally` block to prevent socket leaks.
