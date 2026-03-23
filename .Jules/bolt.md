## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-23 - Connection Pooling in Scraper Threads
**Learning:** Initializing `requests.Session()` globally or in the main thread for use in scraping threads can cause thread-safety issues. However, creating a new `requests.get()` call for every URL creates immense overhead from TCP/TLS handshakes.
**Action:** Always initialize `requests.Session()` inside the thread's `run()` method (or worker function) to ensure thread-safety while gaining the massive performance benefits of connection pooling. Ensure it is closed in a `finally` block to prevent socket leaks.
