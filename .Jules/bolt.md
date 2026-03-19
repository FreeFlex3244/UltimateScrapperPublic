## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Connection Pooling
**Learning:** The scraper was creating a new TCP connection and TLS handshake for every URL by using requests.get() instead of requests.Session(). In a recursive domain scraper, this lack of connection pooling creates significant latency overhead.
**Action:** Always initialize and use requests.Session() within the scraping thread to reuse TCP connections, improving request speed.
