## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-06-14 - HTTP Connection Pooling with requests.Session
**Learning:** Using `requests.get()` within a scraping loop creates a new TCP connection for every request. Since a targeted scraper frequently hits the same domain, this introduces a massive overhead in TCP/TLS handshakes.
**Action:** Replaced `requests.get()` with `self.session.get()` via `requests.Session()` initialized at thread start. This enables HTTP Keep-Alive, reusing the underlying connections and significantly reducing network latency bottlenecks.
