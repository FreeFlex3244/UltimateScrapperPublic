## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-07-03 - Avoid urlparse in scraping loops
**Learning:** Calling `urlparse(self.start_url)` inside a scraping loop that processes thousands of links causes significant O(N) performance overhead because the start URL string is static and doesn't change.
**Action:** Always precompute parsed components of static URLs during class initialization (like `__init__`) rather than resolving them continuously within recursive or iterative structures.
