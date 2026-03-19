## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Connection Pooling in Recursive Web Scrapers
**Learning:** Making repeated `requests.get()` calls to the same domain inside a scraping loop introduces massive overhead by continuously opening and closing TCP connections and performing new TLS handshakes.
**Action:** Use `requests.Session()` within the scraper execution thread to implement connection pooling. This reuses the underlying connections, dramatically reducing network latency and improving overall scrape speed.
