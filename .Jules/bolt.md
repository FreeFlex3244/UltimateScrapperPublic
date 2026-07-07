## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-07-07 - Precompute Static URL Parsing in Crawl Loops
**Learning:** Calling urlparse repeatedly on a static URL (like start_url) inside a loop over every extracted link creates a hidden quadratic scaling bottleneck.
**Action:** Always precompute parsed components for static URLs during class initialization before entering recursive or iterative scraping loops.
