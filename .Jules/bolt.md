## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precompute static URL properties in recursive crawls
**Learning:** Parsing the static `start_url` inside the inner loop of the recursive crawl causes unnecessary overhead. Using O(n) loops to match ends with extensions is also an overhead.
**Action:** Precompute static properties (e.g. `self.start_netloc`, `self.extensions_tuple`) in `__init__` before starting the crawl to remove O(N) penalties and take advantage of C-level tuple matching.
