## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-31 - Precompute Static URLs for Recursive Loops
**Learning:** Calling `urlparse(self.start_url).netloc` repeatedly on static URLs inside a recursive scraping loop causes unnecessary parsing overhead.
**Action:** Precompute static parsed components (like `self.start_netloc = urlparse(start_url).netloc`) during class initialization.
