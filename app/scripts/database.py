import sqlite3
import os

# Get absolute path to database file
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "dashboard.db")

con = sqlite3.connect(DB_PATH)
cur = con.cursor()
def create_tables():
    cur.execute('''CREATE TABLE IF NOT EXISTS github_stats
                (stars INTEGER, followers INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS instagram_stats
                (followers INTEGER, following INTEGER)''')
    con.commit()
    con.close() 

def update_github_stats(stars , followers):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO github_stats (stars, followers) VALUES (?, ?)", 
                (stars, followers))
    con.commit()
    con.close()

def update_instagram_stats(followers, following):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO instagram_stats (followers, following) VALUES (?, ?)", 
                (followers, following))
    con.commit()
    con.close()

if __name__ == "__main__":
    create_tables()