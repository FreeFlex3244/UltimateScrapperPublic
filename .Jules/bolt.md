## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2026-03-02 - [Connection Pooling in Scraper]
**Learning:** The scraper was opening a new connection for every HTTP request, introducing significant overhead. Using requests.Session() to pool and reuse connections can drastically improve the speed of the scraper when doing multiple calls to the same or different hosts, without adding much complexity.
**Action:** Utilize requests.Session() for multiple sequential requests, especially in scraping or iterative processes, to gain a performance boost from Keep-Alive connection reuse.
