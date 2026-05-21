## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precompute extensions for file extension checking
**Learning:** Checking file extensions with `endswith()` in a python loop over an extension list scales poorly (O(n)). While a single regex or `rsplit('.', 1)` might seem better, `rsplit` breaks on multi-dot extensions (e.g., `.tar.gz`). The fastest approach is passing a precomputed tuple of string extensions to `endswith(tuple)`, which uses C-level optimization.
**Action:** When validating URL paths against a list of file extensions, precompute a tuple of formatted extensions (e.g., `('.zip', '.tar.gz')`) and use `path.endswith(tuple)` for O(1) C-level performance.
