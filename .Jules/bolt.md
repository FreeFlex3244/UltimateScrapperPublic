## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-04-17 - O(1) URL extension validation
**Learning:** Validating URL paths against a large list of file extensions using an O(N) Python loop is inefficient. Instead, precomputing a tuple of formatted extensions and using `path.endswith(tuple)` provides O(1) C-level performance.
**Action:** Use `str.endswith(tuple)` for fast extension matching.
