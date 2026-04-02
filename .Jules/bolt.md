## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-04-02 - Thread-Safe Session Management
**Learning:** Implementing connection pooling via `requests.Session` in a multi-threaded application requires instantiating the session *inside* the thread's `run` loop (or specifically per-thread) rather than in `__init__`. Additionally, test harnesses bypassing `run` will fail if the session isn't manually mocked in `setUp`.
**Action:** When adding `requests.Session` for performance, verify thread safety by initializing it in the thread's execution context, and remember to mock it manually in test suites that bypass the main thread start sequence.
