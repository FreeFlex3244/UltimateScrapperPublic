## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-04-14 - Tuple vs List in path.endswith()
**Learning:** When validating URL paths against a large list of file extensions, using a Python `for` loop or `rsplit('.', 1)` creates an O(N) bottleneck, particularly because `rsplit` breaks multi-dot extensions (like `.tar.gz`). Python's `str.endswith()` accepts a tuple of strings and executes in C, making it essentially O(1) for our purposes and significantly faster.
**Action:** Precompute a tuple of formatted extensions (e.g., `('.zip', '.tar.gz')`) and use `path.endswith(tuple)` for O(1) C-level performance when matching file extensions against a list.
