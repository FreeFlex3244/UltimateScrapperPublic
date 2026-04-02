## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2026-04-02 - Connection Pooling in Threads
**Learning:** When using `requests` in a threaded application, using `requests.get()` establishes a new TCP connection for every request, which is a major performance bottleneck separate from database latency or queue management. `requests.Session()` allows for connection pooling and TCP connection reuse, but must be instantiated inside the thread's `run()` method to ensure thread safety.
**Action:** Always instantiate `requests.Session()` inside the thread's `run()` method and use `session.get()` instead of `requests.get()` to optimize scraping operations, ensuring `session.close()` is called in the `finally` block.
