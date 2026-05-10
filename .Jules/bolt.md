## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-22 - URL Parsing in Scraper Loop
**Learning:** Calling `urlparse` on a static URL like `start_url` inside the iterative link processing loop introduces unnecessary parsing overhead.
**Action:** Precompute static URL components (e.g., `netloc`) during initialization to eliminate redundant parsing inside loops.
