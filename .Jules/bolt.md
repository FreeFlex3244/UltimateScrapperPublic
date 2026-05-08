## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - O(1) Extension Matching and Caching URL Parse
**Learning:** Checking URL paths against a list of file extensions using an O(N) Python loop causes redundant processing, especially since most discovered URLs (like normal HTML links) are not target files. Python's `str.endswith()` accepts a tuple, allowing for an O(1) C-level string match which acts as a fast-path rejection. Additionally, repeatedly calling `urlparse()` on a static URL like `start_url` inside the scraping loop adds unnecessary parsing overhead.
**Action:** Precomputed a tuple of formatted extensions (e.g., `('.zip', '.tar.gz')`) and `self.start_netloc` during class initialization. Used `path.endswith(tuple)` for O(1) rejection and the precomputed netloc to eliminate redundant parsing.
