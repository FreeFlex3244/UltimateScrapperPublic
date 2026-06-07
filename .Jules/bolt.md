## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-06-07 - Precomputing Static URLs in Scraping Loops
**Learning:** Calling `urlparse` repeatedly on a static URL like `start_url` inside a recursive/iterative web crawling loop introduces unnecessary parsing overhead, wasting CPU cycles on a constant value.
**Action:** Precompute static URL components (e.g., `netloc`, `scheme`) during class initialization to enable O(1) attribute access within performance-critical loops.
