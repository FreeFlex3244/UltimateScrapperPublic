## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Thread-Safe HTTP Connection Pools
**Learning:** Initializing `requests.Session()` directly in `Scraper.__init__` creates thread-safety problems because the `Scraper` class inherits from `threading.Thread`. Sockets and sessions generated in the main thread shouldn't be shared implicitly into spawned threads.
**Action:** Always initialize connection pools and database connections inside the `run()` method of threaded processes to ensure proper thread isolation and prevent "socket closed" or connection dropping errors.
