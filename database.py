import sqlite3

# Ensure this function is at the top of your file
def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            link TEXT,
            source TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Other functions like get_jobs_from_db and insert_job should follow
def get_jobs_from_db(job_title, location):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT title, company, location, link, source FROM job_listings WHERE title=? AND location=?", (job_title, location))
    jobs = cursor.fetchall()
    
    conn.close()
    return jobs

def insert_job(job):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO job_listings (title, company, location, link, source) VALUES (?, ?, ?, ?, ?)",
                   (job['title'], job['company'], job['location'], job['link'], job['source']))
    
    conn.commit()
    conn.close()