## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-06-16 - [Eliminate Redundant urlparse Calls in Loop]
**Learning:** Calling `urlparse` on static configuration URLs (like `start_url`) inside the inner link processing loop creates a hidden O(N*M) bottleneck, as it executes repeatedly for every link discovered on every page.
**Action:** Precompute parsed components of static URLs during class initialization (e.g., in `__init__`) to avoid redundant parsing overhead in iterative scraping paths.
