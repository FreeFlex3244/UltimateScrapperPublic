## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-06-24 - Avoid redundant urlparse in scraping loops
**Learning:** Calling `urlparse` on a static URL inside an inner recursive/iterative loop adds unnecessary O(N) parsing overhead which compounds linearly with the number of scraped links.
**Action:** Precompute the parsed components (like `netloc`) of static URLs during class initialization to eliminate repetitive processing inside loops.
