## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - URL Path Extension Validation
**Learning:** When validating URL paths against a large list of file extensions, using a Python loop or `rsplit('.', 1)` (which breaks multi-dot extensions like `.tar.gz`) is O(N) and slow.
**Action:** Always precompute a tuple of formatted extensions (e.g., `('.zip', '.tar.gz')`) during initialization and use `path.endswith(tuple)` for O(1) C-level performance.
