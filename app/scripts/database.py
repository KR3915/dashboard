import sqlite3

con = sqlite3.connect("../database/dashboard.db")
cur = con.cursor()


def create_tables():
    cur.execute('''CREATE TABLE IF NOT EXISTS github_stats
                (stars INTEGER, followers INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS instagram_stats
                (followers INTEGER, following INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS gmail_stats
                (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, emails_sent INTEGER)''')
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

def update_gmail_stats(emails_sent):
    con = sqlite3.connect("../database/dashboard.db")
    cur = con.cursor()
    cur.execute("INSERT INTO gmail_stats (emails_sent) VALUES (?)",
                (emails_sent,))
    con.commit()
    con.close()

if __name__ == "__main__":
    create_tables()