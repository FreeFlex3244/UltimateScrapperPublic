## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.
## 2024-11-20 - Redundant URL Parsing in Recursive Loops
**Learning:** In a recursive web scraper, evaluating `urlparse()` against a static property like `self.start_url` inside the inner crawler loop causes severe and unnecessary overhead, resulting in O(N) redundant string parsing (where N is the number of crawled URLs).
**Action:** Precompute static values or invariants (like `self.start_domain = urlparse(self.start_url).netloc`) during initialization or class instantiation to ensure they are parsed only once and can be referenced cheaply in O(1) time within loops.
