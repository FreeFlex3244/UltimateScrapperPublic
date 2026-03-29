## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-29 - Connection Pooling in Scraper
**Learning:** Repeatedly making HTTP requests to the same host using `requests.get()` incurs significant overhead from establishing a new TCP connection (and potentially a TLS handshake) for each request. This network latency severely bottlenecks recursive web scraping operations.
**Action:** Use `requests.Session()` to enable HTTP keep-alive, allowing the scraper to pool and reuse TCP connections when crawling the same host, which drastically improves performance.
