## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-06-17 - Repeated parsing of static URLs
**Learning:** The scraper repeatedly called `urlparse(self.start_url)` inside the inner link processing loop. This creates unnecessary overhead, as the static URL components never change during the crawl.
**Action:** Always precompute `urlparse` components for static URLs like `start_url` during class initialization to eliminate redundant parsing overhead in iterative loops.
