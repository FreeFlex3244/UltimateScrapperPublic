## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-04-02 - Reuse TCP Connections for HTTP Scrapers
**Learning:** Initializing `requests.Session()` within a scraper thread allows reusing underlying TCP connections between HTTP requests to the same domains, reducing latency by avoiding multiple connection setups.
**Action:** When implementing scraping or making many repeated API calls, always initialize and use a `Session` object properly within the executing thread instead of calling `requests.get()` directly. Make sure to close the session appropriately when done.
