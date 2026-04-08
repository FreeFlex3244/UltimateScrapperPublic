## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - HTTP Connection Pooling
**Learning:** The scraper was creating a new TCP connection and performing a new DNS lookup/TLS handshake for every single `requests.get` call. In a crawler fetching multiple pages from the same domain, this is a significant bottleneck.
**Action:** Use `requests.Session()` within threads performing multiple HTTP requests to the same host to enable connection pooling and reuse underlying TCP connections.
