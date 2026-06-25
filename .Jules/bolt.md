## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-06-25 - Avoid Repeated URL Parsing in Scraper Inner Loops
**Learning:** Repeatedly parsing static configuration properties like `start_url` inside deep nested loops (like per-link evaluation during crawling) introduces compounding performance overhead due to string manipulation and validation in Python's standard library.
**Action:** Precompute parsed components (like `netloc`) during object initialization rather than evaluating them on demand for each iteration within `crawl()`.
