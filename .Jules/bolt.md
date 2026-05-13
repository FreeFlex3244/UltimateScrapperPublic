## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-23 - Precompute static URL components
**Learning:** Calling `urlparse()` on a static string like `start_url` inside a recursive loop (executed for every found link) adds massive overhead due to redundant parsing.
**Action:** Precompute static components like `self.start_netloc = urlparse(start_url).netloc` during class initialization.
