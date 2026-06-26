## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-06-26 - Precompute static URL parsing in scraping loops
**Learning:** Calling `urlparse()` inside an inner recursive or iterative scraping loop on a static property like `start_url` causes unnecessary redundant parsing overhead that scales linearly with the number of links processed per page.
**Action:** Precompute the parsed components of static URLs during class initialization and reference the cached values in hot paths to eliminate repeated C-level string parsing overhead.
