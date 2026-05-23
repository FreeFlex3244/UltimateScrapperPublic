## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-23 - URL parsing and extension checks bottleneck
**Learning:** Calling `urlparse` on static URLs (like `start_url`) inside a recursive crawling loop adds significant parsing overhead. Similarly, looping over an extension list to check file paths via `endswith` is O(N) in Python. Precomputing `urlparse().netloc` and converting a list of extensions into a tuple for `path.endswith(tuple)` provides an O(1) C-level performance boost and eliminates repetitive URL parsing.
**Action:** Always precompute static URL components and use tuple-based `endswith` checks to eliminate redundant processing in iterative loops.
