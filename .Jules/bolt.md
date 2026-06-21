## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Repeated urlparse inside Scraping Loops
**Learning:** Repeatedly calling urlparse on a static URL inside a loop processing every found link creates unnecessary overhead and slows down the scraper. Precomputing static URL components like netloc is essential for recursive crawling.
**Action:** Always precompute parsed components of static URLs during class initialization to eliminate redundant parsing overhead inside iterative loops.
