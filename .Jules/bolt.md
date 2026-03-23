## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-22 - Optimize HTTP Requests with Connection Pooling
**Learning:** Initializing a `requests.Session()` within the scraper thread reuses TCP connections and reduces TLS handshake overhead for repeated requests to the same domains, significantly improving scraping performance.
**Action:** Always prefer `requests.Session` for applications making multiple HTTP requests to similar domains instead of using stateless `requests.get()`.
