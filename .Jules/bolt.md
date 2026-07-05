## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-07-05 - Avoid Redundant Parsing in Recursive Scrapers
**Learning:** Parsing static URLs (like `start_url`) with `urlparse` repeatedly inside deep scraping loops creates O(N) overhead per page, where N is the number of links.
**Action:** Always precompute static parsed components (like domains or paths) during class initialization before entering recursive or iterative scraping loops.
