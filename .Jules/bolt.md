## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precomputing urlparse inside iterative loops
**Learning:** The scraper was repeatedly calling `urlparse` on the static `start_url` for every single discovered link inside the `crawl` loop to check if the domains match. This created a hidden CPU bottleneck, as `urlparse` is slow when called thousands of times redundantly.
**Action:** Always precompute static parsed components during class initialization to eliminate redundant parsing overhead in iterative scraping loops.
