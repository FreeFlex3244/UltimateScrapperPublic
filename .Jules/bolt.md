## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - HTTP Keep-Alive for Scraper Performance
**Learning:** Making repeated HTTP requests to the same domain using `requests.get()` without a session opens a new TCP connection (and potentially TLS handshake) each time, which acts as a hidden bottleneck.
**Action:** Always use `requests.Session()` to utilize HTTP Keep-Alive and connection pooling when scraping multiple pages on the same site.
