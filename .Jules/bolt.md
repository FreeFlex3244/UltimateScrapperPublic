## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-28 - Precompute Static URL Parsing
**Learning:** Repeatedly calling `urlparse` on a static variable like `start_url` inside a recursive loop is a major hidden performance bottleneck.
**Action:** Pre-compute components like `netloc` during class initialization to save redundant parsing overhead.
