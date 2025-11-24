import sqlite3

con = sqlite3.connect("../database/dashboard.db")
cur = con.cursor()
def create_tables():
    cur.execute('''CREATE TABLE IF NOT EXISTS github_stats
                (stars INTEGER, followers INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS instagram_stats
                (followers INTEGER, following INTEGER)''')
    con.commit()
    con.close() 

def update_github_stats(stars , followers):
    con = sqlite3.connect("../database/dashboard.db")
    cur = con.cursor()
    cur.execute("INSERT INTO github_stats (stars, followers) VALUES (?, ?)", 
                (stars, followers))
    con.commit()
    con.close()

def update_instagram_stats(followers, following):
    con = sqlite3.connect("../database/dashboard.db")
    cur = con.cursor()
    cur.execute("INSERT INTO instagram_stats (followers, following) VALUES (?, ?)", 
                (followers, following))
    con.commit()
    con.close()