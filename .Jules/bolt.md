## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-24 - Precomputing Extension Tuples for Path Validation
**Learning:** Using an O(N) Python loop with `path.endswith()` against a large list of file extensions creates a performance bottleneck during crawling.
**Action:** Precompute a tuple of formatted extensions and use `path.endswith(tuple)` for O(1) C-level performance, preserving the exact return format by doing a quick lookup only when the tuple matches.
