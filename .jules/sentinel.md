## 2024-05-24 - [CRITICAL] Fix SSRF via automatic redirect following
 **Vulnerability:** SSRF bypass via automatic redirect following. The scraper was checking `is_safe_url` before fetching, but `requests.get` implicitly follows redirects, potentially bouncing to an unsafe, internal location.
 **Learning:** Validating a URL prior to requesting it is insufficient if the HTTP client can automatically follow redirects to a new destination without validation.
 **Prevention:** Always use `allow_redirects=False` in HTTP requests. Manually process redirects (status codes 301-308), extract the `Location` header, validate the new destination URL with `is_safe_url`, and limit redirect counts to prevent infinite loops.
