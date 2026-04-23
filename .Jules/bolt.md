## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-23 - Tuple-based O(1) checking vs Loop-based O(N) checking
**Learning:** Python's `str.endswith()` method is highly optimized C-level code that can accept a tuple of string choices to check against, running in O(1) instead of using a Python O(N) loop to iterate and check strings individually.
**Action:** Always precompute a tuple of formatted extensions (e.g. `('.zip', '.tar.gz')`) and use `path.endswith(tuple)` instead of loops for performance improvements during multi-dot extension matching.
