## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-24 - Precomputing URL Properties in Scraping Loops
**Learning:** Repeatedly calling `urlparse` on static URLs (like `start_url`) inside recursive scraping loops or using O(N) string formatting/iteration for file extension matching creates significant, measurable bottlenecks (25x and 3.6x slowdowns respectively).
**Action:** Precompute static parsed components (`urlparse(url).netloc`) and formatted check tuples (`tuple(f".{ext}"...)`) during class initialization to eliminate redundant parsing and enable O(1) C-level `endswith(tuple)` checks.
