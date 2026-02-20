# Community Global Scraper 🌍🕷️

An advanced, recursive web scraper and search engine designed for the global community. Easily index downloadable files from any website (e.g., Myrient, open directories) with configurable depth and file extensions.

Featuring a beautiful dark-mode interface with a powerful search engine and **Catalan Pride** 💛❤️💛❤️💛.

## Features ✨

- **Recursive Scraping**: Crawl websites up to a specified depth (e.g., 7 levels deep).
- **Customizable Filters**: Target specific file extensions (zip, iso, mp3, flac, etc.).
- **Built-in Search Engine**: Instantly search your indexed database by filename or extension.
- **Direct Links**: Copy direct download links to your clipboard with one click.
- **Modern UI**: A sleek, dark-themed web interface built with Flask and Bootstrap.
- **Database Persistence**: All found links are stored in a local SQLite database (`files.db`).

## Installation 🛠️

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/community-global-scraper.git
    cd community-global-scraper
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage 🚀

1.  **Start the application:**
    ```bash
    python3 -m src.app
    ```

2.  **Open your browser:**
    Navigate to `http://127.0.0.1:5000`.

3.  **Configure & Scrape:**
    - Enter the **Target URL** (e.g., a directory listing).
    - Set the **Depth** (how many sub-levels to follow).
    - detailed the **Extensions** you want to find.
    - Click **Start Indexing**.

4.  **Search & Download:**
    - Use the search bar to find specific files.
    - Click the **Copy** icon to grab the direct link.

## Example Configuration 📝

- **URL**: `https://myrient.erista.me/files/`
- **Depth**: `3` (Be careful with high depths on large sites!)
- **Extensions**: `zip,7z,iso,cue,bin`

## Disclaimer ⚠️

This tool is for educational and archival purposes only. Please respect the `robots.txt` of websites and do not overload servers with excessive requests. Use responsibly.

---
*Built with ❤️ for the Community.*
