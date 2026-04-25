## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-04-25 - Avoid repeated urlparse on static URLs inside loops
**Learning:** Calling `urlparse(self.start_url).netloc` inside a scraping loop repeatedly parses the same static string. In a benchmark, precomputing the parsed components resulted in a ~100x speedup for that specific operation compared to the unoptimized version.
**Action:** Always precompute parsed components (like `netloc`) for static URLs (like `start_url`) during class initialization before entering a recursive or iterative scraping loop.
