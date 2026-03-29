## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2026-03-28 - [Connection Pooling in Scraper]
**Learning:** Implementing `requests.Session()` for connection pooling is a significant performance boost in recursive scrapers by avoiding TCP handshakes for requests to the same domain.
**Action:** Always initialize a `requests.Session()` in recursive scrapers and ensure sockets are cleaned up in the `finally` block of the thread's execution.
