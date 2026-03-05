## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-03-05 - TLS Handshake Bottleneck
**Learning:** When web scraping multiple pages on the same domain, repeatedly calling `requests.get()` creates a significant performance bottleneck due to the overhead of opening new TCP connections and negotiating TLS handshakes for every single request.
**Action:** Always use `requests.Session()` to leverage connection pooling (Keep-Alive), which reuses the underlying TCP connection and significantly improves scraping speed.
