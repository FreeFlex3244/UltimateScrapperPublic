## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Connection Pooling for Repeated API/Network Calls
**Learning:** The scraper was making a new TCP and TLS handshake for every single URL visited (`requests.get(url)`). For a recursive crawler hitting the same domain hundreds of times, this adds massive overhead per request.
**Action:** Always use `requests.Session()` to enable connection pooling for HTTP requests when making multiple requests to the same host/domain, eliminating repeated TCP handshake latency. Make sure to close the session to avoid lingering connections.
