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
        def side_effect(url, **kwargs):
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
                # Depth 2 -> Links to Depth 3 (should not be processed further
                # due to max_depth=2)
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
    def test_stop(self, mock_get):
        # Set stop event
        self.scraper.stop()
        self.assertTrue(self.scraper.stop_event.is_set())

        # Manually seed queue to see if it processes anything
        self.scraper.queue.append(("http://example.com", 0, 0))

        # Run crawl
        self.scraper.crawl()

        # Since stopped, it should check stop_event and exit immediately
        # So requests.get should NOT be called
        self.assertFalse(mock_get.called)

    @patch('src.scraper.requests.get')
    def test_redirect_handling(self, mock_get):
        # Setup mock response content for 6 redirects to test the limit
        def side_effect(url, **kwargs):
            mock_response = MagicMock()
            # Redirect chain: example.com -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
            if url == "http://example.com":
                mock_response.status_code = 301
                mock_response.headers = {'Location': 'http://example.com/1'}
            elif url == "http://example.com/1":
                mock_response.status_code = 301
                mock_response.headers = {'Location': 'http://example.com/2'}
            elif url == "http://example.com/2":
                mock_response.status_code = 301
                mock_response.headers = {'Location': 'http://example.com/3'}
            elif url == "http://example.com/3":
                mock_response.status_code = 301
                mock_response.headers = {'Location': 'http://example.com/4'}
            elif url == "http://example.com/4":
                mock_response.status_code = 301
                mock_response.headers = {'Location': 'http://example.com/5'}
            elif url == "http://example.com/5":
                mock_response.status_code = 301
                mock_response.headers = {'Location': 'http://example.com/6'}
            elif url == "http://example.com/6":
                mock_response.status_code = 200
                mock_response.headers = {'Content-Type': 'text/html'}
                mock_response.content = b''
            return mock_response

        mock_get.side_effect = side_effect

        # Run crawl which will start with http://example.com, depth=0,
        # redirect_count=0
        self.scraper.crawl()

        calls = set(args[0][0] for args in mock_get.call_args_list)

        # It should process original + 5 redirects (since the 5th redirect has redirect_count=5 and will not append the 6th URL)
        # The URLs requested should be:
        # 0. http://example.com
        # 1. http://example.com/1
        # 2. http://example.com/2
        # 3. http://example.com/3
        # 4. http://example.com/4
        # 5. http://example.com/5
        self.assertIn("http://example.com", calls)
        self.assertIn("http://example.com/1", calls)
        self.assertIn("http://example.com/5", calls)
        self.assertNotIn("http://example.com/6", calls)


if __name__ == '__main__':
    unittest.main()
