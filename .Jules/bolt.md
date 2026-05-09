## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precompute vars in scraper loop
**Learning:** Calling urlparse on static URLs inside a recursive crawl loop and using O(N) loops for string suffix matching (like file extensions) causes measurable performance overhead.
**Action:** Precompute static parsed URLs (like start_netloc) and tuples for string suffix matching during class initialization.
