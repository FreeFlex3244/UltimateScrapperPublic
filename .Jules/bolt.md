## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-23 - Inner Loop Optimizations
**Learning:** Parsing static URLs like `start_url` repeatedly inside a scraping loop using `urlparse` causes unnecessary overhead. Similarly, looping through a list to check file extensions using `endswith` is slower than passing a pre-formatted tuple directly to `endswith`.
**Action:** Precompute static values (like domain names and extension tuples) during class initialization to optimize inner loop performance.
