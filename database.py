import sqlite3
conn = sqlite3.connect("health.db",check_same_thread=False)
cursor=conn.cursor()
def create_table():
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS patients(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   query TEXT,
                   response TEXT
                   )
                   """)
    conn.commit()

def save_chat(query,response):
    cursor.execute(
        "INSERT INTO patients (query,response) VALUES (?,?)",(query,response)

    )
    conn.commit()

def get_history():
    cursor.execute("SELECT query,response FROM patients ORDER BY id DESC LIMIT 5")
    return cursor.fetchall()


    