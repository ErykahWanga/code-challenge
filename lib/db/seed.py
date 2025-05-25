from lib.db.connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        INSERT OR IGNORE INTO authors (name) VALUES ('Test Author');
        INSERT OR IGNORE INTO magazines (name, category) VALUES ('Test Mag', 'Tech');
        INSERT OR IGNORE INTO articles (title, author_id, magazine_id) 
        VALUES ('Test Article', 1, 1);
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_database()
