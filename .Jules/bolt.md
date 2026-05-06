## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precomputing values for inner loops
**Learning:** Repeatedly calling `urlparse()` on a static URL and using an O(N) iteration for `.endswith()` string checks inside a scraping loop introduces significant overhead.
**Action:** Precompute static values like `netloc` during initialization and use O(1) tuple checks (`path.endswith(tuple)`) before falling back to iterative matching.
