## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Precomputing static loop invariants
**Learning:** Repeatedly calling `urlparse(start_url)` inside the recursive scrape loop and using O(n) python loops for checking `.endswith()` against extensions causes unnecessary CPU overhead. Python's `endswith` accepts a tuple of strings and runs at C-level, making it significantly faster for multi-extension matching.
**Action:** Always precompute static URL components and extension tuples during initialization. Use `path.endswith(tuple)` instead of explicit loops for suffix checking.
