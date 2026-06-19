## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-06-19 - Precomputing urlparse inside recursive loops
**Learning:** Calling `urlparse()` on static URLs inside recursive or iterative loops (like BFS queue processing) causes unnecessary overhead.
**Action:** Always precompute parsed components like `.netloc` during class initialization to prevent redundant parsing.
