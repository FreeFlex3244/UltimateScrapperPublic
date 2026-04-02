## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-23 - Connection Pooling for Web Scrapers
**Learning:** Using `requests.get()` inside a recursive scraping loop creates a new TCP connection and performs a new TLS handshake for every single request, causing a massive performance bottleneck.
**Action:** Always use `requests.Session()` (connection pooling) for applications that make repeated HTTP requests to the same domains. Initialize it cleanly and ensure it is closed to free up sockets.
