## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Connection Pooling with Requests Session
**Learning:** Using `requests.get()` in a loop creates a new TCP/TLS connection for every page it crawls. This is a huge performance hit due to connection overhead, especially when scraping many pages on the same domain.
**Action:** Always initialize a `requests.Session()` object when making multiple HTTP requests to the same host. This utilizes Keep-Alive and connection pooling, drastically reducing network latency and improving crawl speed.
