## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-24 - Precomputing Static URL Properties in Loops
**Learning:** Calling functions like `urlparse()` on a static variable (like a `start_url`) inside a high-frequency loop (such as processing every discovered link in a scraper) introduces unnecessary O(n) overhead. In this architecture, it caused redundant CPU cycles per parsed link.
**Action:** Always inspect loops in crawling algorithms to ensure static values are precomputed outside the loop, typically during object initialization.
