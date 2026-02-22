import socket
import ipaddress
from urllib.parse import urlparse

def is_safe_url(url):
    """
    Checks if a URL is safe to scrape (i.e., not a private/loopback IP or localhost).

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    try:
        parsed = urlparse(url)
    except Exception:
        return False

    if parsed.scheme not in ('http', 'https'):
        return False

    hostname = parsed.hostname
    if not hostname:
        return False

    # Check for localhost explicit string
    if hostname.lower() == 'localhost':
        return False

    try:
        # Check if it's an IP address directly
        ip = ipaddress.ip_address(hostname)
        if ip.is_private or ip.is_loopback or ip.is_link_local:
            return False
    except ValueError:
        # Not an IP address, it's a domain name.
        # We should verify it doesn't resolve to a private IP.
        try:
            # Resolve to IP
            ip_str = socket.gethostbyname(hostname)
            ip = ipaddress.ip_address(ip_str)
            if ip.is_private or ip.is_loopback or ip.is_link_local:
                return False
        except (socket.gaierror, ValueError):
            # DNS resolution failed or invalid IP returned
            # Fail safe
            return False

    return True
