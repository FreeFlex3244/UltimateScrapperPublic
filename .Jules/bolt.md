## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-18 - Avoid repeated URL parsing in loops
**Learning:** Inside recursive or iterative scraping loops (like BFS queue processing), repeatedly calling `urlparse` on a static URL (like `start_url`) introduces unnecessary parsing overhead.
**Action:** Precompute static parsed components (like `urlparse(start_url).netloc`) during class initialization to eliminate redundant processing inside loops, turning it into a simple string comparison.
