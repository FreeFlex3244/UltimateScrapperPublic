## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-23 - Connection Pooling for Scraper
**Learning:** Re-opening TCP connections for every HTTP request in a scraper introduces significant latency. The requests library does not pool connections across different `requests.get()` calls.
**Action:** Use `requests.Session()` within the scraper's execution thread to enable connection pooling, which keeps TCP connections alive and reuses them for subsequent requests to the same host, reducing overhead.
