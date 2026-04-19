## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-23 - Tuple endswith for File Extensions
**Learning:** Checking URL paths against a large list of file extensions using a Python loop creates an O(N) bottleneck.
**Action:** Precompute a tuple of formatted extensions (e.g., `('.zip', '.tar.gz')`) and use `path.endswith(tuple)` for O(1) C-level performance.
