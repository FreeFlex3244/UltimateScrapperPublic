## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - O(N) Extension Checking to O(1) C-Level Tuple Matching
**Learning:** Checking a URL path against a list of extensions (e.g. `path.endswith(".zip")`) in a Python loop for every URL crawled is incredibly slow (O(N) Python loop allocations). Even for small lists, strings allocations and Python iterators add up quickly in web scrapers processing thousands of links.
**Action:** When validating ends of strings against a list of possibilities, precompute a tuple of the formatted endings (e.g., `('.zip', '.rar')`) and use Python's built-in `str.endswith(tuple)` method. This pushes the iteration to a highly optimized C-level loop and acts in pseudo-O(1) time compared to native Python code.
