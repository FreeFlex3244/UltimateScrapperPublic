## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-23 - Precompute static URL components and use tuple-based string suffix matching
**Learning:** Repeatedly calling `urlparse` on static URLs inside recursive or iterative scraping loops creates significant overhead. In addition, checking file extensions with an O(N) python loop is inefficient.
**Action:** Precompute static URL components (e.g., `self.start_netloc = urlparse(start_url).netloc`) during class initialization. Precompute a tuple of formatted extensions (e.g., `('.zip', '.tar.gz')`) and use `path.endswith(tuple)` for O(1) C-level performance.
