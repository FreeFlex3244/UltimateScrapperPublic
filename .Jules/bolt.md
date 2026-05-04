## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-22 - Repeated urlparse in scraping loops
**Learning:** Calling `urlparse(self.start_url).netloc` inside a while loop over HTML links repeatedly recalculates a static value. This causes unnecessary parsing overhead which adds up rapidly across many crawled pages.
**Action:** Precompute static values (like the starting domain `netloc`) during class initialization (`__init__`) and reuse the cached variable inside loops to eliminate redundant overhead.
