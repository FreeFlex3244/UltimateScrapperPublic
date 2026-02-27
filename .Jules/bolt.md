## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Connection Pooling with requests.Session()
**Learning:** The scraper used individual `requests.get()` calls for every crawled URL, triggering a new TCP connection and TLS handshake for every single request. In a recursive web scraper traversing a single domain, this network overhead is an immense performance bottleneck.
**Action:** Replaced `requests.get()` with `requests.Session().get()`. `requests.Session()` inherently utilizes HTTP Keep-Alive, allowing subsequent requests to the same host to reuse the underlying TCP connection, drastically improving throughput. Ensured the session is cleanly closed in the `finally` block of the thread's `run()` method.