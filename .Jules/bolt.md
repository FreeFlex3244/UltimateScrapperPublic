## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-23 - Precompute Static Data & O(1) Endswith
**Learning:** Calling `urlparse` on static data (like the start URL) inside recursive scraping loops or using `O(n)` loops to match file extensions causes hidden performance bottlenecks.
**Action:** Always precompute static parsed parts (e.g., `urlparse(start).netloc`) during class initialization. Use `tuple` of formatted extensions with `str.endswith(tuple)` for O(1) matching instead of iterating in a loop.
