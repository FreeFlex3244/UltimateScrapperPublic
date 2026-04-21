## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precomputing Extension Tuples
**Learning:** Using an O(N) loop to validate URL extensions against a large list creates a hidden bottleneck for non-matching URLs. A precomputed tuple used with path.endswith() provides O(1) C-level performance and avoids string splits.
**Action:** Precompute extension tuples for endswith() checks in high-frequency validation functions rather than looping.
