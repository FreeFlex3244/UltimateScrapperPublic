## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Precomputing invariants in crawling loops
**Learning:** Calling `urlparse(self.start_url).netloc` inside the nested link-processing loop caused O(N) redundant string parsing overhead per discovered link. Similarly, iterating through extensions to check `endswith` on each path is slow.
**Action:** Precompute static URL parts (`self.start_netloc`) and extension tuples (`self.extensions_tuple`) in the class constructor (`__init__`). Use `path.endswith(tuple)` for O(1) C-level performance during target file checks.
