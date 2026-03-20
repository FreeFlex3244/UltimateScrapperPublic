## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Connection Pooling in Scraper
**Learning:** The recursive web scraper was instantiating a new TCP connection via `requests.get` for every single page fetched. This meant a full TCP handshake (and SSL negotiation) for every link, which is a massive hidden bottleneck. Using `requests.Session()` reuses TCP connections to the same host, speeding up the crawl significantly.
**Action:** Always check if consecutive HTTP requests hit the same domains in a loop, and use an HTTP connection pooling client (like `requests.Session()`) to optimize.
