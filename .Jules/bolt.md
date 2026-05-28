## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-22 - Precompute Static URL Parsing
**Learning:** Calling `urlparse(self.start_url)` repeatedly inside the nested BFS URL discovery loop introduces redundant parsing overhead for a value that never changes.
**Action:** Precompute static parsed components (like `start_netloc`) during class initialization to prevent redundant loop overhead.
