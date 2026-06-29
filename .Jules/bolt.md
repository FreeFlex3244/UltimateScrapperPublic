## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-24 - Precomputing URL Parsed Components in Inner Loops
**Learning:** Inside recursive web scraping loops, calling `urlparse` repeatedly on a static base URL introduces redundant overhead. Since the base URL doesn't change, its parts (like netloc) remain constant.
**Action:** Always precalculate and store URL components for static URLs (e.g., `self.start_url`) during class initialization rather than computing them for every single link evaluated in iterative functions.
