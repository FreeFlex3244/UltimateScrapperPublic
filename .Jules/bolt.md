## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-05-30 - Precomputing static URL parsing in iterative loops
**Learning:** The scraper repeatedly called `urlparse(self.start_url).netloc` inside the BFS crawl loop for every single discovered link. This creates unnecessary parsing overhead that scales linearly with the number of links found on the page and the total depth.
**Action:** Precompute the netloc of the start URL during object initialization and reuse it within iterative loops.
