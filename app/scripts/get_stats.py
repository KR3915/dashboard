import sqlite3
import os

# Get absolute path to database file
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "dashboard.db")

def get_latest_github_stats():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT stars, followers FROM github_stats ORDER BY ROWID DESC LIMIT 1")
    result = cur.fetchone()
    con.close()
    if result:
        return result
    return (0, 0)

def get_latest_instagram_stats():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT followers, following FROM instagram_stats ORDER BY ROWID DESC LIMIT 1")
    result = cur.fetchone()
    con.close()
    if result:
        return result
    return (0, 0)

def get_latest_gmail_stats():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT emails_sent FROM gmail_stats ORDER BY timestamp DESC LIMIT 1")
    result = cur.fetchone()
    con.close()
    if result:
        return result[0]
    return 0