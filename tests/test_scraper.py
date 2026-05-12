import unittest
from unittest.mock import MagicMock, patch
import threading
import time
from src.scraper import Scraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        # Initialize Scraper with dummy values
        self.scraper = Scraper("http://example.com", 2, "zip,iso")
        # Mock the database connection object
        self.scraper.db = MagicMock()

    @patch('src.scraper.requests.get')
    def test_crawl_depth(self, mock_get):
        # Setup mock response content
        def side_effect(url, timeout=10, allow_redirects=False):
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.headers = {'Content-Type': 'text/html'}

            # Simple simulation of depth
            if url == "http://example.com":
                # Depth 0 -> Links to Depth 1
                mock_response.content = b'<a href="page1.html">Page 1</a><a href="file.zip">File</a>'
            elif url == "http://example.com/page1.html":
                # Depth 1 -> Links to Depth 2
                mock_response.content = b'<a href="page2.html">Page 2</a><a href="file2.iso">File 2</a>'
            elif url == "http://example.com/page2.html":
                # Depth 2 -> Links to Depth 3 (should not be processed further due to max_depth=2)
                mock_response.content = b'<a href="page3.html">Page 3</a>'
            else:
                mock_response.content = b''
            return mock_response

        mock_get.side_effect = side_effect

        # Call crawl directly (bypassing run() which sets up DB)
        # We manually set self.db in setUp
        self.scraper.crawl()

        # Check that add_file was called
        # We expect file.zip and file2.iso to be added
        self.assertTrue(self.scraper.db.add_file.called)
        self.assertEqual(self.scraper.db.add_file.call_count, 2)

        # Verify specific calls if needed
        # args: (filename, extension, url, source_url, depth)
        # call_args_list[0] -> file.zip
        # call_args_list[1] -> file2.iso

    @patch('src.scraper.requests.get')
    def test_crawl_redirect(self, mock_get):
        # Mock a 301 response that redirects to a local IP
        mock_response = MagicMock()
        mock_response.status_code = 301
        mock_response.headers = {'Location': 'http://127.0.0.1/admin'}
        mock_get.return_value = mock_response

        # Run crawl
        self.scraper.crawl()

        # The initial request to start_url should be made
        self.assertEqual(mock_get.call_count, 1)

        # The redirect should be blocked by is_safe_url, leaving the queue empty
        self.assertEqual(len(self.scraper.queue), 0)

    @patch('src.scraper.requests.get')
    def test_stop(self, mock_get):
        # Set stop event
        self.scraper.stop()
        self.assertTrue(self.scraper.stop_event.is_set())

        # Clear state to prevent duplicate start_url queuing from crawl()
        self.scraper.queue.clear()
        self.scraper.visited.clear()

        # Run crawl
        self.scraper.crawl()

        # Since stopped, it should check stop_event and exit immediately
        # So requests.get should NOT be called
        self.assertFalse(mock_get.called)

if __name__ == '__main__':
    unittest.main()
