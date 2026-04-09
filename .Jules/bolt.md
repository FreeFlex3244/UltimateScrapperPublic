## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-23 - Substring Search Overhead in Extension Filtering
**Learning:** During the web scraper run (`is_target_file`), the extension filter iteratively checked `path.endswith(ext)` for every single parsed link. Since 99% of crawled links are HTML pages (misses), this resulted in significant O(N) string processing overhead per URL.
**Action:** Pre-calculate tuples of formatted target extensions (`.zip`, `.tar.gz`) during object initialization and leverage Python's built-in `str.endswith(tuple)` for a single C-optimized pass to quickly reject non-matching URLs.
