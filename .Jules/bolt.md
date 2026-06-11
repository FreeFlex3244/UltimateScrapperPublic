## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-29 - Precompute urlparse netloc
**Learning:** Calling `urlparse(self.start_url).netloc` repeatedly inside a recursive/iterative scraping loop introduces O(N) redundant string parsing overhead, where N is the number of links processed.
**Action:** Precompute static URL components (like `netloc`) during class initialization (`__init__`) and reuse the cached variable inside scraping loops to eliminate redundant string parsing.
