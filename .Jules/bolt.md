## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precompute static URLs
**Learning:** Repeatedly calling `urlparse` on static URLs (like `start_url`) inside recursive or iterative scraping loops creates unnecessary overhead.
**Action:** Precompute the parsed components (e.g., `self.start_netloc = urlparse(start_url).netloc`) during class initialization to eliminate redundant parsing.
