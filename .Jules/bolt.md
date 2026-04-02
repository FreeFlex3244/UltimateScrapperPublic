## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-22 - Connection Pooling for TCP Optimization
**Learning:** Calling `requests.get()` in a loop without a session means establishing a new TCP connection and performing an SSL handshake for every single request, which creates huge network latency overhead.
**Action:** Always utilize `requests.Session()` within loops to automatically leverage connection pooling and HTTP keep-alive, reducing latency and resource exhaustion significantly.
