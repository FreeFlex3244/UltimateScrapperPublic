import unittest
from unittest.mock import patch
from src.security import is_safe_url
import socket

class TestSecurity(unittest.TestCase):
    @patch('src.security.socket.gethostbyname')
    def test_safe_urls(self, mock_gethostbyname):
        mock_gethostbyname.return_value = "8.8.8.8"
        self.assertTrue(is_safe_url("http://example.com"))
        self.assertTrue(is_safe_url("https://google.com"))

    def test_unsafe_schemes(self):
        self.assertFalse(is_safe_url("ftp://example.com"))
        self.assertFalse(is_safe_url("file:///etc/passwd"))
        self.assertFalse(is_safe_url("javascript:alert(1)"))

    def test_localhost(self):
        self.assertFalse(is_safe_url("http://localhost"))
        self.assertFalse(is_safe_url("http://localhost:8080"))

    def test_private_ips(self):
        self.assertFalse(is_safe_url("http://127.0.0.1"))
        self.assertFalse(is_safe_url("http://10.0.0.1"))
        self.assertFalse(is_safe_url("http://192.168.1.1"))
        self.assertFalse(is_safe_url("http://172.16.0.1"))

    @patch('src.security.socket.gethostbyname')
    def test_dns_resolution_block(self, mock_gethostbyname):
        # Mock internal.local resolving to a private IP
        mock_gethostbyname.return_value = "192.168.1.100"
        self.assertFalse(is_safe_url("http://internal.local"))

        # Mock malicious.com resolving to loopback
        mock_gethostbyname.return_value = "127.0.0.1"
        self.assertFalse(is_safe_url("http://malicious.com"))

    @patch('src.security.socket.gethostbyname')
    def test_dns_failure(self, mock_gethostbyname):
        mock_gethostbyname.side_effect = socket.gaierror("DNS Error")
        self.assertFalse(is_safe_url("http://nonexistent.domain"))

if __name__ == '__main__':
    unittest.main()
