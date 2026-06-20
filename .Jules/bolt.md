## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-24 - Precomputing Static URLs in Scraping Loops
**Learning:** In the web scraper, `urlparse(self.start_url)` was called inside a nested loop for every scraped link to check domain scope, causing redundant parsing overhead and O(N*M) redundant urlparse calls.
**Action:** Always precompute properties of static variables like `start_url` (e.g., `start_netloc`) during class initialization to avoid redundant computation in recursive/iterative hot paths.
