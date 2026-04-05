1. **Understand and fix the SSRF Vulnerability via Redirects**
   - In `src/scraper.py`, `requests.get` currently follows redirects by default (`allow_redirects=True`). This means a malicious server can return a 301/302 redirect to an internal IP (like `http://127.0.0.1` or `http://169.254.169.254/`), bypassing the initial `is_safe_url` validation and causing Server-Side Request Forgery (SSRF).
   - I will modify `src/scraper.py` to manually handle HTTP redirects. `allow_redirects=False` will be passed to `self.session.get`.
   - Any `Location` header in the redirect response will be extracted, validated with `is_safe_url`, and if safe, pushed onto the queue.
   - The queue will include a `redirect_count` tuple value to prevent infinite redirect loops (e.g., maximum 5 redirects).
2. **Setup Session Management**
   - I will modify `src/scraper.py` to instantiate and use a `requests.Session()` to handle network requests efficiently and close the session properly in the thread's `finally` block.
3. **Update Tests**
   - Update `tests/test_scraper.py` so that it mocks `self.scraper.session.get` instead of patching `requests.get`. Ensure the mocked `side_effect` function accepts `allow_redirects`.
   - Update `queue.append` arguments to include the new `redirect_count` in tests.
4. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**
   - Run `python3 -m unittest discover tests`.
   - Make sure all tests pass.
5. **Report and Submit PR**
   - Submit the PR with title format "🛡️ Sentinel: [CRITICAL] Fix SSRF vulnerability via HTTP redirects" and appropriate description.
