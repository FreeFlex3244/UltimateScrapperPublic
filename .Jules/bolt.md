## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Connection Pooling for Repeated API/Network Calls
**Learning:** Making repeated requests to the same domain using `requests.get()` opens and closes a new TCP connection (and performs TLS handshakes) every time. This adds substantial overhead for scraping tasks.
**Action:** Always reuse HTTP connections when scraping or calling APIs by using `requests.Session()` within the thread's lifecycle. Ensure proper socket cleanup by calling `.close()` on the session instance in a finally block.