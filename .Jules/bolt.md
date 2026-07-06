## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-24 - Precomputing Static URLs in Scraping Loops
**Learning:** Calling `urlparse` on static URLs like `start_url` inside recursive or iterative scraping loops introduces severe O(N) redundancy per page scraped.
**Action:** Precompute static URL components (like `netloc`) during class initialization to eliminate parsing overhead inside loops.
