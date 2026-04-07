## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2026-04-07 - Connection Pooling Overhead
**Learning:** The web scraper created a new TCP connection and TLS handshake for every single URL visited. This creates substantial latency overhead when repeatedly querying the same domains.
**Action:** Use `requests.Session` for connection pooling to reuse sockets across multiple requests in the same thread, significantly improving crawler performance.
