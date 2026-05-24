## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-23 - Precomputing values and tuple string matching
**Learning:** Repeatedly calling `urlparse` on static URLs inside scraping loops and doing O(N) string end checks in loops creates noticeable overhead.
**Action:** Precompute static parsed components during initialization and use tuples with `.endswith` for O(1) matching in loop structures.
