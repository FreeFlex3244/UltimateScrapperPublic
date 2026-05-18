## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2024-05-22 - Precomputing static properties for hot loops
**Learning:** Checking string extensions against a list of options in a loop scales poorly. Calling `urlparse(static_url).netloc` inside an iterative scrape loop also introduces redundant CPU overhead per processing tick. Python's `str.endswith(tuple)` is a fast-fail C-level check.
**Action:** When working with values derived from constructor arguments that remain static (like base url and target extensions), precompute them into C-friendly structures (like tuples) directly in `__init__` rather than recalculating them in the processing loop.
