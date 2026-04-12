## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2026-04-12 - O(1) URL Extension Validation
**Learning:** Checking URL extensions against a list using a Python `for` loop with `endswith` runs in O(N) time and creates a massive bottleneck when validating thousands of miss URLs during a web crawl. Using `rsplit('.', 1)` fails for multi-dot extensions like `.tar.gz`.
**Action:** Precompute a tuple of formatted extensions (e.g., `('.zip', '.tar.gz')`) and pass it to `str.endswith(tuple)` for O(1) C-level performance, falling back to the loop only to identify the specific matched extension when a hit occurs.
