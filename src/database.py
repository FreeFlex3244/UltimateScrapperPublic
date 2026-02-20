import sqlite3
import os

class Database:
    def __init__(self, db_name='files.db'):
        # Ensure the database file is stored in the same directory as this script or a 'data' folder
        # For simplicity, let's put it in the root or relative to the script
        self.db_name = db_name
        self.conn = None
        self.connect()
        self.create_table()
        self.create_indexes()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            extension TEXT NOT NULL,
            url TEXT UNIQUE NOT NULL,
            source_url TEXT,
            depth INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def create_indexes(self):
        """Creates indexes for frequently queried columns to improve performance."""
        queries = [
            "CREATE INDEX IF NOT EXISTS idx_files_extension_timestamp ON files(extension, timestamp DESC)",
            "CREATE INDEX IF NOT EXISTS idx_files_timestamp ON files(timestamp DESC)"
        ]
        try:
            cursor = self.conn.cursor()
            for query in queries:
                cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating indexes: {e}")

    def add_file(self, filename, extension, url, source_url, depth):
        query = """
        INSERT OR IGNORE INTO files (filename, extension, url, source_url, depth)
        VALUES (?, ?, ?, ?, ?)
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (filename, extension, url, source_url, depth))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding file: {e}")
            return None

    def search_files(self, query=None, ext=None):
        base_query = "SELECT * FROM files WHERE 1=1"
        params = []

        if query:
            base_query += " AND filename LIKE ?"
            params.append(f"%{query}%")

        if ext:
            base_query += " AND extension = ?"
            params.append(ext.lower().strip('.'))

        base_query += " ORDER BY timestamp DESC"

        try:
            cursor = self.conn.cursor()
            cursor.execute(base_query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            print(f"Error searching files: {e}")
            return []

    def get_all_extensions(self):
        query = "SELECT DISTINCT extension FROM files ORDER BY extension ASC"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [row['extension'] for row in rows]
        except sqlite3.Error as e:
            print(f"Error fetching extensions: {e}")
            return []

    def clear_database(self):
        query = "DELETE FROM files"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error clearing database: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
