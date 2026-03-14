## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-14 - Thread-Safe Session Pooling
**Learning:** The scraper used `requests.get()` inside the thread, opening new TCP/TLS connections per page. Moving to `requests.Session()` adds connection pooling but requires initializing the Session INSIDE the thread's `run()` method to avoid thread-safety issues, and explicitly closing it in `finally` to prevent socket leaks.
**Action:** When adding connection pooling to multi-threaded scrapers, strictly bind the session lifecycle to the thread's execution block.
