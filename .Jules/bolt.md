## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-24 - Connection Pooling in Scraper Threads
**Learning:** The scraper was creating a new TCP connection for every recursive fetch via `requests.get()`. Because scraping heavily queries the same domain repeatedly, connection overhead (TCP handshake, TLS negotiation) was a major bottleneck. However, `requests.Session()` is not thread-safe if shared across multiple scraper threads.
**Action:** Use `requests.Session()` to enable connection pooling for recursive requests, but instantiate it *inside* the thread's `run()` method to ensure thread safety and avoid bleeding sockets.