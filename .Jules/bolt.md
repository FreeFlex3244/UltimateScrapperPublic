## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2026-06-28 - Avoid redundant URL parsing in loops
**Learning:** Calling `urlparse(self.start_url).netloc` inside a recursive link-parsing loop adds substantial overhead since `self.start_url` never changes. Precomputing static URL components in `__init__` removes redundant parsing.
**Action:** Always inspect inner loops for redundant parsing of static data and move them to initialization logic.
