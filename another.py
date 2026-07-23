import sqlite3
conn = sqlite3.connect('anoth.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT,
    short TEXT
)
""")
conn.commit()

def add_link(link):
    cursor.execute("INSERT INTO users (link) VALUES (?)", (link))
    conn.commit()

def look_up(short):
    cursor.execute("SELECT link FROM users WHERE short = ?", (short,))
    result = cursor.fetchone()
    return result[0] if result else None

def generate_short_code(link):
    cursor.execute("SELECT MAX(id) FROM users")
    row = cursor.fetchone()
    last_id = row[0]
    return str(last_id + 1) if last_id is not None else "1"