## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - O(1) File Extension Matching & Netloc Precomputation
**Learning:** Using `endswith(tuple)` provides O(1) C-level performance compared to O(N) Python loops over file extensions. Additionally, repeatedly parsing static URLs like `start_url` inside a recursive/iterative loop adds unnecessary overhead.
**Action:** Precomputed `start_netloc` and `ext_tuple` during initialization. Replaced O(N) loop in `is_target_file` with O(1) `path.endswith(tuple)` check.
