## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Connection pooling for HTTP requests
**Learning:** Initializing and reusing a single `requests.Session()` object pools TCP connections, significantly improving repeated HTTP request performance in the web scraper by eliminating the overhead of repeatedly setting up and tearing down TCP/TLS connections.
**Action:** Use `requests.Session()` instead of `requests.get()` in areas making repeated network calls, especially within iterative loops.
