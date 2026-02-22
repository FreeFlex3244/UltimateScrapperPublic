## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Requests Session for Scraper
**Learning:** The scraper was establishing a new TCP/TLS connection for every single URL, which is extremely inefficient for crawling the same domain repeatedly.
**Action:** Replaced `requests.get` with `requests.Session().get` to enable connection pooling (Keep-Alive), significantly reducing latency per request.
