## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2026-05-22 - Precompute static URL parsing in loops
**Learning:** Repeatedly calling `urlparse` on static URLs (like `start_url`) inside a recursive or iterative loop (like BFS crawling) introduces unnecessary string parsing overhead on every iteration.
**Action:** Precompute parsed components (like `netloc`) during class initialization or outside the loop to eliminate redundant parsing.
