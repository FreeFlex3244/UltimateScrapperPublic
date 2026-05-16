## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-24 - Precomputing Static URL Parts and Using Tuple Endswith
**Learning:** Inside a web scraper's recursive/iterative loop, repeatedly calling `urlparse` on a static URL like `start_url` causes unnecessary parsing overhead. Additionally, using a Python `for` loop to check if a URL path ends with any of several extensions is slow (O(N)).
**Action:** Precompute static parsed components (e.g., `urlparse(start_url).netloc`) during class initialization. For extension matching, precompute a tuple of formatted extensions and use `path.endswith(tuple)` for O(1) C-level performance.
