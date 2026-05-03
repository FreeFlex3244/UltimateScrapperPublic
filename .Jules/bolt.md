## 2025-05-22 - List vs Deque for BFS Queue
**Learning:** The scraper used a standard Python list for its BFS queue with `pop(0)`, which is an O(n) operation. As the crawl queue grows, this creates a hidden quadratic bottleneck purely in queue management, separate from network latency.
**Action:** Always inspect queue implementations in recursive/iterative processing loops. Replaced with `collections.deque` for O(1) pops.

## 2025-05-22 - Caching Static URL Parsing in Scraping Loops
**Learning:** Repeatedly calling `urlparse` on a static base URL inside a recursive crawling loop introduces redundant CPython overhead that accumulates over thousands of links.
**Action:** Precompute static parsed components (like `.netloc`) in the class constructor (`__init__`) to turn O(N) repetitive parsing into an O(1) attribute lookup.
