import time
import requests
import threading
from bs4 import BeautifulSoup

def mock_server():
    from flask import Flask
    import logging
    app = Flask(__name__)
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True

    @app.route('/')
    def index():
        return "<html><body><a href='/1'>1</a><a href='/2'>2</a></body></html>"
    @app.route('/<id>')
    def page(id):
        return "<html><body>OK</body></html>"
    app.run(port=5001, debug=False)

t = threading.Thread(target=mock_server, daemon=True)
t.start()
time.sleep(1)

def bench_get():
    start = time.time()
    for _ in range(100):
        requests.get('http://127.0.0.1:5001/')
    return time.time() - start

def bench_session():
    start = time.time()
    s = requests.Session()
    for _ in range(100):
        s.get('http://127.0.0.1:5001/')
    return time.time() - start

print(f"requests.get: {bench_get():.3f}s")
print(f"requests.Session: {bench_session():.3f}s")
