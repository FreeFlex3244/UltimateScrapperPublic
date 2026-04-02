## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2026-04-02 - Connection Pooling in Scraper Threads
**Learning:** Reusing HTTP connections with `requests.Session` significantly reduces overhead (such as TCP handshakes and DNS lookups) during recursive scraping, compared to instantiating new connections for each request. Sessions must be properly initialized and closed in thread contexts to avoid socket leakage.
**Action:** Always instantiate `requests.Session()` inside the thread's run method and use a `finally` block to securely close connections using `self.session.close()`.
