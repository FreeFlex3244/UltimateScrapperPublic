## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-24 - Requests Session Object Connection Pooling Thread Safety
**Learning:** Initializing `requests.Session()` within the scraper's `run()` method (the thread context) enables connection pooling, which reuses the underlying TCP connections rather than opening a new connection for every HTTP request. This dramatically speeds up scraping. However, sharing `Session` objects across threads can be problematic, so it's critical to initialize it inside the thread's execution context (`run()` rather than `__init__()`) and ensure proper socket cleanup using a `finally` block to call `session.close()`.
**Action:** Always utilize connection pooling for multi-request scraping or API calls, and remember to respect thread-safety and socket cleanup rules.
