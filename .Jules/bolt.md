## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-02-14 - Precompute parsed URL components
**Learning:** Repeatedly calling `urlparse` on static URLs inside a web scraper's recursive loop creates unnecessary overhead and degrades performance.
**Action:** Always precompute parsed components of static URLs during class initialization to optimize performance in loops.
