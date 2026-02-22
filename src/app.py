from flask import Flask, render_template, request, jsonify
from src.scraper import Scraper
from src.database import Database
from src.security import is_safe_url
import threading
import os

app = Flask(__name__)
DB_NAME = 'files.db'

# Global variable to hold the scraper thread
scraper_thread = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/start', methods=['POST'])
def start_scrape():
    global scraper_thread

    if scraper_thread and scraper_thread.is_alive():
        return jsonify({'status': 'error', 'message': 'Scraper is already running'}), 400

    data = request.json
    url = data.get('url')
    depth = data.get('depth')
    extensions = data.get('extensions')

    if not url or not depth or not extensions:
        return jsonify({'status': 'error', 'message': 'Missing parameters'}), 400

    if not is_safe_url(url):
        return jsonify({'status': 'error', 'message': 'Invalid or restricted URL'}), 400

    scraper_thread = Scraper(url, depth, extensions, db_name=DB_NAME)
    scraper_thread.start()

    return jsonify({'status': 'success', 'message': 'Scraper started'})

@app.route('/api/stop', methods=['POST'])
def stop_scrape():
    global scraper_thread
    if scraper_thread and scraper_thread.is_alive():
        scraper_thread.stop()
        return jsonify({'status': 'success', 'message': 'Stopping scraper...'})
    return jsonify({'status': 'error', 'message': 'Scraper not running'})

@app.route('/api/status', methods=['GET'])
def get_status():
    global scraper_thread
    if scraper_thread:
        status = scraper_thread.status
        found = scraper_thread.total_found
        depth = scraper_thread.current_depth
        is_alive = scraper_thread.is_alive()
        current_url = scraper_thread.current_url
    else:
        status = "Idle"
        found = 0
        depth = 0
        is_alive = False
        current_url = ""

    # Also get total files in DB?
    # db = Database(DB_NAME)
    # total_db = ...
    # db.close()

    return jsonify({
        'status': status,
        'found': found,
        'depth': depth,
        'is_alive': is_alive,
        'current_url': current_url
    })

@app.route('/api/search', methods=['GET'])
def search_files():
    query = request.args.get('q', '')
    ext = request.args.get('ext', '')

    db = Database(DB_NAME)
    results = db.search_files(query, ext)
    db.close()

    return jsonify({'results': results})

@app.route('/api/clear', methods=['POST'])
def clear_db():
    global scraper_thread
    if scraper_thread and scraper_thread.is_alive():
         return jsonify({'status': 'error', 'message': 'Cannot clear DB while scraper is running'}), 400

    db = Database(DB_NAME)
    db.clear_database()
    db.close()
    return jsonify({'status': 'success', 'message': 'Database cleared'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
