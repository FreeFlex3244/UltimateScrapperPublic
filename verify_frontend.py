from playwright.sync_api import sync_playwright
import time
import subprocess
import os

def main():
    # Start the Flask app
    server_process = subprocess.Popen(["python3", "-m", "src.app"])
    time.sleep(2) # Give it time to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://127.0.0.1:5000")
            page.wait_for_selector("body")

            # Simple interaction: search for a file
            page.screenshot(path="frontend_screenshot.png")
            print("Screenshot saved to frontend_screenshot.png")
            browser.close()
    finally:
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    main()
