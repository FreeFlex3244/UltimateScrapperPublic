## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-24 - Precomputing Static URL Parsing
**Learning:** Calling `urlparse` repeatedly on a static URL like `start_url` inside recursive/iterative scraping loops introduces significant parsing overhead.
**Action:** Precompute parsed components (like `.netloc`) during class initialization to eliminate redundant overhead and speed up domain checks.
