import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import threading
import time
import os
import sqlite3
from collections import deque
from src.database import Database
from src.security import is_safe_url

class Scraper(threading.Thread):
    def __init__(self, start_url, max_depth, extensions, db_name='files.db'):
        super().__init__()
        self.start_url = start_url
        self.max_depth = int(max_depth)
        # Clean extensions list
        self.extensions = [ext.lower().strip().lstrip('.') for ext in extensions.split(',') if ext.strip()]
        self.db_name = db_name
        self.stop_event = threading.Event()
        self.visited = set()
        self.queue = deque()
        self.status = "Idle"
        self.total_found = 0
        self.current_depth = 0
        self.current_url = ""

    def run(self):
        self.status = "Running"
        # Initialize DB connection within the thread
        self.db = Database(self.db_name)
        # ⚡ Bolt: Initialize requests Session within the thread for thread-safety.
        # This reuses TCP connections across requests, significantly reducing latency and overhead.
        self.session = requests.Session()
        try:
            self.crawl()
        except Exception as e:
            print(f"Scraper error: {e}")
            self.status = f"Error: {e}"
        finally:
            self.db.close()
            self.session.close()
            if not self.stop_event.is_set():
                self.status = "Completed"
            else:
                self.status = "Stopped"

    def stop(self):
        self.stop_event.set()

    def is_target_file(self, url):
        path = urlparse(url).path
        for ext in self.extensions:
            if path.lower().endswith(f".{ext}"):
                return True, ext
        return False, None

    def crawl(self):
        # BFS
        self.queue.append((self.start_url, 0))
        self.visited.add(self.start_url)

        while self.queue and not self.stop_event.is_set():
            url, depth = self.queue.popleft()
            self.current_depth = depth
            self.current_url = url

            # Update status for UI
            # self.status = f"Depth {depth}: {url}"

            if depth > self.max_depth:
                continue

            if not is_safe_url(url):
                print(f"Skipping unsafe URL: {url}")
                continue

            try:
                # Fetch page
                # ⚡ Bolt: Use connection pooling via session.
                # This reuses TCP connections across requests, significantly reducing latency and overhead.
                response = self.session.get(url, timeout=10)
                if response.status_code != 200:
                    continue

                # Check content type - only parse HTML
                content_type = response.headers.get('Content-Type', '')
                if 'text/html' not in content_type:
                    continue

                soup = BeautifulSoup(response.content, 'html.parser')
                links = soup.find_all('a', href=True)

                for link in links:
                    href = link['href']
                    full_url = urljoin(url, href)

                    # Normalize URL (remove fragment)
                    parsed_full = urlparse(full_url)
                    clean_url = parsed_full.scheme + "://" + parsed_full.netloc + parsed_full.path
                    if parsed_full.query:
                        clean_url += "?" + parsed_full.query

                    if clean_url in self.visited:
                        continue

                    # Check if it's a file we want
                    is_target, ext = self.is_target_file(clean_url)

                    if is_target:
                        filename = os.path.basename(parsed_full.path)
                        self.db.add_file(filename, ext, clean_url, url, depth)
                        self.total_found += 1
                        self.visited.add(clean_url) # Mark file as visited so we don't re-add
                    else:
                        # It's a potential directory/page to follow
                        # Only follow if:
                        # 1. Depth < Max Depth
                        # 2. Same domain (to contain scope)
                        if depth < self.max_depth:
                            if parsed_full.netloc == urlparse(self.start_url).netloc:
                                self.visited.add(clean_url)
                                self.queue.append((clean_url, depth + 1))

                # Sleep slightly to be nice
                time.sleep(0.1)

            except Exception as e:
                print(f"Error crawling {url}: {e}")
