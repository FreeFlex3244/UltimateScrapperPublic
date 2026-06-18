## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-10-24 - Precomputing static URLs outside recursive loop
**Learning:** Calling `urlparse` on static URLs inside a recursive web scraping loop creates significant hidden parsing overhead for every link processed.
**Action:** Always precompute parsed components like `netloc` during class initialization to eliminate redundant URL parsing inside heavy iterative or recursive operations.
