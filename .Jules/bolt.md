## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Precompute Static URL Parsing
**Learning:** Repeatedly calling `urlparse` on a static URL inside an inner loop causes significant performance overhead.
**Action:** Precompute static values like `urlparse(start_url).netloc` during initialization to eliminate repetitive processing.
