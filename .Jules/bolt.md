## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Requests Connection Pooling in Threaded Scraper
**Learning:** `requests.get()` opens a new TCP connection for every request, which creates a huge bottleneck when scraping many pages on the same domain. While `requests.Session()` solves this via connection pooling, initializing it in `__init__` when the class is a `threading.Thread` can lead to thread-safety issues because the sockets are shared between the parent thread and the worker thread.
**Action:** When optimizing network requests in a multithreaded architecture, always use `requests.Session()` but initialize it *inside* the `run()` method (the worker thread context). Always remember to close it (`session.close()`) in the `finally` block to prevent resource leaks.
