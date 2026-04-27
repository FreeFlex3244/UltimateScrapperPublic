## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Precompute start URL netloc to optimize scraper loop
**Learning:** The scraper was repeatedly calling `urlparse(self.start_url).netloc` inside the inner link-processing loop to check if a domain matched the start domain. This introduced significant O(N) parsing overhead for static URLs.
**Action:** Always precompute parsed components (like `netloc`) for static URLs during class initialization to eliminate redundant parsing overhead in iterative scraping loops.
