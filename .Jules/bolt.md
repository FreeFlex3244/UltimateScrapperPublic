## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2025-05-22 - Repeated Static URL Parsing in Scraper Loops
**Learning:** Calling `urlparse()` repeatedly on the exact same static URL (like a user-provided `start_url`) inside a recursive or iterative web crawling loop adds massive parsing overhead, especially since the string never changes.
**Action:** Always inspect inner loops for loop-invariant computations. Precompute and cache parsed URL components (like `netloc`) during class initialization.
