## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precompute Static Values in Loops
**Learning:** Repeatedly parsing the same static URL (like `start_url`) inside a recursive scraping loop introduces unnecessary overhead. `urlparse` execution times stack up significantly over millions of iterations.
**Action:** Precompute static values (like `start_netloc = urlparse(start_url).netloc`) during class initialization and reference the precomputed attribute within loops for O(1) performance instead of redundant parsing.
